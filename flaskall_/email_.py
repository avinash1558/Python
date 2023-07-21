#pip install flask
#pip install flask_sqlalchemy
#pip install flask_mail

from flask import Flask, render_template ,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime

app=Flask(__name__)
# mail config
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME='as0223080@gmail.com',
    MAIL_PASSWORD='8286585455'
)
mail=Mail(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pizza'
# data=SQLAlchemy(app)

# class Contact(data.Model):
#     sno=data.Column(data.Integer,primary_key=True)
#     # name=data.Column(data.String(10),unique=False,nullable=False)
#     name=data.Column(data.String(100),nullable=False)
#     email=data.Column(data.String(100),nullable=False)
#     password=data.Column(data.String(100),nullable=False)
#     feedb=data.Column(data.String(100),nullable=False)
#     date=data.Column(data.String(12),nullable=True)

@app.route('/',methods=['GET','POST'])
def home():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        feed=request.form.get('feed')
        # entry=Contact(name=name,email=email,password=password,feedb=feed,date=datetime.now())
        # data.session.add(entry)
        # data.session.commit()
        mail.send_message('New message'+name,
                          sender=email,
                          recipients=['as0223080@gmail.com'],
                          body=feed+"\n"+email +password
                        )
                        # 1st allow to less secure app
    return render_template('html1.html')
app.run(debug=True)