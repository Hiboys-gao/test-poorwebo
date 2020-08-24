from flask import Flask,Blueprint,redirect,session

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from author.view import user_bp
from article.view import article_bp
from libs.pub import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:gao000@localhost:3306/p_weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db.init_app(app)
app.secret_key=r'M\xd2\x16\xa0K\x01\x0f@\x9f(\xab2V\xd7\xe3\x00'

manager=Manager(app)

migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

app.register_blueprint(user_bp)
app.register_blueprint(article_bp)

@app.route('/')
def home():
    return redirect('/author/home')

if __name__ == '__main__':
    manager.run()