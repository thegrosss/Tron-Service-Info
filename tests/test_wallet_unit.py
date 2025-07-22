from app.schemas.wallet import Wallet
from app.services.service import create_wallet_query

def test_create_wallet_query():
    test_data = {
        "address" : "TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf",
        "bandwidth" : 100,
        "energy" : 200,
        "trx_balance" : 22
    }

    wallet = create_wallet_query(test_data)

    assert isinstance(wallet, Wallet)
    assert wallet.address == test_data["address"]
    assert wallet.trx_balance == test_data["trx_balance"]