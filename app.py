from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    name = request.form["name"]
    goal = request.form["goal"]
    skills = request.form["skills"]
    education = request.form["education"]

    prompt = f"""
You are an AI Career Roadmap Generator.

Student Details:
Name: {name}
Career Goal: {goal}
Current Skills: {skills}
Education: {education}

Create a VISUAL TEXT CAREER ROADMAP.

Follow this EXACT format.

══════════════════════════════════════

🎯 CAREER GOAL
{goal}

⬇

📍 CURRENT SKILLS
• Mention the student's current skills

⬇

🚧 SKILL GAPS
• List only the missing skills

⬇

🗓️ LEARNING ROADMAP

🌱 Week 1
• 3 learning topics

⬇

🌿 Week 2
• 3 learning topics

⬇

🌳 Week 3
• 3 learning topics

⬇

🚀 Week 4
• 3 learning topics

⬇

💻 BUILD THESE PROJECTS
• Project 1
• Project 2
• Project 3

⬇

🎤 INTERVIEW PREPARATION
• Technical Questions
• HR Questions

⬇

📄 RESUME TIPS

⬇

🏆 READY FOR INTERNSHIP

══════════════════════════════════════

Rules:
- Use arrows (⬇) between every section.
- Use bullet points.
- Do NOT write long paragraphs.
- Keep each section short.
- Make it look like a roadmap, not an essay.
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        result = response.text

    except Exception as e:

        result = f"""
⚠️ Gemini AI is temporarily unavailable.

Reason:
{e}
"""

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)