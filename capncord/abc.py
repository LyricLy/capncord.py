from abc import ABC, abstractmethod
from typing import List


class Messageable(ABC):
    def __init__(self, bot):
        self.bot = bot

    @abstractmethod
    async def send(self, content: str) -> Message:
        pass

    @abstractmethod
    async def history(self) -> List[Message]:
        pass
