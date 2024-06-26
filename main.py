import logging

from aiogram import Bot, Dispatcher, executor, types
import wikipedia


API_TOKEN = '7477948054:AAHk8GFNEhbO_3c_Hv9LCGH3y8s6yjROz9o'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom🙌\nBotga xush kelibsiz Xabaringizni yozib yuboring")



@dp.message_handler()
async def wiki(message: types.Message):
    try:
        result=wikipedia.summary(message.text)
        await message.answer(result)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi😒')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
