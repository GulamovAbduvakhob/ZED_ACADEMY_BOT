import logging
from buttons import but_start,but_start1,but_start2
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

@dp.message_handler(text_contains=["Backend darslari 👨🏻‍💻"])
async def darslar(message: aiogram.types.Message):
    await message.answer("BACKEND",reply_markup=but_start1)

@dp.message_handler(text_contains=["About backend"])
async def about(message: aiogram.types.Message):
    await message.answer("""In ENGLISH🇬🇧:The back end refers to parts of a computer application or a program's code that allow it to operate and that cannot be accessed by a user. Most data and operating syntax are stored and accessed in the back end of a computer system. Typically the code is comprised of one or more programming languages. 
    На РУССКОМ🇷🇺:Серверная часть относится к частям компьютерного приложения или кода программы, которые позволяют ему работать и к которым пользователь не может получить доступ . Большинство данных и рабочего синтаксиса хранятся и доступны в задней части компьютерной системы. Обычно код состоит из одного или нескольких языков программирования.""")

@dp.message_handler(text_contains=["Orqaga"])
async def back(message:aiogram.types.Message):
    await message.reply("Orqaga",reply_markup=but_start)

@dp.message_handler(text_contains=["qoshilish"])
async def ariza(message:aiogram.types.Message):
    await message.reply("Darslarga qoshilishni hohlasangiz pastdagi raqamga murojat qilishingiz mumkin. A dan Zed gacha birga!!")
    await message.answer_contact("+998945327744","Zed it","academy")

@dp.message_handler(text_contains=["chilar"])
async def oquvchi(message:aiogram.types.Message):
    await message.answer("Hozirda backend oqiyatgan oquvchilar soni 4 ta.")

@dp.message_handler(text_contains=["Uztozlar"])
async def ustoz(message:aiogram.types.Message):
    await message.answer("Hozirda backend darslarini malakali ustoz Azamjon Usmonaliyev otib boryaptilar.")











if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)