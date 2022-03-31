import random
'''

letters = "abcdefghijklmnopqrstuvwxyz"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

# Make an 8 letter password by combining characters from the three strings

#outcome = random.choice(letters)

alphanum = letters + caps + numbers
#outcome = random.choice(alphanum)
output = ""

for i in range(8):
    output = output + random.choice(alphanum)
    
print(output)
'''


'''
nouns = ['tissue', 'processor', 'headquarters', 'favorite', 'cure', 'ideology', 'funeral', 'engine', 'isolation', 'perception', 'hat', 'mountain', 'session', 'case', 'legislature', 'consent', 'spread', 'shot', 'direction', 'data', 'tragedy', 'illness', 'serving', 'mess', 'resistance', 'basis', 'kitchen', 'mine', 'temple', 'mass', 'dot', 'final', 'chair', 'picture', 'wish', 'transfer', 'profession', 'suggestion', 'purse', 'rabbit', 'disaster', 'evil', 'shorts', 'tip', 'patrol', 'fragment', 'assignment', 'view', 'bottle', 'acquisition', 'origin', 'lesson', 'Bible', 'act', 'constitution', 'standard', 'status', 'burden', 'language', 'voice', 'border', 'statement', 'personnel', 'shape', 'computer', 'quality', 'colony', 'traveler', 'merit', 'puzzle', 'poll', 'wind', 'shelter', 'limit', 'talent']
verbs = ['represent', 'warm', 'whisper', 'consider', 'rub', 'march', 'claim', 'fill', 'present', 'complain', 'offer', 'provoke', 'yield', 'shock', 'purchase', 'seek', 'operate', 'persist', 'inspire', 'conclude', 'transform', 'add', 'boast', 'gather', 'manage', 'escape', 'handle', 'transfer', 'tune', 'born', 'decrease', 'impose', 'adopt', 'suppose', 'sell', 'disappear', 'join', 'rock', 'appreciate', 'express', 'finish', 'modify', 'keep', 'invest', 'weaken', 'speed', 'discuss', 'facilitate', 'question', 'date', 'coordinate', 'repeat', 'relate', 'advise', 'arrest', 'appeal', 'clean', 'disagree', 'guard', 'gaze', 'spend', 'owe', 'wait', 'unfold', 'back', 'waste', 'delay', 'store', 'balance', 'compete', 'bake', 'employ', 'dip', 'frown', 'insert']
adjs = ['busy', 'closer', 'national', 'pale', 'encouraging', 'historical', 'extreme', 'cruel', 'expensive', 'comfortable', 'steady', 'necessary', 'isolated', 'deep', 'bad', 'free', 'voluntary', 'informal', 'loud', 'key', 'extra', 'wise', 'improved', 'mad', 'willing', 'actual', 'OK', 'gray', 'little', 'religious', 'municipal', 'just', 'psychological', 'essential', 'perfect', 'intense', 'blue', 'following', 'Asian', 'shared', 'rare', 'developmental', 'uncomfortable', 'interesting', 'environmental', 'amazing', 'unhappy', 'horrible', 'philosophical', 'American']

# Make a four word password by combining words from the list of nouns, verbs and adjs


allwords = nouns + verbs + adjs

output = ""
for i in range(4):
    output = output + random.choice(allwords)
    
print(output)
'''
'''
import sys
sys.setExecutionLimit(60000) # 60 seconds
letters = "abcdefghijklmnopqrstuvwxyz"
my_password = "abcd"
guess_num = 0
done = False
while not done:

    guessed_pw = ""
    for i in range(4):
        guessed_pw = guessed_pw + random.choice(letters)
    guess_num = guess_num + 1
    if guessed_pw == my_password:
        print("found it after ", guess_num, " tries")
        done = True
'''

#This goes through it sequentially

import random

letters = "abcdefghijklmnopqrstuvwxyz"
my_password = "abcd"
guess_num = 0
done = False


guessed_pw = ""
for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            for letter4 in letters:
                guessed_pw = letter1 + letter2 + letter3 + letter4
                    
                guess_num = guess_num + 1
                if guessed_pw == my_password:
                    print("found it after ", guess_num, " tries")
                
