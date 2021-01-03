import smtplib
from email.message import EmailMessage


def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "abdisamk@gmail.com"
    msg['from'] = user
    password = "y j s v x j v x p j o c s v t e"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()




if __name__ == "__main__":
    email_alert("Hey", "hello word","0939167494@ethiotelecom.et")
