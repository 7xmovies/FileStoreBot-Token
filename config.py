#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6832302226:AAFas_mCbhRD9M8eZe34JWFkBBnSz6o1e-w")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21489763"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "308f5362db7844a59272c33634e9e792")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1005100345229"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5100345229"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = "mongodb+srv://7xmovieshub:uoc0ajFxBrQ0wksk@movies7x.4axozzk.mongodb.net/?retryWrites=true&w=majority&appName=Movies7x"
DB_NAME = os.environ.get("DATABASE_NAME", "Movies7x")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "04d597189645c3ab00ee4c0bfbceb27b13c25d6a")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","help_7xmovies/3")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001933966820"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI am only a file provider from my owner we dont own any file.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5100345229 6159530722 5985318277 5922250004 6474779115").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We  or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "{first} welcome <b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5100345229 6159530722 5985318277 5922250004 6474779115)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
