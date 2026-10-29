from flask import Flask, render_template, request, redirect

app = Flask(__name__)

ACCOUNT_DATA = {"balance": 100, "error": None}

@app.route("/")
def index():
    error = ACCOUNT_DATA.get("error")
    ACCOUNT_DATA["error"] = None
    return render_template("index.html", balance=ACCOUNT_DATA["balance"], error=error)

@app.route("/deposit", methods=["POST"])
def deposit():
    amount = float(request.form.get("amount", 0))
    if amount > 0:
        ACCOUNT_DATA["balance"] += amount
    return redirect("/")

@app.route("/withdraw", methods=["POST"])
def withdraw():
    amount = float(request.form.get("amount", 0))
    if amount > ACCOUNT_DATA["balance"]:
        ACCOUNT_DATA["error"] = "Insufficient funds"
    elif amount > 0:
        ACCOUNT_DATA["balance"] -= amount
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
