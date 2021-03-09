from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db/test.db'
db=SQLAlchemy(app)
class todos(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    
    

@app.route('/')
def index():
    todo=todos.query.all()
    return render_template('crud/crud.html',data=todo)
@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST' and request.form['title']!='':
        new=todos(title=request.form['title'])
        db.session.add(new)
        db.session.commit()
        return redirect('/')
    else:return redirect('/')

@app.route('/updatelink/<id>',methods=['GET','POST'])
def updatelink(id):
    updateduser=todos.query.filter_by(id=id).first()
    if request.method=='POST':
        updateduser.title=request.form['title']
        db.session.commit()
        return redirect('/')
    return render_template('crud/crudupdate.html',data=updateduser)


    

@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    de=todos.query.filter_by(id=id).first()
    db.session.delete(de)
    db.session.commit()
    return redirect('/')
    

    
    

 
if __name__=='__main__':
    app.run(debug=True)

