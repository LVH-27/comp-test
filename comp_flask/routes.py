from . import comp_app
from flask import request


members = ["Member 1", "Member 2", "Member 3"]
@comp_app.route('/', methods=['GET'])
def index():
    print("hi from the console")
    return "hi, I'm the response"


@comp_app.route('/members', methods=['GET'])
def get_members():
    return ', '.join(members)


@comp_app.route('/members/add', methods=['POST'])
def add_member():
    member_name = request.json.get('name')
    members.append(member_name)
    print("Added member " + member_name)
    return ', '.join(members)


