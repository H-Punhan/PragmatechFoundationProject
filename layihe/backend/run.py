from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db=SQLAlchemy(app)
users=[]
id=0

class Posts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    content=db.Column(db.String(50))

@app.route('/',methods=["GET",'POST'])
def add():
    if request.method=='POST' and request.form['title'] !='' and request.form['content'] !='' :

        users=Posts(title=request.form['title'],content=request.form['content'])
        db.session.add(users)
        db.session.commit()
        d=Posts.query.all()
        return render_template('index.html',users=d)
    else:
        d=Posts.query.all()
        return render_template('index.html',users=d)

@app.route('/delete/<deyer>')
def delete(deyer):
    suser=Posts.query.filter_by(id=deyer).first()
    db.session.delete(suser)
    db.session.commit()
    return redirect('/')
    

        
    
    

 


if __name__=='__main__':
    app.run(debug=True)

