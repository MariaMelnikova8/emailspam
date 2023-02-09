import json
import os
from dotenv import load_dotenv
import mail
import argparse

# Добавление в код секретных данных из файла .env
load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

# Добавление к программе аргументов командной строки
parser = argparse.ArgumentParser(
        description='Описание программы'
)
parser.add_argument('--m', help='Для файла с почтами.')
parser.add_argument('--t', help='Для файла с текстом письма.')
parser.add_argument('--s', help='Для заголовка письма')
emails_file_path = parser.parse_args().m
text_file_path = parser.parse_args().t
theme = parser.parse_args().s

# Открываем файл с почтами
try:
    with open(emails_file_path, 'r') as file:
        emails = file.read()
    emails = json.loads(emails)
except FileNotFoundError:
    print('Файл введен неправильно')
    exit()

try:
    with open(text_file_path, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print('Файл введен неправильно')
    exit()

# Вызов функции в цикле для отправки письма на несколько почт
for email in emails:
    mail.send_mail(login, password, theme, text, email)

