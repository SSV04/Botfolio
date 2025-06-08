#!/usr/bin/env python3
"""
Setup script for Botfolio - AI CLI Portfolio

Author: SSV
Date: June 2025
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = []
try:
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
except FileNotFoundError:
    requirements = [
        'colorama>=0.4.6',
        'pyjokes>=0.6.0',
    ]

setup(
    name="botfolio",
    version="1.0.0",
    author="SSV",
    author_email="ssv.dev@example.com",
    description="Botfolio - AI CLI Portfolio - An interactive command-line bot showcasing your portfolio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SSV04/Botfolio",
    project_urls={
        "Bug Tracker": "https://github.com/SSV04/Botfolio/issues",
        "Documentation": "https://github.com/SSV04/Botfolio/wiki",
        "Source Code": "https://github.com/SSV04/Botfolio",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Office/Business",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "ai": [
            "transformers>=4.21.0",
            "torch>=1.12.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
        ],
        "full": [
            "transformers>=4.21.0",
            "torch>=1.12.0",
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "portfolio-bot=assistant:main",
            "ai-portfolio=assistant:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.txt", "*.md"],
    },
    keywords=[
        "portfolio",
        "cli",
        "chatbot",
        "ai",
        "assistant",
        "interactive",
        "resume",
        "career",
        "showcase",
        "terminal",
        "command-line",
    ],
    zip_safe=False,
)