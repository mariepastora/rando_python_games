import dice
import mapping_snakes_ladders

#note: board is here --> https://www.google.com/search?q=snake+and+ladder+board&newwindow=1&safe=active&sxsrf=ALeKk01lLnNfsFTgslJQTohvZDb87bYT0w:1608751209335&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjkvvSi6eTtAhVOQBoKHaJjACEQ_AUoAXoECBIQAw&biw=861&bih=679#imgrc=OfZcRBPYJpVR_M

def check_validity_input_number(num):
    """
    param: an input 
    return: a boolean (True if int between 2 and 5 inclusive, False otherwise)
    """
    try: 
        num = int(num)
        if (num >= 2 and num <= 5):
                return True 
        else:
            return False
    except:
        return False


def play_one_round(player_num, position, list_positions):
    """
    param: a player number (not needed though; simplify to do), an int, a list of int
    return: an int and a list of int
    """
    # roll die
    die = dice.roll_one_die()
    if position + die > 100:
        position = position
        # because this is a roll of die! so even if it's repeated, append it
        # these are not actual moves
        list_positions.append(position)
        return position, list_positions
    else:
        position = position + die
        if position in snakes_or_ladders.keys():
            position = snakes_or_ladders[position]
        list_positions.append(position)
        return position, list_positions

def main():
    # snakes or ladders mapping as global var
    global snakes_or_ladders
    snakes_or_ladders = mapping_snakes_ladders.snakes_or_ladders

    # get number of players as input
    num_players = input("type a number between 2 and 5")
    # check if valid number
    while not check_validity_input_number(num_players):
        num_players = input("you REALLY need a number between 2 and 5")
    num_players = int(num_players)

    # get player names
    players = [input("Enter name of player: ") for _ in range(num_players)]
    # int player positions and num of moves // refine last one
    positions = [0 for each in range(num_players)]
    list_positions = [[] for each in range(num_players)]

    # everyone throws a dice: first highest starts
    init_dice = [dice.roll_one_die() for _ in range(num_players)]
    index_player_starting = init_dice.index(max(init_dice))
 
    # re-arrange array of names as player orders
    players_reorg = players[:index_player_starting] + players[index_player_starting:]

    # if no one has reached 100, keep playing
    while 100 not in positions:
        for player_num in range(num_players):
            positions[player_num], list_positions[player_num] = play_one_round(player_num, positions[player_num], list_positions[player_num])
    
    # otherwise get who has won -- if several, the winner is the first one reaching
    index_winner = positions.index(100)
    print("You reached the top and won. Congrats player", players_reorg[index_winner], ". You did this in", len(list_positions[index_winner]), "rolls of die.")
    print("Your trajectory was:", list_positions[index_winner])

if __name__ == "__main__":
    main()