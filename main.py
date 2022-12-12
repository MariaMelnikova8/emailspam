import json
import os
from dotenv import load_dotenv
import mail


load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

with open('mail.json', 'r') as file:
    emails = file.read()
emails = json.loads(emails)

heading = 'invitaion'

text = ""

for email in emails:
    mail.send_mail(login, password, heading, text, email)

