from flask import Flask, render_template
import flask_sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import engine
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
db = flask_sqlalchemy.SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
