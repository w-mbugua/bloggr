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
    blog = db.relationship('Blog', backref = 'user', lazy = 'dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__='blogs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    post =  db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    comments = db.relationship('Comment', backref = 'blog', lazy = 'dynamic')

    def __repr__(self):
        return f"User('{self.title}\n{self.post}\n{self.user}')"
    
class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120))
    body = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    

    def __repr__(self):
        return f"User('{self.date_posted}')"