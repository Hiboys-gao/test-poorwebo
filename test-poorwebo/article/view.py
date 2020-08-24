import datetime

from flask import Blueprint,request,render_template,session,redirect

from libs.pub import db
from article.model import Article


article_bp=Blueprint('article',__name__,url_prefix='/article',template_folder='./templates')

@article_bp.route('/home')
def home():
    articles=Article.query.order_by(Article.id.desc()).all()
    art_info=[]
    for article in articles:
        title=article.title
        datetime=article.datetime
        uid=article.id
        info=[title,datetime,uid]
        art_info.append(info)

    render_template('home.html',art_info=art_info)

@article_bp.route('/art_info')
def art_info():
    uid = request.args.get('uid')
    article=Article.query.get(uid).one()
    return render_template('art_info.html',uid=uid,article=article)

@article_bp.route('/write',methods=('POST','GET'))
def write():
    if request.method=='POST':
        title=request.form.get('title')
        content=request.form.get('content')
        article=Article(title=title,content=content,datetime=datetime.datetime.now())
        db.session.add(article)
        db.session.commit()
        session['title']=title
        return redirect('/article/home')
    else:
        return render_template('write.html')

@article_bp.route('/del')
def delete():
    uid=request.args.get('uid')
    Article.query.get(uid).delete()
    redirect('/article/home')