from shop_bot.repository.base import BaseRepository
from shop_bot.models.db.item import Item

import sqlalchemy


class ItemRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)

    async def select_all(self):
        stmt = sqlalchemy.select(Item)
        query = await self.session.execute(statement=stmt)
        return query.scalars().all()