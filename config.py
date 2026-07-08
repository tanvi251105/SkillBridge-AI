import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "skillbridge_ai_secret"

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

DATABASE = os.path.join(BASE_DIR, "database", "users.db")