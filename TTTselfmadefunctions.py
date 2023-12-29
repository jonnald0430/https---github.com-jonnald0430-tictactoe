# tic-tac-toe: functions tutorial

# tip: break down a project into small pieces to work on

'''
project questions: 
    how do we visualize the game itself?
    how do we know if we scored? 
    what will be our values?
'''

'''
if you have repetition in your code that have
slight differences, use functions

'''

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

# prints out the gameboard
def game_board():
    print('   A  B  C')
    for count, row in enumerate(game):
        print(count, row)

game_board()
