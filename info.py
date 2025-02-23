import re
from os import environ
from Script import script

# Corrected ID pattern
id_pattern = re.compile(r'^-?\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '7515868'))  # Ensure default is a valid int
API_HASH = environ.get('API_HASH', 'dbd251e9ad4883b0443cc82b618ac6fa')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Admins & Users
ADMINS = [int(admin) if id_pattern.match(admin) else admin for admin in environ.get('ADMINS', '6081617163').split()]
auth_users = [int(user) if id_pattern.match(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else ADMINS  # Ensure non-empty list

# Log and file channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002068597390'))
CHANNELS = [int(ch) if id_pattern.match(ch) else ch for ch in environ.get('CHANNELS', '-1001660912346').split()]

# Force subscription channels
REQUEST_TO_JOIN_MODE = str(environ.get('REQUEST_TO_JOIN_MODE', "False")).lower() == "true"
TRY_AGAIN_BTN = str(environ.get('TRY_AGAIN_BTN', "False")).lower() == "true"
AUTH_CHANNELS = [int(ch) if id_pattern.match(ch) else ch for ch in environ.get('AUTH_CHANNEL', '').split() if ch]

# Request and support settings
REQST_CHANNEL = int(environ.get('REQST_CHANNEL_ID', '-1002456481410'))
SUPPORT_CHAT_ID = int(environ.get('SUPPORT_CHAT_ID', '0'))
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
DELETE_CHANNELS = [int(dch) if id_pattern.match(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

# Database settings
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Arya")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Arya')
MULTIPLE_DATABASE = str(environ.get('MULTIPLE_DATABASE', "False")).lower() == "true"

O_DB_URI = environ.get('O_DB_URI', "")
F_DB_URI = environ.get('F_DB_URI', "")
S_DB_URI = environ.get('S_DB_URI', "")

# Referral settings
PREMIUM_AND_REFERAL_MODE = str(environ.get('PREMIUM_AND_REFERAL_MODE', "False")).lower() == "true"
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', '')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '')

# Feature toggles
AI_SPELL_CHECK = str(environ.get('AI_SPELL_CHECK', "True")).lower() == "true"
PM_SEARCH = str(environ.get('PM_SEARCH', "True")).lower() == "true"
AUTO_FFILTER = str(environ.get('AUTO_FFILTER', "True")).lower() == "true"
AUTO_DELETE = str(environ.get('AUTO_DELETE', "True")).lower() == "true"
PROTECT_CONTENT = str(environ.get('PROTECT_CONTENT', "False")).lower() == "true"
PUBLIC_FILE_STORE = str(environ.get('PUBLIC_FILE_STORE', "True")).lower() == "true"
BUTTON_MODE = str(environ.get("BUTTON_MODE", "single")).lower()
SPELL_CHECK_REPLY = str(environ.get("SPELL_CHECK_REPLY", "True")).lower() == "true"
PROTECT_CONTENT = str(environ.get("PROTECT_CONTENT", "False")).lower() == "true"
AUTO_DELETE = str(environ.get("AUTO_DELETE", "True")).lower() == "true"
MAX_BTN = int(environ.get("MAX_BTN", "10"))
AUTO_FFILTER = str(environ.get("AUTO_FFILTER", "True")).lower() == "true"
SHORTLINK_API = environ.get("SHORTLINK_API", "")
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")
SHORTLINK_MODE = str(environ.get("SHORTLINK_MODE", "False")).lower() == "true"
TUTORIAL = environ.get("TUTORIAL", "")
IS_TUTORIAL = str(environ.get("IS_TUTORIAL", "False")).lower() == "true"

# Cache and response settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
MSG_ALRT = environ.get('MSG_ALRT', 'Hi 🎀 Pookie ❤️')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)

# IMDB settings
IMDB = environ.get("IMDB", "https://www.imdb.com")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")

# Fix for missing variable
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
