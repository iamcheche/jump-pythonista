Libraries and Modules

- eve
- flask
- flask-restful
- flask-sqlalchemy
- SQLAlchemy
- uuid (verification code)
- smtplib (email sending)
- email
- mimemultipart
- mimetext
- datetime

API CALLS

REGISTRATION

	Pre-registration 
	endpoint: /preregi
	method: POST
	parameters:
		membership code
		email

	return:


	Registration
	endpoint: /registration
	method: POST
	parameters:
		firstname
		lastname
		birthdate
		mobile number
		verification code
		password
		
ASK

	Question
	endpoint: /ask
	method: POST
	parameters:
		question
		email
		email password