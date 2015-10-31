from willie import module
import random

responses = ['k', 'rekt', 'owned', 'lol', 'pls', 'no u', 'pls no', 'wat', 'fak', 'pics', 'rip', 'pls stop', 'y', 'k', 'dicks', 'k']

rare_responses = ['node.js++', 'fucking rekt', 'php++', 'golang++', 'uber++', 'travis.kalkanicks.sweaty.nutsack++', 'visual.basic++', 'microsoft.word++', 'rust--', 'm\'lady']

rare_replies = ['hi, ', ':( ']

random_karma = ['--', '++']

@module.rule('[a-z]+')
def chat(bot, trigger):
    i = random.randint(1, 200)
    if i < 7 :
        bot.say(random.choice(responses))
    if (i > 96) and (i < 99) :
        bot.say(random.choice(rare_responses))
    if i == 100 :
        bot.say(random.choice(rare_replies) + trigger.nick)
    if i == 95 :
        bot.say(trigger.nick + random.choice(random_karma))

@module.rule('ted|wexler|abotinacan|amaninacan')
def nickchat(bot, trigger):
    bot.say(trigger.nick + ': ' + random.choice(responses))
