from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton

but_back = KeyboardButton("Backend darslari 👨🏻‍💻")
but_front = KeyboardButton("Frontend darslari 👨‍💻")
but_tel = KeyboardButton("Qong'iroq uchun☎️")
but_man = KeyboardButton("Manzilimiz📍")
but_kan = KeyboardButton("Kanalimiz🔗")

but_start = ReplyKeyboardMarkup().add(but_back, but_front, but_man, but_tel, but_kan)


but_oqit = KeyboardButton("Uztozlar")
but_oquv = KeyboardButton("Backendchilar")
but_ariza = KeyboardButton("Darslarga qoshilish")
but_mal = KeyboardButton("About backend")
but_orqa = KeyboardButton("Orqaga")
but_start1 = ReplyKeyboardMarkup().add(but_oqit,but_oquv,but_ariza,but_mal,but_orqa)

but_oqit1 =KeyboardButton("Ustozlar")
but_oquv1 = KeyboardButton("Frontendchilar")
but_ariza1 = KeyboardButton("Darslarga qoshilish")
but_mal1 = KeyboardButton("About 'Frontend'")

but_start2 = ReplyKeyboardMarkup().add(but_oqit1,but_oquv1,but_ariza1,but_mal1,but_orqa)