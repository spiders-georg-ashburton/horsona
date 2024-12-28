from cerebras.cloud.sdk import AsyncCerebras, AsyncStream
from cerebras.cloud.sdk.types.chat.chat_completion import CompletionCreateResponse

from .oai_engine import AsyncOAIEngine


class AsyncCerebrasEngine(AsyncOAIEngine):
    """
    An asynchronous implementation of ChatEngine for interacting with Cerebras models.

    This class provides an asynchronous interface for querying Cerebras language models.

    Attributes:
        model (str): The name of the Cerebras model to use.
        client (AsyncCerebras): An instance of the asynchronous Cerebras client for API interactions.

    Inherits from:
        AsyncChatEngine
    """

    def __init__(self, model: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.model = model
        self.client = AsyncCerebras()

    async def create(
        self, **kwargs
    ) -> AsyncStream[CompletionCreateResponse] | CompletionCreateResponse:
        kwargs["model"] = self.model
        return await self.client.chat.completions.create(timeout=2, **kwargs)
