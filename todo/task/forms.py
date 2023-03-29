from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SelectField, SubmitField, TextAreaField, DateField


class TaskForm(FlaskForm):
    name = StringField('Task name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    project = SelectField('Project', validators=[], choices=['Project 1', 'Project 2', 'Project 3'])
    status = SelectField('Status', validators=[DataRequired()], choices=['In progress', 'Completed', 'Not started'])
    finish_by = DateField('Finish by', validators=[DataRequired()])
    submit = SubmitField('Add new task')
