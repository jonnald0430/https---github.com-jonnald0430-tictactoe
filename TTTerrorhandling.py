# tic-tac-toe: error handling tutorial

# tip: break down a project into small pieces to work on

'''
project questions: 
    how do we visualize the game itself?
    how do we know if we scored? 
    what will be our values?
'''

'''
notes:

people contributing or playing with my program will try dumb things,
try and prevent that through error handling

can use try and except methods for exception or error handling as shown below
'''

game = [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    # try and except handled error instead of terminal error
    try:
        print('   A  B  C')
        if not just_display:
            game_map[row][column] = player 
        for count, row in enumerate(game_map):
            print(count, row) 
        return game_map
    # can handle a certain error like indexerror
    except IndexError as e:
        print('Error: did you input row/column as 0 1 or 2?', e)
    # can handle all errors and exceptions     
    except Exception as e:
        print('Something went very wrong!', e)



game = game_board(game_map=game, player=1,row=3,column=0)
game = game_board(game_map=game, just_display=True)
