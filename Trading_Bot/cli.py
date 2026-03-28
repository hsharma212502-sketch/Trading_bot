import argparse
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger


def print_order_summary(args):
    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol      : {args.symbol}")
    print(f"Side        : {args.side}")
    print(f"Type        : {args.type}")
    print(f"Quantity    : {args.quantity}")
    if args.type == "LIMIT":
        print(f"Price       : {args.price}")
    print("==================================\n")


def print_order_response(order):
    print("\n========== ORDER RESPONSE ==========")
    print(f"Order ID     : {order.get('orderId')}")
    print(f"Status       : {order.get('status')}")
    print(f"Executed Qty : {order.get('executedQty')}")
    print(f"Avg Price    : {order.get('avgPrice', 'N/A')}")
    print("===================================\n")


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        print_order_summary(args)

        order = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print_order_response(order)
        print("✅ Order placed successfully")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()