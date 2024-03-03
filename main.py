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

# 1 меню главное меню
button_random_tea = KeyboardButton(text='Категории чая')
#button_random_tea = KeyboardButton(text='Случайный чай')
button_name_tea = KeyboardButton(text='Полный список')
# 2 меню категории чая
button_green_tea = KeyboardButton(text='Зеленый чай')
button_black_tea = KeyboardButton(text='Черный чай')
button_fruit_tea = KeyboardButton(text='Фруктовый чай')
button_mix_tea = KeyboardButton(text='Смесь чайов')
button_oolong_tea = KeyboardButton(text='чай Улун')
button_rooibos_tea = KeyboardButton(text='Ройбуш чай')
button_fireweed_tea = KeyboardButton(text='Иван-чай')
# в Главное меню
button_first_table = KeyboardButton(text='В Главное меню')

# все чаи рандомный среди всех
button_name_tea_random = KeyboardButton(text='Случайный из всех чайов')
# к выбору сорта
button_type_tea = KeyboardButton(text='Назад к выбору сорта')



# 3 меню выбор случайный или список
button_green_tea_random = KeyboardButton(text='Рандомный Зеленый чай')
button_black_tea_random = KeyboardButton(text='Рандомный Черный чай')
button_fruit_tea_random = KeyboardButton(text='Рандомный Фруктовый чай')
button_mix_tea_random = KeyboardButton(text='Рандомная Смесь чая')
button_oolong_tea_random = KeyboardButton(text='Рандомный чай Улун')
button_rooibos_tea_random = KeyboardButton(text='Рандомный Ройбуш чай')
button_ivan_tea_random = KeyboardButton(text='Рандомный Иван-чай')
# посмотреть весь список определенного чая
button_full_black_tea = KeyboardButton(text='посмотреть весь список Черного чая')
button_full_green_tea = KeyboardButton(text='посмотреть весь список Зеленого чая')
button_full_fruit_tea = KeyboardButton(text='посмотреть весь список Фруктовых чайов')
button_full_mix_tea = KeyboardButton(text='посмотреть весь список Смесь чая')
button_full_oolong_tea = KeyboardButton(text='посмотреть весь список чай Улун')
button_full_rooibos_tea = KeyboardButton(text='посмотреть весь список Ройбуш чай')
button_full_ivan_tea = KeyboardButton(text='посмотреть весь список Иван-чай')
# 4 меню случайный конкретный сорт чая
button_green_tea_random_again = KeyboardButton(text='Выбрать ещё раз Зеленый чай')
button_black_tea_random_again = KeyboardButton(text='Выбрать ещё раз Черный чай')
button_fruit_tea_random_again = KeyboardButton(text='Выбрать ещё раз Фруктовый чай')
button_mix_tea_random_again = KeyboardButton(text='Выбрать ещё раз Смесь чая')
button_oolong_tea_random_again = KeyboardButton(text='Выбрать ещё раз чай Улун')
button_rooibos_tea_random_again = KeyboardButton(text='Выбрать ещё раз Ройбуш чай')
button_ivan_tea_random_again = KeyboardButton(text='Выбрать ещё раз Иван-чай')

# 5 меню весь список конкретного чая

# 6 меню случайный чай из всех
# все чаи рандомный среди всех 2
button_name_tea_random_again = KeyboardButton(text='Выбрать ещё раз Случайный из всех чайов')
# 7 меню просмотр всех чайов

# --------------------------------------------------#--------------------------------------------------
# Создаем объект клавиатуры, добавляя в него кнопки
first_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_random_tea],
              [button_name_tea_random],
              [button_name_tea]],
    resize_keyboard=True
)
# --------------------------------------------------#--------------------------------------------------
two_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_green_tea, button_black_tea],
              [button_fruit_tea, button_mix_tea],
              [button_oolong_tea, button_rooibos_tea],
              [button_fireweed_tea, button_first_table]],
    resize_keyboard=True
)
# --------------------------------------------------#--------------------------------------------------
tree_keyboard_black = ReplyKeyboardMarkup(
    keyboard=[[button_black_tea_random],
              [button_full_black_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
tree_keyboard_green = ReplyKeyboardMarkup(
    keyboard=[[button_green_tea_random],
              [button_full_green_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
tree_keyboard_fruit = ReplyKeyboardMarkup(
    keyboard=[[button_fruit_tea_random],
              [button_full_fruit_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
tree_keyboard_mix = ReplyKeyboardMarkup(
    keyboard=[[button_mix_tea_random],
              [button_full_mix_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
tree_keyboard_oolong = ReplyKeyboardMarkup(
    keyboard=[[button_oolong_tea_random],
              [button_full_oolong_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
tree_keyboard_rooibos = ReplyKeyboardMarkup(
    keyboard=[[button_rooibos_tea_random],
              [button_full_rooibos_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
tree_keyboard_ivan = ReplyKeyboardMarkup(
    keyboard=[[button_ivan_tea_random],
              [button_full_ivan_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
# --------------------------------------------------#--------------------------------------------------
four_keyboard_black = ReplyKeyboardMarkup(
    keyboard=[[button_black_tea_random_again],
              [button_full_black_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
four_keyboard_green = ReplyKeyboardMarkup(
    keyboard=[[button_green_tea_random_again],
              [button_full_green_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
four_keyboard_fruit = ReplyKeyboardMarkup(
    keyboard=[[button_fruit_tea_random_again],
              [button_full_fruit_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
four_keyboard_mix = ReplyKeyboardMarkup(
    keyboard=[[button_mix_tea_random_again],
              [button_full_mix_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
four_keyboard_oolong = ReplyKeyboardMarkup(
    keyboard=[[button_oolong_tea_random_again],
              [button_full_oolong_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
four_keyboard_rooibos = ReplyKeyboardMarkup(
    keyboard=[[button_rooibos_tea_random_again],
              [button_full_rooibos_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
four_keyboard_ivan = ReplyKeyboardMarkup(
    keyboard=[[button_ivan_tea_random_again],
              [button_full_ivan_tea],
              [button_type_tea],
              [button_first_table]],
    resize_keyboard=True
)
# --------------------------------------------------#--------------------------------------------------
'''
five_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_black_tea_random],
              [button_back_tea]],
    resize_keyboard=True
)
'''
# --------------------------------------------------#--------------------------------------------------
"""[button_name_tea_random],"""
six_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_name_tea_random_again],
              [button_first_table]],
    resize_keyboard=True
)
# --------------------------------------------------#--------------------------------------------------
'''
seven_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_black_tea_random],
              [button_back_tea]],
    resize_keyboard=True
)
# --------------------------------------------------#--------------------------------------------------
'''
# --------------------------------------------------#--------------------------------------------------

# --------------------------------------------------#--------------------------------------------------
# хендлер для /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="Привет!\nЯ создан чтобы помочь Тебе с выбором сорта чая. \n\n"
             "Если хочешь узнать все\n"
             "мои возможности - отправь команду /help",
        reply_markup=first_keyboard
    )
# хендлер для /keyboard_tea тоже самое что и (Категориий чай)
@dp.message(F.text == 'Назад к выбору сорта')
async def process_black_tea_command(message: Message):
    await message.answer(
        text="Выберите чай",
        reply_markup=two_keyboard
    )
# хендлер для /keyboard_tea тоже самое что и (Случайный чай)
@dp.message(F.text == 'Случайный чай из всех чайов')
async def process_black_tea_command(message: Message):
    await message.answer(
        text="Выберите чай",
        reply_markup=six_keyboard
    )
# хендлер для /keyboard_tea
@dp.message(F.text == 'Категории чая')
async def process_black_tea_command(message: Message):
    await message.answer(
        text="Выберите чай",
        reply_markup=two_keyboard
    )
# хендлер для /keyboard_tea для переходы в главное меню
@dp.message(F.text == 'В Главное меню')
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
@dp.message(F.text == 'Случайный из всех чайов')
async def process_random_tea_command(message: Message):
    a = random.choice(tea_all_table[1])
    b = 0

    for i in range(0, len(tea_all_table[1])):
        if tea_all_table[1][i] == a:
            b = i
            break
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b]}\n\n'
             f'Описание:\n    {tea_all_table[2][b]}\n\n',
        reply_markup=six_keyboard
    )
# хендлер для 'Рандомные Все чаи' 2
@dp.message(F.text == 'Выбрать ещё раз Случайный из всех чайов')
async def process_random_tea_command(message: Message):
    a = random.choice(tea_all_table[1])
    b = 0

    for i in range(0, len(tea_all_table[1])):
        if tea_all_table[1][i] == a:
            b = i
            break
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b]}\n\n'
             f'Описание:\n    {tea_all_table[2][b]}\n\n',
        reply_markup=six_keyboard
    )
# ==========================================================================================
# ==========================================================================================
# хендлер для 'Зелёный чай' выводит весь список
@dp.message(F.text == 'посмотреть весь список Зеленого чая')
async def process_green_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Зелёный':
            await message.answer(f'{tea_all_table[1][i]}')

# хендлер для 'Зеленый чай'
@dp.message(F.text == 'Зеленый чай')
async def process_black_tea_command(message: Message):
    await message.answer(
                    text="Хотите посмотреть весь\n"
                         "список зеленого чая или\n"
                         "доверить судьбу чаепития\n"
                         "богу рандома?\n(0_-)",
                    reply_markup=tree_keyboard_green
    )

# хендлер для рандомного чая зеленый
@dp.message(F.text == 'Рандомный Зеленый чай')
async def process_green_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Зелёный':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup = four_keyboard_green
    )
# хендлер для рандомного чая зеленый 2
@dp.message(F.text == 'Выбрать ещё раз Зеленый чай')
async def process_green_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Зелёный':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup = four_keyboard_green
    )
# ==========================================================================================
# ==========================================================================================
# хендлер для 'Черный чай' выводит весь список
@dp.message(F.text == 'посмотреть весь список Черного чая')
async def process_black_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Чёрный чай':
            await message.answer(f'{tea_all_table[1][i]}')

# хендлер для 'Черный чай'
@dp.message(F.text == 'Черный чай')
async def process_black_tea_command(message: Message):
    await message.answer(
                    text="Хотите посмотреть весь\n"
                         "список черного чая или\n"
                         "доверить судьбу чаепития\n"
                         "богу рандома?\n(0_-)",
                    reply_markup=tree_keyboard_black
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
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup = four_keyboard_black
    )
# хендлер для рандомного чая черный 2
@dp.message(F.text == 'Выбрать ещё раз Черный чай')
async def process_green_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Чёрный чай':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup = four_keyboard_black
    )
# ==========================================================================================
# ==========================================================================================
# хендлер для 'Фруктовый чай' выводит весь список
@dp.message(F.text == 'посмотреть весь список Фруктовых чайов')
async def process_fruit_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Фруктовый':
            await message.answer(f'{tea_all_table[1][i]}')

# хендлер для 'Черный чай'
@dp.message(F.text == 'Фруктовый чай')
async def process_fruit_tea_command(message: Message):
    await message.answer(
                    text="Хотите посмотреть весь\n"
                         "список фруктового чая или\n"
                         "доверить судьбу чаепития\n"
                         "богу рандома?\n(0_-)",
                    reply_markup=tree_keyboard_fruit
    )

# хендлер для рандомного чая фруктового
@dp.message(F.text == 'Рандомный Фруктовый чай')
async def process_fruit_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Фруктовый':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup = four_keyboard_fruit
    )
# хендлер для рандомного чая еще раз фруктового
@dp.message(F.text == 'Выбрать ещё раз Фруктовый чай')
async def process_fruit_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Фруктовый':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup = four_keyboard_fruit
    )
# ==========================================================================================
# ==========================================================================================
# хендлер для 'Смесь чайов' выводит весь список
@dp.message(F.text == 'посмотреть весь список Смесь чая')
async def process_mix_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Смесь':
            await message.answer(f'{tea_all_table[1][i]}')

# хендлер для 'Смесь чайов'
@dp.message(F.text == 'Смесь чайов')
async def process_mix_tea_command(message: Message):
    await message.answer(
                    text="Хотите посмотреть весь\n"
                         "список Смесь чая или\n"
                         "доверить судьбу чаепития\n"
                         "богу рандома?\n(0_-)",
                    reply_markup=tree_keyboard_mix
    )

# хендлер для рандомная Смесь чайов
@dp.message(F.text == 'Рандомная Смесь чая')
async def process_mix_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Смесь':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup=four_keyboard_mix
    )
# хендлер для рандомная Смесь чайов 2
@dp.message(F.text == 'Выбрать ещё раз Смесь чая')
async def process_mix_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Смесь':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup=four_keyboard_mix
    )
# ==========================================================================================
# ==========================================================================================
# хендлер для 'чай Улун' выводит весь список
@dp.message(F.text == 'посмотреть весь список чай Улун')
async def process_oolong_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Улун':
            await message.answer(f'{tea_all_table[1][i]}')


# хендлер для 'чая Улун'
@dp.message(F.text == 'чай Улун')
async def process_oolong_tea_command(message: Message):
    await message.answer(
                    text="Хотите посмотреть весь\n"
                         "список чая Улун или\n"
                         "доверить судьбу чаепития\n"
                         "богу рандома?\n(0_-)",
                    reply_markup=tree_keyboard_oolong
    )

# хендлер для рандомного чая Улун
@dp.message(F.text == 'Рандомный чай Улун')
async def process_oolong_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Улун':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup=four_keyboard_oolong
    )
# хендлер для рандомного чая Улун 2
@dp.message(F.text == 'Выбрать ещё раз чай Улун')
async def process_oolong_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Улун':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup=four_keyboard_oolong
    )
# ==========================================================================================
# ==========================================================================================
# хендлер для 'Ройбуш чай' выводит весь список
@dp.message(F.text == 'посмотреть весь список Ройбуш чай')
async def process_rooibos_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Ройбуш':
            await message.answer(f'{tea_all_table[1][i]}')

# хендлер для 'Черный чай'
@dp.message(F.text == 'Ройбуш чай')
async def process_rooibos_tea_command(message: Message):
    await message.answer(
                    text="Хотите посмотреть весь\n"
                         "список чая Ройбуш или\n"
                         "доверить судьбу чаепития\n"
                         "богу рандома?\n(0_-)",
                    reply_markup=tree_keyboard_rooibos
    )

# хендлер для рандомного чая черный
@dp.message(F.text == 'Рандомный Ройбуш чай')
async def process_rooibos_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Ройбуш':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup=four_keyboard_rooibos
    )
# хендлер для рандомного чая черный 2
@dp.message(F.text == 'Выбрать ещё раз Ройбуш чай')
async def process_rooibos_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Ройбуш':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup=four_keyboard_rooibos
    )
# ==========================================================================================
# ==========================================================================================
# хендлер для 'Иван-чай' выводит весь список
@dp.message(F.text == 'посмотреть весь список Иван-чай')
async def process_ivan_tea_command(message: Message):
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Иван-чай':
            await message.answer(f'{tea_all_table[1][i]}')

# хендлер для Иван-чай
@dp.message(F.text == 'Иван-чай')
async def process_ivan_tea_command(message: Message):
    await message.answer(
                    text="Хотите посмотреть весь\n"
                         "список Иван-чая или\n"
                         "доверить судьбу чаепития\n"
                         "богу рандома?\n(0_-)",
                    reply_markup=tree_keyboard_ivan
    )

# хендлер для рандомного Иван-чай
@dp.message(F.text == 'Рандомный Иван-чай')
async def process_ivan_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Иван-чай':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup=four_keyboard_ivan
    )
# хендлер для рандомного Иван-чай2
@dp.message(F.text == 'Выбрать ещё раз Иван-чай')
async def process_ivan_tea_command(message: Message):
    a12 = []
    b12 = 0
    for i in range(len(tea_all_table[4])):
        if tea_all_table[4][i] == 'Иван-чай':
            a12.append(i)
    b12 = random.choice(a12)
    await message.answer(
        text=f'Название:\n    {tea_all_table[1][b12]}\n\n'
             f'Сорт:\n    {tea_all_table[4][b12]}\n\n'
             f'Описание:\n    {tea_all_table[2][b12]}\n\n',
        reply_markup=four_keyboard_ivan
    )
# ==========================================================================================
# ==========================================================================================

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
