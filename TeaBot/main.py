from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import BotCommand, Message, KeyboardButton, ReplyKeyboardMarkup # , ReplyKeyboardRemove


import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import random

BOT_TOKEN = '7023815986:AAGqZLAIqYsFG30fsN2FLvVka8EPGK6mCNY'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# код для связи с базой данных

CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '120ZJHUemFjdFvNUP7OMMQ3WcaJtvjJI5SZzZd9xkV-o'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

valuess = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:F50',
    majorDimension='COLUMNS'  # COLUMNS - В СПИСКАХ КОЛОНКИ // ROWS - В СПИСКАХ СТРОКИ
).execute()

del valuess['range']
del valuess['majorDimension']
tea_all_table = list(valuess.values())
tea_all_table = tea_all_table[0]
print(tea_all_table[1])
print(len(tea_all_table[1]))

# словарь для хранения данных пользователя
# users = {}

# Создаем объекты кнопок
# 1 меню
button_category_tea = KeyboardButton(text='Категории чая')
button_random_tea = KeyboardButton(text='Случайный чай')
button_name_tea = KeyboardButton(text='Полный список')
# 2 меню
# зеленый чай
button_green_tea = KeyboardButton(text='Зеленый чай')
button_green_tea_random = KeyboardButton(text='Рандомный Зеленый чай')
# черный чай
button_black_tea = KeyboardButton(text='Черный чай')
button_black_tea_random = KeyboardButton(text='Рандомный Черный чай')
# фруктовый чай
button_fruit_tea = KeyboardButton(text='Фруктовый чай')
button_fruit_tea_random = KeyboardButton(text='Рандомный Фруктовый чай')
# смесь
button_mix_tea = KeyboardButton(text='Смесь чайов')
button_mix_tea_random = KeyboardButton(text='Рандомная Смесь чай')
# улун
button_oolong_tea = KeyboardButton(text='чай Улун')
button_oolong_tea_random = KeyboardButton(text='Рандомный чай Улун ')
# ройбуш
button_rooibos_tea = KeyboardButton(text='Ройбуш чай')
button_rooibos_tea_random = KeyboardButton(text='Рандомный Ройбуш чай')
# иван-чай
button_fireweed_tea = KeyboardButton(text='Иван-чай')
button_fireweed_tea_random = KeyboardButton(text='Рандомный Иван-чай')
# все чаи
button_name_tea_random = KeyboardButton(text='Рандомные Все чаи')
# назад
button_back_tea = KeyboardButton(text='Назад')






# Создаем объект клавиатуры, добавляя в него кнопки
first_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_category_tea],
              [button_random_tea],
              [button_name_tea]],
    resize_keyboard=True
)
two_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_green_tea, button_black_tea],
              [button_fruit_tea, button_mix_tea],
              [button_oolong_tea, button_rooibos_tea],
              [button_fireweed_tea, button_back_tea]],
    resize_keyboard=True
)
tree_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_black_tea_random],
              [button_back_tea]],
    resize_keyboard=True
)


# хендлер для /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="Привет!\nЯ создан чтобы помочь Тебе с выбором сорта чая. \n\n"
             "Если хочешь узнать все\n"
             "мои возможности - отправь команду /help",
        reply_markup=first_keyboard
    )

# хендлер для рандомного чая черный
@dp.message(F.text == 'Рандомный Черный чай')
async def process_green_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Чёрный чай':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(f'Название:\n    {tea_all_table[1][b12]}\n\n'
                         f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
                         f'Описание:\n    {tea_all_table[2][b12]}\n\n')

# хендлер для рандомного чая зеленый
@dp.message(F.text == 'Рандомный Зеленый чай')
async def process_green_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Зелёный':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(f'Название:\n    {tea_all_table[1][b12]}\n\n'
                         f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
                         f'Описание:\n    {tea_all_table[2][b12]}\n\n')


@dp.message(F.text == 'Зеленый чай')
async def process_green_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Зелёный':
            await message.answer(f'{tea_all_table[1][i]}')


    '''
    # если нов.пользов., то добавим в словарь
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0,
            'loss': 0

        }
    '''


# хендлер для /keyboard_tea
@dp.message(F.text == 'Случайный чай')
async def process_black_tea_command(message: Message):
    await message.answer(
        text="Выберите чай",
        reply_markup=two_keyboard
    )

# хендлер для /keyboard_tea
@dp.message(F.text == 'Назад')
async def process_black_tea_command(message: Message):
    await message.answer(
        text="(0_0)",
        reply_markup=first_keyboard
    )

# хендлер для /reset_table
@dp.message(Command(commands='reset_table'))
async def process_reset_table_command(message: Message):
    valuess = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:F150',
        majorDimension='COLUMNS'  # COLUMNS - В СПИСКАХ КОЛОНКИ // ROWS - В СПИСКАХ СТРОКИ
    ).execute()
    del valuess['range']
    del valuess['majorDimension']
    tea_all_table = list(valuess.values())
    tea_all_table = tea_all_table[0]


# хендлер для /name_tea
@dp.message(F.text == 'Полный список')
async def process_tea_command(message: Message):
    for i in range(len(tea_all_table[1])):
        await message.answer(f'{tea_all_table[1][i]}')


# хендлер для /help
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(f'Заглушка, здесь будет ПОМОЩЬ\n'
                         f'/name_tea - Отправляет названия всех чайов\n'
                         f'/green_tea - Полный список всех ЗЕЛЕНЫХ чайов\n')



# хендлер для 'Рандомные Все чаи'
@dp.message(F.text == 'Рандомные Все чаи')
async def process_random_tea_command(message: Message):
    a = random.choice(tea_all_table[1])
    b = 0

    for i in range(0, len(tea_all_table[1])):
        if tea_all_table[1][i] == a:
            b = i
            break
    await message.answer(f'Название:\n    {tea_all_table[1][b]}\n\n'
                         f'Сорт:\n    {tea_all_table[4][b]}\n\n'
                         f'Описание:\n    {tea_all_table[2][b]}\n\n')


# хендлер для 'Зелёный чай'
@dp.message(F.text == 'Зелёный чай')
async def process_green_tea_command(message: Message):
    a = []
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Зелёный':
            a.append(tea_all_table[4][i])
            await message.answer(f'{tea_all_table[1][i]}')


# хендлер для 'Черный чай'
@dp.message(F.text == 'Черный чай')
async def process_black_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Чёрный чай':
            await message.answer(f'{tea_all_table[1][i]}')


# хендлер для 'Фруктовый чай'
@dp.message(F.text == 'Фруктовый чай')
async def process_fruit_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Фруктовый':
            await message.answer(f'{tea_all_table[1][i]}')


# хендлер для "чай Улун"
@dp.message(F.text == 'чай Улун')
async def process_ulugh_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Улун':
            await message.answer(f'{tea_all_table[1][i]}')


# хендлер на остальные сообщения
@dp.message()
async def process_other_answer(message: Message):
    await message.answer(
        'Я Тебя не понимаю ТТ \n'
        'Воспользуйся кнопкой "Меню" или командой /help'
    )


# Создаем асинхронную функцию для кнопки menu
async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запускает бота'),
        BotCommand(command='/reset_table',
                   description='Обновление таблицы'),
        BotCommand(command='/name_tea',
                   description='Отправляет названия всех чайов'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/green_tea',
                   description='Полный список всех ЗЕЛЕНЫХ чайов'),
        BotCommand(command='/black_tea',
                   description='Полный список всех ЧЕРНЫХ чайов'),
        BotCommand(command='/fruit_tea',
                   description='Полный список всех ФРУКТОВЫХ чайов'),
        BotCommand(command='/ulugh_tea',
                   description='Полный список всех "УЛУН" чайов'),
        BotCommand(command='/random_tea',
                   description='Случайный из всех чайов'),
        BotCommand(command='/keyboard_tea',
                   description='Случайный из всех чайов'),
    ]
    await bot.set_my_commands(main_menu_commands)


# Регистрируем асинхронную функцию в диспетчере,
# которая будет выполняться на старте бота,
dp.startup.register(set_main_menu)

if __name__ == '__main__':
    dp.run_polling(bot)

'''
-----------------------------------------------------------------------------------
from pprint import pprint

import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '120ZJHUemFjdFvNUP7OMMQ3WcaJtvjJI5SZzZd9xkV-o'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http = httpAuth)

valuess = service.spreadsheets().values().get(
    spreadsheetId = spreadsheet_id,
    range = 'A1:E37',
    majorDimension = 'COLUMNS' # COLUMNS - В СПИСКАХ КОЛОНКИ // ROWS - В СПИСКАХ СТРОКИ
).execute()
del valuess['range']
del valuess['majorDimension']
tea_all_table = list(valuess.values())
tea_all_table = tea_all_table[0]
print(tea_all_table[1][5])
print(tea_all_table[1])
-----------------------------------------------------------------------------------
'''

"""
-----------------------------------------------------------------------------------
import prettytable as pt
from telegram import ParseMode
from telegram.ext import CallbackContext, Updater


def send_table(update: Updater, context: CallbackContext):
    table = pt.PrettyTable(['Symbol', 'Price', 'Change'])
    table.align['Symbol'] = 'l'
    table.align['Price'] = 'r'
    table.align['Change'] = 'r'

    data = [
        ('ABC', 20.85, 1.626),
        ('DEF', 78.95, 0.099),
        ('GHI', 23.45, 0.192),
        ('JKL', 98.85, 0.292),
    ]
    for symbol, price, change in data:
        table.add_row([symbol, f'{price:.2f}', f'{change:.3f}'])

    update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)
    # or use markdown
    update.message.reply_text(f'```{table}```', parse_mode=ParseMode.MARKDOWN_V2)
-----------------------------------------------------------------------------------
"""
