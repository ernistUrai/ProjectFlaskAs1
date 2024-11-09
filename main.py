from django.shortcuts import redirect
from flask import Flask, render_template,  request # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///story.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime)
    
    def __repr__(self):
        return '<Story %r>' % self.id
    
    

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")






if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)