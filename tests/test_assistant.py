#!/usr/bin/env python3
"""
Unit Tests for Botfolio - AI CLI Portfolio

Author: SSV
Date: June 2025
"""

import unittest
import json
import tempfile
import os
from pathlib import Path
import sys

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from assistant import PortfolioAssistant
except ImportError as e:
    print(f"Failed to import assistant: {e}")
    sys.exit(1)

class TestPortfolioAssistant(unittest.TestCase):
    """Test cases for the Portfolio Assistant"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create a temporary data file for testing
        self.test_data = {
            "name": "Test User",
            "title": "Test Developer",
            "school": "Test University",
            "degree": "Computer Science",
            "skills": ["Python", "JavaScript", "Testing"],
            "projects": [
                {"name": "Test Project", "description": "A test project"},
                {"name": "Another Project", "description": "Another test project"}
            ],
            "contact": {
                "email": "test@example.com",
                "github": "https://github.com/testuser"
            },
            "certifications": ["Test Certification"],
            "experience": [
                {"role": "Test Developer", "company": "Test Corp", "duration": "2023-2024"}
            ]
        }
        
        # Create temporary file
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        json.dump(self.test_data, self.temp_file)
        self.temp_file.close()
        
        # Initialize assistant (we'll mock the data loading)
        self.assistant = PortfolioAssistant()
        self.assistant.data = self.test_data
        
    def tearDown(self):
        """Clean up test fixtures"""
        os.unlink(self.temp_file.name)
        
    def test_initialization(self):
        """Test assistant initialization"""
        self.assertIsNotNone(self.assistant.data)
        self.assertEqual(self.assistant.data['name'], "Test User")
        
    def test_resume_response(self):
        """Test resume information response"""
        response = self.assistant.get_resume_info()
        self.assertIn("Test User", response)
        self.assertIn("Test Developer", response)
        self.assertIn("Computer Science", response)
        
    def test_education_response(self):
        """Test education information response"""
        response = self.assistant.get_education_info()
        self.assertIn("Test University", response)
        self.assertIn("Computer Science", response)
        
    def test_projects_response(self):
        """Test projects information response"""
        response = self.assistant.get_projects_info()
        self.assertIn("Test Project", response)
        self.assertIn("Another Project", response)
        
    def test_skills_response(self):
        """Test skills information response"""
        response = self.assistant.get_skills_info()
        self.assertIn("Python", response)
        self.assertIn("JavaScript", response)
        self.assertIn("Testing", response)
        
    def test_contact_response(self):
        """Test contact information response"""
        response = self.assistant.get_contact_info()
        self.assertIn("test@example.com", response)
        self.assertIn("github.com/testuser", response)
        
    def test_certifications_response(self):
        """Test certifications information response"""
        response = self.assistant.get_certifications_info()
        self.assertIn("Test Certification", response)
        
    def test_experience_response(self):
        """Test experience information response"""
        response = self.assistant.get_experience_info()
        self.assertIn("Test Developer", response)
        self.assertIn("Test Corp", response)
        
    def test_joke_response(self):
        """Test joke functionality"""
        response = self.assistant.get_joke()
        self.assertIn("😄", response)
        # Should contain some joke content
        self.assertTrue(len(response) > 10)
        
    def test_help_response(self):
        """Test help information"""
        response = self.assistant.get_help()
        self.assertIn("Commands", response)
        self.assertIn("resume", response)
        self.assertIn("projects", response)
        
    def test_about_response(self):
        """Test about information"""
        response = self.assistant.get_about_info()
        self.assertIn("Assistant", response)
        self.assertIn("Python", response)
        
    def test_command_recognition(self):
        """Test command recognition functionality"""
        # Test resume commands
        response = self.assistant.get_response("resume")
        self.assertIn("Test User", response)
        
        response = self.assistant.get_response("cv")
        self.assertIn("Test User", response)
        
        # Test education commands
        response = self.assistant.get_response("school")
        self.assertIn("Test University", response)
        
        response = self.assistant.get_response("education")
        self.assertIn("Test University", response)
        
        # Test projects commands
        response = self.assistant.get_response("projects")
        self.assertIn("Test Project", response)
        
        # Test skills commands
        response = self.assistant.get_response("skills")
        self.assertIn("Python", response)
        
    def test_default_response(self):
        """Test default response for unrecognized commands"""
        response = self.assistant.get_response("random_unknown_command")
        self.assertIn("help", response.lower())
        
    def test_case_insensitive_commands(self):
        """Test that commands work regardless of case"""
        response1 = self.assistant.get_response("RESUME")
        response2 = self.assistant.get_response("resume")
        response3 = self.assistant.get_response("Resume")
        
        # All should contain the same key information
        for response in [response1, response2, response3]:
            self.assertIn("Test User", response)
            
    def test_partial_command_matching(self):
        """Test partial command matching"""
        # "school" should match education info
        response = self.assistant.get_response("tell me about school")
        self.assertIn("Test University", response)
        
        # "project" should match projects info
        response = self.assistant.get_response("what projects have you worked on")
        self.assertIn("Test Project", response)
        
    def test_empty_data_handling(self):
        """Test handling of missing data"""
        # Create assistant with minimal data
        minimal_data = {"name": "Test User"}
        self.assistant.data = minimal_data
        
        # Should not crash and should provide helpful message
        response = self.assistant.get_projects_info()
        self.assertIn("No projects", response)
        
        response = self.assistant.get_skills_info()
        self.assertIn("not available", response)

class TestDataValidation(unittest.TestCase):
    """Test data validation and error handling"""
    
    def test_sample_data_creation(self):
        """Test sample data creation when file is missing"""
        assistant = PortfolioAssistant()
        
        # Should create sample data if file is missing
        sample_data = assistant.create_sample_data()
        self.assertIsNotNone(assistant.data)
        self.assertIn("name", assistant.data)
        self.assertIn("skills", assistant.data)
        
    def test_malformed_json_handling(self):
        """Test handling of malformed JSON data"""
        # This would typically be tested with actual file I/O
        # For now, we test the data validation logic
        
        assistant = PortfolioAssistant()
        
        # Test with missing required fields
        incomplete_data = {"name": "Test"}
        assistant.data = incomplete_data
        
        # Should handle missing fields gracefully
        response = assistant.get_education_info()
        self.assertIn("Not specified", response)

class TestResponseFormatting(unittest.TestCase):
    """Test response formatting and styling"""
    
    def setUp(self):
        """Set up test assistant"""
        self.assistant = PortfolioAssistant()
        
    def test_response_contains_emojis(self):
        """Test that responses contain appropriate emojis"""
        response = self.assistant.get_resume_info()
        self.assertTrue(any(emoji in response for emoji in ["📄", "📋", "🎓"]))
        
        response = self.assistant.get_projects_info()
        self.assertTrue(any(emoji in response for emoji in ["🚀", "💻"]))
        
    def test_response_formatting(self):
        """Test that responses are properly formatted"""
        response = self.assistant.get_help()
        
        # Should contain proper sections
        self.assertIn("Commands", response)
        self.assertIn("•", response)  # Bullet points
        
    def test_color_codes_present(self):
        """Test that color codes are included in responses"""
        response = self.assistant.get_resume_info()
        # Should contain ANSI color codes (from colorama)
        self.assertTrue(any(code in response for code in ['\x1b[', 'Fore.']))

def run_tests():
    """Run all tests"""
    print("🧪 Running Portfolio Assistant Tests...")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestPortfolioAssistant))
    suite.addTests(loader.loadTestsFromTestCase(TestDataValidation))
    suite.addTests(loader.loadTestsFromTestCase(TestResponseFormatting))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    if result.wasSuccessful():
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ {len(result.failures)} test(s) failed")
        print(f"❌ {len(result.errors)} error(s) occurred")
        
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)