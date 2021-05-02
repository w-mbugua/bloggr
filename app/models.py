from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(writer_id):
    return Writer.query.get(int(writer_id))

class Writer(UserMixin, db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(120), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    image_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref = 'writer', lazy = 'dynamic')
   
    
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'Writer {self.username}'

class Blog(db.Model):
    __tablename__='blogs'
    id = db.Column(db.Integer, primary_key = True)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    title = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    post =  db.Column(db.Text)
    comments = db.relationship('Comment', backref = 'blog', lazy = 'dynamic')

    def __repr__(self):
        return f"Writer('{self.title}\n{self.post}\n{self.writer}')"
    
class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120))
    body = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
     

    def __repr__(self):
        return f"Writer('{self.date_posted}')"