from typing import Union

from aiogram.dispatcher.filters import Command
from aiogram import types

from keyboards.inline.menu_keybord import categories_keybord, items_keybord, menu_cd, subcategories_keybord
from loader import dp
from utils.db_api.commands import get_item


@dp.message_handler(Command("menu"))
async def show_menu(messege: types.Message):
    await messege.answer("Выберите соответствующий пункт меню")
    await list_categories(messege)


async def list_categories(message: Union[types.Message, types.CallbackQuery]):
    markup = await categories_keybord()
    if isinstance(message, types.Message):
        await message.answer("Представленные БАДы", reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def list_subcategories(callback: types.CallbackQuery, category, subcategory, **kwargs):
    markup = await subcategories_keybord(category)
    await callback.message.edit_reply_markup(markup)


async def list_items(callback: types.CallbackQuery, category, subcategory, **kwargs):
    markup = await  items_keybord(category=category, subcategory=subcategory)
    await callback.message.edit_text("Представленные БАДы", reply_markup=markup)


async def show_item(callback: types.CallbackQuery, category, subcategory, item_id):
    markup = items_keybord(category, subcategory, item_id)

    item = await get_item(item_id)
    text = f"Купите {item}"
    await callback.message.edit_text(text, reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")
    category = callback_data.get("category")
    subcategory = callback_data.get("subcategory")
    item_id = callback_data.get('item_id')
    levels = {
        "0": list_categories,
        "1": list_subcategories,
        "2": list_items,
        "3": show_item
    }
    current_level_function = levels[current_level]

    await current_level_function(
        call,
        category=category,
        subcategory=subcategory,
        item_id=item_id
    )
