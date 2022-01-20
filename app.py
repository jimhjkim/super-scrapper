from flask import Flask, render_template, request, redirect
from scraper import get_jobs

app = Flask("SuperScraper")

db = {}
# app.run(debug=True)
# app.env("development")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        from_db = db.get(word)
        if from_db:
            jobs = from_db
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", word=word, resultsCount=len(jobs))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
