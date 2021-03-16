from setting import app,render_template,redirect,request
from model import *
@app.route('/')
def index():
    about=authors.query.all()
    return render_template('index.html',data=about)

@app.route('/about')
def about():
    about=authors.query.all()
    return render_template('index.html',data=about)

@app.route('/resume')
def resume():
    kno=knowledges.query.all()
    skill=skills.query.all()
    educations=education.query.all()
    experiences=experience.query.all()
    return render_template('resume.html',data=kno,skil=skill,edu=educations,exp=experiences)


@app.route('/portfolio')
def portfolio():
    
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    
    return render_template('blog.html')

@app.route('/contact')
def contact():
    
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')
