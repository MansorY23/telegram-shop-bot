from aiogram.filters import Filter
from aiogram.types import Message

import re


class CorrectURLFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
        if not re.match(url_pattern, message.text):
            return False
        return True