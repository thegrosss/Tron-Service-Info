from tronpy import Tron

from app.core.database import SessionLocal
from app.core.config import settings
from app.models.wallet import Wallet
from app.schemas.wallet import Wallet as WalletSchema

# Получает информацию о кошельке из сети tron
def get_wallet_info(address: str) -> dict:
    try:
        client = Tron(network=settings.TRON_NETWORK)

        balance = client.get_account_balance(address)
        bandwidth = client.get_bandwidth(address)
        energy = client.get_energy(address)

        return {
            "bandwidth": bandwidth,
            "energy": energy,
            "trx_balance": balance,
            "address": address
        }
    except:
        return {
            "bandwidth": None,
            "energy": None,
            "trx_balance": None,
            "address": address
        }

# Создает запись в базе о запросе кошелька
def create_wallet_query(wallet_data: dict) -> WalletSchema:
    with SessionLocal() as session:
        wallet = Wallet(**wallet_data)
        session.add(wallet)
        session.commit()
        session.refresh(wallet)
        return WalletSchema.model_validate(wallet, from_attributes=True)

# Возвращает пагинированный список запросов кошельков
def get_wallet_entries(page: int, per_page: int):
    with SessionLocal() as session:
        offset = (page - 1) * per_page
        entries = session.query(Wallet) \
            .order_by(Wallet.id) \
            .offset(offset).limit(per_page).all()
        count = session.query(Wallet).count()

        items = [WalletSchema.model_validate(entry, from_attributes=True) for entry in entries]

        return {
            "count": count,
            "page": page,
            "per_page": per_page,
            "items": items
        }
