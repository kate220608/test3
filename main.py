from telebot.async_telebot import AsyncTeleBot
import asyncio

bot = AsyncTeleBot('6192388726:AAFYAAJr01ir3klolGA36mVkXMyIomuMaQY')


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, 'приветствую тебя, новый пользователь!')


@bot.message_handler(commands=['hooray'])
async def hooray(message):
    await bot.reply_to(message, 'ураа')


@bot.message_handler(commands=['hi'])
async def hi(message):
    await bot.reply_to(message, 'привет')


@bot.message_handler(commands=['music'])
async def music(message):
    await bot.reply_to(message, 'фаниманки витя')


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    text_message = message.text.lower()
    if 'дел' in text_message or 'настроен' in text_message:
        await bot.reply_to(message, 'все ок, у вас?')
    elif 'факт' in text_message:
        await bot.reply_to(message, 'луна - спутник земли')
    elif 'шутк' in text_message:
        await bot.reply_to(message, 'хахахахахахахахаха')
    else:
        await bot.reply_to(message, message.text)


asyncio.run(bot.polling())
