from aiogram import Bot, Dispatcher, executor, types
import random
import os

bot = Bot(token='YOURBOTTOKEN')
dp = Dispatcher(bot)


@dp.message_handler(commands=['YOURCOMMANDNAME'])
async def send_welcome(message: types.Message):
    photo_file = random.choice([
        x for x in os.listdir(os.path.join('Photo'))
        if os.path.isfile(os.path.join(os.path.join('Photo'), x))
    ])
    with open(os.path.join('Photo', photo_file), 'rb') as photo:
        await bot.send_photo(message.chat.id,photo)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    a = random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    print(a)
