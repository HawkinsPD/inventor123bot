import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7589765067:AAHP4xl755AKS-xfKsXIgi1Gd0s7d-YiPJw")
# Диспетчер
dp = Dispatcher()

layout_button = KeyboardButton(text='schmot')
layout_button2 = KeyboardButton(text='schmot2')
layout_menu = ReplyKeyboardMarkup(keyboard=[
    [layout_button], [layout_button2]
])


@dp.message(lambda msg: "schmot" == msg.text)
async def test(message: types.Message) -> None:
    await message.answer(text="qwe")

@dp.message(lambda msg: "schmot2" == msg.text)
async def test(message: types.Message) -> None:
    await message.answer(text="asd123")



# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # await message.answer(text="test")
    await message.answer(reply_markup = layout_menu, text="test")

@dp.message(Command("qwe123"))
async def cmd_start(message: types.Message):
    await message.answer(message.text)

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.reply_dice(emoji="🎲")



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

# 7589765067:AAHP4xl755AKS-xfKsXIgi1Gd0s7d-YiPJw