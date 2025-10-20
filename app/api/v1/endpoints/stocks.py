from fastapi import APIRouter
from app.repository import alpha_vantage

router = APIRouter()

@router.get('/search')
def search(q: str):
    return alpha_vantage.search(q)

@router.get('/intraday')
def track(symbol: str):
    return alpha_vantage.intraday(symbol)

@router.get('/quote')
def quote(symbol: str):
    return alpha_vantage.quote(symbol)