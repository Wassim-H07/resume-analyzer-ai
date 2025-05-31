import os
import openai
from flask import Flask, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)

# Load .env file variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Keywords to match
KEYWORDS = ["python", "c#", "docker", "git", "rest api", "tdd", "sql", "react", "asp.net", "flask"]

# Function to generate AI feedback using OpenAI
def get_ai_feedback(resume_text):
    prompt = f"""
Review the following CV and provide 3 concise, helpful suggestions to improve it.
Focus on technical strength, clarity, and missing keywords.

CV:
{resume_text}
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional CV reviewer and career advisor."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"AI feedback unavailable: {e}"

# Flask route for the home page and CV form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cv_text = request.form["cv_text"].lower()

        # Match and score keywords
        matched_keywords = [kw for kw in KEYWORDS if kw in cv_text]
        missing_keywords = [kw for kw in KEYWORDS if kw not in matched_keywords]
        score = int(len(matched_keywords) / len(KEYWORDS) * 100)

        # Get AI feedback
        ai_feedback = get_ai_feedback(cv_text)

        return render_template(
            "result.html",
            score=score,
            keywords=matched_keywords,
            missing_keywords=missing_keywords,
            ai_feedback=ai_feedback
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)