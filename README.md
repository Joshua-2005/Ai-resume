# 🤖 AI Resume Analyzer

An AI-powered web application that analyzes resumes and provides insights based on a given job role.  
This project uses AI to evaluate candidates and generate structured analysis including score, strengths, weaknesses, and recommendations.

---

## 🚀 Live Demo

🔗 https://ai-resume-oaq8.onrender.com

---

## 📌 Features

- 📄 Upload PDF resume
- 🎯 Enter job role for analysis
- 🤖 AI-based resume evaluation
- 📊 Match score & skill match percentage
- ❌ Missing skills detection
- 💪 Strengths analysis
- ⚠️ Weaknesses analysis
- ✅ Final recommendation

---

## 🛠️ Tech Stack

- Frontend: HTML, CSS  
- Backend: Python (Flask)  
- API: OpenRouter (LLM API)  
- PDF Processing: PyPDF2  
- Deployment: Render  

---

## ⚙️ Installation (Local Setup)

### 1. Clone the repository

git clone https://github.com/Joshua-2005/Ai-resume.git  
cd Ai-resume

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Set API Key

Option 1 (Recommended)

Create a .env file:

API_KEY=your_openrouter_api_key

Option 2 (For testing only)

API_KEY = "your_api_key"

---

### 4. Run the application

python app.py

Open in browser:

http://127.0.0.1:5000/

---

## 🌐 Deployment (Render)

Steps:

1. Push code to GitHub  
2. Connect repo to Render  
3. Add environment variable: API_KEY  
4. Deploy Web Service  

---

## 🔐 Security

- API keys are stored using environment variables  
- API keys are not exposed in public code  

---

## 📸 Output

The application generates:

- Match Score (out of 10)
- Skill Match Percentage
- Missing Skills
- Strengths
- Weaknesses
- Final Recommendation

---

## 👨‍💻 Author

Joshua  
Electronics & Communication Engineering Student  

---

## ⭐ Acknowledgements

- OpenRouter API  
- Flask Documentation  
- PyPDF2  

---

## 📌 Future Improvements

- Better resume parsing  
- Improved UI/UX  
- Authentication system  
- Multiple resume comparison  
- Advanced scoring system  

---

## 💡 Project Purpose

This project demonstrates:

- Backend development using Flask  
- AI API integration  
- PDF file handling  
- Deployment on cloud (Render)  
- Real-world problem solving  

---

⭐ If you like this project, give it a star!
