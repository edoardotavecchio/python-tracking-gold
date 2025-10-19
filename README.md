# python-tracking-gold

📈 Monitoraggio in tempo reale del valore di ETF che tracciano oro responsabile

Una piccola API in FastAPI per esporre endpoint che permettono di tracciare i prezzi di mercato di ETF legati a fonti di oro etico (es. HANEtf o altri ETF US-listed). Il progetto è ancora in fase embrionale: la struttura minima è in `src/main.py` e le note iniziali si trovano in `docs/reference.md`.

## Caratteristiche
- API REST basata su FastAPI
- Modelli Pydantic per le richieste/risposte
- Integrazione prevista con AlphaVantage per dati intraday (vedi `docs/reference.md`)
- Documentazione interattiva generata automaticamente

## Documentazione interattiva
- Swagger UI: `GET /docs`
- ReDoc: `GET /redoc`

Avvia l'app (esempio):

```bash
# con uvicorn installato nel virtualenv
uvicorn main:app --reload
```

Poi apri nel browser:
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Note di sviluppo
- Il file `src/main.py` contiene un endpoint di esempio `/track` con il modello `ETF` (pydantic). L'endpoint è da correggere per tornare dati reali.
- Aggiungere variabili d'ambiente per chiavi API (es. `ALPHAVANTAGE_API_KEY`) e caricarle tramite `python-dotenv` o `pydantic.BaseSettings`.

## Contribuire
Aggiungi piccoli moduli in `src/` (models, routers, services) e test in `tests/`.

---
Se vuoi, posso: generare un `pyproject.toml` o `requirements.txt`, correggere l'endpoint di esempio, o aggiungere un modulo di integrazione con AlphaVantage.
