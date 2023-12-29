# tic-tac-toe: calculating horizonal winner

# tip: break down a project into small pieces to work on

'''
project questions: 
    how do we visualize the game itself?
    how do we know if we scored? 
    what will be our values?
'''


game = [ [1, 1, 1],
         [0, 2, 0],
         [2, 2, 0], ]

def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print('winner')


win(game)

