import os
import random
import string
import smtplib
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, send_from_directory, session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import tensorflow as tf
import numpy as np
from PIL import Image
import google.generativeai as genai
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from datetime import datetime, timedelta

# --- App Initialization and Configuration ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-very-secret-key-that-should-be-changed'

# --- CORRECTED PATHS ---
# Use absolute paths to prevent ambiguity
app.instance_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'instance')
app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'uploads')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'greenguardian.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- Create Directories ---
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.instance_path, exist_ok=True)

# --- Database and Login Manager Setup ---
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# --- Gemini API Configuration ---
try:
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "dummy_key_for_testing"))
    print("✅ Gemini API configured.")
except (AttributeError, KeyError):
    print("⚠️  Warning: Gemini API Key not found. Using dummy configuration for testing.")
    # Don't exit, continue for UI testing

# --- Load The Trained CNN Model ---
try:
    model_cnn = tf.keras.models.load_model('GreenGuardian_model.h5')
    print("✅ CNN model loaded successfully.")
except Exception as e:
    print(f"⚠️  Warning: Could not load 'GreenGuardian_model.h5'. {e}")
    print("🔧 Running in demo mode for UI testing...")
    model_cnn = None  # Set to None for demo mode

# --- Define Constants ---
CLASS_NAMES = [
    'Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Tomato_Bacterial_spot',
    'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two-spotted_spider_mite',
    'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf_Curl_Virus',
    'Tomato__Tomato_mosaic_virus', 'Tomato_healthy'
]
IMAGE_SIZE = 256

# --- Database Models ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    histories = db.relationship('DiagnosisHistory', backref='user', lazy=True)

class DiagnosisHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_filename = db.Column(db.String(100), nullable=False)
    disease_name = db.Column(db.String(100), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    recommendation = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- AI Recommendation Function ---
model_genai = genai.GenerativeModel('gemini-1.5-flash-latest')

def get_ai_recommendation(disease_name):
    if "healthy" in disease_name.lower():
        return "The plant appears to be healthy! No treatment is necessary."
    
    # Check if we have a valid API key
    if not os.environ.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY") == "dummy_key_for_testing":
        return f"""
## Treatment for {disease_name.replace('_', ' ')}

### Overview
This plant has been diagnosed with {disease_name.replace('_', ' ')}. Here's a general treatment approach:

### Immediate Actions
1. **Isolate** the affected plant to prevent spread
2. **Remove** any severely affected leaves
3. **Improve** air circulation around the plant

### Treatment
- Apply appropriate fungicide or treatment based on the specific condition
- Adjust watering schedule to prevent overwatering
- Ensure proper lighting conditions

### Prevention
- Maintain good plant hygiene
- Avoid overcrowding plants
- Water at soil level, not on leaves
- Monitor regularly for early signs

*Note: This is a general recommendation. For a detailed AI-powered treatment plan, please configure the Gemini API key.*
        """
    
    prompt = f"""
    You are GreenGuardian, an expert AI assistant for plant health.
    A plant has been diagnosed with: "{disease_name.replace('_', ' ')}".
    Please provide a helpful, easy-to-understand guide for a home gardener on how to treat this disease. Structure your response in clear sections (e.g., Overview, Immediate Actions, Treatment, Prevention). Use markdown for formatting.
    """
    try:
        response = model_genai.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating recommendation: {e}"

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('❌ User not found. Please check your username.', 'danger')
            return render_template('login.html')
        
        if check_password_hash(user.password, password):
            login_user(user)
            flash('✅ Successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('❌ Invalid password. Please check your credentials.', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validation
        if User.query.filter_by(username=username).first():
            flash('❌ Username already exists. Please choose a different username.', 'danger')
            return render_template('register.html')
            
        if User.query.filter_by(email=email).first():
            flash('❌ Email already registered. Please use a different email.', 'danger')
            return render_template('register.html')
        
        # Create the user account
        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password, method='pbkdf2:sha256')
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash('🎉 Account created successfully! Please log in with your credentials.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/history')
@login_required
def history():
    user_history = DiagnosisHistory.query.filter_by(user_id=current_user.id).order_by(DiagnosisHistory.timestamp.desc()).all()
    return render_template('history.html', history=user_history)

@app.route('/api/recent-diagnoses')
@login_required
def get_recent_diagnoses():
    recent = DiagnosisHistory.query.filter_by(user_id=current_user.id).order_by(DiagnosisHistory.timestamp.desc()).limit(3).all()
    diagnoses = []
    for diagnosis in recent:
        diagnoses.append({
            'id': diagnosis.id,
            'disease': diagnosis.disease_name,
            'confidence': diagnosis.confidence,
            'image_filename': diagnosis.image_filename,
            'timestamp': diagnosis.timestamp.strftime('%B %d, %Y at %I:%M %p')
        })
    return jsonify(diagnoses)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/predict', methods=['POST'])
@login_required
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_filename = f"{timestamp}_{secure_filename(file.filename)}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)

        # Check if model is loaded
        if model_cnn is None:
            # Demo mode - return sample predictions
            import random
            sample_diseases = [
                'Tomato_healthy', 'Pepper__bell___healthy', 'Potato___healthy',
                'Tomato_Early_blight', 'Potato___Late_blight', 'Tomato_Bacterial_spot'
            ]
            predicted_class_name = random.choice(sample_diseases)
            confidence = random.uniform(75.0, 98.0)
            print(f"🎭 Demo mode: Simulated prediction - {predicted_class_name} ({confidence:.2f}%)")
        else:
            # Real prediction
            img = Image.open(filepath).resize((IMAGE_SIZE, IMAGE_SIZE))
            img_array = np.array(img)
            img_array = np.expand_dims(img_array, 0)
            predictions = model_cnn.predict(img_array)
            predicted_class_index = np.argmax(predictions[0])
            predicted_class_name = CLASS_NAMES[predicted_class_index]
            confidence = float(np.max(predictions[0])) * 100

        recommendation = get_ai_recommendation(predicted_class_name)

        new_history_entry = DiagnosisHistory(
            user_id=current_user.id,
            image_filename=unique_filename,
            disease_name=predicted_class_name.replace('_', ' '),
            confidence=confidence,
            recommendation=recommendation
        )
        db.session.add(new_history_entry)
        db.session.commit()

        return jsonify({
            'disease': predicted_class_name.replace('_', ' '),
            'confidence': f"{confidence:.2f}%",
            'recommendation': recommendation
        })
    return jsonify({'error': 'Prediction failed'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5002)
