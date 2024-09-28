from shop_bot.repository.base import BaseRepository
from shop_bot.models.db.category import Category

import sqlalchemy


class CategoryRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)

    async def select_all(self):
        stmt = sqlalchemy.select(Category)
        query = await self.session.execute(statement=stmt)
        return query.scalars().all()