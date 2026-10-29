from flask import Flask, render_template, request, redirect

app = Flask(__name__)

ACCOUNT_DATA = {"balance": 100}

@app.route("/")
def index():
    return render_template("index.html", balance=ACCOUNT_DATA["balance"])

@app.route("/deposit", methods=["POST"])
def deposit():
    amount = float(request.form.get("amount", 0))
    if amount > 0:
        ACCOUNT_DATA["balance"] += amount
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
