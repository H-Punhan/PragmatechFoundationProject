from setting import app,render_template,redirect,request
from model import *
@app.route('/admin')
def admin():
    
    return render_template('admin/src/index.html')

@app.route('/admin/profile')
def profile():
    data=authors.query.all()
    return render_template('admin/src/profile.html',data=data)

@app.route('/admin/add/')
def add():
    
    return render_template('admin/src/add.html')

@app.route('/admin/add/author',methods=['GET','POST'])
def admin_add_author():
    if request.method=='POST' and request.form['name']!='' and request.form['desc']!='':
        
        data=authors(fullname=request.form['name'],about=request.form['desc'])
        db.session.add(data)
        db.session.commit()
        
        return redirect('/admin/add/author')

    return render_template('admin/src/add-authors.html')

@app.route('/admin/add/knowledge',methods=['GET','POST'])
def admin_add_know():
    if request.method=='POST' and request.form['know']!='':
        know=knowledges(name=request.form['know'])
        db.session.add(know)
        db.session.commit()
        return redirect('/resume')

    return render_template('admin/src/add-know.html')

@app.route('/admin/add/skills',methods=['GET','POST'])
def admin_add_skills():
    if request.method=='POST':
        if request.form['skillname']!='' and request.form['skilllevel']!='':
            
                data=skills(name=request.form['skillname'],level=request.form['skilllevel'])
                db.session.add(data)
                db.session.commit()
                return redirect('/resume') 
        
    return render_template('admin/src/add-skill.html')

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

@app.route('/admin/add/experience',methods=['GET','POST'])
def admin_add_experience():

    if request.method=='POST':
        year=request.form['year']
        company=request.form['company']
        work=request.form['work']
        description=request.form['description']
        if year!='' and work!='' and company!='' and description!='':
            
            data=experience(year=year,company=company,work=work,description=description)
            db.session.add(data)
            db.session.commit()
            return redirect('/resume')
    return render_template('admin/experience.html')








