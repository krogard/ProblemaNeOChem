import asyncio

from utils.db_api.commands import add_item
from utils.db_api.database import create_db


async def add_items():
    await add_item(name = "Бад",
                    category_name="Для здорового сна",cotegory_code="BAD",subcotegory_name="AD" ,subcotegory_code="BADS",
                   price=100,
                   photo="-")
    await add_item(name="Бадс",
                   category_name="Для легкого пищеварения",cotegory_code="BAD",subcotegory_name="AD" ,subcotegory_code="BADS",
                   price=150,
                   photo="-")
    await add_item(name="Бадд",
                   category_name="Для здорового сна",cotegory_code="BAD",subcotegory_name="AD" ,
                   subcotegory_code="BADS", price=200,
                   photo="-")
    await add_item(name="Баддс",
                   category_name="Для легкого пищеварения",cotegory_code="BAD",
                   subcotegory_name="AD",subcotegory_code="BADS", price=300,photo="-")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
    loop.run_until_complete(add_items())