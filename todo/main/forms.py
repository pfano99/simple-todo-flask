from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError, Email
from wtforms import StringField, TextAreaField, SubmitField, SelectField, IntegerField

class RegistrationForm(FlaskForm):
	firstName = StringField('First Name*', validators=[DataRequired()])
	lastName = StringField('Last Name*', validators=[DataRequired()])
	email = StringField('Email*', validators=[DataRequired(), Email(message="Invalid email address.\nMake sure there's no spaces before and after your email")])
	
	# experience = IntegerField('How long have you been farming(Years)*', validators=[DataRequired()])

	suburb = StringField('Township/Suburb*', validators=[DataRequired()])
	province = SelectField('Province*', validators=[DataRequired()], choices=['Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo', 'Mpumalanga', 'Northern Cape', 'North West', 'Western Cape'])

	user_type = SelectField('Are you a Seller or Buyer?*', validators=[DataRequired()], choices=['Choose', 'Seller', 'Buyer'])
	product = TextAreaField('Which products intested in selling/buying*')

	submit = SubmitField('Register')

	def validate_firstName(self, firstName):
		firstName.data = str(firstName.data).strip()
		for i in firstName.data:
			if str(i).isdigit() or ord(i) < 65 or ord(i) > 122:
				if not str(i).isspace(): 
					raise ValidationError('First name should not contain any Symbols or numbers.')

	def validate_email(self, email):
		email.data = str(email.data).strip()
	
	def validate_lastName(self, lastName):
		lastName.data = str(lastName.data).strip()
		if not str(lastName.data).isalpha():
			raise ValidationError('Last name should not contain any Symbols or numbers.')

	def validate_experience(self, experience):
		if not str(experience.data).isalnum():
			raise ValidationError("Years of experience should not include any letters or symbols. only put a number eg. 4 if you have 4 years of experience")

	def validate_user_type(self, user_type):
		if user_type.data == 'Choose':
			raise ValidationError("Please choose a valid choice. (Seller or Buyer)")

class QuestionForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	subject = StringField('Subject', validators=[DataRequired()])
	body = TextAreaField('Question')
	submit = SubmitField('Send')

