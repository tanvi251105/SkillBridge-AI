from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for
)

from dotenv import load_dotenv

from google import genai

from werkzeug.utils import secure_filename

import os
import pathlib
import sqlite3

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

# ==========================================
# FLASK APP
# ==========================================

app = Flask(__name__)

app.secret_key = "skillbridge_ai_secret_key"

# ==========================================
# GEMINI
# ==========================================

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ==========================================
# DATABASE
# ==========================================

DATABASE = "database/users.db"

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {
    "pdf",
    "doc",
    "docx"
}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

pathlib.Path(UPLOAD_FOLDER).mkdir(
    exist_ok=True
)

# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT UNIQUE,

        password TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS reports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        career_goal TEXT,

        report TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()

    conn.close()


create_tables()

# ==========================================
# HELPERS
# ==========================================

def allowed_file(filename):

    return "." in filename and \
    filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")

# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:

        return redirect("/login")

    return render_template(

        "dashboard.html",

        name=session["user_name"]

    )

# ==========================================
# RESUME PAGE
# ==========================================

@app.route("/resume")
def resume():

    if "user_id" not in session:

        return redirect("/login")

    return render_template("resume.html")

# ==========================================
# AI CAREER ANALYSIS
# ==========================================

@app.route("/analyze", methods=["POST"])
def analyze():

    name = request.form["name"]

    goal = request.form["goal"]

    skills = request.form["skills"]

    education = request.form["education"]

    prompt = f"""

You are SkillBridge AI.

Student Name : {name}

Career Goal : {goal}

Skills : {skills}

Education : {education}

Generate a structured career roadmap.

Return sections:

🎯 Career Goal

📊 Current Skills

❌ Skill Gap

🗓️ 30-Day Learning Plan

Week 1

Week 2

Week 3

Week 4

💻 Projects

🎤 Interview Questions

📄 Resume Tips

🏆 Final Advice

Use bullet points.

"""

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash-lite",

            contents=prompt

        )

        report = response.text

    except Exception as e:

        report = f"Error : {e}"

    if "user_id" in session:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """

            INSERT INTO reports

            (user_id,career_goal,report)

            VALUES(?,?,?)

            """,

            (

                session["user_id"],

                goal,

                report

            )

        )

        conn.commit()

        conn.close()

    return render_template(

        "index.html",

        result=report

    )
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for
)

from dotenv import load_dotenv

from google import genai

from werkzeug.utils import secure_filename

import os
import pathlib
import sqlite3

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

# ==========================================
# FLASK APP
# ==========================================

app = Flask(__name__)

app.secret_key = "skillbridge_ai_secret_key"

# ==========================================
# GEMINI
# ==========================================

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ==========================================
# DATABASE
# ==========================================

DATABASE = "database/users.db"

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {
    "pdf",
    "doc",
    "docx"
}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

pathlib.Path(UPLOAD_FOLDER).mkdir(
    exist_ok=True
)

# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT UNIQUE,

        password TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS reports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        career_goal TEXT,

        report TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()

    conn.close()


create_tables()

# ==========================================
# HELPERS
# ==========================================

def allowed_file(filename):

    return "." in filename and \
    filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")

# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:

        return redirect("/login")

    return render_template(

        "dashboard.html",

        name=session["user_name"]

    )

# ==========================================
# RESUME PAGE
# ==========================================

@app.route("/resume")
def resume():

    if "user_id" not in session:

        return redirect("/login")

    return render_template("resume.html")

# ==========================================
# AI CAREER ANALYSIS
# ==========================================

@app.route("/analyze", methods=["POST"])
def analyze():

    name = request.form["name"]

    goal = request.form["goal"]

    skills = request.form["skills"]

    education = request.form["education"]

    prompt = f"""

You are SkillBridge AI.

Student Name : {name}

Career Goal : {goal}

Skills : {skills}

Education : {education}

Generate a structured career roadmap.

Return sections:

🎯 Career Goal

📊 Current Skills

❌ Skill Gap

🗓️ 30-Day Learning Plan

Week 1

Week 2

Week 3

Week 4

💻 Projects

🎤 Interview Questions

📄 Resume Tips

🏆 Final Advice

Use bullet points.

"""

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash-lite",

            contents=prompt

        )

        report = response.text

    except Exception as e:

        report = f"Error : {e}"

    if "user_id" in session:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """

            INSERT INTO reports

            (user_id,career_goal,report)

            VALUES(?,?,?)

            """,

            (

                session["user_id"],

                goal,

                report

            )

        )

        conn.commit()

        conn.close()

    return render_template(

        "index.html",

        result=report

    )