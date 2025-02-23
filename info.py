import re
from os import environ
from Script import script

id_pattern = re.compile(r'^-?\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '7515868'))
API_HASH = environ.get('API_HASH', 'dbd251e9ad4883b0443cc82b618ac6fa')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Admins & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6081617163').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else ADMINS

# Log and file channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002068597390'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001660912346').split()]

# Force subscription channels (Fixed)
auth_channel = environ.get('AUTH_CHANNEL', '-1002022125199 -1001713521586 -1001798300759')
AUTH_CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in auth_channel.split()]

REQUEST_TO_JOIN_MODE = str(environ.get('REQUEST_TO_JOIN_MODE', "False")).lower() == "true"
TRY_AGAIN_BTN = str(environ.get('TRY_AGAIN_BTN', "False")).lower() == "true"

# Request and support settings (Fixed)
REQST_CHANNEL = int(environ.get('REQST_CHANNEL_ID', '-1002456481410'))
SUPPORT_CHAT_ID = environ.get('SUPPORT_CHAT_ID', 'https://t.me/Arya_Bro_Bot')  # No int()
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

# MongoDB (Fixed Security Issue)
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://suresv262:predvd@cluster0.w5qug.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Arya")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Arya')
MULTIPLE_DATABASE = str(environ.get('MULTIPLE_DATABASE', "False")).lower() == "true"

O_DB_URI = environ.get('O_DB_URI', "")
F_DB_URI = environ.get('F_DB_URI', "")
S_DB_URI = environ.get('S_DB_URI', "")

# Premium & Referral
PREMIUM_AND_REFERAL_MODE = str(environ.get('PREMIUM_AND_REFERAL_MODE', "False")).lower() == "true"
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')

# Feature Toggles (Fixed Boolean Conversion)
AI_SPELL_CHECK = str(environ.get('AI_SPELL_CHECK', "True")).lower() == "true"
PM_SEARCH = str(environ.get('PM_SEARCH', "True")).lower() == "true"
BUTTON_MODE = str(environ.get('BUTTON_MODE', "True")).lower() == "true"
MAX_BTN = int(environ.get('MAX_BTN', "10"))  # Convert properly
AUTO_FFILTER = str(environ.get('AUTO_FFILTER', "True")).lower() == "true"
AUTO_DELETE = str(environ.get('AUTO_DELETE', "True")).lower() == "true"
PROTECT_CONTENT = str(environ.get('PROTECT_CONTENT', "False")).lower() == "true"
PUBLIC_FILE_STORE = str(environ.get('PUBLIC_FILE_STORE', "True")).lower() == "true"

# IMDB settings
IMDB = environ.get("IMDB", "https://www.imdb.com")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")

# Fix missing variable
MELCOW_NEW_USERS = str(environ.get("MELCOW_NEW_USERS", "False")).lower() == "true"

# Storage settings
if MULTIPLE_DATABASE:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = O_DB_URI
    FILE_DB_URI = F_DB_URI
    SEC_FILE_DB_URI = S_DB_URI
else:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
