from flask import Flask,render_template,request,redirect
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

@app.route('/admin/add/addknowledge',methods=['GET','POST'])
def admin_add_know():
    if request.method=='POST' and request.form['know']!='':
        know=knowledges(name=request.form['know'])
        db.session.add(know)
        db.session.commit()
        return redirect('/resume')

    return render_template('admin/addknowledge.html')

@app.route('/admin/add/addskills',methods=['GET','POST'])
def admin_add_skills():
    if request.method=='POST':
        if request.form['skillname']!='' and request.form['skilllevel']!='':
            
                data=skills(name=request.form['skillname'],level=request.form['skilllevel'])
                db.session.add(data)
                db.session.commit()
                return redirect('/resume') 
        
    return render_template('admin/addskills.html')

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
    return render_template('resume.html',data=kno,skil=skill)


@app.route('/portfolio')
def portfolio():
    
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    
    return render_template('blog.html')

@app.route('/contact')
def contact():
    
    return render_template('contact.html')



    
    

 
if __name__=='__main__':
    app.run(debug=True)

