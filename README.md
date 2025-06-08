# 🤖 Botfolio - AI CLI Portfolio

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/SSV04/Botfolio?style=social)](https://github.com/SSV04/Botfolio)

> A fun, interactive command-line assistant that showcases your portfolio with personality! 🚀

## 🎯 What is this?

This is a **personal AI-powered CLI bot** that acts as your digital portfolio assistant. Instead of boring static resumes, let people interact with a chatbot version of you that can:

- 📋 Share your resume and experience
- 🎓 Talk about your education
- 💼 Showcase your projects
- 🏆 Display your certifications
- 😄 Tell programming jokes
- 🤖 Respond with AI-powered natural language (optional)

## ✨ Features

- **🎨 Colorful CLI Interface** - Beautiful terminal output with colors
- **💬 Interactive Chat** - Natural conversation flow
- **📁 File Management** - Dynamically serves documents (resume, certificates)
- **🎭 Personality** - Humorous and engaging responses
- **🧠 AI Integration** - Optional GPT-powered responses
- **⚡ Fast & Lightweight** - Pure Python, no heavy dependencies
- **🔧 Customizable** - Easy to modify for your own portfolio

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/SSV04/Botfolio.git
cd Botfolio

# Install dependencies
pip install -r requirements.txt

# Run the assistant
python src/assistant.py
```

### Usage
```bash
$ python src/assistant.py

🤖 Welcome to SSV's Botfolio Assistant!
Ask me anything about my background, projects, or just chat!

Ask me something: resume
📄 Opening your latest resume... [displays resume path]

Ask me something: school
🎓 I studied Computer Science at XYZ University with a focus on AI and Machine Learning

Ask me something: projects
🚀 Here are my recent projects:
• AI Portfolio Bot (This one!)
• Web Scraper Tool
• Data Analysis Dashboard

Ask me something: joke  
💡 Why do programmers prefer dark mode? Because light attracts bugs! 🐛

Ask me something: exit
👋 Thanks for chatting! Don't forget to star this repo! ⭐
```

## 🎛️ Available Commands

| Command | Description | Example Response |
|---------|-------------|------------------|
| `resume` | Shows resume information | 📄 Displays resume details |
| `school` / `education` | Educational background | 🎓 University and degree info |
| `projects` | Recent projects | 🚀 List of GitHub projects |
| `skills` | Technical skills | 💻 Programming languages & tools |
| `contact` | Contact information | 📧 Email and social links |
| `certifications` | Certificates & achievements | 🏆 Professional certifications |
| `joke` | Programming humor | 😄 Random developer jokes |
| `help` | Available commands | 📋 Command list |
| `exit` | Quit the assistant | 👋 Goodbye message |

## 🔧 Customization

### 1. Personal Information
Edit `src/data.json` with your details:
```json
{
  "name": "Your Name",
  "school": "Your University",
  "degree": "Your Degree",
  "skills": ["Python", "JavaScript", "React"],
  "projects": ["Project 1", "Project 2"],
  "contact": {
    "email": "your.email@example.com",
    "github": "https://github.com/yourusername",
    "linkedin": "https://linkedin.com/in/yourprofile"
  }
}
```

### 2. Add Your Documents
- Place your resume in `docs/resume.pdf`
- Add certificates to `docs/certificates/`

### 3. Customize Responses
Modify the response functions in `src/assistant.py` to match your personality and style.

## 🧠 AI Integration (Optional)

Enable AI-powered responses by installing transformers:
```bash
pip install transformers torch
```

Then uncomment the AI sections in `assistant.py` for natural language processing.

## 📁 Project Structure

```
Botfolio/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── src/
│   ├── assistant.py      # Main bot logic
│   ├── ai_chat.py       # AI integration (optional)
│   └── data.json        # Your personal data
├── docs/
│   ├── resume.pdf       # Your resume
│   └── certificates/   # Your certificates
├── tests/
│   └── test_assistant.py # Unit tests
└── assets/
    └── banner.txt       # ASCII art banner
```

## 🛠️ Technical Details

- **Language**: Python 3.8+
- **Dependencies**: colorama, pyjokes, transformers (optional)
- **Architecture**: Modular design with separate AI and data components
- **Testing**: Unit tests included
- **Documentation**: Comprehensive README and code comments

## 🤝 Contributing

Feel free to fork this project and make it your own! Some ideas for improvements:

- 🎵 Add voice commands
- 🌐 Create a web version
- 📱 Mobile app integration
- 🔍 Add search functionality
- 📊 Analytics dashboard

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the need for more interactive portfolio presentations
- Built with love for the developer community
- Thanks to all contributors and users!

---

**⭐ If you found this helpful, please give it a star on GitHub! ⭐**

Made with ❤️ by [Your Name](https://github.com/yourusername)
