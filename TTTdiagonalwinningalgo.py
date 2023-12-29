# tic-tac-toe: diagonal winning algorithm

# tip: break down a project into small pieces to work on

'''
project questions: 
    how do we visualize the game itself?
    how do we know if we scored? 
    what will be our values?
'''

'''
notes:

use zip() function to bring together different lists
'''

game = [ [2, 1, 1],
         [0, 2, 0],
         [2, 2, 2], ]


# diagonal win
diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])

# reverse diagonal win
diags = []
# note: index is the enumerate, row is the reversed range len
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

print(diags)

'''
for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print('winner')
    print(check)
'''
      
'''
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print('winner')


win(game)
'''

