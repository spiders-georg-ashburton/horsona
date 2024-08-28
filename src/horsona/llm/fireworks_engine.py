from fireworks.client import AsyncFireworks, Fireworks

from .chat_engine import AsyncChatEngine, ChatEngine


class FireworksEngine(ChatEngine):
    """
    A concrete implementation of ChatEngine for interacting with Fireworks models.

    This class provides a synchronous interface for querying Fireworks language models.

    Attributes:
        model (str): The name of the Fireworks model to use.
        client (Fireworks): An instance of the Fireworks client for API interactions.

    Inherits from:
        ChatEngine
    """

    def __init__(self, model: str, *args, **kwargs):
        """
        Initialize the FireworksEngine.

        Args:
            model (str): The name of the Fireworks model to use.
            *args: Variable length argument list to pass to the parent constructor.
            **kwargs: Arbitrary keyword arguments to pass to the parent constructor.
        """
        super().__init__(*args, **kwargs)
        self.model = model
        self.client = Fireworks()

    def query(self, **kwargs):
        response = self.client.chat.completions.create(
            model=self.model, stream=False, **kwargs
        )
        return response.choices[0].message.content


class AsyncFireworksEngine(AsyncChatEngine):
    """
    An asynchronous implementation of ChatEngine for interacting with Fireworks models.

    This class provides an asynchronous interface for querying Fireworks language models.

    Attributes:
        model (str): The name of the Fireworks model to use.
        client (AsyncFireworks): An instance of the asynchronous Fireworks client for API interactions.

    Inherits from:
        AsyncChatEngine
    """

    def __init__(self, model: str, *args, **kwargs):
        """
        Initialize the AsyncFireworksEngine.

        Args:
            model (str): The name of the Fireworks model to use.
            *args: Variable length argument list to pass to the parent constructor.
            **kwargs: Arbitrary keyword arguments to pass to the parent constructor.
        """
        super().__init__(*args, **kwargs)
        self.model = model
        self.client = AsyncFireworks()

    async def query(self, **kwargs):
        response = await self.client.chat.completions.acreate(
            model=self.model, stream=False, **kwargs
        )
        return response.choices[0].message.content
