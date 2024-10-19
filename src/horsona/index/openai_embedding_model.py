from openai import AsyncOpenAI

from horsona.index.embedding_model import EmbeddingModel


class OpenAIEmbeddingModel(EmbeddingModel):
    def __init__(self, model: str, **kwargs):
        super().__init__()
        self.model = model
        self.kwargs = kwargs

    async def get_data_embeddings(self, sentences):
        client = AsyncOpenAI(**self.kwargs)
        response = await client.embeddings.create(model=self.model, input=sentences)
        return [embedding.embedding for embedding in response.data]

    async def get_query_embeddings(self, sentences):
        return await self.get_data_embeddings(sentences)