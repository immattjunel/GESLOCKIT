import  smtplib
# email must be open first to to send messages
content='''Wazzup
HEy'''
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('geslockit@gmail.com','thesislol')
server.sendmail('geslockit@gmail.com','yvetteprivate@gmail.com', content)
server.close()
