from flask import Flask, render_template

app = Flask(__name__)

# Context
author_names = [
    {"name": "Peter"}, 
    {"name": "Bill"},
    {"name": "Clayton"}
]

@app.route("/")
def home():
    context = {
        "title"           : "Student Results Portal",
        "welcome_message" : "Welcome to the Student Results Portal",
        "description"     : "Here you can view student performance in the Python Challenge. Click on Results to see how students performed."
    }
    return render_template("base.html", **context)

@app.route("/authors")
def authors():
    context = {
        "title": "Authors",
        "author_names": author_names
    }
    return render_template("authors.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
