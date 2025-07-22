from fastapi import FastAPI

from app.core.database import create_tables
from app.schemas.wallet import Wallet, PaginatedWallet
import app.services.service as service

create_tables()

app = FastAPI()

@app.post("/wallet/info", response_model=Wallet)
def get_wallet_info(address: str):
    info = service.get_wallet_info(address=address)
    query = service.create_wallet_query(info)
    return query

@app.get("/wallet/entries", response_model=PaginatedWallet)
def get_entries(page: int, per_page: int):
    entries = service.get_wallet_entries(page, per_page)

    return entries