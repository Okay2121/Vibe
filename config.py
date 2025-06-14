"""
Configuration file for the Solana Memecoin Trading Bot
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Ensure bot token is available - try multiple loading methods
if not BOT_TOKEN:
    # Try to load from .env file again with explicit path
    load_dotenv('.env', override=True)
    BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    
    if not BOT_TOKEN:
        # Log error if token is not found
        import logging
        logging.error("TELEGRAM_BOT_TOKEN not found in environment variables or .env file")
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")
ADMIN_USER_ID = os.environ.get('ADMIN_USER_ID', '5488280696')  # Admin Telegram ID
ADMIN_IDS = [os.environ.get('ADMIN_USER_ID', '5488280696')]  # List of authorized admin IDs

# Database Configuration - Use local PostgreSQL database
DATABASE_URL = os.environ.get('DATABASE_URL')

# Solana Configuration
MIN_DEPOSIT = 0.5  # Minimum deposit amount in SOL
MAX_DEPOSIT = 5000  # Maximum deposit amount in SOL
SOLANA_NETWORK = "mainnet-beta"  # mainnet-beta, testnet, or devnet
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"  # Default public RPC endpoint
GLOBAL_DEPOSIT_WALLET = "2pWHfMgpLtcnJpeFRzuRqXxAxBs2qjhU46xkdb5dCSzD"  # Default global deposit address

# Global Settings
DEFAULT_WALLET = "2pWHfMgpLtcnJpeFRzuRqXxAxBs2qjhU46xkdb5dCSzD"  # Default deposit wallet address
SUPPORT_USERNAME = "thrivebotadmin"  # Default support username

# API endpoints
TELEGRAM_API_URL = "https://api.telegram.org/bot{}"  # Will be formatted with token

# ROI Configuration
SIMULATED_DAILY_ROI_MIN = 0.5  # Minimum daily ROI percentage
SIMULATED_DAILY_ROI_MAX = 2.2  # Maximum daily ROI percentage
SIMULATED_LOSS_PROBABILITY = 0.15  # Probability of a daily loss (15%)

# Notification settings
DAILY_UPDATE_HOUR = 9  # Hour of the day (0-23) to send daily updates

# User Engagement Settings
PROFIT_MILESTONES = [10, 25, 50, 75, 100]  # Profit percentage milestones to trigger notifications
STREAK_MILESTONES = [3, 5, 7, 10, 14]  # Consecutive profitable days milestones
INACTIVITY_THRESHOLD = 3  # Days of inactivity before sending a reminder