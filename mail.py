import smtplib


def send_mail(login, password, heading, text):
    title = f'''From: {login}
    To: {login}
    Subject: {heading}
    Content-Type: text/plain; charset="UTF-8";'''

    letter = f'{title}\n\n{text}'
    letter = letter.encode("UTF-8")

    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login(login, password)
    server.sendmail(login, login, letter)
    server.quit()