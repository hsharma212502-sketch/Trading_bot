import logging
import os

LOG_FILE = "trading_bot.log"

def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename=os.path.join("logs", LOG_FILE),
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )