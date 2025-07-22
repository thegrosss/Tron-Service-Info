from pydantic import BaseModel, ConfigDict

# Информация о кошельке
class WalletInfo(BaseModel):
    address: str | None
    bandwidth: float | None
    energy: float | None
    trx_balance: float | None

# Схема для валидации адреса при запросах
class WalletAddress(BaseModel):
    address: str

# Схема модели из базы данных
class Wallet(WalletInfo):
    id: int

    model_config = ConfigDict(from_attributes=True)

# Пагинированный список для получения данных из бд
class PaginatedWallet(BaseModel):
    count: int
    page: int
    per_page: int
    items: list[Wallet]

    model_config = ConfigDict(from_attributes=True)