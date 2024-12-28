import argparse
import asyncio

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from horsona.interface import node_graph


async def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Node Graph API")
    parser.add_argument(
        "--session-timeout", type=float, default=9e9, help="Session timeout in seconds"
    )
    parser.add_argument(
        "--session-cleanup-interval",
        type=float,
        default=60,
        help="Session cleanup interval in seconds",
    )
    parser.add_argument(
        "--extra-modules", nargs="+", default=[], help="Extra modules to allow"
    )
    parser.add_argument(
        "--host", type=str, default="127.0.0.1", help="Host to run the server on"
    )
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to run the server on"
    )
    args = parser.parse_args()

    app = FastAPI(title="Horsona Node Graph")
    app.include_router(node_graph.api_router)
    node_graph.configure(
        session_timeout=args.session_timeout,
        session_cleanup_interval=args.session_cleanup_interval,
        extra_modules=args.extra_modules,
    )

    config = uvicorn.Config(app, host=args.host, port=args.port, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
