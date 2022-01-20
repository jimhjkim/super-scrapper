from flask import Flask

app = Flask("SuperScraper")

# app.run(debug=True)
# app.env("development")


@app.route("/")
def home():
    return "Hello! Welcome to mi casa!"


@app.route("/<username>")
def contact(username):
    return f"Hello {username} how are you doing?"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
