###########################
#### Email Template #######
###########################



url = [['https://plot.ly/~robertnixhydra/12.png?share_key=ZeNhjo863BR7FuTY6zmdy8','This is sample text for test purposes. text of choice can be displayed here. the above graph is using fake data for demo purposes.'],
['https://plot.ly/~robertnixhydra/14.png', 'this is more sample text for test purposes. any test can go here. the above graph is using fake data for demo purposes.']]


from IPython.display import display, HTML

template = (''
    '<a href="{graph_url}" target="_blank">' # Open the interactive graph when you click on the image
        '<img src="{graph_url}">'        # Use the ".png" magic url so that the latest, most-up-to-date image is included
    '</a>'
    '{caption}'                              # Optional caption to include below the graph
    '<br>'                                   # Line break
    '<a href="{graph_url}" style="color: rgb(190,190,190); text-decoration: none; font-weight: 200;" target="_blank">'
        'Click to comment and see the interactive graph'  # Direct readers to Plotly for commenting, interactive graph
    '</a>'
    '<br>'
    '<hr>'                                   # horizontal line
'')

email_body = ''
for u in url:
	_ = template
	_ = _.format(graph_url=u[0], caption=u[1])
	email_body += _

display(HTML(email_body))


###########################
#### Sending the email ####
###########################



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


me  = 'robert@nixhydragames.com'
recipient = [
	'recipient1 email',
'recipient2 email',
'recipient3 email',
'recipient4 email',
'recipient5 email']

subject = 'Graph Report'

email_server_host = 'smtp.gmail.com'
port = 587
email_username = me
email_password = os.environ["GPASS"]


msg = MIMEMultipart('alternative')
msg['From'] = me
msg['To'] = ", ".join(recipient)
msg['Subject'] = subject

msg.attach(MIMEText(email_body, 'html'))

server = smtplib.SMTP(email_server_host, port)
server.ehlo()
server.starttls()
server.login(email_username, email_password)
server.sendmail(me, recipient, msg.as_string())
server.close()
