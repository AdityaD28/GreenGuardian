# GreenGuardian - AI-Powered Plant Disease Detection & Management System

GreenGuardian is a comprehensive web application that combines cutting-edge AI technology with user-friendly design to help gardeners, farmers, and plant enthusiasts identify, treat, and manage plant diseases effectively. Built with a modern tech stack, it offers real-time disease detection, personalized treatment recommendations, secure user authentication, and complete diagnosis history tracking.

![GreenGuardian Banner](https://github.com/AdityaD28/GreenGuardian/blob/main/GreenguardianBanner.png?raw=true)

---

## Key Features

### **AI-Powered Disease Detection**
- **Advanced CNN Model**: Utilizes a fine-tuned MobileNetV2 architecture trained on 15+ plant disease classes
- **High Accuracy**: Provides confidence scores for each prediction with 95%+ accuracy
- **Multi-Plant Support**: Covers Tomato, Potato, and Bell Pepper diseases
- **Real-Time Processing**: Instant image analysis and results under 2 seconds
- **Smart Image Processing**: Automatic preprocessing and optimization for optimal results

### **Intelligent Treatment Recommendations**
- **AI-Generated Guidance**: Leverages Google Gemini 1.5 Flash for personalized treatment plans
- **Structured Information**: Organized sections including Overview, Immediate Actions, Treatment, and Prevention
- **Markdown Formatting**: Clean, readable recommendations with proper formatting
- **Context-Aware**: Tailored advice based on specific disease diagnosis and confidence levels
- **Fallback System**: Default recommendations when API is unavailable

### **Simple & Secure Authentication**
- **User Registration**: Simple account creation with username, email, and password
- **Secure Login**: Password-based authentication with secure session management
- **Password Security**: PBKDF2-SHA256 encryption for maximum security
- **Session Management**: Flask-Login integration with secure cookie handling
- **User Accounts**: Personal profiles for tracking diagnosis history

### **User Management**
- **Easy Registration**: Simple one-step registration process
- **Account Validation**: Username and email uniqueness verification
- **Secure Password Storage**: Industry-standard password hashing
- **User Sessions**: Persistent login sessions with secure logout
- **Personal Profiles**: Individual user accounts for private data

### **Comprehensive History Tracking**
- **Diagnosis Archive**: Complete history of all plant diagnoses with detailed metadata
- **Advanced Search & Filter**: Find specific diagnoses by disease type, date, or confidence level
- **Smart Search Bar**: Real-time search with optimized spacing and visual feedback
- **Visual Timeline**: Chronological view of plant health journey with timestamps
- **Data Analytics**: Statistics on total diagnoses, healthy vs. diseased plants, and average confidence scores
- **Export Capabilities**: Copy recommendations for offline use and sharing
- **User-Specific Data**: Each user maintains their own private diagnosis history

### **Modern User Interface**
- **Responsive Design**: Seamless experience across desktop, tablet, and mobile devices
- **Dark Theme**: Professional dark theme with green accent colors and optimal contrast
- **Glassmorphism Effects**: Modern UI design with glass-like elements and smooth transitions
- **Interactive Components**: Smooth animations, hover effects, and loading states
- **Form Stability**: Ultra-robust form handling with clean CSS design
- **Accessibility**: WCAG-compliant design for inclusive user experience
- **Tailwind CSS**: Utility-first styling with custom color schemes and components

---

## Technology Stack

### **Backend Architecture**
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Web Framework** | Flask 2.3+ | RESTful API and web server with routing |
| **Database** | SQLite + SQLAlchemy | User data and diagnosis history storage |
| **Authentication** | Flask-Login + Werkzeug | Secure user management with session handling |
| **Password Security** | PBKDF2-SHA256 | Secure password hashing and validation |
| **File Handling** | Werkzeug | Secure file uploads and processing |
| **Session Management** | Flask Sessions | Secure user state management |

### **AI & Machine Learning**
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Disease Detection** | TensorFlow/Keras 2.13+ | CNN model for image classification |
| **Model Architecture** | MobileNetV2 | Efficient mobile-optimized CNN with transfer learning |
| **Recommendation Engine** | Google Gemini 1.5 Flash | AI-powered treatment recommendations |
| **Image Processing** | PIL (Pillow) 10.0+ | Image preprocessing, resizing, and optimization |
| **Model Training** | PlantVillage Dataset | 15+ disease classes with thousands of training images |

### **Frontend & UI**
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Styling Framework** | Tailwind CSS 3.3+ | Responsive utility-first CSS with custom themes |
| **Template Engine** | Jinja2 | Dynamic HTML rendering with template inheritance |
| **Icons** | Font Awesome 6.4+ | Professional icon library with plant/medical themes |
| **Typography** | Google Fonts (Inter) | Modern, readable typography optimized for screens |
| **JavaScript** | Vanilla ES6+ | Interactive frontend functionality and form validation |
| **Form Handling** | Custom CSS + JS | Ultra-stable form components with drift protection |

### **Security & Authentication**
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Password Hashing** | Werkzeug PBKDF2 | Industry-standard password security |
| **Session Security** | Flask Secret Key | Secure session cookies and CSRF protection |
| **Input Validation** | WTForms + Custom | Server-side form validation and sanitization |
| **User Authentication** | Flask-Login | Secure user session management |

### **Development & Deployment**
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Environment Management** | Conda/pip | Isolated Python environment with dependency management |
| **Version Control** | Git | Source code management and collaboration |
| **API Integration** | Google AI Studio | Gemini API access for AI recommendations |
| **File Storage** | Local filesystem | Image uploads and database storage |
| **Development Server** | Flask Dev Server | Hot reloading and debugging capabilities |
| **Database Management** | SQLAlchemy ORM | Database migrations and schema management |

---

## AI Model Details

### **Disease Detection Model**
- **Architecture**: MobileNetV2-based Convolutional Neural Network with transfer learning
- **Input Size**: 256x256 RGB images with automatic preprocessing
- **Classes Supported**: 15 different plant diseases and healthy states across 3 plant species
- **Training Dataset**: PlantVillage Dataset with 50,000+ labeled high-quality images
- **Accuracy**: 95%+ confidence with detailed prediction scores
- **Performance**: < 2 seconds inference time on standard hardware
- **Model Size**: Optimized for web deployment (~25MB)

### **Supported Disease Classes**
```
Bell Pepper (2 classes):
   Healthy
   Bacterial Spot

Potato (3 classes):
   Healthy
   Early Blight
   Late Blight

Tomato (10 classes):
   Healthy
   Bacterial Spot
   Early Blight
   Late Blight
   Leaf Mold
   Septoria Leaf Spot
   Spider Mites (Two-spotted)
   Target Spot
   Yellow Leaf Curl Virus
   Mosaic Virus
```

### **Recommendation Generation**
- **Model**: Google Gemini 1.5 Flash Latest with advanced prompt engineering
- **Prompt Engineering**: Structured prompts for consistent, helpful, and actionable responses
- **Output Format**: Markdown-formatted treatment guides with clear sections
- **Content Sections**: Overview, Immediate Actions, Treatment Protocol, Prevention Strategies
- **Fallback System**: Default expert recommendations when API is unavailable
- **Response Time**: < 3 seconds for comprehensive treatment plans

## Project Structure

```
GreenGuardian_WebApp/
│
├── Core Application
│   ├── app.py                         # Main Flask application with routes, models, and AI integration
│   ├── GreenGuardian_model.h5         # Pre-trained TensorFlow CNN model (MobileNetV2-based, ~25MB)
│   └── environment.yml                # Conda environment configuration for reproducible setup
│
├── User Interface
│   ├── templates/                     # Jinja2 template directory with modern UI components
│   │   ├── base.html                  # Base template with Tailwind CSS, Font Awesome, and dark theme
│   │   ├── index.html                 # Main landing page with drag-drop disease detection interface
│   │   ├── home.html                  # User dashboard with recent diagnoses and quick actions
│   │   ├── login.html                 # Clean login form with password authentication
│   │   ├── register.html              # Simple registration form with validation
│   │   └── history.html               # Diagnosis history with advanced search, filters, and export features
│   └── index.html                     # Static landing page template
│
├── Data Storage
│   ├── instance/                      # Flask instance folder (auto-created)
│   │   ├── greenguardian.db          # SQLite database with users and diagnosis history
│   │   └── uploads/                   # User-specific uploaded images (logged-in users)
│   └── uploads/                       # Public uploads directory for guest users
│
├── Configuration
│   ├── environment.yml                # Conda environment with TensorFlow, Flask, and all dependencies
│   └── README.md                      # Comprehensive project documentation (this file)
│
└── Additional Files
    ├── .gitignore                     # Git ignore patterns for Python, Flask, and ML projects
    └── LICENSE                        # MIT License for open-source distribution
```

---

## Installation & Setup Guide

### Prerequisites

Ensure you have the following installed on your system:

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | 3.9+ | Core runtime environment |
| **Conda** | Latest | Environment and package management |
| **Git** | Latest | Version control and repository cloning |
| **Modern Browser** | Any | Web interface access |

### Step-by-Step Installation

#### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/GreenGuardian_WebApp.git
cd GreenGuardian_WebApp
```

#### 2. **Environment Setup**
Create and activate the conda environment from the provided configuration:

```bash
# Create environment from environment.yml
conda env create -f environment.yml

# Activate the environment
conda activate greenguardian
```

> **Apple Silicon (M1/M2/M3) Optimization**  
> The environment is pre-configured with `tensorflow-macos` and `tensorflow-metal` for optimal performance on Apple's ARM processors.

#### 3. **API Configuration**
Configure the Google Gemini API for AI-powered recommendations:

1. **Get API Key**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Create Free Account**: Sign up for free API access
3. **Generate Key**: Create a new API key
4. **Configure Application**: Update `app.py` with your API key:

```python
# Replace in app.py around line 15
genai.configure(api_key="YOUR_ACTUAL_GEMINI_API_KEY_HERE")
```

#### 4. **Database Initialization**
The application automatically creates the SQLite database on first run:

```bash
# The app will create instance/greenguardian.db automatically
# No manual database setup required
```

#### 5. **Launch Application**
Start the Flask development server:

```bash
python app.py
```

**Access the Application**: Open your browser and navigate to `http://127.0.0.1:5000`

### Security Configuration (Production)

For production deployment, ensure you:
- Set a secure `SECRET_KEY` in app.py
- Use environment variables for API keys
- Configure HTTPS/SSL certificates
- Set up proper file upload restrictions

---

## User Guide & Features

### **Getting Started**

#### **1. User Registration (Simple Process)**
- Navigate to the registration page (`/register`)
- Enter username (3-20 characters), email address, and secure password (minimum 6 characters)
- Click "Create Account" to complete registration
- Automatic redirect to login page upon successful registration

#### **2. User Authentication**
- Enter your username and password on the login page
- Click "Sign In" for immediate access
- Secure session management with automatic logout option

#### **3. Security Features**
- **Account Validation**: Username and email uniqueness verification
- **Secure Storage**: PBKDF2-SHA256 password hashing
- **Session Management**: Automatic logout and secure cookie handling
- **Input Validation**: Server-side form validation and sanitization

### **Disease Detection Workflow**

#### **Step 1: Image Upload**
- Drag and drop or click to select plant image
- Supported formats: JPG, JPEG, PNG
- Automatic image preprocessing and optimization

#### **Step 2: AI Analysis**
- Real-time CNN model inference
- Confidence score calculation
- Disease classification across 15+ categories

#### **Step 3: Results & Recommendations**
- Detailed diagnosis with confidence percentage
- AI-generated treatment recommendations
- Structured guidance in 4 key sections:
  - **Overview**: Disease description and impact
  - **Immediate Actions**: Urgent steps to take
  - **Treatment**: Detailed treatment protocols
  - **Prevention**: Long-term prevention strategies

#### **Step 4: History Tracking**
- Automatic save to personal diagnosis history
- Searchable archive of all past diagnoses
- Performance analytics and trends

### **History Management**

#### **Advanced Search & Filtering**
- **Real-Time Search**: Instant search with optimized spacing (pl-48 padding)
- **Search by Disease**: Find specific disease types and classifications
- **Filter by Date**: Chronological organization with date ranges
- **Confidence Sorting**: Order by prediction accuracy and reliability
- **Quick Stats**: Total diagnoses, healthy vs. diseased plant ratios
- **User-Specific Data**: Private history accessible only to account owners

#### **Data Export & Sharing**
- **Copy to Clipboard**: One-click copying of detailed treatment recommendations
- **Save Treatment Guides**: Download comprehensive disease management protocols
- **Track Progress**: Monitor plant health improvements over time
- **Visual Analytics**: Charts and graphs showing diagnosis trends and patterns

#### **Advanced Features**

#### **User Dashboard**
- **Quick Actions**: Easy access to image upload and recent diagnoses
- **Recent Activity**: View latest 3 diagnoses with quick access
- **Statistics Overview**: Total diagnoses and account information
- **Navigation**: Seamless access to all application features

#### **Image Processing Pipeline**
- **Smart Upload**: Drag-and-drop interface with real-time preview
- **Format Support**: JPG, JPEG, PNG with automatic optimization
- **Size Validation**: 16MB maximum with client-side validation
- **Processing Feedback**: Loading states and progress indicators

---

## API Documentation

### **Core Endpoints**

| Endpoint | Method | Purpose | Authentication | Features |
|----------|--------|---------|----------------|----------|
| `/` | GET | Landing page and image upload interface | Optional | Disease detection for all users |
| `/home` | GET | User dashboard with recent diagnoses | Required | Personalized user homepage |
| `/predict` | POST | Disease detection and AI recommendation | Optional | CNN inference + Gemini API |
| `/register` | GET/POST | User registration with validation | None | Simple account creation |
| `/login` | GET/POST | Password-based authentication | None | Secure user login |
| `/logout` | GET | User logout and session cleanup | Required | Secure session termination |
| `/history` | GET | View personal diagnosis history | Required | Search, filter, export features |
| `/api/recent-diagnoses` | GET | Get user's recent diagnoses | Required | JSON API for dashboard |
| `/uploads/<filename>` | GET | Serve uploaded images | Optional | Static file serving |

### **Database Schema**

#### **User Model**
```python
class User(db.Model):
    id: Integer (Primary Key)
    username: String(150) (Unique, Not Null)
    email: String(150) (Unique, Not Null)
    password: String(150) (Not Null)       # PBKDF2-SHA256 hashed
    histories: Relationship (→ DiagnosisHistory)
```

#### **DiagnosisHistory Model**
```python
class DiagnosisHistory(db.Model):
    id: Integer (Primary Key)
    user_id: Integer (Foreign Key → User.id)
    image_filename: String(100) (Not Null)
    disease_name: String(100) (Not Null)
    confidence: Float (0.0 - 1.0 range)
    recommendation: Text (AI-generated content)
    timestamp: DateTime (Default: UTC now)
```

### **API Response Formats**

#### **Disease Detection Response**
```json
{
    "success": true,
    "disease": "Tomato___Early_Blight",
    "confidence": 0.9234,
    "recommendations": "## Overview\n...",
    "timestamp": "2025-08-12T10:30:00Z"
}
```

#### **User Registration Response**
```json
{
    "success": true,
    "message": "Account created successfully! Please log in with your credentials.",
    "redirect": "/login"
}
```

---

## Configuration & Environment Variables

### **Required Configuration**
```python
# app.py configuration
SECRET_KEY = 'your-secret-key-here'          # Change in production
GEMINI_API_KEY = 'your-gemini-api-key'       # Required for AI recommendations
UPLOAD_FOLDER = 'instance/uploads'           # Image storage directory
MAX_CONTENT_LENGTH = 16 * 1024 * 1024        # 16MB max file size

# Database Configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/greenguardian.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### **Environment Variables (Production Ready)**
```bash
# Development
export FLASK_ENV=development
export FLASK_DEBUG=1

# Production
export FLASK_ENV=production
export FLASK_DEBUG=0
export SECRET_KEY=your_super_secure_secret_key_here
export GEMINI_API_KEY=your_actual_gemini_api_key

# Optional Database URL (for PostgreSQL in production)
export DATABASE_URL=postgresql://user:pass@localhost:5432/greenguardian
```

### **Security Recommendations**
```python
# Production Security Settings
import secrets
SECRET_KEY = secrets.token_hex(32)           # Generate random secret key
SESSION_COOKIE_SECURE = True                # HTTPS only cookies
SESSION_COOKIE_HTTPONLY = True              # Prevent XSS attacks
PERMANENT_SESSION_LIFETIME = timedelta(hours=1)  # Session timeout
```

---

## Deployment Guide

### **Local Development**
```bash
# Development server
python app.py
# Runs on http://127.0.0.1:5000
```

### **Production Deployment Options**

#### **1. Traditional Server (Ubuntu/CentOS)**
```bash
# Install dependencies
sudo apt update
sudo apt install python3-pip nginx

# Set up application
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

#### **2. Docker Deployment**
```dockerfile
# Dockerfile (create this file)
FROM python:3.9-slim
WORKDIR /app
COPY environment.yml .
RUN pip install conda && conda env create -f environment.yml
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

#### **3. Cloud Platforms**
- **Heroku**: Direct Git deployment with `Procfile`
- **AWS EC2**: Traditional server deployment
- **Google Cloud Run**: Containerized deployment
- **Vercel**: Serverless deployment option

---

## Testing & Validation

### **Model Performance**
- **Accuracy**: 95%+ on PlantVillage test set
- **Inference Time**: < 2 seconds per image
- **Supported Image Formats**: JPG, JPEG, PNG
- **Optimal Image Size**: 256x256 pixels

### **Supported Plant Diseases**
The model recognizes **15 different disease classes** across 3 plant types:

**Bell Pepper (2 classes)**
- Bacterial Spot
- Healthy

**Potato (3 classes)**
- Early Blight
- Late Blight
- Healthy

**Tomato (10 classes)**
- Bacterial Spot
- Early Blight
- Late Blight
- Leaf Mold
- Septoria Leaf Spot
- Spider Mites (Two-spotted)
- Target Spot
- Yellow Leaf Curl Virus
- Mosaic Virus
- Healthy

### **Testing Checklist**
- [ ] User registration and authentication
- [ ] Image upload and processing
- [ ] Disease detection accuracy
- [ ] AI recommendation generation
- [ ] History tracking and search
- [ ] Responsive design across devices

---

## Security Features

### **User Authentication**
- **Password Hashing**: PBKDF2 with SHA256
- **Session Management**: Flask-Login with secure cookies
- **CSRF Protection**: Built-in Flask security features

### **File Upload Security**
- **File Type Validation**: Only image files allowed
- **Size Restrictions**: 16MB maximum file size
- **Secure Filename Handling**: Werkzeug secure_filename()

### **Database Security**
- **SQL Injection Prevention**: SQLAlchemy ORM protection
- **Input Validation**: Server-side form validation
- **Data Encryption**: Secure password storage

---

## Future Enhancements

### **Immediate Roadmap**
- [ ] **Mobile App**: React Native/Flutter mobile application
- [ ] **Advanced Analytics**: Disease trend analysis and insights
- [ ] **Multi-language Support**: Internationalization support
- [ ] **Offline Mode**: Local model deployment for offline usage

### **Long-term Vision**
- [ ] **Computer Vision Improvements**: Object detection for multiple diseases
- [ ] **IoT Integration**: Connect with plant monitoring sensors
- [ ] **Community Features**: User forums and knowledge sharing
- [ ] **API Monetization**: Premium API access for agricultural businesses

### **Technical Improvements**
- [ ] **Model Optimization**: TensorFlow Lite for mobile deployment
- [ ] **Real-time Processing**: WebSocket-based live image analysis
- [ ] **Advanced ML**: Multi-modal AI combining image and text analysis
- [ ] **Edge Computing**: Deploy models on edge devices

---

### **Frequently Asked Questions**

**Q: What image formats are supported?**
A: JPG, JPEG, and PNG formats are supported. For best results, use clear, well-lit images of individual leaves.

**Q: How accurate is the disease detection?**
A: The model achieves 95%+ accuracy on the PlantVillage dataset. However, real-world performance may vary based on image quality and lighting conditions.

**Q: Can I use this commercially?**
A: Yes, but please ensure you comply with the model's licensing terms and Google's Gemini API usage policies.

**Q: How do I improve prediction accuracy?**
A: Use high-quality images with good lighting, focus on individual leaves, and ensure the disease symptoms are clearly visible.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### **MIT License Summary**
- Commercial use allowed
- Modification allowed
- Distribution allowed
- Private use allowed
- No warranty provided
- No liability assumed

---

## Developed By

* **Aditya Dasappanavar**
* **GitHub:** [AdityaD28](https://github.com/AdityaD28)
* **LinkedIn:** [adityadasappanavar](https://www.linkedin.com/in/adityadasappanavar/)

</div>
