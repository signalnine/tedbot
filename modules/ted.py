from willie import module
import random

responses = ['k', 'rekt', 'owned', 'lol', 'pls', 'no u', 'pls no', 'wat', 'fak', 'pics', 'rip', 'pls stop', 'y', 'dicks']

@module.rule('[a-z]+')
def chat(bot, trigger):
    i = random.randint(1, 100)
    if i < 9 :
        bot.say(random.choice(responses))

@module.rule('ted|wexler|abotinacan|amaninacan')
def nickchat(bot, trigger):
    bot.say(trigger.nick + ': ' + random.choice(responses))
