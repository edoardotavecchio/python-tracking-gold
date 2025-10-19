from fastapi import FastAPI 
from pydantic import BaseModel
from src.repositories.alpha_vantage import intraday

app = FastAPI()

class ETF(BaseModel):
    isin: str
    name: str

@app.get('/track/{symbol}')
def track(symbol: str):
    return intraday(symbol)