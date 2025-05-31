# AI Resume Analyzer

A simple and fast Flask-based web app that analyzes resumes by detecting key skills and generating AI-powered improvement tips.

## Features

- Detects keywords like Python, Git, Docker, React, etc.
- Calculates a match score (%)
- Shows top missing skills
- Generates AI suggestions using OpenAI GPT-3.5
- Clean, responsive interface (HTML/CSS)

## Tech Stack
- Python 3  
- Flask  
- OpenAI API  
- HTML / CSS / Jinja2  
- dotenv for environment variable handling

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root directory:
   ```
   OPENAI_API_KEY=your_openai_key_here
   ```

5. **Run the app**
   ```bash
   python app.py
   ```

6. **Open in browser**
   ```
   http://localhost:5000
   ```

## Security Note

- Your `.env` file should **NOT** be committed. It’s excluded by `.gitignore`.

## Example Keywords Used

`python`, `c#`, `docker`, `git`, `rest api`, `tdd`, `sql`, `react`, `asp.net`, `flask`