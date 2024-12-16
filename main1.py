from aiogram import Bot, Dispatcher, types
import asyncio

from aiogram.filters import Command

bot=Bot(token="8087486318:AAHnC8UsRBG-SoAe64ih5gArHfu_yHN7B6A")
dp=Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Salom botga xush kelibsiz😃")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
