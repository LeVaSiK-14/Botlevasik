import os
import random
import telebot
from telebot import types


TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)
smile = ('😀', '😬', '😁', '😃', '😂', '🤣', '😇', '😉', '🤗', '☹️', '👌', '💀', '🤘', '👍', '😍', '😘', '😝', '😉')
stic = ('CAADAgADAQADwDZPExguczCrPy1RFgQ', 'CAADAgADAgEAAladvQpO4myBy0Dk_xYE', 'CAADAgAD6gIAArrAlQVnuN_EB5amiRYE', 'CAADAgAD3gIAArrAlQXuwFScyZ0O5xYE', 'CAADAgAD2QIAArrAlQW14nX_pisAATYWBA', 'CAADAgAD2AIAArrAlQU4Tn73vH9DKBYE', 'CAADAgAD1wIAArrAlQWUjwizSI-AxBYE', 'CAADAgAD3QIAArrAlQVwL1UKRyToARYE', 'CAADAgAD4AIAArrAlQVVl5fPaZBrnhYE', 'CAADAgADHAUAAj-VzAoN8ZWzAfPFKBYE', 'CAADAgADGwUAAj-VzAq5dzWRhLpLvxYE', 'CAADAgAD5gADVp29CgABASgoWjZr-xYE', 'CAADAgAD1wADVp29Cg09r24xpO5XFgQ', 'CAADAgADBAEAAladvQreBNF6Zmb3bBYE')
citata1 = ('Жизнь добрых людей – вечная молодость.', 'Без пользы жить – безвременная смерть', 'Человеческая жизнь похожа на коробку спичек. Обращаться с ней серьезно – смешно. Обращаться несерьезно – опасно.', 'Если человек начинает интересоваться смыслом жизни или ее ценностью – это значит, что он болен.', 'Живи так, как будто ты сейчас должен проститься с жизнью, как будто время, оставленное тебе, есть неожиданный подарок.', 'Жизнь как пьеса в театре: важно не то, сколько она длится, а насколько хорошо сыграна.', 'В диалоге с жизнью важен не ее вопрос, а наш ответ.', 'Суть жизни – найти самого себя.', 'Определить свою цель – это как найти Полярную звезду. ...', 'Любовь - это не тогда, когда человек делает для тебя этот мир, а тогда, когда вы творите его вместе.')
citata2 = ('Когда падаешь, не забывай о двух вещах - кто тебя толкнул и кто тебя не поддержал. Это обязательно пригодится, когда снова встанешь на ноги.', 'Те, кто больше всего скучают или страдают,обычно делают это молча.', 'Мужчина который подарил женщине крылья, никогда не будет носить рога!', 'Мое сердце закрыто на замок, а ключ лежит только в одном месте - в твоей душе.', 'Угасший костер любви, нужно разжигать с уголька...')
citata = citata1 + citata2




@bot.message_handler(commands=["start"])
def send_text(message):
    bot.send_message(message.chat.id, 'Список команд:👌                                                                                             1) /geo - показывает вашу геолокацию                                                         2) Смайлик - отправит вам смайлик                                                                   3) Стикер - отправит вам стикер                                                                    4) Цитата - отправит вам цитату')



@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение",
                     reply_markup=keyboard)


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        print(message.location)
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        bot.send_message(message.chat.id, '😈😈Спасибо за твои координаты за тобой уже выехали!!😈😈')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Смайлик':
        bot.send_message(message.chat.id, random.choice(smile))
    elif message.text == 'Стикер':
        bot.send_sticker(message.chat.id, random.choice(stic))
    elif message.text == 'Цитата':
        bot.send_message(message.chat.id, random.choice(citata))
    elif message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет!')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю тебя, прочитай список команд ещё раз')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()