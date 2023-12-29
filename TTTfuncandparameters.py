# tic-tac-toe: parameters tutorial

# tip: break down a project into small pieces to work on

'''
project questions: 
    how do we visualize the game itself?
    how do we know if we scored? 
    what will be our values?
'''


'''
example function w/ parameters

def addition(x,y):
    return x + y

print(addition(5,3))

output is 8


can also do strings!

print(addition('hey','there'))

output is hey there


you cant add integers and strings as they aren't the same value type

like addition(5, 'hey')
'''

# should add this into a function, as modifying this outside of function is inefficient
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

# have to use parameters in functions or else error
def game_board(player=0, row=0, column=0, just_display=False):
    print('   A  B  C')
    if not just_display:
        game[row][column] = player #sets the row and column to player input
    for count, row in enumerate(game):
        print(count, row)

# instead of hard typing values, could do this
game_board(player=1,row=2,column=0)
#or
game_board(just_display=True)
