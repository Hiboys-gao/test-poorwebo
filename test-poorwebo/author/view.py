from flask import Blueprint,request,render_template,session,redirect

from libs.pub import db
from author.model import User


user_bp=Blueprint('user',__name__,url_prefix='/user',template_folder='./templates')


@user_bp.route('/home')
def home():
    return render_template('home.html')

@user_bp.route('/login',methods=('POST','GET'))
def login():
    if request.method=='POST':
        name=request.form.get('name')
        password=request.form.get('password')

        user=User.query.filter_by(name=name).one()
        if user:
            if user.password == password:
                session['uid']=user.id
                session['username']=user.name
                return redirect('/article/home')
            else:
                return '密码错误'
        else:
            return '账号不存在'
    else:
        return render_template('login.html')

@user_bp.route('/register',methods=('POST','GET'))
def register():
    if request.method=='POST':
        name=request.form.get('name')
        password=request.form.get('password')
        gender=request.form.get('gender')
        age=request.form.get('age')
        city=request.form.get('city')
        tel=request.form.get('tel')

        username= User.query.filter_by(name).one()
        if not username:
            user=User(name=name,password=password,gender=gender,age=age,city=city,tel=tel)
            db.session.add(user)
            db.session.commit()

            redirect('/author/login')
        else:
            return '用户名已存在'

    else:
        render_template('register.html')

@user_bp.route('/logout')
def logout():
    session.pop(key=('uid','username'))
    return redirect('/')