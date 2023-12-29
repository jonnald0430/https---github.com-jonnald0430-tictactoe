import itertools
import numpy as np

player_choice = itertools.cycle([1,2])

for i in range(10):
    print(player_choice.next())



game_size = 3

# concatenation
s = ' '
for i in range(game_size):
    s += '  '+str(i) 

# list comprehension
s = '   '+'  '.join([str(i) for i in range(game_size)])

# numpy zeroes
print(np.zeros([3,3]))

# dictionaries
dictionaries = {'key1':15, 'key2':32}

print(dictionaries['key1'])

dictionaries['hitthere'] = 92

print(dictionaries)

# making game dynamic testing

game_size = 5

game = []

for i in range(game_size):
    row = []
    for i in range(game_size):
        row.append(0)
    game.append(row)


#print(game)

# in one line
game_size = input('What size game of tic tac toe? ')
game = [[0 for i in range(game_size)] for i in range(game_size)]
print(game)