import telebot
from PIL import Image
import qrcode
from telebot import types
import configure
import random

client = telebot.TeleBot(configure.config["token"])

@client.message_handler(content_types = ["text"])
def create_qr(message):
    img = qrcode.make(message)
    img.save("image.png")
    client.send_photo(message.chat.id, "image.png")

client.polling(none_stop = True, interval = 0)
