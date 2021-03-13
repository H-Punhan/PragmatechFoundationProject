from setting import db
class about(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fullname=db.Column(db.String(50))
    about=db.Column(db.String(1000))
    img=db.Column(db.String(50))

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

