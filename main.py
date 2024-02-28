from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import BotCommand, Message

import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

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


# словарь для хранения данных пользователя
# users = {}


# хендлер для /name_tea
@dp.message(Command(commands='name_tea'))
async def process_tea_command(message: Message):
    for i in range(len(tea_all_table[1])):
        await message.answer(f'{tea_all_table[1][i]}')


# хендлер для /help
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(f'Заглушка, здесь будет ПОМОЩЬ\n'
                         f'/name_tea - Отправляет названия всех чайов\n'
                         f'/green_tea - Полный список всех ЗЕЛЕНЫХ чайов\n')


# хендлер для /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Привет!\nЯ создан чтобы помочь Тебе с выбором сорта чая. \n\n'
        'Если хочешь узнать все\n'
        'мои возможности - отправь команду /help'
    )

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

# хендлер для /green_tea
@dp.message(Command(commands='green_tea'))
async def process_tea_command(message: Message):
    for i in range(len(tea_all_table[1])):
        if tea_all_table[5][i] == 'Зелёный':
            await message.answer(f'{tea_all_table[1][i]}')

# хендлер для /black_tea
@dp.message(Command(commands='black_tea'))
async def process_tea_command(message: Message):
    for i in range(len(tea_all_table[1])):
        if tea_all_table[5][i] == 'Чёрный чай':
            await message.answer(f'{tea_all_table[1][i]}')

# хендлер для /black_tea
@dp.message(Command(commands='fruit_tea'))
async def process_tea_command(message: Message):
    for i in range(len(tea_all_table[1])):
        if tea_all_table[5][i] == 'Фруктовый':
            await message.answer(f'{tea_all_table[1][i]}')

# хендлер для /black_tea
@dp.message(Command(commands='ulugh_tea'))
async def process_tea_command(message: Message):
    for i in range(len(tea_all_table[1])):
        if tea_all_table[5][i] == 'Улун':
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
