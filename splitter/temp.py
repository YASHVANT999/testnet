import smtplib
from email.message import EmailMessage

def send_email(email, amount, curr_user):
    user = "thakurmukeshkumar785@gmail.com"
    password = "nzbzdgtiitiozntz"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)

    msg = EmailMessage()
    msg.set_content(f"Please clear your debt with {curr_user} of amount {amount}")
    msg['subject'] = "Debt clear"
    msg['to'] = email
    msg['from'] = user
    server.send_message(msg)
    print("done")

send_email("thakurmukeshkumar785@gmail.com", 122, "smksd")