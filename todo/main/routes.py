from flask import Blueprint, render_template
from flask_login import login_required, current_user

from todo.models import Task

main = Blueprint('Main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    _tasks = [
        {
            "name": "task 01",
            "finish_by": "10-11-2013",
            "description": "some task desciption",
            "status": "finished"
        },
        {
            "name": "task 01",
            "finish_by": "10-11-2013",
            "description": "some task desciption",
            "status": "finished"
        },
        {
            "name": "task 01",
            "finish_by": "10-11-2013",
            "description": "some task desciption",
            "status": "finished"
        },
        {
            "name": "task 01",
            "finish_by": "10-11-2013",
            "description": "some task desciption",
            "status": "finished"
        },
        {
            "name": "task 01",
            "finish_by": "10-11-2013",
            "description": "some task desciption",
            "status": "finished"
        },
        {
            "name": "task 01",
            "finish_by": "10-11-2013",
            "description": "some task desciption",
            "status": "finished"
        },
        {
            "name": "task 01",
            "finish_by": "10-11-2013",
            "description": "some task desciption",
            "status": "finished"
        },
    ]

    tasks = Task.query.filter_by(user_id=current_user.id)
    return render_template('dashboard.html', tasks=tasks)
