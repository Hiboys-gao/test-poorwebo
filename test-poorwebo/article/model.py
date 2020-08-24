from libs.pub import db


class Article(db.Model):
    __tablename__='article'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50) , nullable=False)
    content=db.Column(db.Text,nullable=False)
    datetime=db.Column(db.DateTime)