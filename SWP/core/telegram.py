import telebot
from telebot.types import Message, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery, InlineKeyboardMarkup, \
    InlineKeyboardButton

import config

bot = telebot.TeleBot(token=config.TOKEN)


def send_greetings():
    button_hi = KeyboardButton('Get question')

    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    greet_kb.add(button_hi)

    bot.send_message(config.CHAT_ID, "New question available", reply_markup=greet_kb)


@bot.callback_query_handler(func=lambda q: q.data == 'accept')
def accepted_question(call: CallbackQuery):
    USER_QUESTION = "What's going on?"

    volunteer_id = call.from_user.id
    volunteer_name = call.from_user.first_name
    bot.delete_message(chat_id=config.CHAT_ID, message_id=call.message.message_id)
    bot.send_message(chat_id=config.CHAT_ID, text="Question was picked by " + volunteer_name)
    bot.send_message(
        volunteer_id, "Question: " + USER_QUESTION
    )

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Start", callback_data="start")
    )
    keyboard.add(
        InlineKeyboardButton(text="Finish", callback_data="finish")
    )
    bot.send_message(volunteer_id, "Choose the action", reply_markup=keyboard)


@bot.message_handler(func=lambda m: m.text == "Get question")
def send_question(message: Message):
    USER_QUESTION = "NOOOOOOOOOOO?"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Accept ✅", callback_data="accept"))
    keyboard.add(
        InlineKeyboardButton(text="Decline ❌", callback_data="decline")
    )
    bot.send_message(
        config.CHAT_ID,
        "Question: " + USER_QUESTION, reply_markup=keyboard
    )


@bot.message_handler()
def send_answer(message: Message):
    print(message.text)


@bot.callback_query_handler(func=lambda q: q.data =="start")
def start_help(call: CallbackQuery):
    bot.send_message(call.from_user.id, "Please, write the solution")


@bot.callback_query_handler(func=lambda q: q.data == 'finish')
def finish_help(call: CallbackQuery):
    bot.send_message(call.from_user.id, "Your answer was sent\nThank you!")


if __name__ == "__main__":
    bot.infinity_polling()
