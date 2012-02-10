from util import hook

@hook.regex(r'<rs>')
def rs(match, say=None):
    say('badum tsshh')
