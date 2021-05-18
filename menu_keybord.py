from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup

from utils.db_api.commands import get_categories, count_items, get_subcategories, get_items

menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")


def callback_date(level, category="0", subcategory="0", item_id="0"):
    return menu_cd.new(level=level, category=category,
                       subcategory=subcategory, item_id=item_id)


async def categories_keybords():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()

    categories = await get_categories()
    for category in categories:
        num_of_items = await count_items(category.category_code)
        button_text = f"{category.category_name} ({num_of_items} шт)"
        callback_data = callback_date(level=CURRENT_LEVEL + 1,
                                      category=category.category_code)
        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


async def subcategories_keybord(category):
    CURENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    subcategories = await  get_subcategories(category)
    for subcategory in subcategories:
        number_og_items = await count_items(category_code=category,
                                            subcategory_code=subcategory)
        button_text = f"{subcategory.subcategory_name} ({number_og_items}) шт"
        callback_data = callback_date(level=CURENT_LEVEL + 1,
                                      category=category,
                                      subcategory=subcategory.subcategory_code)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardMarkup(
            text="Назад",
            callback_data=callback_date(level=CURENT_LEVEL - 1)
        )
    )
    return markup


async def items_keybord(category, subcategory):
    CURENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)

    items = await get_items(category, subcategory)
    for item in items:
        button_text = f"{item.name} - ${item.price}"
        callback_data = callback_date(level=CURENT_LEVEL + 1,
                                      category=category, subcategory=subcategory,
                                      item_id=item.id)
        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardMarkup(
            text="Назад",
            callback_data=callback_date(level=CURENT_LEVEL - 1,
                                        category=category)
        )
    )
    return markup


def item_keybord(category, subcategory, item_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardMarkup(text="Купить",
                             callback_data=buy_item.new(item_id=item_id))
    )
    markup.row(
        InlineKeyboardMarkup(text="Назад",
                             callback_data=callback_date(level=CURRENT_LEVEL - 1,
                                                         category=category,
                                                         subcategory=subcategory)
                             )
    )
    return markup
