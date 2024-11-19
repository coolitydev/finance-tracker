import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI

from api import router

from core import settings, db_helper, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
