from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
from app import keyboards as kb
from app import database as db
from random import randint, choice

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)



async def on_startup(_):
    await db.db_start()
    print('Бот успешно запущен!')





@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAPjZEJRG_UCPLPRfxw8VDH_hfdV7S4AAtUFAAL6C7YIBh9vLn4bP0ovBA')
    await message.answer(f"{message.from_user.first_name},Приветствую тебя у меня на канале!", reply_markup=kb.main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы зарегистрировались как администратор!', reply_markup=kb.main_admin)


@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст', reply_markup=kb.catalog_list)


@dp.message_handler(text='Корзина')
async def recycle(message: types.Message):
    await message.answer(f'Корзина пуста')


@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    await message.answer(f'Контакты: https://www.youtube.com/@user-nd4uj8gt9p')



@dp.message_handler(text='Админ-панель')
async def contacts(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли в админ-панель', reply_markup=kb.admin_panel)
    else:
        await message.reply("Я вас не понимаю")


"""Проверка ID юзера"""
@dp.message_handler(commands=['id'])
async def cmd_id(message:types.Message):
    await message.answer(f'{message.from_user.id}')

"""Стикер в приветствие"""
@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply("Я вас не понимаю")


"""Хвалилка присланных фото"""

random_answer = ('Какая красивая фотография!',
'Очень хороший ракурс!',
'Цвета на этой фотографии просто потрясающие!',
'Я люблю, как эта фотография передает настроение!',
'Очень интересная композиция!',
'Я бы повесил эту фотографию на стене!',
'Очень талантливый фотограф!',
'Фотография просто изумительная!',
'Как хорошо, что у вас есть такой талант!'
)
@dp.message_handler(content_types=['photo'])
async def get_user_photo(message):
    await bot.send_message(message.chat.id, choice(random_answer))



if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)



#-----------------------------------------------





# наброски
#
# class Bot_message():
#     @bot.message_handler(content_types=['text'])
#     def get_user_text(message):
#         if message.text =="Hello":
#             bot.send_message(message.chat.id, 'И тебе привет!', parse_mode="html")
#         elif message.text == "id":
#             bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode="html")
#         elif message.text == "photo":
#             photo = open('/TELEGRAM_BOT/IMG_6399.PNG', 'rb')
#             bot.send_photo(message.chat.id, photo)
#         else:
#             bot.send_message(message.chat.id,"Я тебя не понимаю", parse_mode="html")
