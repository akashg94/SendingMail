import smtplib  # connect with mail server

Sender_email = "xyz@gmail.com"
Reciever_email = "abc@gmail.com"
password = input('enter your email password: ')
#email body
subject = "test"
body = "hello there"
message = f'subject :{subject}\n\n{body}'
#creating port to send the email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Sender_email, password)

    smtp.sendmail(Sender_email, Reciever_email, message)
