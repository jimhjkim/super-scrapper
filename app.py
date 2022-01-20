from flask import Flask, render_template, request

app = Flask("SuperScraper")

# app.run(debug=True)
# app.env("development")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    return render_template("report.html", word=word)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
