# (c) @AM_ROBOTS

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 15898846))
    API_HASH = os.environ.get("API_HASH", "8ddd6065c9101ac2678ef29437ec8dd7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6443763987:AAFqZrFnJHux_0pHRddE5xtmZEIY89RmOK0")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQDymN4AZz3xlzV1vxpxbfVERC4J9Ph2Fqtp3rGJH7ftQ-glPVni8GXycKiQoD5zrNtlcCnyUgyIGP5y02nAFCWJoNYTTgQ_9OWNER6GdrsvbH-dbatgxvP9fGVmmL5RK4VCT9FTj_vmfJpPYYt762uS9WhulpzQ9q-FVJGdzvFEnDwgmDTQi8aBDtMUwa_QnltwUvgj6d1Mxf7-3jgp3TNvcpn4aMvmcWWGot36ApMjGW0_DeiAOmuzC3rMLJr5sKQaKGbbKXc_hS6bg6i6vmY9xhBql1q1AlIwxGsyN8dydCXLLnxiXQNsGN1uIltlC2Dihb-kcSvyDxiVxV5NW0diTFEzcwAAAAE96hcYAA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001929711696))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MOVIES_VILLA_SEARCH_BOT")
    BOT_OWNER = int(os.environ.get("BOT_OWNER" 6651109872))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Searchbot:Mongodb.bot@cluster0.5xixyjh.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001956982290)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://t.me/MOVIES_VILLA_SEARCH_BOT'>Lin Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/tgnvs'>TGNVS</a></b>
"""

    ABOUT_HELP_TEXT = """<b>Donation</b>
<b>Thanks for showing interest in donation
Donate Us To Keep Alive
Continously Alive

You Can Send Any Amount
Donate Only One Rupee
Of 10₹,20₹,30₹,50₹,100₹ 😁

💸Payment Methods:
Only UPI
UPI:-</b> tgnvs@airtel
-<b> <a href=https://upier.vercel.app/pay/tgnvs@airtel?am=15>Donation Link</a></b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @tgnvs</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @tgnvs</a></b>
"""

