from util import hook
from chatterbotapi import ChatterBotFactory, ChatterBotType

factory = ChatterBotFactory()

bot = factory.create(ChatterBotType.CLEVERBOT)
bot_session = bot.create_session()

@hook.regex(r'^(.+)$')
def chat(match, nick='', say=None):
    line = match.group(1)
    names = [
        'johnnyfive',
        'j5',
        'johnny',
        'johnny5',
    ]
    in_line = lambda l: any((s in line.lower()) for s in l)

    if in_line(names):
        line = line.lower()
        for n in names:
            line.replace(n, '')
        response = bot_session.think(line.strip())
        say(response)
