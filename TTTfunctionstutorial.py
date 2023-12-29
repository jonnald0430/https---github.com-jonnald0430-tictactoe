# tic-tac-toe: functions tutorial

# tip: break down a project into small pieces to work on

'''
project questions: 
    how do we visualize the game itself?
    how do we know if we scored? 
    what will be our values?
'''

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

print('   A  B  C')

# built in function enumerate() gives the index value of a list by iterating through it
for count, row in enumerate(game):
   print(count, row)




