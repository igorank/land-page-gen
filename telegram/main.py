import os
import logging

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

from generate_from_file import get_list_of_dirs, generate

logging.basicConfig(level=logging.INFO)

cwd = os.getcwd()
root = os.path.split(os.path.split(cwd)[0])[0] + '\\' \
       + os.path.split(os.path.split(cwd)[0])[1]
templates_dir = os.path.join(root, 'templates')

API_TOKEN = '6211790389:AAEZI-aryehqSpbbQWPwnn3k9B2sOBrVlNs'
MENU = ["💎 Сгенерировать вайт", "🆘 Помощь", "💳 Баланс", "📄 Профиль"]
start_text = "Привет, этот бот может генерировать уникальные вайты 😎"
file_help = open('help.txt', 'r', encoding='UTF-8')
help_text = file_help.read()

bot = Bot(token=API_TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def get_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("💎 Сгенерировать вайт", "🆘 Помощь")
    markup.add("💳 Баланс", "📄 Профиль")
    return markup


# States
class Form(StatesGroup):
    choosing_solution = State()
    choosing_landing_page_name = State()
    choosing_landing_page_details = State()
    choosing_landing_page_category = State()
    help = State()


# @dp.message_handler(commands='start')
@dp.message_handler(state='*', commands='start')
@dp.message_handler(Text(equals='start', ignore_case=True), state='*')
async def cmd_start(message: types.Message, state: FSMContext):
    """
    Conversation's entry point
    """
    # # Set state
    # await Form.intro.set()
    await state.set_state(Form.choosing_solution)

    # Configure ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("💎 Сгенерировать вайт", "🆘 Помощь")
    markup.add("💳 Баланс", "📄 Профиль")

    await message.reply(start_text, reply_markup=get_menu_markup())


@dp.message_handler(lambda message: message.text not in MENU, state=Form.choosing_solution)
async def process_solution_invalid(message: types.Message):
    return await message.reply("Команда не найдена")


# # You can use state '*' if you need to handle all states
# @dp.message_handler(state='*', commands='cancel')
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
# async def cancel_handler(message: types.Message, state: FSMContext):
#     """
#     Allow user to cancel any action
#     """
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#
#     logging.info('Cancelling state %r', current_state)
#     # Cancel state and inform user about it
#     await state.finish()
#     # And remove keyboard (just in case)
#     await message.reply('Cancelled', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text in MENU, state=Form.choosing_solution)
async def process_solution(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sol1'] = message.text

    match data['sol1']:
        case "💎 Сгенерировать вайт":
            await state.set_state(Form.choosing_landing_page_name)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
            markup.add("Назад")

            await message.answer("Введите название вайта", reply_markup=markup)
        case "🆘 Помощь":
            await message.answer(help_text)
        case "📄 Профиль":
            await message.answer(f"Ваш ID: {message.from_user.id}\n"
                                 f"Ваш никнейм: {message.from_user.username}")
        case _:
            pass


@dp.message_handler(lambda message: message.text == "Назад", state=Form.choosing_landing_page_name)
async def name_back(message: types.Message, state: FSMContext):
    await Form.previous()
    await bot.send_message(message.from_user.id, start_text, reply_markup=get_menu_markup())


@dp.message_handler(state=Form.choosing_landing_page_name)
async def process_landing_page_name(message: types.Message, state: FSMContext):
    if not message.text:
        await message.reply("Недопустимое имя")

    async with state.proxy() as data:
        data['landing_page_name'] = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Назад")

    await state.set_state(Form.choosing_landing_page_details)
    await message.answer("Введите описание вайт пейджа", reply_markup=markup)


@dp.message_handler(lambda message: message.text == "Назад", state=Form.choosing_landing_page_details)
async def details_back(message: types.Message, state: FSMContext):
    await state.set_state(Form.choosing_landing_page_name)
    await bot.send_message(message.from_user.id, "Введите название вайта")


@dp.message_handler(state=Form.choosing_landing_page_details)
async def process_landing_page_details(message: types.Message, state: FSMContext):
    if not message.text:
        await message.reply("Недопустимое описание")

    async with state.proxy() as data:
        data['landing_page_details'] = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Назад")

    dirs = get_list_of_dirs(templates_dir)
    dirs.sort()
    newline = "\n"

    await state.set_state(Form.choosing_landing_page_category)
    await message.answer(f'Выберите категорию сайта:\n{newline.join(f"{value}" for value in dirs)}',
                         reply_markup=markup)


@dp.message_handler(lambda message: message.text == "Назад", state=Form.choosing_landing_page_category)
async def details_back(message: types.Message, state: FSMContext):
    await state.set_state(Form.choosing_landing_page_details)
    await bot.send_message(message.from_user.id, "Введите описание вайт пейджа")


@dp.message_handler(lambda message: message.text not in get_list_of_dirs(templates_dir),
                    state=Form.choosing_landing_page_category)
async def process_solution_invalid(message: types.Message):
    return await message.reply("Категория не найдена")


@dp.message_handler(state=Form.choosing_landing_page_category)
async def process_landing_page_details(message: types.Message, state: FSMContext):
    if not message.text:
        await message.reply("Недопустимая категория")

    await message.answer("Вайт-пейдж генерируется...", reply_markup=types.ReplyKeyboardRemove())

    async with state.proxy() as data:
        data['landing_page_category'] = message.text
        page_data = {'name': data['landing_page_name'], 'details': data['landing_page_details']}
        if not generate(root, templates_dir, data['landing_page_category'], page_data):
            await state.set_state(Form.choosing_solution)
            await message.answer("Ошибка: Вы достигли лимита. Пожалуйста, повторите попытку позже.")
            await message.answer(start_text, reply_markup=get_menu_markup())
        else:
            await state.set_state(Form.choosing_solution)
            await message.answer_document(open(root + "\\white_page.zip", "rb"))
            await message.answer(start_text, reply_markup=get_menu_markup())


@dp.message_handler(state=Form.help)
async def process_help(message: types.Message, state: FSMContext):
    inline_btn = types.InlineKeyboardButton('Назад', callback_data='back')
    inline_kb = types.InlineKeyboardMarkup().add(inline_btn)

    await message.reply("Назад", reply_markup=inline_kb)


# @dp.callback_query_handler(text='back', state=Form.choosing_landing_page_name)
# async def back(message: types.CallbackQuery, state: FSMContext):
#     await Form.previous()
#     await bot.send_message(message.from_user.id, start_text)


# # Check age. Age gotta be digit
# @dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
# async def process_age_invalid(message: types.Message):
#     """
#     If age is invalid
#     """
#     return await message.reply("Age gotta be a number.\nHow old are you? (digits only)")


# @dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
# async def process_age(message: types.Message, state: FSMContext):
#     # Update state and data
#     await Form.next()
#     await state.update_data(age=int(message.text))
#
#     # Configure ReplyKeyboardMarkup
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
#     markup.add("Male", "Female")
#     markup.add("Other")
#
#     await message.reply("What is your gender?", reply_markup=markup)
#
#
# @dp.message_handler(lambda message: message.text not in ["Male", "Female", "Other"], state=Form.gender)
# async def process_gender_invalid(message: types.Message):
#     """
#     In this example gender has to be one of: Male, Female, Other.
#     """
#     return await message.reply("Bad gender name. Choose your gender from the keyboard.")
#
#
# @dp.message_handler(state=Form.gender)
# async def process_gender(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['gender'] = message.text
#
#         # Remove keyboard
#         markup = types.ReplyKeyboardRemove()
#
#         # And send message
#         await bot.send_message(
#             message.chat.id,
#             md.text(
#                 md.text('Hi! Nice to meet you,', md.bold(data['name'])),
#                 md.text('Age:', md.code(data['age'])),
#                 md.text('Gender:', data['gender']),
#                 sep='\n',
#             ),
#             reply_markup=markup,
#             parse_mode=ParseMode.MARKDOWN,
#         )
#
#     # Finish conversation
#     await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
