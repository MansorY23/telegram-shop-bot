from aiogram.filters import Filter
from aiogram.types import Message


class CorrectNameFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        #words = message.text.split()
        #for word in words:
        #    if (not word.isalpha()) or (not word.istitle()):
        #        return False
        return True