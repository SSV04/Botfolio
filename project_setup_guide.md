# Botfolio - AI CLI Portfolio - Complete Setup Guide

## 📁 Project Structure
Create the following folder structure in VS Code:

```
Botfolio/
├── README.md
├── requirements.txt
├── .gitignore
├── setup.py
├── src/
│   ├── __init__.py
│   ├── assistant.py
│   ├── ai_chat.py
│   └── data.json
├── docs/
│   ├── resume.pdf (your actual resume)
│   └── certificates/
├── tests/
│   ├── __init__.py
│   └── test_assistant.py
└── assets/
    └── banner.txt
```

## 🚀 Step-by-Step Setup Instructions

### 1. Initialize Git Repository
```bash
cd your-project-folder
git init
git branch -M main
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Assistant
```bash
python src/assistant.py
```

## 📝 Usage Examples
```bash
$ python src/assistant.py
Ask me something: resume
> 📄 Opening your latest resume...

Ask me something: school
> 🎓 You studied Computer Science at XYZ University

Ask me something: projects
> 🚀 Here are my recent projects: AI Portfolio Bot, Web Scraper...

Ask me something: joke
> 💡 Why do programmers prefer dark mode? Because light attracts bugs! 🐛
```

## 🔧 Customization
1. Edit `src/data.json` with your personal information
2. Add your resume to `docs/resume.pdf`
3. Modify responses in `assistant.py` to match your personality
4. Add certificates to `docs/certificates/`

## 🌐 GitHub Deployment
1. Create new repository on GitHub
2. Push your code:
```bash
git add .
git commit -m "Initial commit: AI CLI Portfolio Assistant"
git remote add origin https://github.com/SSV04/Botfolio.git
git push -u origin main
```

## 🎯 Features Included
- ✅ Interactive CLI interface
- ✅ Colorful terminal output
- ✅ Personal data retrieval
- ✅ Fun responses with jokes
- ✅ File handling for documents
- ✅ Optional AI-powered responses
- ✅ Professional project structure
- ✅ Complete documentation