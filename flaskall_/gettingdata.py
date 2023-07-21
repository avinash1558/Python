#pip install flask
#pip install flask_sqlalchemy

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/data2'
data = SQLAlchemy(app)

class First(data.Model):
    sn = data.Column(data.Integer, primary_key=True)
    # name=data.Column(data.String(10),unique=False,nullable=False)
    title = data.Column(data.String(30), nullable=False)
    slg = data.Column(data.String(20), nullable=False)
    date = data.Column(data.String(12), nullable=True)

@app.route('/')
def home():
    post=First.query.filter_by().all()[0:4]
    return render_template('html1.html',post= post)
@app.route('/post')
def homepost():
    post=First.query.filter_by().all()[0:4]
    return render_template('allpost.html',post= post)

@app.route("/post/<string:get_data>", methods=['GET'])
def post_requesting(get_data):
    getting = First.query.filter_by(slg=get_data).first()
    return render_template('poster.html', post=getting)

app.run(debug=True)


