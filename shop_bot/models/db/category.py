from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shop_bot.models.db.item import Item
from shop_bot.models.db.base import BaseModel


class Category(BaseModel):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    items: Mapped["Item"] = relationship(back_populates='categories')
