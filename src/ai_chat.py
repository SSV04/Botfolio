#!/usr/bin/env python3
"""
AI Chat Integration Module
Optional AI-powered responses for the portfolio assistant

Author: SSV
Date: June 2025
"""

import os
import json
from pathlib import Path

try:
    from transformers import pipeline, set_seed
    import torch
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    print("⚠️  AI features require transformers. Install with: pip install transformers torch")

class AIChat:
    """AI-powered chat functionality for the portfolio assistant"""
    
    def __init__(self, model_name="gpt2"):
        self.model_name = model_name
        self.chatbot = None
        self.context_data = None
        self.initialize_ai()
        self.load_context()
        
    def initialize_ai(self):
        """Initialize the AI model"""
        if not AI_AVAILABLE:
            return False
            
        try:
            print("🧠 Loading AI model... This may take a moment on first run.")
            
            # Set seed for reproducible results
            set_seed(42)
            
            # Initialize the text generation pipeline
            self.chatbot = pipeline(
                "text-generation",
                model=self.model_name,
                max_length=200,
                temperature=0.7,
                pad_token_id=50256  # GPT-2 pad token
            )
            
            print("✅ AI model loaded successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Failed to load AI model: {e}")
            return False
            
    def load_context(self):
        """Load personal context data for AI responses"""
        try:
            data_path = Path(__file__).parent / "data.json"
            with open(data_path, 'r', encoding='utf-8') as file:
                self.context_data = json.load(file)
        except FileNotFoundError:
            print("⚠️  No context data found. AI responses will be generic.")
            self.context_data = {}
            
    def generate_context_prompt(self, user_query):
        """Generate a context-aware prompt based on personal data"""
        if not self.context_data:
            return f"Answer this question professionally: {user_query}"
            
        # Extract relevant context
        name = self.context_data.get('name', 'the developer')
        title = self.context_data.get('title', 'Software Developer')
        skills = ', '.join(self.context_data.get('skills', [])[:5])  # Top 5 skills
        
        context_prompt = f"""
You are {name}, a {title} with expertise in {skills}.
Answer the following question about your background professionally and concisely:

Question: {user_query}

Answer:"""
        
        return context_prompt
        
    def clean_response(self, generated_text, original_prompt):
        """Clean and format the AI response"""
        # Remove the original prompt from the response
        response = generated_text.replace(original_prompt, "").strip()
        
        # Clean up common AI artifacts
        response = response.replace("Answer:", "").strip()
        response = response.replace("Question:", "").strip()
        
        # Limit response length
        sentences = response.split('.')
        if len(sentences) > 3:
            response = '. '.join(sentences[:3]) + '.'
            
        # Remove incomplete sentences at the end
        if response and not response.endswith(('.', '!', '?')):
            last_period = response.rfind('.')
            if last_period > 0:
                response = response[:last_period + 1]
                
        return response.strip()
        
    def generate_response(self, user_query, max_length=150):
        """Generate AI response to user query"""
        if not self.chatbot:
            return "🤖 AI chat is not available. Please install required dependencies."
            
        try:
            # Create context-aware prompt
            prompt = self.generate_context_prompt(user_query)
            
            # Generate response
            result = self.chatbot(
                prompt,
                max_length=max_length,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=50256
            )
            
            # Extract and clean the response
            generated_text = result[0]['generated_text']
            cleaned_response = self.clean_response(generated_text, prompt)
            
            if not cleaned_response:
                return "🤔 I'm not sure how to respond to that. Try asking about my skills, projects, or experience!"
                
            return cleaned_response
            
        except Exception as e:
            return f"🤖 AI processing error: {str(e)}"
            
    def get_smart_response(self, query):
        """Get intelligent response based on query type"""
        query_lower = query.lower()
        
        # Handle specific query types with custom prompts
        if any(word in query_lower for word in ['project', 'work', 'build', 'develop']):
            return self.generate_project_response(query)
        elif any(word in query_lower for word in ['skill', 'technology', 'programming', 'code']):
            return self.generate_skill_response(query)
        elif any(word in query_lower for word in ['experience', 'job', 'career', 'background']):
            return self.generate_experience_response(query)
        else:
            return self.generate_response(query)
            
    def generate_project_response(self, query):
        """Generate project-focused response"""
        if not self.context_data.get('projects'):
            return "I have several exciting projects! Check out my GitHub for the latest work."
            
        projects = self.context_data['projects'][:3]  # Top 3 projects
        project_names = [p.get('name', 'Project') for p in projects if isinstance(p, dict)]
        
        prompt = f"I've worked on projects like {', '.join(project_names)}. {query}"
        return self.generate_response(prompt, max_length=120)
        
    def generate_skill_response(self, query):
        """Generate skill-focused response"""
        if not self.context_data.get('skills'):
            return "I have experience with various programming languages and technologies."
            
        skills = ', '.join(self.context_data['skills'][:6])
        prompt = f"My technical skills include {skills}. {query}"
        return self.generate_response(prompt, max_length=100)
        
    def generate_experience_response(self, query):
        """Generate experience-focused response"""
        if not self.context_data.get('experience'):
            return "I have professional experience in software development and engineering."
            
        experience = self.context_data['experience'][0]  # Most recent experience
        role = experience.get('role', 'Developer')
        company = experience.get('company', 'a tech company')
        
        prompt = f"I worked as {role} at {company}. {query}"
        return self.generate_response(prompt, max_length=120)
        
    def is_available(self):
        """Check if AI functionality is available"""
        return self.chatbot is not None
        
    def get_model_info(self):
        """Get information about the loaded model"""
        if not self.chatbot:
            return "No AI model loaded"
            
        return f"Using {self.model_name} for AI responses"

# Utility functions for the main assistant
def create_ai_chat(model_name="gpt2"):
    """Factory function to create AI chat instance"""
    return AIChat(model_name)

def test_ai_functionality():
    """Test AI functionality"""
    if not AI_AVAILABLE:
        print("❌ AI functionality not available")
        return False
        
    try:
        ai = AIChat()
        if ai.is_available():
            test_response = ai.generate_response("What programming languages do you know?")
            print(f"✅ AI test successful: {test_response[:50]}...")
            return True
        else:
            print("❌ AI model failed to load")
            return False
    except Exception as e:
        print(f"❌ AI test failed: {e}")
        return False

if __name__ == "__main__":
    # Test the AI functionality
    print("🧪 Testing AI Chat functionality...")
    test_ai_functionality()