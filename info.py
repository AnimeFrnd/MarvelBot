import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.-?\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '7515868'))
API_HASH = environ.get('API_HASH', 'dbd251e9ad4883b0443cc82b618ac6fa')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Admins & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6081617163').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Log and file channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002068597390'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001660912346').split()]

# Force subscription channels
REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False))
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False))
AUTH_CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '-1002009379876 -1001713521586 -1001798300759').split() if ch]

# Request and support settings
REQST_CHANNEL = int(environ.get('REQST_CHANNEL_ID', '-1002456481410'))
SUPPORT_CHAT_ID = int(environ.get('SUPPORT_CHAT_ID', '0'))
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

# Database settings
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Arya")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Arya')
MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', False))
O_DB_URI = environ.get('O_DB_URI', "")
F_DB_URI = environ.get('F_DB_URI', "")
S_DB_URI = environ.get('S_DB_URI', "")

# Referral settings
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', False))
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', '')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '')

# Feature toggles
AI_SPELL_CHECK = bool(environ.get('AI_SPELL_CHECK', True))
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', False))
PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', True))

# Cache and response settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
MSG_ALRT = environ.get('MSG_ALRT', 'Hi 🎀 Pookie ❤️')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)

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
