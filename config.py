#(©)CodeXBotz
#By @Codeflix_Bots



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26930219"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f61fa0adcd48b6bec464b6866fbd2822")

BAN = int(os.environ.get("BAN", "1198543450")) #Owner user id
OWNER = os.environ.get("OWNER", "hey_ronnie") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "6376864232")) #Owner user id
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "ULTROIDOFFICIAL_CHAT") # WITHOUR @
CHANNEL = os.environ.get("CHANNEL", "ULTROID_OFFICIAL") # WITHOUR @


#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002154334233"))

#OWNER ID
#OWNER_ID = int(os.environ.get("OWNER_ID", "6376864232"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sewifix882:bC2XGzdeCNlJtMED@cluster0.ak9ns.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "aquib")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1001785013016"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", ""))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#token varibles
# my shortner https://dashboard.shareus.io/signup/lifetime/U9AZbV

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "api.shareus.io")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "PUIAQBIFrydvLhIzAOeGV8yZppu2")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID","gojfsi/2")

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n ɪ ᴀᴍ ᴍᴜʟᴛɪ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ , ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ » </b>")
try:
    ADMINS=[6695586027]
    for x in (os.environ.get("ADMINS", "6695586027").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first} 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝘁𝗼 𝗷𝗼𝗶𝗻 𝗺𝘆 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗳𝗶𝗿𝘀𝘁 𝘁𝗼 𝗮𝗰𝗰𝗲𝘀𝘀 𝗳𝗶𝗹𝗲𝘀..\n\n 𝗦𝗼 𝗽𝗹𝗲𝗮𝘀𝗲 𝗷𝗼𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗳𝗶𝗿𝘀𝘁 𝗮𝗻𝗱 𝗰𝗹𝗶𝗰𝗸 𝗼𝗻 “𝗡𝗼𝘄 𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲” 𝗯𝘂𝘁𝘁𝗼𝗻....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @ultroidxTeam</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ !"

ADMINS.append(OWNER_ID)
ADMINS.append(6376864232)

LOG_FILE_NAME = "ultroidxTeam.txt"

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
