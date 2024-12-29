
def send_email(message, recipient, sender="university.help@gmail.com"):

    # Проверка на отправителя по умолчанию
    if sender != "university.help@gmail.com":
        standart_sender = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! '
    else:
        standart_sender = ''

    # Проверка на корректность e-mail отправителя и получателя.
    recipient_correct = None
    sender_correct = None
    for i in ('.com', '.ru', '.net'):
        if '@' in recipient and recipient.endswith(i):
            recipient_correct = True
        if '@' in sender and sender.endswith(i):
            sender_correct = True

    # Проверка на отправку самому себе
    if sender == recipient:
        return print('Нельзя отправить письмо самому себе!')

    # Вывод сообщений
    if recipient_correct != True or sender_correct != True:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        print(standart_sender+f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

print()
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')