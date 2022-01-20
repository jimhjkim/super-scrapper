from flask import Flask, render_template

app = Flask("SuperScraper")

# app.run(debug=True)
# app.env("development")


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
