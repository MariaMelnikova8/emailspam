import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
text = ('''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

> Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
> Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
> Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся > %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.''')
my_name = 'Maria'
friend_name = 'Julia'
link = 'Polus101 - polus101.ru'
heading = 'invitaion'
mail = os.environ["EMAIL"]
password = os.environ["EMAIL_PASSWORD"]

text = text.replace('%website%',link)
text = text.replace('%friend_name%',friend_name)
text = text.replace('%my_name%',my_name)

title = f'''From: {mail}
To: {mail}
Subject: {heading}
Content-Type: text/plain; charset="UTF-8";'''

letter = f'{title}\n\n{text}'
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(mail, password)
server.sendmail(mail, mail, letter)
server.quit()