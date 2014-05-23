from eve import Eve
from eve.io.sql import SQL, ValidatorSQL
from eve.auth import TokenAuth
from tables import Users, Membercode, Preregi, Questions
from flask import request, jsonify
from flask.ext.restful import Api, Resource
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import uuid, smtplib, datetime


app = Eve(validator=ValidatorSQL, data=SQL)
api = Api(app)

        
class Register(Resource):

	def post(self):
		mail = request.form['email']
		member = request.form['membership code']
		mem = Membercode.query.filter_by(code=member).first()
		vcode =  str(uuid.uuid4()).replace('-','')
		if mem is None:
			return {'message': 'membership code invalid'}
		prereg = Preregi(email=mail, mem_code=member, verification_code=vcode)
		db.session.add(prereg)
		db.session.delete(mem)
		db.session.commit()
		receiver = request.form['email']
		froms = 'Healthy Options  <no-reply@no-email.com>'
		sender1 = "Healthy Options <no-reply@no-email.com>"
		recipient = "<%s>" %(receiver)
		subject = "Confirm your registration"
		body = "%s" %(vcode)
		html = """\
		<html>
			<head></head>
			<body>
				<p> <b> Here is the verification code you need </b> %s 
				</p>
				<p> Click this <a href="www.facebook.com">link</a>
				to continue.
				</p>
			</body>
		</html>""" %(vcode) 
		params = {'sender':froms, 'recipient':receiver, 'from':sender1, 'to':recipient, 'subject':subject, 'body':body, 'html': html}
		mailer(params)
		return {'message':'ok','email':prereg.email, 'membership code':prereg.mem_code, 'verification code': vcode}
	

class Final(Resource):

	def post(self):
		fname = request.form['firstname']
		lname = request.form['lastname']
		bday = request.form['birthdate']
		mob = request.form['mobile number']
		ver = request.form['verification code']
		password = request.form['password']
		conpass = request.form['confirm password']
		if password != conpass:
			return {'message':'passwords do not match'}
		check = Preregi.query.filter_by(verification_code=ver).first()
		if check is None:
			return {'message':'invalid verification code'}
		regi = Users(firstname=fname, lastname=lname, password=password, fullname=fname+' '+lname, birthday=bday, mobile=mob, email=check.email)
		db.session.add(regi)
		db.session.delete(check)
		db.session.commit()
		return {'message':'ok'}


class Ask(Resource):
	def post(self):
                customer = request.form['email']
		question = request.form['question']
		password = request.form['password']
		mail = Users.query.filter_by(email=customer).first()
		if mail is None:
			return {'message':'not yet a member'}
		ask = Questions(question=question, dateasked=datetime.datetime.now(), askedby=mail.email)
		db.session.add(ask)
		db.session.commit()
		receiver = "basyc2014@gmail.com"
                froms = '%s <%s>' %(mail.fullname, mail.email)
		sender1 = "Healthy Options Customer <%s>" %(customer)
		recipient = "Healthy Options <%s>" %(receiver)
		subject = "Customer Question"
		body = "%s" %(question)
		html = """\
		<html>
			<head></head>
			<body>
				<p> %s asked: <b> %s
				</p>
				<p> Reply at his/her email address: %s </p>
			</body>
		</html>"""  %(mail.fullname, question, mail.email) 
		params = {'sender':froms,'recipient':receiver, 'from':sender1, 'to':recipient, 'subject':subject, 'body':body, 'html': html}
		custom ={'username':customer, 'password':password}
		questions(params, custom)
		return {'message':'inquiry sent'}
	    
	
class Resend(Resource):

	def get(self, email):
		mail = Preregi.query.filter_by(email=email).first()
		if mail is None:
			return {'message':'email not yet registered'}
		else:
			receiver = email
			froms = 'Healthy Options <no-reply@no-email.com>'
			sender1 = "Healthy Options <no-reply@no-email.com>"
			recipient = "<%s>" %(receiver)
			subject = "Resend Verification Code"
			body = "%s" %(mail.verification_code)
			html = """\
			<html>
				<head></head>
				<body>
					<p> <b> Here is your verification code </b> %s 
					</p>
					<p> Click this <a href="www.facebook.com">link</a>
					to continue.
					</p>
				</body>
			</html>""" %(mail.verification_code) 
			params = {'sender':froms, 'recipient':receiver, 'from':sender1, 'to':recipient, 'subject':subject, 'body':body, 'html': html}
			# parameters = [receiver, froms, sender1, recipient, subject, body]
			mailer(params)
			return {'message':'verification code successfully resent'}


def questions(params=None, custom=None):

	if params is not None:
		sender = params['sender']
		receivers = params['recipient']
		message = MIMEMultipart('alternative')
		message['Subject'] = params['subject']
		message['From'] = params['from']
		message['To']= params['to']
		text = params['body']
		html = params['html']
	
	else:
		sender = '<sender>'
		receivers = '<receiver>'
		message = MIMEMultipart('alternative')
		message['Subject'] = '<subject>'
		message['From'] = '<from>'
		message['To']= '<to>'
		text = '<body>'
		html = """\
		<html>
			<head></head>
			<body>
				
			</body>
		</html>"""
	
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	message.attach(part1)
	message.attach(part2)
	
	try:
		if custom['username'].find("yahoo")!=-1:
			session = smtplib.SMTP('smtp.mail.yahoo.com', 587)
		elif custom['username'].find("outlook")!=-1:
			session = smtplib.SMTP('smtp.live.com', 587)
		else:
			saq = custom['username'].split('@')[1]
			host = 'smtp.%s' %(saq)
			session = smtplib.SMTP(host ,587) # default smtp service and port assigned
		session.ehlo()
		session.starttls()
		session.login(custom['username'], custom['password'])	
		session.sendmail(sender,receivers,message.as_string())
		session.quit()
	except smtplib.SMTPException:
		return {'message': 'unable to send email'}


def mailer(params=None):
	
	if params is not None:
		sender = params['sender']
		receivers = params['recipient']
		message = MIMEMultipart('alternative')
		message['Subject'] = params['subject']
		message['From'] = params['from']
		message['To']= params['to']
		text = params['body']
		html = params['html']
	
	else:
		sender = '<sender>'
		receivers = '<receiver>'
		message = MIMEMultipart('alternative')
		message['Subject'] = '<subject>'
		message['From'] = '<from>'
		message['To']= '<to>'
		text = '<body>'
		html = """\
		<html>
			<head></head>
			<body>
				
			</body>
		</html>"""
	
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	message.attach(part1)
	message.attach(part2)
	
	try:
		session = smtplib.SMTP('smtp.gmail.com', 587)
		session.ehlo()
		session.starttls()
		session.login('basyc2014@gmail.com','kenkristelledeanneivanpurposelyaltered')		
		session.sendmail(sender,receivers,message.as_string())
		session.quit()
	except smtplib.SMTPException:
		return {'message': 'unable to send email'}


api.add_resource(Ask, '/ask', endpoint='question')
api.add_resource(Resend, '/resend/<string:email>', endpoint='resend')
api.add_resource(Final, '/registration', endpoint='registered')
api.add_resource(Register, '/preregi', endpoint='register')
db = app.data.driver
db.create_all()
app.run(debug=True)

