# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23303247"))
API_HASH = getenv("API_HASH", "23623f737dc15708708c65a7297e1510")
BOT_TOKEN = getenv("BOT_TOKEN", "7351726996:AAGdewDxj1RBReSTcqPjOtUWZGrNNl4bTbw")
OWNER_ID = int(getenv("OWNER_ID", "6931140424"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://Sarkar123:GAUTAMMISHRA@sarkar.1uiwqkd.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002166457568"))
FORCESUB = getenv("FORCESUB", "DeveloperRadha")
