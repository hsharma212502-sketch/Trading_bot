# Binance Futures Testnet Trading Bot

## Features
- Market and Limit Orders
- BUY and SELL support
- CLI-based input
- Input validation
- Logging of requests/responses/errors
- Clean modular structure

## Setup

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt

3. Create `.env` file from `.env.example`

4. Run examples:

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Logs
Logs are stored in:
logs/trading_bot.log

## Assumptions
- Binance Futures Testnet account is active
- API keys are valid