# 🚀 SkillBridge AI

> **An AI-Powered Career Guidance Platform that helps students bridge the gap between education and employment.**

SkillBridge AI is a full-stack web application that provides personalized career guidance using Artificial Intelligence. It analyzes users' skills, identifies skill gaps, generates learning roadmaps, offers resume analysis, and helps users prepare for interviews—all in one platform.

🌍 **Aligned with UN Sustainable Development Goal 8 (SDG 8): Decent Work and Economic Growth**

---

## 📌 Features

### 🤖 AI Career Roadmap Generator
- Personalized career roadmap based on user goals
- Skill gap identification
- Weekly learning plan
- Project recommendations
- Interview preparation guidance

### 📄 AI Resume Analyzer
- Upload PDF/DOCX resumes
- ATS-style resume analysis
- Skill improvement suggestions
- Resume enhancement recommendations

### 👤 User Authentication
- Secure Sign Up
- Login & Logout
- Session Management

### 📊 Dashboard
- Career Progress
- Resume Score
- Interview Readiness
- Learning Progress
- Personalized Dashboard

### 🎯 Career Guidance
- Career Goal Analysis
- Personalized Learning Resources
- AI Career Suggestions

### 🌍 SDG 8 Support
Helping students become job-ready through AI-powered guidance, promoting quality employment and economic growth.

---

# 🛠 Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

## Backend
- Python
- Flask

## Database
- SQLite

## Artificial Intelligence
- Google Gemini API

## Libraries
- pdfplumber
- python-docx
- Werkzeug
- python-dotenv

## Tools
- Git
- GitHub
- VS Code

---

# 📂 Project Structure

```text
SkillBridge-AI/
│
├── database/
│   ├── db.py
│   ├── models.py
│   └── users.db
│
├── routes/
│   ├── auth.py
│   ├── career.py
│   ├── dashboard.py
│   ├── interview.py
│   ├── quiz.py
│   ├── resume.py
│
├── services/
│   ├── ai_service.py
│   ├── career_service.py
│   ├── interview_service.py
│   ├── resume_service.py
│   └── roadmap_service.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── resume.html
│   └── ...
│
├── presentation/
├── reports/
├── uploads/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/tanvi251105/SkillBridge-AI.git
```

---

## 2️⃣ Navigate to the Project

```bash
cd SkillBridge-AI
```

---

## 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Create a `.env` File

Create a file named `.env` in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 7️⃣ Initialize the Database

```bash
python setup_db.py
```

---

## 8️⃣ Run the Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---


# 📑 Documentation

The repository also includes:

- 📘 Project Report
- 📊 PowerPoint Presentation
- 📋 Lean Canvas
- 📝 Concept Notes
- 📄 Business Model Canvas

---

# 🎯 Future Enhancements

- 🔍 Real ATS Resume Parsing
- 🎤 AI Mock Interview Evaluation
- 📈 Learning Progress Analytics
- 💼 AI Job Recommendation System
- 📥 PDF Report Generation
- ☁️ Cloud Deployment
- 🌐 Multi-language Support
- 📧 Email Notifications

---

# 🌍 Sustainable Development Goal (SDG 8)

This project contributes to **United Nations Sustainable Development Goal 8 – Decent Work and Economic Growth** by helping students improve employability through AI-powered career guidance, resume analysis, interview preparation, and personalized learning pathways.

---

# 👩‍💻 Developer

**Tanvi Mahabal**

- GitHub: https://github.com/tanvi251105

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# ⭐ Show Your Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share it with others

---

## 📄 License

This project is created for educational and portfolio purposes.
````

### One suggestion

After uploading screenshots to an `assets/screenshots/` folder, you can make the README look even better by embedding them, for example:

```markdown
## 🏠 Home Page

![Home Page](assets/screenshots/home.png)

## 📊 Dashboard

![Dashboard](assets/screenshots/dashboard.png)

## 📄 Resume Analyzer

![Resume Analyzer](assets/screenshots/resume.png)
```

This gives visitors an immediate preview of your application without downloading anything.
