# tic-tac-toe: indexes and slices tutorial

# tip: break down a project into small pieces to work on

'''
project questions: 
    how do we visualize the game itself?
    how do we know if we scored? 
    what will be our values?
'''

''' 
indexes and slices example

(practice on terminal)

list = [1,2,3,4,5]

# gets the first item from the list
list[0]

# gets the last item from the list 
list[-1]

# gets the index of an item and all the other items in the list after
list[0:]

# gets the index of an item and for example the second item of the list
list[0:2]

# could also do this if you want to get values up to a certain item in a list (4th item in this case)
list[:4]

'''


game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

# example of how to set nested lists to a value
game[0][1] = 1


print('   A  B  C')
for count, row in enumerate(game):
   print(count, row)


