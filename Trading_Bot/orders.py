import logging
from typing import Optional, Dict, Any
from bot.client import get_client

client = get_client()

def place_order(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: Optional[float] = None
) -> Dict[str, Any]:

    try:
        logging.info(
            f"REQUEST | symbol={symbol} side={side} type={order_type} qty={quantity} price={price}"
        )

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        else:
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"RESPONSE | {response}")

        return response

    except Exception as e:
        logging.error(f"ERROR | {str(e)}")
        raise RuntimeError(f"Failed to place order: {str(e)}")