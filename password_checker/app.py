from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$&*^~]", password):
        score += 1

    if score <= 2:
        return "Weak", "red", 30
    elif score <= 4:
        return "Medium", "orange", 60
    else:
        return "Strong", "green", 100

@app.route("/", methods=["GET", "POST"])
def index():
    strength = ""
    color = ""
    percent = 0

    if request.method == "POST":
        password = request.form["password"]
        strength, color, percent = check_password(password)

    return render_template(
        "index.html",
        strength=strength,
        color=color,
        percent=percent
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
