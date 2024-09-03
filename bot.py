# 1. Импорт библиотек

import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 2. Реализованная функция

def transcript_name(name: str) -> str:
    trans_dict = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh',
        'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
        'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts',
        'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
    }
    return ''.join(trans_dict.get(char, char) for char in name)

#3. Инициализация объектов

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# 4. Обработка команды /start

@dp.message(Command(commands=['start']))
async def send_welcome(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Напиши свои полные ФИО, и я верну тебе транскрипцию по правилам МИД РФ.'
    logging.info(f'{user_name} {user_id} использует бот.')
    await bot.send_message(chat_id=user_id, text=text)

# 5. Обработка сообщений

@dp.message()
async def send_mirror(message: Message):
    fio_kirillica = message.text
    logger.info(f"Получены ФИО: {fio_kirillica}")
    fio_latinica = transcript_name(fio_kirillica)
    await message.reply(f"Твои ФИО на латинице по правилам МИД: {fio_latinica}")

#Запуск процесса пуллинга

if __name__ == '__main__':
    dp.run_polling(bot)
    
    
