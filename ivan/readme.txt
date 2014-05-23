Mailer Function


Requirements:

> import smtplib
> from email.mime.multipart import MIMEMultipart
> from email.mime.text import MIMEText

Functionality:

> sends email to the user/member. (verification code and for resending)
> also the user/member can send email to Healthy Options if they have 
  any questions.

How it works:

> First, the program gets the specified parameters per part and assigns them
  to their corresponding variable.

> Second, part the message part so it will have a cleaner look of the program

> Start a session by first trying to access the the email registered by 	  using the SMTP host and port assigned to it.

 > It requires 'starttls' for authentication purposes.

 > Log in the credentials provided.

 > Compile the details of the email to be sent.

 > Quit the session.



 Note:

 ***The server to be accessed (smtp.mail.yahoo.com) for example needs the user to be registered on that server.