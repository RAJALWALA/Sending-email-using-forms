import smtplib,ssl

host = "smtp.gmail.com"
port = 465
user_name = "bunnyaluvala@gmail.com"
password="braw qsjs wbky cqfv"

recevier_email = "bunnyaluvala@gmail.com"
context = ssl.create_default_context()

message = """
hello
hii
bye!
"""

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(user_name,password)
    server.sendmail(user_name,recevier_email,message)
