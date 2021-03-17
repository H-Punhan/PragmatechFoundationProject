from setting import app,render_template,redirect,request
from model import *
@app.route('/admin')
def admin():
    
    return render_template('admin/src/index.html')

@app.route('/admin/about')
def profile():
    data=authors.query.all()
   
    return render_template('admin/src/profile.html',data=data)

# ADD  ROUTES
@app.route('/admin/add/')
def add():
    
    return render_template('admin/src/adddata/add.html')

@app.route('/admin/add/author',methods=['GET','POST'])
def admin_add_author():
    if request.method=='POST' and request.form['name']!='' and request.form['desc']!='':
        
        data=authors(fullname=request.form['name'],about=request.form['desc'])
        db.session.add(data)
        db.session.commit()
        
        return redirect('/admin/add/author')

    return render_template('admin/src/adddata/add-authors.html')

@app.route('/admin/add/knowledge',methods=['GET','POST'])
def admin_add_know():
    data=knowledges.query.all()
    if request.method=='POST' and request.form['know']!='':
        know=knowledges(name=request.form['know'])
        db.session.add(know)
        db.session.commit()
        return redirect('/resume')

    return render_template('admin/src/adddata/add-know.html',data=data)

@app.route('/admin/add/skills',methods=['GET','POST'])
def admin_add_skills():
    data=skills.query.all()
    if request.method=='POST':
        if request.form['skillname']!='' and request.form['skilllevel']!='':
            
                data=skills(name=request.form['skillname'],level=request.form['skilllevel'])
                db.session.add(data)
                db.session.commit()
                return redirect('/resume') 
        
    return render_template('admin/src/adddata/add-skill.html',data=data)

@app.route('/admin/add/education',methods=['GET','POST'])
def admin_add_education():
    data=education.query.all()
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
    return render_template('admin/src/adddata/add-education.html',data=data)

@app.route('/admin/add/experience',methods=['GET','POST'])
def admin_add_experience():
    data=experience.query.all()
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
    return render_template('admin/src/adddata/add-experience.html',data=data)

@app.route('/admin/add/tags',methods=['GET','POST'])
def admin_add_tags():
    data=tags.query.all()
    if request.method=='POST' and request.form['tagname'] !='':
        add=tags(name=request.form['tagname'])
        db.session.add(add)
        db.session.commit()
        return redirect('/admin/add/tags')
        

    return render_template('admin/src/adddata/add-tags.html',data=data)
    

#UPDATE ROUTES

@app.route('/admin/update/about/<id>',methods=['GET','POST'])
def update_profile(id):
    sdata=authors.query.filter_by(id=id).first()
    if request.method=='POST' and request.form['fullname']!='' and request.form['desc']!='':
        sdata.fullname=request.form['fullname']
        sdata.about=request.form['desc']
        db.session.commit()
  
    return redirect('/admin/about')


# DELETE ROUTES

@app.route('/admin/delete/knowledge/<id>')
def delete_knowledge(id):
    data=knowledges.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/admin/add/knowledge')

@app.route('/admin/delete/skills/<id>')
def delete_skills(id):
    data=skills.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/admin/add/skills')

@app.route('/admin/delete/education/<id>')
def delete_education(id):
    data=education.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/admin/add/education')

@app.route('/admin/delete/experience/<id>')
def delete_experience(id):
    data=experience.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/admin/add/experience')



@app.route('/admin/delete/tags/<id>')
def delete_tag(id):
    data=tags.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/admin/add/tags')





