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
    BOT_TOKEN = "1658914050:AAFFKFlpvH3Dzk-_Z9WJFQh07fUOBDoanVE"
    DATABASE_URL = "postgres://raufxawjiixdoz:9100f7c038db9c736414e8803ef3f364d73400b90293af9c79f0379589a71082@ec2-54-90-13-87.compute-1.amazonaws.com:5432/da9akve5chtpdn"
    APP_ID = "2380939"
    API_HASH = "b608996adf636d07b4801da802386144"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(411872315)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Sep**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Comm**\n__/Forcee - To get the current settings.\n/Foribe no/off/disable - To turn of ForceSubscribe.\n/Forib - To turn on and setup the channel.\n/Forbe  - To unmute all members who muted by me.\n\nNote: /cribe__",
        
        "**@bankirkundaligi Adminidan**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
