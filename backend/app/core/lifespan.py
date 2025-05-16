from contextlib import asynccontextmanager
from fastapi import FastAPI
from app import domain
from app.database import setup as db_setup

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_setup.run()
    yield