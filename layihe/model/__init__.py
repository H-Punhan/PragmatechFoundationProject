from setting import db


class authors(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fullname=db.Column(db.String(50))
    about=db.Column(db.Text)
    blog_id=db.relationship('blog',backref='authors')
    

class knowledges(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

class education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    year=db.Column(db.Integer)
    school=db.Column(db.String(50))
    lesson=db.Column(db.String(50))
    description=db.Column(db.Text)

class experience(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    year=db.Column(db.Integer)
    company=db.Column(db.String(50))
    work=db.Column(db.String(50))
    description=db.Column(db.Text)

class skills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    level=db.Column(db.Integer)

class tags(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    blog_id=db.relationship('blog',backref='tags')
class blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    img=db.Column(db.String(50))
    content=db.Column(db.Text)
    post_date=db.Column(db.String(50))
    tag_id=db.Column(db.Integer,db.ForeignKey('tags.id'))
    author_id=db.Column(db.Integer,db.ForeignKey('authors.id'))

