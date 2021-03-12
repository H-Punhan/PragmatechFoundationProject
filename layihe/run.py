from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db/test.db'
db=SQLAlchemy(app)
migrate=Migrate(app,db)

class knowledges(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

class education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    year=db.Column(db.Integer)
    school=db.Column(db.String(50))
    lesson=db.Column(db.String(50))
    description=db.Column(db.String(200))

class experience(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    year=db.Column(db.Integer)
    company=db.Column(db.String(50))
    work=db.Column(db.String(50))
    description=db.Column(db.String(200))

class skills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    level=db.Column(db.Integer)




@app.route('/admin')
def admin():
    
    return render_template('admin/admin.html')
@app.route('/admin/add/')
def add():
    
    return render_template('admin/add.html')

@app.route('/admin/add/knowledge',methods=['GET','POST'])
def admin_add_know():
    if request.method=='POST' and request.form['know']!='':
        know=knowledges(name=request.form['know'])
        db.session.add(know)
        db.session.commit()
        return redirect('/resume')

    return render_template('admin/knowledge.html')

@app.route('/admin/add/skills',methods=['GET','POST'])
def admin_add_skills():
    if request.method=='POST':
        if request.form['skillname']!='' and request.form['skilllevel']!='':
            
                data=skills(name=request.form['skillname'],level=request.form['skilllevel'])
                db.session.add(data)
                db.session.commit()
                return redirect('/resume') 
        
    return render_template('admin/skills.html')

@app.route('/admin/add/education',methods=['GET','POST'])
def admin_add_education():
    if request.method=='POST':
        year=request.form['year']
        schol=request.form['school']
        les=request.form['lesson']
        des=request.form['description']
        if year!='' and schol!='' and les!='' and des!='':
            data=education(year=year,school=schol,lesson=les,description=des)
            db.session.add(data)
            db.session.commit()
            return redirect('/resume')
    return render_template('admin/education.html')
# --------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    
    return render_template('index.html')

@app.route('/resume')
def resume():
    kno=knowledges.query.all()
    skill=skills.query.all()
    educations=education.query.all()
    return render_template('resume.html',data=kno,skil=skill,edu=educations)


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

    
    

 
if __name__=='__main__':
    app.run(debug=True)

