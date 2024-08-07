import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email content
sender_email = "theexploristofficial@gmail.com"
password = 'srehgfyclcrxaagz'  # Replace with your actual password
subject = "Daily Reminder - 10 Tips"
message = """\
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

# Function to read emails from file
def read_recipients(filename):
    with open(filename, "r") as file:
        emails = file.read().splitlines()
    return emails

# File containing list of recipient emails
emails_file = "emails.txt"

# List of recipient emails read from file
recipient_emails = read_recipients(emails_file)

# Connect to Gmail's SMTP server
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)  # Replace with your actual password

    for receiver_email in recipient_emails:
        # Prepare actual message for each recipient
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Email sent successfully to {receiver_email}")
        except Exception as e:
            print(f"Error sending email to {receiver_email}: {e}")

except Exception as e:
    print(f"Error connecting to the SMTP server: {e}")
finally:
    server.quit()
