from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = "5160233570:AAF_z2jV3rP0EjgTqjJgG1NgLzLqvqkw1i8"
bot = Bot(token=token)

dp = Dispatcher(bot)


try:
    @dp.message_handler(commands=["sirena"])
    async def start_command(message: types.Message):
        await bot.send_message(chat_id=message.chat.id, text="Наразі є 2 види сигналів:\n— Переривистий «Увага всім». Він означає підготовку до укриття.\n— Безперервний. Він означає повітряну тривогу.\n ----------------------------------------------------------------------------------------------\nЗвук команди «Увага всім» постійний та рівномірний, загальною тривалістю до 7 секунд.\nЗвук повітряної тривоги довгий і триває до 1 хвилини.\nКоли ви чуєте звук «Увага всім», потрібно увімкнути телевізор або приймач і слухати подальші інструкції;\nКоли ви чуєте звук повітряної тривоги, потрібно терміново перейти до найближчого укриття. Такі сигнали зазвичай подаються 3 рази.\nПісля звучання сирен, команда відбій звучати не буде. За рекомендаціями виходити з укриттів пропонується через 1 годину 15 хвилин. Якщо протягом цього часу буде звучати повторна сирена, це сигнал, що знову виникла загроза. Рахунок часу ведеться від останнього сигналу.\n\n Додаток який сповіщає про повітряну тривогу: https://play.google.com/store/apps/details?id=com.ukrainealarm")

    @dp.message_handler(commands=["shelter"])
    async def send_photo(message: types.Message):
        with open('1.jpg', 'rb') as photo:
            await bot.send_photo(chat_id=message.chat.id, photo=photo)
        with open('2.jpg', 'rb') as photo:
            await bot.send_photo(chat_id=message.chat.id, photo=photo)


    @dp.message_handler(commands=["other_information"])
    async def send_info(message: types.Message):
        await bot.send_message(chat_id=message.chat.id, text="Додаткова інформація:\n")
        with open('3.jpg', 'rb') as photo:
            await bot.send_photo(chat_id=message.chat.id,photo=photo)
        await bot.send_message(chat_id=message.chat.id,text="\n@stop_russian_war_bot")
        await bot.send_message(chat_id=message.chat.id,text="\nЯкщо вам є що додати до цього боту напишіть в особисті повідомлення @verybigmen")
except: 
    pass
if __name__ == "__main__":
    executor.start_polling(dp)