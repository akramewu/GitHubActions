import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email():
    mail_server = os.getenv('MAIL_SERVER')
    mail_port = os.getenv('MAIL_PORT')
    mail_username = os.getenv('MAIL_USERNAME')
    mail_password = os.getenv('MAIL_PASSWORD')
    to_email = "theexploristofficial@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = mail_username
    msg['To'] = to_email
    msg['Subject'] = "Daily Reminder - 10 Tips"

    body = """
    10 Tips for Seeking Allah's Help

    1. Seek Allah S.W.T's help.
    2. Tell someone that you trust.
    3. Lower the gaze.
    4. Set realistic goals (small goals).
    5. Don't be upset. Never give up on change. Allah will help us, Ameen.
    6. Develop new habits.
    7. Be honest.
    8. Beware of false quitting.
    9. Always remind yourself about the bad consequences that could happen. Allah is watching us.
    10. The industry is evil. Maintain self-awareness.

    Help me Ya Rabb, :'( Help my brothers and sisters. Don't give up hope.
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(mail_server, int(mail_port))
        server.starttls()
        server.login(mail_username, mail_password)
        text = msg.as_string()
        server.sendmail(mail_username, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()
