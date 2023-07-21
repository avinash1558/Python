#pip install flask
#pip install flask_sqlalchemy

from flask import Flask, render_template ,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

with open('jsonfile.json', 'r') as c:
    params = json.load(c)
    par=params['params']
    # print(par['database'])
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@localhost/{par["database"]}'
data=SQLAlchemy(app)

class Contact(data.Model):
    sno=data.Column(data.Integer,primary_key=True)
    # name=data.Column(data.String(10),unique=False,nullable=False)
    name=data.Column(data.String(100),nullable=False)
    email=data.Column(data.String(100),nullable=False)
    password=data.Column(data.String(100),nullable=False)
    feedb=data.Column(data.String(100),nullable=False)
    date=data.Column(data.String(12),nullable=True)

@app.route('/',methods=['GET','POST'])
def home():
    title=par["datatitle"]
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        feed=request.form.get('feed')
        entry=Contact(name=name,email=email,password=password,feedb=feed,date=datetime.now())
        data.session.add(entry)
        data.session.commit()
    return render_template('html1.html',name=title)
app.run(debug=True)


