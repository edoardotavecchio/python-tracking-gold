from fastapi import FastAPI
from app.api.v1.router import router as v1_router

# Creazione app FastAPI
app = FastAPI()

# Inclusione dei router
app.include_router(v1_router)