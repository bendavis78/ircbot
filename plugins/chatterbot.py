from util import hook
from chatterbotapi import ChatterBotFactory, ChatterBotType
from random import randint

factory = ChatterBotFactory()

bot = factory.create(ChatterBotType.CLEVERBOT)
bot_session = bot.create_session()

@hook.regex(r'^(.+)$')
def chat(match, nick='', say=None):
    line = match.group(1)
    if 'farbot' in line or 'Farbot' in line:# or randint(1,20) == 1:
        response = bot_session.think(line)
        say(response)
