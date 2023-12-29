# tic-tac-toe: calculating vertical winner

# tip: break down a project into small pieces to work on

'''
project questions: 
    how do we visualize the game itself?
    how do we know if we scored? 
    what will be our values?
'''


game = [ [2, 1, 1],
         [0, 2, 0],
         [2, 2, 1], ]


# vertical winner
for col in range(len(game)):
    check = []
    # note: appends the value of each index into the list
    # other note: it goes through the 0th index of each list
    #             then the 1st, then the 2nd and until a certain value
    #             until a certain value appears as much as the length of 
    #             the list  
    for row in game:
        check.append(row[col])

    # note: check.count(check[0]) checks if all elements in the list are equal to the first element
    if check.count(check[0]) == len(check) and check[0] != 0:
        print('winner')
    print(check)

      
'''
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print('winner')


win(game)
'''

