import logging
from buttons import but_start
import aiogram

API_TOKEN = '6077407519:AAEsWutj8nqQ5U9BH6ZHuBAECd1bZB8WAhQ'


logging.basicConfig(level=logging.INFO)


bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: aiogram.types.Message):
    await message.reply("Zed It Academy hush kelibsiz!!",reply_markup=but_start)



@dp.message_handler(text_contains=["Kanalimiz"])
async def echo(message: aiogram.types.Message):
    await message.answer("https://t.me/zeditacademy")
@dp.message_handler(text_contains=["☎️"])
async def echo(message: aiogram.types.Message):
    await message.answer_contact("+998945327744","Zed it","academy")
@dp.message_handler(text_contains=["Manzil"])
async def man(message: aiogram.types.Message):
    await message.reply_location(40.3911725263081, 71.78637436836638)

@dp.message_handler(text_contains=["Backend"])
async def man(message: aiogram.types.Message):
    await message.answer(reply_markup=)

if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)