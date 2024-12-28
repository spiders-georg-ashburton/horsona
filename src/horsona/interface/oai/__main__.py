import argparse
import asyncio

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from horsona.config import load_llms
from horsona.interface import oai

load_dotenv()
engines = load_llms()


async def main():
    app = FastAPI(title="Horsona OAI")
    app.include_router(oai.api_router)
    for engine in engines.values():
        oai.add_llm_engine(engine)

    config = uvicorn.Config(app, host="0.0.0.0", port=8001, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
