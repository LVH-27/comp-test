from comp_flask import db
from sqlalchemy.sql import func


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("members.id", ondelete="CASCADE"))


class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False, server_default=func.now())
    color = db.Column(db.String(255), nullable=False, default='blue')
    blog_posts = db.relationship('BlogPost', backref="author")
