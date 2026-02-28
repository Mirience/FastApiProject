import asyncio
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes import posts

app = FastAPI(root_path="/api/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router, prefix="/posts", tags=["posts"])

async def run() -> None:
    config = uvicorn.Config("main:app", host="localhost", port=8000, reload=False)
    server = uvicorn.Server(config=config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(run())