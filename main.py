from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

all_books = []
#Create a new table
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

# db.create_all()

@app.route('/')
def home():
    books = Books.query.all()
    return render_template('index.html', books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Books(title=request.form.get("title"), author=request.form.get("author"), rating=request.form.get("rating"))
        # new_book = Books({
        #     "title": request.form.get("title"),
        #     "author": request.form.get("author"),
        #     "rating": request.form("rating"),
        # })
        # all_books.append(new_book)

        db.session.add(new_book)
        db.session.commit()


        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

