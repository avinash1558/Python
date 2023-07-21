#pip install flask
#pip install flask_sqlalchemy 
from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.secret_key="super-secret-key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/data2'
data = SQLAlchemy(app)


class First(data.Model):
    sn = data.Column(data.Integer, primary_key=True)
    title = data.Column(data.String(30), nullable=False)
    slg = data.Column(data.String(20), nullable=False)
    date = data.Column(data.String(12), nullable=True)


@app.route('/')
def home():
    post = First.query.filter_by().all()[0:1]
    return render_template('html1.html', post=post)

@app.route('/edit/<string:sn>',methods=['GET', 'POST'])
def edit(sn):
    if "user" in session and session["user"]=="avinash":
        if request.method=="POST":
            title=request.form.get("title")
            slg=request.form.get("slg")
            if sn=="0":
                post=First(title=title,slg=slg,date=datetime.now())
                data.session.add(post)
                data.session.commit()
            else:
                post=First.query.filter_by(sn=sn).first()
                post.title=title
                post.slg=slg
                data.session.commit()
                return redirect(f"/edit/{sn}")
        post=First.query.filter_by(sn=sn).first()
        return render_template('edit.html',post=post)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if "user" in session and session["user"]=="avinash":
        post=First.query.all()
        return render_template("admin.html",post=post)

    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username=="avinash" and password=="password":
            post=First.query.all()
            session["user"]=username
            return render_template("admin.html",post=post)
    return render_template("login.html")
@app.route('/logout')
def home3():
    session.pop('user')
    return redirect("/admin")
# @app.route("/post/<string:get_data>", methods=['GET'])
# def post_requesting(get_data):
#     getting = First.query.filter_by(slg=get_data).first()
#     return render_template('poster.html', post=getting)


app.run(debug=True)
