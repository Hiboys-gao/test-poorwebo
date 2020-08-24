from libs.pub import db


class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16) , nullable=False)
    password=db.Column(db.String(16),nullable=False)
    gender=db.Column(db.String(16),default='保密')
    age=db.Column(db.Integer,default=0)
    city=db.Column(db.String(16),default='保密')
    tel=db.Column(db.String(16),unique=True,nullable=False)