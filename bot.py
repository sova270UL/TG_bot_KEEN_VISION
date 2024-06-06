import asyncio
from aiogram import Bot, Dispatcher, F, types, filters
from aiogram. filters import Command 
from aiogram.types import Message

import keybords
import config 

TOKEN = config.token
bot = Bot(TOKEN) 
dp = Dispatcher() 


objects_list = ["obj 1", "obj 2"]

location = ''
final_data = {}
@dp.message(Command("start")) 
async def start(message: Message): 
    await message.answer("Выберите объект", reply_markup=keybords.location_repair_KB)

@dp.callback_query(F.data == "obj 1")
async def obj(callback: types.CallbackQuery):
    global location
    await callback.message.answer(f"Отправьте фото несиправности на {callback.data}")
    location = callback.data
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)



    
@dp.callback_query(F.data == "obj 2")
async def obj(callback: types.CallbackQuery):
    global location
    await callback.message.answer(f"Отправьте фото несиправности на {callback.data}")
    location = callback.data
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
        
    
@dp.message(F.photo)
async def photo_handler(message: Message):
    global location
    if location != "":
        photo = message.photo[-1]
        await bot.send_message(chat_id='-1002188703768', text = f"С объекта {location} пришла фотография")
        await bot.send_photo(chat_id='-1002188703768', photo=photo.file_id, reply_markup=keybords.variants_repair_KB)
    else:
        await message.answer("Перед отправкой фото начала выполните /start и выберите объект")

@dp.callback_query(F.data)
async def variants_repair(callback: types.CallbackQuery):
    global location
    global final_data
    for i in keybords.variants_repair_Cb_list:
        if callback.data == i:
            await bot.send_message(chat_id='-1002188703768', text = f"На объекте {location} неисправность {i} \n\nОТПАРВЛЕННО")
            final_data = {"location" : location, "variants": i}
            print(final_data)

async def main(): 
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot) 

if __name__ == "__main__": 
    asyncio.run(main()) 