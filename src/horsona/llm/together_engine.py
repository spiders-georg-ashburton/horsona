from together import AsyncTogether, Together

from .chat_engine import AsyncChatEngine, ChatEngine


class TogetherEngine(ChatEngine):
    """
    A concrete implementation of ChatEngine for interacting with Together models.

    This class provides a synchronous interface for querying Together language models.

    Attributes:
        model (str): The name of the Together model to use.
        client (Together): An instance of the Together client for API interactions.

    Inherits from:
        ChatEngine
    """

    def __init__(self, model: str, *args, **kwargs):
        """
        Initialize the TogetherEngine.

        Args:
            model (str): The name of the Together model to use.
            *args: Variable length argument list to pass to the parent constructor.
            **kwargs: Arbitrary keyword arguments to pass to the parent constructor.
        """
        super().__init__(*args, **kwargs)
        self.model = model
        self.client = Together()

    def query(self, **kwargs):
        response = self.client.chat.completions.create(
            model=self.model, stream=False, **kwargs
        )
        return response.choices[0].message.content


class AsyncTogetherEngine(AsyncChatEngine):
    """
    An asynchronous implementation of ChatEngine for interacting with Together models.

    This class provides an asynchronous interface for querying Together language models.

    Attributes:
        model (str): The name of the Together model to use.
        client (AsyncTogether): An instance of the asynchronous Together client for API interactions.

    Inherits from:
        AsyncChatEngine
    """

    def __init__(self, model: str, *args, **kwargs):
        """
        Initialize the AsyncTogetherEngine.

        Args:
            model (str): The name of the Together model to use.
            *args: Variable length argument list to pass to the parent constructor.
            **kwargs: Arbitrary keyword arguments to pass to the parent constructor.
        """
        super().__init__(*args, **kwargs)
        self.model = model
        self.client = AsyncTogether()

    async def query(self, **kwargs):
        response = await self.client.chat.completions.create(
            model=self.model, stream=False, **kwargs
        )
        return response.choices[0].message.content