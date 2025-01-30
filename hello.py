from flask import Flask, render_template
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

app = Flask(__name__)

def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    return str(soup)

@app.route("/epub")
def view_epub():
    book = epub.read_epub('data/plath-bell-jar.epub')
    
    # Get the book title
    title = book.get_metadata('DC', 'title')[0][0] if book.get_metadata('DC', 'title') else "The Bell Jar"
    
    # Process chapters
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append({
                'title': item.get_name(),
                'content': chapter_to_str(item)
            })
    
    return render_template('epub_viewer.html', title=title, chapters=chapters)

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
