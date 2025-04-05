
from abc import ABC, abstractmethod
from typing import AsyncIterable


class LlmProvider(ABC):

    @abstractmethod
    async def async_stream_chat(self, messages, model) -> AsyncIterable[dict]:
        raise NotImplementedError

