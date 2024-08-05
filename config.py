import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25405632"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "310460a5a086393880bb37883b411fe7")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://felixyumnam7:fdfQDsuHhmVOtWJp@cluster0.cdtopqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
