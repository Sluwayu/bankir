import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1612700614:AAFjGzZS3lhxxq9TJn4lDOneFCyulm5Msug"
    DATABASE_URL = "postgres://ysugfwmhvoayhj:9a4f7b8bb6fc9648679ef9d726eb80c0162d6abf393a65ded67646cbda671432@ec2-35-171-57-132.compute-1.amazonaws.com:5432/dc7pjust0gauhv"
    APP_ID = "738109"
    API_HASH = "c9a08d37e37d81f87e64c3db2183c3ec"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(411872315)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Sep**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Comm**\n__/Forcee - To get the current settings.\n/Foribe no/off/disable - To turn of ForceSubscribe.\n/Forib - To turn on and setup the channel.\n/Forbe  - To unmute all members who muted by me.\n\nNote: /cribe__",
        
        "**@omadlottouz Adminidan**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
