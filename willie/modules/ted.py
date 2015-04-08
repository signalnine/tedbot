from willie import module
import random

responses = ['k', 'rekt', 'owned', 'lol', 'pls', 'no u', 'pls no', 'wat', 'fak', 'pics', 'rip', 'pls stop', 'y', 'k', 'dicks', 'k']

rare_responses = ['what ru jerking off to?', 'fucking rekt', 'weed++', 'sex++', 'your.mom++', 'dongs++', 'pussy++', 'bots++', 'humans--', 'm\'lady']

rare_replies = ['suck a dick, ', '--', '++', '/me tips his fedora at ']

@module.rule('[a-z]+')
def chat(bot, trigger):
    i = random.randint(1, 100)
    if i < 8 :
        bot.say(random.choice(responses))
    if (i > 96) and (i < 99) 
        bot.say(random.choice(rare_responses))
    if i == 100
        bot.say(random.choice(rare_replies) + trigger.nick)

@module.rule('ted|wexler|abotinacan|amaninacan')
def nickchat(bot, trigger):
    bot.say(trigger.nick + ': ' + random.choice(responses))
