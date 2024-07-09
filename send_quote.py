import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Read quotes from text file
with open('quotes.txt', 'r') as file:
    quotes = file.readlines()

# Read email addresses from emails.txt
with open('emails_quote.txt', 'r') as file:
    email_addresses = [line.strip() for line in file if line.strip()]

# Email configuration
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('EMAIL_PASSWORD')

def send_email(quote, receiver_email):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Daily Islamic Quote'

    # Attach the quote to the email body
    msg.attach(MIMEText(quote, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
        print(f'Email sent successfully to {receiver_email}')
    except Exception as e:
        print(f'Error sending email to {receiver_email}: {e}')

def send_daily_quote():
    current_day = datetime.now().day
    quote = quotes[current_day % len(quotes)].strip()  # Get the quote of the day
    for email in email_addresses:
        send_email(quote, email)

if __name__ == "__main__":
    send_daily_quote()
