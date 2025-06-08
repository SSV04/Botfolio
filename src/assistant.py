#!/usr/bin/env python3
"""
Botfolio - AI CLI Portfolio
A fun, interactive command-line bot that showcases your portfolio with personality!

Author: SSV
Date: June 2025
"""

import json
import os
import random
import sys
import subprocess
from pathlib import Path
from colorama import Fore, Style

def auto_install(package):
    try:
        __import__(package)
    except ImportError:
        print(f"🔄 Installing missing package: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

auto_install("colorama")
auto_install("pyjokes")

import pyjokes

# Optional AI integration
try:
    from transformers import pipeline
    AI_AVAILABLE = True
    print(f"{Fore.GREEN}🧠 AI mode available! Use 'ai: your question' for smart responses{Style.RESET_ALL}")
except ImportError:
    AI_AVAILABLE = False

class PortfolioAssistant:
    def __init__(self):
        self.load_data()
        self.setup_ai()
        self.show_banner()
        
    def load_data(self):
        """Load personal data from JSON file"""
        try:
            data_path = Path(__file__).parent / "data.json"
            with open(data_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"{Fore.RED}❌ data.json not found! Creating a sample file...{Style.RESET_ALL}")
            self.create_sample_data()
            
    def create_sample_data(self):
        """Create sample data file"""
        sample_data = {
            "name": "Your Name",
            "title": "AI Engineer & Developer",
            "school": "Your University",
            "degree": "Computer Science",
            "graduation_year": "2024",
            "skills": ["Python", "JavaScript", "React", "Machine Learning", "Django"],
            "projects": [
                {"name": "AI Portfolio Bot", "description": "This interactive CLI assistant"},
                {"name": "Web Scraper", "description": "Data extraction tool"},
                {"name": "ML Classifier", "description": "Image recognition system"}
            ],
            "contact": {
                "email": "your.email@example.com",
                "github": "https://github.com/yourusername",
                "linkedin": "https://linkedin.com/in/yourprofile",
                "portfolio": "https://yourportfolio.com"
            },
            "certifications": [
                "AWS Cloud Practitioner",
                "Google Data Analytics",
                "Python Programming"
            ],
            "experience": [
                {"role": "Software Developer Intern", "company": "Tech Corp", "duration": "2023-2024"}
            ]
        }
        
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, 'w', encoding='utf-8') as file:
            json.dump(sample_data, file, indent=2)
        self.data = sample_data
        
    def setup_ai(self):
        """Initialize AI chatbot if available"""
        if AI_AVAILABLE:
            try:
                # Use Microsoft's Phi-2 model for better Q&A
                self.ai_chatbot = pipeline(
                    "text-generation",
                    model="microsoft/phi-2",
                    max_length=150,
                    truncation=True
                )
            except Exception as e:
                print(f"{Fore.YELLOW}⚠️  AI setup failed: {e}{Style.RESET_ALL}")
                self.ai_chatbot = None
        else:
            self.ai_chatbot = None
            
    def show_banner(self):
        """Display welcome banner"""
        banner = f"""
{Fore.CYAN}{'='*60}
🤖 Welcome to {self.data.get('name', 'My')} Botfolio Assistant!
{'='*60}{Style.RESET_ALL}

{Fore.GREEN}Ask me anything about my master's background, projects, or just chat!
Type 'help' for available commands or 'exit' to quit.{Style.RESET_ALL}

{Fore.YELLOW}💡 Pro tip: Try 'resume', 'projects', 'skills', or 'joke'!{Style.RESET_ALL}
"""
        print(banner)
        
    def get_response(self, user_input):
        """Generate response based on user input"""
        query = user_input.lower().strip()
        
        # AI-powered responses
        if query.startswith('ai:') and self.ai_chatbot:
            return self.ai_response(query[3:].strip())
            
        # Command mapping
        responses = {
            'resume': self.get_resume_info,
            'cv': self.get_resume_info,
            'school': self.get_education_info,
            'education': self.get_education_info,
            'university': self.get_education_info,
            'projects': self.get_projects_info,
            'work': self.get_projects_info,
            'skills': self.get_skills_info,
            'tech': self.get_skills_info,
            'contact': self.get_contact_info,
            'email': self.get_contact_info,
            'social': self.get_contact_info,
            'certifications': self.get_certifications_info,
            'certificates': self.get_certifications_info,
            'experience': self.get_experience_info,
            'job': self.get_experience_info,
            'joke': self.get_joke,
            'funny': self.get_joke,
            'help': self.get_help,
            'commands': self.get_help,
            'about': self.get_about_info,
            'info': self.get_about_info
        }
        
        # Find matching command
        for keyword, handler in responses.items():
            if keyword in query:
                return handler()
                
        # Default responses for unrecognized input
        return self.get_default_response(query)
        
    def get_resume_info(self):
        """Return resume information"""
        # Instead of using resume_path, use your Google Drive link
        drive_link = "https://drive.google.com/drive/folders/1pX6i1j9g70Vmc3gSqYIFTHmeTpX0HlCP?usp=sharing"
        
        response = f"{Fore.BLUE}📄 Resume Information:{Style.RESET_ALL}\n\n"
        response += f"📋 {self.data.get('name', 'N/A')} - {self.data.get('title', 'Developer')}\n"
        response += f"🎓 {self.data.get('degree', 'N/A')} from {self.data.get('school', 'N/A')}\n"
        response += f"\n📎 View or download full resume here: {drive_link}"
        return response
        
    def get_education_info(self):
        """Return education information"""
        response = f"{Fore.GREEN}🎓 Education Background:{Style.RESET_ALL}\n\n"
        response += f"🏛️  University: {self.data.get('school', 'Not specified')}\n"
        response += f"📚 Degree: {self.data.get('degree', 'Not specified')}\n"
        response += f"📅 Graduation: {self.data.get('graduation_year', 'Not specified')}\n"
        
        if 'certifications' in self.data:
            response += f"\n🏆 Key Certifications:\n"
            for cert in self.data['certifications'][:3]:  # Show top 3
                response += f"   • {cert}\n"
                
        return response
        
    def get_projects_info(self):
        """Return projects information"""
        response = f"{Fore.MAGENTA}🚀 Recent Projects:{Style.RESET_ALL}\n\n"
        
        if 'projects' in self.data:
            for i, project in enumerate(self.data['projects'][:5], 1):  # Show top 5
                if isinstance(project, dict):
                    response += f"{i}. {Fore.CYAN}{project.get('name', 'Unnamed Project')}{Style.RESET_ALL}\n"
                    response += f"   {project.get('description', 'No description available')}\n\n"
                else:
                    response += f"{i}. {Fore.CYAN}{project}{Style.RESET_ALL}\n\n"
        else:
            response += "No projects listed yet. Update data.json to showcase your work!"
            
        return response
        
    def get_skills_info(self):
        """Return skills information"""
        response = f"{Fore.YELLOW}💻 Technical/ Non-technical Skills:{Style.RESET_ALL}\n\n"
        
        if 'skills' in self.data:
            # Group skills nicely
            skills = self.data['skills']
            for i, skill in enumerate(skills):
                response += f"🔸 {skill}"
                if i < len(skills) - 1:
                    response += "  "
                if (i + 1) % 3 == 0:  # New line every 3 skills
                    response += "\n"
            response += "\n"
        else:
            response += "Skills list not available. Update data.json!"
            
        return response
        
    def get_contact_info(self):
        """Return contact information"""
        response = f"{Fore.CYAN}📧 Contact Information:{Style.RESET_ALL}\n\n"
        
        contact = self.data.get('contact', {})
        if contact.get('email'):
            response += f"📧 Email: {contact['email']}\n"
        if contact.get('github'):
            response += f"🐙 GitHub: {contact['github']}\n"
        if contact.get('linkedin'):
            response += f"💼 LinkedIn: {contact['linkedin']}\n"
        if contact.get('portfolio'):
            response += f"🌐 Portfolio: {contact['portfolio']}\n"
            
        if not any(contact.values()):
            response += "Contact info not available. Update data.json!"
            
        return response
        
    def get_certifications_info(self):
        """Return certifications information"""
        response = f"{Fore.GREEN}🏆 Certifications & Achievements:{Style.RESET_ALL}\n\n"
        
        if 'certifications' in self.data:
            for i, cert in enumerate(self.data['certifications'], 1):
                response += f"{i}. 🏅 {cert}\n"
        else:
            response += "No certifications listed. Update data.json to showcase achievements!"
    
        # Add your LinkedIn certificates link
        linkedin_cert_link = "https://www.linkedin.com/in/shivshakti-vashist-11042k23/details/certifications/"
        response += f"\n🔗 View all certificates on LinkedIn: {linkedin_cert_link}"
        return response
        
    def get_experience_info(self):
        """Return work experience information"""
        response = f"{Fore.BLUE}💼 Work Experience:{Style.RESET_ALL}\n\n"
        
        if 'experience' in self.data:
            for exp in self.data['experience']:
                if isinstance(exp, dict):
                    response += f"🏢 {exp.get('role', 'Role')} at {exp.get('company', 'Company')}\n"
                    response += f"📅 Duration: {exp.get('duration', 'Not specified')}\n\n"
                else:
                    response += f"🏢 {exp}\n\n"
        else:
            response += "Work experience not listed. Update data.json!"
            
        return response
        
    def get_joke(self):
        """Return a programming joke"""
        if JOKES_AVAILABLE:
            joke = pyjokes.get_joke(language='en', category='neutral')
            return f"{Fore.YELLOW}😄 Here's a joke for you:\n\n{joke}{Style.RESET_ALL}"
        else:
            # Fallback jokes
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
                "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
                "Why don't programmers like nature? It has too many bugs! 🌿🐛",
                "What's a programmer's favorite hangout place? Foo Bar! 🍺",
                "Why do Java developers wear glasses? Because they can't C#! 👓"
            ]
            return f"{Fore.YELLOW}😄 {random.choice(jokes)}{Style.RESET_ALL}"
            
    def get_help(self):
        """Return help information"""
        return f"""{Fore.GREEN}📋 Available Commands:{Style.RESET_ALL}

{Fore.CYAN}📄 Portfolio Commands:{Style.RESET_ALL}
• resume, cv          - View resume information
• projects, work      - See recent projects  
• skills, tech        - Technical skills overview
• education, school   - Educational background
• experience, job     - Work experience
• certifications      - Certificates & achievements
• contact, email      - Contact information

{Fore.YELLOW}🎮 Fun Commands:{Style.RESET_ALL}
• joke, funny         - Programming humor
• about, info         - About this assistant

{Fore.MAGENTA}🤖 Advanced:{Style.RESET_ALL}
• ai: [question]      - AI-powered responses (if available)
• help, commands      - Show this help menu
• exit, quit, bye     - Exit the assistant

{Fore.GREEN}💡 Pro tip: Just type naturally! I understand variations of these commands.{Style.RESET_ALL}"""

    def get_about_info(self):
        """Return information about the assistant"""
        return f"""{Fore.CYAN}🤖 About This Assistant:{Style.RESET_ALL}

This is an AI-powered CLI portfolio assistant built with Python with some vibe coding! 

{Fore.GREEN}Features:{Style.RESET_ALL}
• Interactive command-line interface
• Dynamic portfolio information retrieval  
• Colorful and engaging responses
• File handling for documents
• Optional AI integration
• Programming humor support

{Fore.YELLOW}Built with:{Style.RESET_ALL} Python, colorama, pyjokes, transformers (optional)

{Fore.MAGENTA}Created by:{Style.RESET_ALL} {self.data.get('name', 'Developer')}
{Fore.BLUE}GitHub:{Style.RESET_ALL} Star this project if you found it helpful! ⭐"""

    def ai_response(self, query):
        """Generate AI-powered response"""
        if not self.ai_chatbot:
            return f"{Fore.RED}🤖 AI mode not available. Install transformers: pip install transformers{Style.RESET_ALL}"
            
        try:
            prompt = f"As a portfolio assistant, answer this question professionally: {query}"
            output = self.ai_chatbot(prompt, max_length=150, truncation=True)
            response = output[0]['generated_text']
        except Exception as e:
            response = f"🤖 AI error: {e}"

        print("🧠 AI Response:", response)
        # Clean up the response
        response = response.replace(prompt, "").strip()
        return f"{Fore.MAGENTA}🧠 AI Response: {response}{Style.RESET_ALL}"
            
    def get_default_response(self, query):
        """Handle unrecognized input with helpful suggestions"""
        suggestions = [
            f"🤔 I'm not sure about '{query}'. Try 'help' to see what I can do!",
            f"❓ Hmm, '{query}' isn't something I recognize. Type 'help' for available commands!",
            f"🔍 I didn't understand '{query}'. Try asking about 'resume', 'projects', or 'skills'!",
            f"💭 '{query}' is not in my vocabulary yet. Use 'help' to see what I can help with!"
        ]
        return f"{Fore.YELLOW}{random.choice(suggestions)}{Style.RESET_ALL}"
        
    def run(self):
        """Main conversation loop"""
        try:
            while True:
                # Get user input
                user_input = input(f"\n{Fore.WHITE}Ask me something: ").strip()
                
                # Check for exit commands
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    print(f"{Fore.GREEN}👋 Thanks for chatting! Don't forget to star this repo! ⭐{Style.RESET_ALL}")
                    break
                    
                # Skip empty input
                if not user_input:
                    continue
                    
                # Generate and display response
                response = self.get_response(user_input)
                print(f"\n{response}")
                
        except KeyboardInterrupt:
            print(f"\n\n{Fore.GREEN}👋 Goodbye! Thanks for using the Botfolio Assistant!{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}❌ An error occurred: {e}{Style.RESET_ALL}")

def main():
    """Main entry point"""
    try:
        assistant = PortfolioAssistant()
        assistant.run()
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to start assistant: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Make sure you have the required dependencies installed: pip install -r requirements.txt{Style.RESET_ALL}")

if __name__ == "__main__":
    main()