import logging
from buttons import but_start
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6077407519:AAEsWutj8nqQ5U9BH6ZHuBAECd1bZB8WAhQ'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Zed It Academy hush kelibsiz!!",reply_markup=but_start)



@dp.message_handler(text_contains=["Kanalimiz"])
async def echo(message: types.Message):
    await message.reply("https://t.me/zeditacademy")
@dp.message_handler(text_contains=["☎️"])
async def echo(message: types.Message):
    await message.reply_contact("+998945327744")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)