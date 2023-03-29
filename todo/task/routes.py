from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from todo import db
from todo.models import Task
from .forms import TaskForm

task = Blueprint('Task', __name__)


@login_required
@task.route("/", methods=['GET', 'POST'])
@task.route("/add", methods=['GET', 'POST'])
def task_handler():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(name=form.name.data, description=form.description.data, finish_by=form.finish_by.data,
                    user_id=current_user.id, status=form.status.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('Main.index'))
    return render_template("task/task_form.html", form=form)
