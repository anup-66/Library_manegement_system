import os
from flask import Flask, render_template, request,jsonify
from main import Index
app = Flask(__name__)
index = Index()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/issue", methods=["GET", "POST"])
def issue():
    if request.method == "POST":
        book = request.form.get("book")
        index = Index()
        issued = index.issue(book)
        if issued:
            return render_template("issue.html",book=book,issued="is issued")
        else:

            return render_template("issue.html",book=book,issued="is not issued")
    else:
        return render_template("issue.html",issued="is not issued")

@app.route("/return", methods=["GET", "POST"])
def return_book():
    if request.method == "POST":
        book = request.form.get("book")
        index = Index()
        returned = index.return_book(book)
        # return render_template("return.html",returned=returned)
        return jsonify({"book": book, "status": "returned"})
    else:
        return render_template("return.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        book = request.form.get("book")
        index = Index()
        count,book = index.search_book(book)
        return render_template("search.html",count=count , book=book)
    else:
        return render_template("search.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        id = request.form.get("id")
        book_name = request.form.get("book_name")
        no_of_books = int(request.form.get("no_of_books"))
        index = Index()
        add = index.addit(id,book_name, no_of_books)
        if add:
            return render_template("add.html",add="Added successfully")
        else:
            return render_template("add.html",add="Not authorised")
    else:
        return render_template("add.html")

@app.route("/count", methods=["GET", "POST"])
def count():
    if request.method == "POST":
        book = request.form.get("book")
        index = Index()
        count = index.count(book)
        ll = index.list_books()
        print(ll)
        # count, book = index.search_book(book)
        return render_template("count.html", Text = 'There are ',count=count,Books = 'books')
    else:
        return render_template("count.html")

@app.route("/list", methods=["GET", "POST"])
def list():
    if request.method == "GET":

        index = Index()
        list_books  = index.list_books()
        # print("yesssss",list_books)
        return render_template("list.html",Map = list_books)
    else:
        return render_template("list.html")

if __name__ == "__main__":
    app.run(debug=True)