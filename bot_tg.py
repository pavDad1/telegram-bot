import os
import random
import telebot
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот. Напиши /help")


@bot.message_handler(commands=["help"])
def help_command(message):
    text = (
        "Мои команды:\n"
        "/start - приветствие\n"
        "/help - список команд\n"
        "/dice - бросить кубик\n"
        "/coin - подбросить монету\n"
        "Любой другой текст я повторю."
    )
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["dice"])
def dice(message):
    number = random.randint(1, 6)
    bot.send_message(message.chat.id, f"Выпало: {number}")


@bot.message_handler(commands=["coin"])
def coin(message):
    result = random.choice(["Орёл", "Решка"])
    bot.send_message(message.chat.id, result)


@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()