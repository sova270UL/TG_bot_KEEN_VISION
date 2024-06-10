from aiogram. filters import Command 
from aiogram.types import Message
from aiogram import Router


router = Router()
@router.message(Command("start")) 
async def start(message: Message): 
    await message.answer("Выберите объект", reply_markup=keybords.location_repair_KB)