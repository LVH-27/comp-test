from . import comp_app, db
from flask import request, jsonify
from .models import Member


@comp_app.route('/', methods=['GET'])
def index():
    print("hi from the console")
    return (jsonify({"content": "hi, I'm the response"}), 200)


@comp_app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return (jsonify([{
                    "id": member.id,
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "date_joined": member.date_joined,
                    "color": member.color,
                    "blog_post_count": len(member.blog_posts)
                } for member in members]), 200)


@comp_app.route('/members/<member_id>', methods=['GET'])
def get_member(member_id):
    member = Member.query.get(member_id)
    if member:
        return (jsonify({
                    "id": member.id,
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "date_joined": member.date_joined,
                    "color": member.color,
                    "blog_post_count": len(member.blog_posts)
                }), 200)
    else:
        return (jsonify({"error": f"Member {member_id} not found!"}), 404)


@comp_app.route('/members/add', methods=['POST'])
def add_member():
    """
    Member structure:
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False, server_default=func.now())
    color = db.Column(db.String(255), nullable=False, default='blue')
    blog_posts = db.relationship('BlogPost', backref="author")

    """
    member_name = request.json
    if "first_name" not in request.json or\
        "last_name" not in request.json:
        return (jsonify({
                    "success": False,
                    "message": "Bad request! first_name and last_name are mandatory"
                }), 400)

    new_member = Member(
        first_name=request.json.get("first_name"),
        last_name=request.json.get("last_name"),
        date_joined=request.json.get("date_joined") or None,
        color=request.json.get("color") or None
    )
    try:
        db.session.add(new_member)
        db.session.commit()
    except Exception as e:
        print(e)
        return (jsonify({"success": False, "message": e}), 500)
    return (jsonify({"success": True, "member_id": new_member.id}), 200)
