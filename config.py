import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN', '8910641792:AAGZ0_4Vt5ow0hUaRvMCYMDwJX5xV6_6BPU')
BOT_OWNER = '@zvxay'
BOT_CHANNEL = '@zvxay_bot'
FORCE_JOIN_CHANNEL = '@zvxay_bot'

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot_database.db')

# Admin IDs (comma-separated)
ADMIN_IDS = list(map(int, os.getenv('ADMIN_IDS', '2089099950').split(',')))

# Prices
ACCOUNT_PRICE = 100  # Default price per account

# Messages
START_MESSAGE = f"""
👋 Welcome to Telegram Accounts Seller Bot

Owner: {BOT_OWNER}
Channel: {BOT_CHANNEL}

Select an option below:
"""

FORCE_JOIN_MESSAGE = f"""
⚠️ Please join our channel to use this bot!

Channel: {BOT_CHANNEL}
"""
