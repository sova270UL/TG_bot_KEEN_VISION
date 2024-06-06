from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

location_repair_KB = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text= "obj 1", callback_data="obj 1"),
        InlineKeyboardButton(text= "obj 2", callback_data="obj 2")

    ]]
)

variants_repair_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "reason 1", callback_data="reason 1")],
        [InlineKeyboardButton(text= "reason 2", callback_data="reason 2")],
        [InlineKeyboardButton(text= "reason 3", callback_data="reason 3")],
        [InlineKeyboardButton(text= "reason 4", callback_data="reason 4")],
        [InlineKeyboardButton(text= "reason 5", callback_data="reason 5")],
        [InlineKeyboardButton(text= "reason 6", callback_data="reason 6")],
        [InlineKeyboardButton(text= "reason 7", callback_data="reason 7")]
    ]
)

variants_repair_Cb_list = [
"reason 1",
"reason 2",
"reason 3",
"reason 4",
"reason 5",
"reason 6",
"reason 7"]