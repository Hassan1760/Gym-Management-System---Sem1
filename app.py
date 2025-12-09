from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/membership")
def membership():
    plans = [
        {
            "name": "Basic Plan",
            "price": "$9 / month",
            "features": ["Access to gym floor", "Locker facility", "1 Trainer session/week"]
        },
        {
            "name": "Pro Plan",
            "price": "$29 / month",
            "features": ["All Basic features", "Unlimited trainer sessions", "Diet & workout plan"]
        },
        {
            "name": "Elite Plan",
            "price": "$99 / month",
            "features": ["All Pro features", "24/7 Access", "Personal trainer + Nutritionist"]
        }
    ]
    return render_template("membership.html", plans=plans)
if __name__ == "__main__":
    app.run(debug=True)
