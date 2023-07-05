import os

from telebot.async_telebot import AsyncTeleBot
import asyncio
import os

from telebot.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')
bot = AsyncTeleBot(TOKEN, parse_mode='HTML')


def generate_markup(buttons, n):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*buttons, row_width=n)
    return markup


def generate_markup2(buttons):
    markup = InlineKeyboardMarkup()
    for el in buttons:
        markup.add(InlineKeyboardButton(el, callback_data=buttons[el]))
    return markup


@bot.message_handler(commands=['choice'])
async def send_botton(message):
    await bot.send_message(message.from_user.id, 'Меню кнопок',
                           reply_markup=generate_markup(['ПЕРВАЯ КНОПКА', 'ВТОРАЯ КНОПКА', 'ТРЕТЬЯ КНОПКА'], 3))


@bot.message_handler(commands=['text'])
async def send_un_text(message):
    print(message.from_user.id)
    await bot.send_message(message.from_user.id, '<i>курсив</i>')
    await bot.send_message(message.from_user.id, '<b>жирный</b>')
    await bot.send_message(message.from_user.id, '<u>подчеркнутый</u>')
    await bot.send_message(message.from_user.id, '<ins>подчеркнутый</ins>')
    await bot.send_message(message.from_user.id, '<s>зачёркнутый</s>')
    await bot.send_message(message.from_user.id, '<strike>зачёркнутый</strike>')
    await bot.send_message(message.from_user.id, '<del>зачёркнутый</del>')
    await bot.send_message(message.from_user.id, '<code>моноширный</code>')
    await bot.send_message(message.from_user.id, '<pre>моноширный</pre>')
    await bot.send_message(message.from_user.id, '<tg-spoiler>спойлер</tg-spoiler>')
    await bot.send_message(message.from_user.id, '<a href="https://github.com/kate220608/test3/blob/main/main.py">ссылка</a>')
    await bot.send_message(message.from_user.id, '<a href="tg://user?id=1006407409">яяяяяяяяя</a>')


@bot.message_handler(commands=['time'])
async def send_time(message):
    bot_message = await bot.send_message(message.from_user.id, 'Начался таймер 5 секунд')
    for i in range(1, 6):
        await asyncio.sleep(1)
        await bot.edit_message_text(f"{i} секунды прошло", message.from_user.id, bot_message.id)
    await bot.delete_message(message.from_user.id, bot_message.id)


@bot.message_handler(commands=['choice2'])
async def send_botton2(message):
    await bot.send_message(message.from_user.id, 'Меню кнопок2', generate_markup2({'ПЕРВАЯ КНОПКА': 'f', 'ВТОРАЯ КНОПКА': 's', 'ТРЕТЬЯ КНОПКА': 't'}))


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    print(message)
    await bot.reply_to(message, 'приветствую тебя, новый пользователь!')


@bot.message_handler(commands=['hooray'])
async def send_hooray(message):
    await bot.reply_to(message, 'ураа')


@bot.message_handler(commands=['hi'])
async def send_hi(message):
    await bot.reply_to(message, 'привет')


@bot.message_handler(commands=['music'])
async def send_music(message):
    await bot.reply_to(message, 'ля')


@bot.message_handler(commands=['simple'])
async def send_simple(message):
    await bot.send_message(message.from_user.id, 'просто', disable_notification=True, protect_content=True)


@bot.message_handler(commands=['smile'])
async def send_smile(message):
    bot_message = await bot.send_dice(message.from_user.id, '🎲')
    print(bot_message.dice.value)


@bot.message_handler(commands=['happy'])
async def send_happy(message):
    await bot.send_sticker(message.from_user.id,
                           'CAACAgIAAxkBAAIiFGSkCxZfOXsiRynxpdEBe_-7bXMGAAL-IAACk88ISMHhCOmR3OssLwQ')


@bot.message_handler(commands=['text'])
async def send_text(message):
    await bot.send_document(message.from_user.id, open('text.txt', 'rb'))


@bot.message_handler(commands=['coords'])
async def send_coords(message):
    await bot.send_location(message.from_user.id, 58.002410, 56.250796)


@bot.message_handler(commands=['video'])
async def send_video(message):
    await bot.send_video(message.from_user.id,
                         'https://web.telegram.org/k/stream/%7B%22dcId%22%3A2%2C%22location%22%3A%7B%22_%22%3A%22inputDocumentFileLocation%22%2C%22id%22%3A%225269646884728746156%22%2C%22access_hash%22%3A%22-4011997868830190044%22%2C%22file_reference%22%3A%5B2%2C98%2C46%2C23%2C179%2C0%2C0%2C4%2C81%2C100%2C163%2C255%2C1%2C16%2C224%2C44%2C161%2C186%2C68%2C47%2C19%2C34%2C235%2C151%2C229%2C49%2C89%2C29%2C32%5D%7D%2C%22size%22%3A10334606%2C%22mimeType%22%3A%22video%2Fmp4%22%2C%22fileName%22%3A%22IMG_1296.MP4%22%7D')


@bot.message_handler(commands=['photo'])
async def send_photo(message):
    await bot.send_photo(message.from_user.id,
                         'https://img.freepik.com/free-photo/a-cupcake-with-a-strawberry-on-top-and-a-strawberry-on-the-top_1340-35087.jpg',
                         caption="photo")


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    text_message = message.text.lower()
    if 'дел' in text_message or 'настроен' in text_message:
        await bot.reply_to(message, 'все ок, у вас?')
    elif 'факт' in text_message:
        await bot.reply_to(message, 'луна - спутник земли')
    elif 'шутк' in text_message or 'анекдот' in text_message or 'смех' in text_message:
        await bot.reply_to(message, 'хахахахахахахахаха')
    else:
        await bot.delete_message(message.from_user.id, message.id)


asyncio.run(bot.polling())
