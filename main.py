from prettytable import PrettyTable

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import BotCommand, Message

BOT_TOKEN = '7023815986:AAGqZLAIqYsFG30fsN2FLvVka8EPGK6mCNY'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# словарь для хранения данных пользователя
users = {}

# Укажите имена столбцов при инициализации таблицы
teaTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

# Добавление строк
teaTable.add_row(["Leanord", "X", "B", "91.2 %"])
teaTable.add_row(["Lean", "X", "B", "91.2 %"])
teaTable.add_row(["Lean\nordsdg", "X", "B", "91.2 %"])
teaTable.add_row(["Leanorddgsdg", "X", "B", "91.2 %"])
# teaTable.title(['заголовок таблицы'])
teaTable._title = 'заголовок таблицы'

# хендлер для /чай
@dp.message(Command(commands='tea'))
async def process_tea_command(message: Message):
    await message.answer(f'{teaTable}')


# хендлер для /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Привет!\nДавайте сыграем в игру "Угадай число"?\n\n'
        'Чтобы получить правила игры и список доступных '
        'команд - отправьте команду /help'
    )
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


# хендлер на остальные сообщения
@dp.message()
async def process_other_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer(
            'Мы же сейчас с вами играем. '
            'Присылайте, пожалуйста, числа от 1 до 100'
        )
    else:
        await message.answer(
            'Я довольно ограниченный бот, давайте '
            'просто сыграем в игру?'
        )


# Создаем асинхронную функцию для кнопки menu
async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/tea',
                   description='Открывает таблицу с чаем'),
    ]
    await bot.set_my_commands(main_menu_commands)


# Регистрируем асинхронную функцию в диспетчере,
# которая будет выполняться на старте бота,
dp.startup.register(set_main_menu)

if __name__ == '__main__':
    dp.run_polling(bot)
