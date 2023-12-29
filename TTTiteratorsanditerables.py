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

    iterable: a thing we can iterate over
        - is an object (everything in Python is an object)
    iterator: a special object with next() method
        - can have a stop iteration

        import itertools

        x = [1,2,3,4] # iterable 

        n = itertools.cycle(x) # iterator ...also iterable

        y = iter(x) #iterator ...also iterable

        print(next(n))


        - if used next() function on iterable and did for loop
          it runs through the other items after the item it iterated over

        - you can iterate over the iterators with an iterable, but it doesn't  
          necessarily make  it an iterator, but some iterators can be iterable

           iterable: can we iterate over it?
           iterate: use for loop




    a backslash ( \ ) in python escapes a value of a different character  

    example:
        string = 'don't' <--- this is a violation
    
    you can do:
        string = 'don\'t'


    iteration example:

        players = [1,0]

        choice = 1
        for i in range(10):
            current_player = choice + 1
            print(current_player)
            choice = players[choice]
    
    this is a pure python approach to switching between player 1 and player 2

    
    itertools example:

    import itertools 

    player_choice = itertools.cycle([1,2])

    for i in range(10):
        print(next(player_choice))

    more condensed method
    - use next() to grab the next value from it






'''

import itertools

game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0], ]


def win(current_game):
    # horizontal win
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f'Player {row[0]} is the winner horizontally!')

    # diagonal win
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(row[0]) == len(diags) and diags[0] != 0:
        print(f'Player {diags[0]} is the winner diagonally! (\\)')

    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f'Player {diags[0]} is the winner diagonally! (/)')

    # vertical win
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f'Player {check[0]} is the winner vertically! (|)')


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    # try and except handled error instead of terminal error
    try:
        print('   0  1  2')
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


play = True
players = [1,2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],]
    # while loop will continue to run until the game has been won
    game_won = False
    game = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f'Current Player: {current_player}')
        column_choice = int(input('What column do you want to play? (0, 1, 2) '))
        row_choice = int(input('What row do you want to play? (0, 1, 2) '))
        game = game_board(game, current_player, row_choice, column_choice)
        


#game = game_board(game_map=game, player=1,row=3,column=0)
#game = game_board(game_map=game, just_display=True)

