import dice
import mapping_snakes_ladders

#note: board is here --> https://www.google.com/search?q=snake+and+ladder+board&newwindow=1&safe=active&sxsrf=ALeKk01lLnNfsFTgslJQTohvZDb87bYT0w:1608751209335&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjkvvSi6eTtAhVOQBoKHaJjACEQ_AUoAXoECBIQAw&biw=861&bih=679#imgrc=OfZcRBPYJpVR_M

def get_user_input():
    """
    this function can be used if you'd like to get user input instead of fixed number input
    """
    # get number of players as input
    num_players = input("type a number between 2 and 5")
    # check if valid number
    while not check_validity_input_number(num_players):
        num_players = input("you REALLY need a number between 2 and 5")
    num_players = int(num_players)
    # get player names
    players = [input("Enter name of player: ") for _ in range(num_players)]

    return num_players, players

def order_players(num_players, players):
    # everyone throws a dice: first highest starts
    init_dice = [dice.roll_one_die() for _ in range(num_players)]
    index_player_starting = init_dice.index(max(init_dice))
    # re-arrange array of names as player orders
    players_reorg = players[:index_player_starting] + players[index_player_starting:]

    return players_reorg

def check_validity_input_number(num):
    """
    param: an input 
    return: a boolean (True if int between 1 and 5 inclusive, False otherwise)
    """
    try: 
        num = int(num)
        if (num >= 1 and num <= 5):
                return True 
        else:
            return False
    except:
        return False

def prepare_data_for_dictionary(counter, tuple_positions, path_simplified):
    row = {}
    row['roll_dice'] = counter
    row['path_complete'] = tuple_positions
    row['path_simplified'] = path_simplified
    row['snake_16_6'] = tuple_positions.count(16)
    row['snake_49_11'] = tuple_positions.count(49)
    row['snake_56_53'] = tuple_positions.count(56)
    row['snake_62_19'] = tuple_positions.count(62)
    row['snake_64_60'] = tuple_positions.count(64)
    row['snake_87_24'] = tuple_positions.count(87)
    row['snake_93_73'] = tuple_positions.count(93)
    row['snake_95_75'] = tuple_positions.count(95)
    row['snake_98_78'] = tuple_positions.count(98)
    row['ladder_1_38'] = tuple_positions.count(1)
    row['ladder_4_14'] = tuple_positions.count(4)
    row['ladder_9_31'] = tuple_positions.count(9)
    row['ladder_21_42'] = tuple_positions.count(21)
    row['ladder_28_84'] = tuple_positions.count(28)
    row['ladder_36_44'] = tuple_positions.count(36)
    row['ladder_56_67'] = tuple_positions.count(56)
    row['ladder_71_91'] = tuple_positions.count(71)
    row['ladder_80_100'] = tuple_positions.count(80)

    return row

def play_one_round(player_num, position, tuple_positions, path_simplified, counter):
    """
    param: a player number (not needed though; simplify to do), an int, a list of int
    return: an int and a list of int
    """
    # roll die
    die = dice.roll_one_die()
    counter = counter + 1
    if position + die > 100:
        position = position
        tuple_positions = tuple_positions + (position,)
        path_simplified = path_simplified + (position,)
        return position, tuple_positions, path_simplified, counter
    else:
        position = position + die
        tuple_positions = tuple_positions + (position,)
        if position in snakes_or_ladders.keys():
            position = snakes_or_ladders[position]
            tuple_positions = tuple_positions + (position,)
        path_simplified = path_simplified + (position,)
        return position, tuple_positions, path_simplified, counter

def play_one_game():
    """
    By default, this simulation is run for one player named player 1.
    To play it with multiple players and pick their names, uncomment the line that uses the get_user_input function, and comment out the one following it.
    """
    # initialize counter for number of dice rolls
    counter = 0
    # snakes or ladders mapping as global var
    global snakes_or_ladders
    snakes_or_ladders = mapping_snakes_ladders.snakes_or_ladders

    # uncomment the following line if you want user input instead of fixed numbers
    #num_players, players = get_user_input()
    # and comment out the following one:
    num_players, players = 1, ['player 1']
    # reordering isn't helpful here but it is if several players and dice pick the one who plays first
    players_reorg = order_players(num_players, players)

    # int player positions and num of moves // refine last one
    positions = [0 for each in range(num_players)]
    list_positions = [() for each in range(num_players)]
    path_simplified = [() for each in range(num_players)]

    # if no one has reached 100, keep playing
    while 100 not in positions:
        for player_num in range(num_players):
            positions[player_num], list_positions[player_num], path_simplified[player_num], counter = play_one_round(player_num, positions[player_num], list_positions[player_num],  path_simplified[player_num], counter)
            
    # otherwise get who has won -- if several, the winner is the first one reaching
    index_winner = positions.index(100)
    
    # if doing an analysis, then this gets the data in table format.
    # if using it to play only, then you won't need it and can comment it out
    row = prepare_data_for_dictionary(counter, list_positions[index_winner], path_simplified[index_winner])

    # if using it to play, comment following line out to get who has won and in how many dice rolls:
    #print('Congratulations to the winner:', players_reorg[index_winner], '! You won in', counter, 'and the path followed was:', path_simplified[index_winner])


    return row

# uncomment the following line to run this code as an interactive game:
#play_one_game()