from fastapi import APIRouter

# Importa i router specifici da ogni endpoint
from app.api.v1.endpoints import stocks

# Crea il router principale per v1
router = APIRouter(
    prefix="/api/v1",
    tags=["v1"],  # Gruppo nel Swagger
)

# Includi i router dei vari endpoint
router.include_router(
    stocks.router,
    prefix="/stocks",
    tags=["stocks"],
    responses={404: {"description": "Non trovato"}}
)