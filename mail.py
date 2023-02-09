import smtplib

# Функция формирует и отправляет письмо на заданный почтовый ящик
def send_mail(login, password, heading, text, mail):
    # Заголовок для корректной отправки письма
    title = f'''From: {login}
To: {mail}
Subject: {heading}
Content-Type: text/plain; charset="UTF-8";'''

    # Формирование письма для отправки
    letter = f'{title}\n\n{text}'
    letter = letter.encode("UTF-8")

    # Вызов функций инициализации, авторизации пользователя и отправки письма через smtp
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login(login, password)
    server.sendmail(login, mail, letter)
    server.quit()