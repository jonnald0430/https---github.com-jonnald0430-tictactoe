# tic-tac-toe: mutability tutorial

# tip: break down a project into small pieces to work on

'''
project questions: 
    how do we visualize the game itself?
    how do we know if we scored? 
    what will be our values?
'''

'''
notes:

if you want to modify a value outside of a function,
we can set a value in that list of lists (in this situation)

cant modify a variable that has immutable values, but can
modify a list outside a function as seen below

heres an example:

game = 'I want to play a game'
print(id(game))

def game_board(player=0,row=0,column=0,just_display=False):
    global game # can global to access variables outside func
    game = 'A game'
    print(id(game))
    print(game)

game_board()
print(game)
print(id(game))
'''

game = [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    print('   A  B  C')
    if not just_display:
        game_map[row][column] = player 
    for count, row in enumerate(game_map):
        print(count, row)

    return game_map


game = game_board(game_map=game, player=1,row=2,column=0)
# or
game = game_board(game_map=game, just_display=True)
