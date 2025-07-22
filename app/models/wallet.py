from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Wallet(Base):
    __tablename__ = "wallet"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    address: Mapped[str] = mapped_column(nullable=True)
    bandwidth: Mapped[float] = mapped_column(nullable=True)
    energy: Mapped[float] = mapped_column(nullable=True)
    trx_balance: Mapped[float] = mapped_column(nullable=True)