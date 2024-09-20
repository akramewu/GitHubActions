import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email content
sender_email = "theexploristofficial@gmail.com"
password = 'srehgfyclcrxaagz'  # Replace with your actual password
subject = "10 Things to Do in Difficulty"
message = """\
1: Read Quran Daily
 Even one verse.

2: Offer Tahajjud and ask Allah for the solution. (be humble)
 There are 3 types of Tahajjud
 a: Offer Tahajjud prayer before sleeping. (Good)
 b: Waking a few minutes before fajar and offering Tahajjud. (Better)
 c: Waking in at midnight offering Tahajjud and then going to sleep until fajar. (Best)

3: Make Dua in the times of acceptance.
 E.g.
 During Rain, While traveling, during sujood, on Jummah after Asar & between Azaan and Ikamah.

4: Make dua for others who are suffering from the same problems.
5: Make sure not to leave morning and evening azkaar. (hisnul Muslim app)
6: Try your best to leave sins.
7: Help the poor and needy. (with consistency)
8: Make lots of Istaghfaar.
9: Making authentic dua's in a state of extreme depression or grief.
10: Read this dua often

لَا إِلَهَ إِلَّا اللَّهُ الْعَظِيمُ الْحَلِيمُ، لَا إِلَهَ إِلَّا اللَّهُ رَبُّ الْعَرْشِ الْعَظِيمِ، لَا إِلَهَ إِلَّا اللَّهُ رَبُّ السَّمَوَاتِ، وَرَبُّ الْأَرْضِ، وَرَبُّ الْعَرْشِ الْكَرِيمِ

La ilaha illallahul-Adheemul-Haleem. La ilaha illallahu Rabbul-‘Arshil-‘Adheem. La ilaha illallahu Rabbus-samawati, wa Rabbul-ardi, wa Rabbul-‘Arshil- Kareem

None has the right to be worshipped except Allah, the Most Great, the Most-Forbearing. None has the right to be worshipped except Allah, Lord of the Magnificent Throne. None has the right to be worshipped except Allah, Lord of the Heavens, Lord of the Earth, and Lord of the Noble Throne.

[Al-Bukhari 6345 and Muslim 2730]
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
