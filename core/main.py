from aiogram import Bot, Dispatcher, executor, types
import random
import string

HELP_COMMAND = """
/help - list of commands
/start - start working with the bot
/description - description the bot
"""

count = 0

TOKEN_API ="6121057759:AAHQodKHIaLFgubwcX73QeLpqgYy1l8XTEY"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)
    
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Welcome in our the telegram bot')
    await message.delete()
    
@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text='The telegram bot can sent random messages')
    await message.delete()
    
@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')    
    count += 1
    
@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        await message.reply('YES')
    else:
        await message.reply('NO')
    
@dp.message_handler()
async def send_random_message(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))


if __name__ == "__main__":
    executor.start_polling(dp)