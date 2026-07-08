from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from database.db import get_connection

auth = Blueprint("auth", __name__)


# ------------------------
# SIGNUP
# ------------------------
@auth.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        existing = cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        if existing:

            flash("Email already registered!", "danger")

            conn.close()

            return redirect(url_for("auth.signup"))

        hashed_password = generate_password_hash(password)

        cursor.execute(
            """
            INSERT INTO users(name,email,password)
            VALUES(?,?,?)
            """,
            (
                name,
                email,
                hashed_password
            )
        )

        conn.commit()
        conn.close()

        flash("Account created successfully!", "success")

        return redirect(url_for("auth.login"))

    return render_template("signup.html")


# ------------------------
# LOGIN
# ------------------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip().lower()
        password = request.form["password"]

        conn = get_connection()

        cursor = conn.cursor()

        user = cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email=?
            """,
            (email,)
        ).fetchone()

        conn.close()

        if user:

            if check_password_hash(
                user["password"],
                password
            ):

                session["user_id"] = user["id"]
                session["user_name"] = user["name"]

                return redirect("/dashboard")

        flash("Invalid email or password!", "danger")

    return render_template("login.html")


# ------------------------
# LOGOUT
# ------------------------
@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/")