from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from connection.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.get('/')
def dashboard():
    return {
        "message": "Dashboard API"
    }
