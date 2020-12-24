import snake_ladder
import csv
import time

def run_sims(num_sim_to_run, csv_name):
    """
    This function is a wrapper that runs the snakes and ladders game for one player 
    and saves the results in a csv
    param: an int, number of times to run the simulation; a string that's the csv name of the output file
    return: None
    """
    start = time.time()

    field_names = ['roll_dice', 'path_complete', 'path_simplified', 'snake_16_6', 'snake_49_11',
    'snake_56_53', 'snake_62_19', 'snake_64_60', 'snake_87_24', 'snake_93_73', 'snake_95_75',
    'snake_98_78', 'ladder_1_38', 'ladder_4_14', 'ladder_9_31', 'ladder_21_42', 'ladder_28_84', 
    'ladder_36_44', 'ladder_56_67', 'ladder_71_91', 'ladder_80_100']

    f = open(csv_name, 'w')

    with f:
        writer = csv.DictWriter(f, fieldnames = field_names)
        writer.writeheader()

        # run simulation
        for i in range(num_sim_to_run):
            # call function in snake_ladder.py and save to filename
            row = snake_ladder.play_one_game()
            writer.writerow(row)

    end = time.time()
    print(num_sim_to_run, 'simulations took', end - start,'seconds to run')

# enter whatever the num of simulations you'd like
run_sims(10, '10_sim.csv')
run_sims(100, '100_sim.csv')
run_sims(1000, '1000_sim.csv')
run_sims(10000, '10000_sim.csv')
