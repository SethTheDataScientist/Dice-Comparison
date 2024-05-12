
import random
import numpy as np
import time

def roll_die(sides):
    """Rolls a die with a given number of sides."""
    return random.randint(1, sides)

def main():
    dice = [4, 6, 8, 10, 12, 20]
    current_index = 0
    # loop_average = []
    # average_rolls = []
    final_rolls = 10000000
    final_roll_value = 6
    full_loop_test = 0
    min_value_seen = 410000000
    cumulative_rolls = 0
    start_time = time.time()  # Start timing the dice rolling process
    while final_rolls != final_roll_value:
        current_index = 0
        
        total_rolls = 0

        # loop_rolls = 0
        while current_index < len(dice):
            sides = dice[current_index]
            result = roll_die(sides)
            total_rolls += 1
            # loop_rolls += 1
            if result != sides:
                # loop_average.append(loop_rolls)
                # loop_rolls = 0
                current_index = 0  # Restart from the first die
            else:
                current_index += 1  # Move to the next die
            # average_rolls.append(total_rolls)
        
        # loop_average.append(loop_rolls)
        cumulative_rolls += total_rolls
        final_rolls = total_rolls
        if total_rolls < min_value_seen:
            min_value_seen = total_rolls
        full_loop_test += 1
        if full_loop_test % 100 == 0:
            print(full_loop_test)   
            print(f'Min Value: {min_value_seen}')
    elapsed_time = time.time() - start_time  # Calculate elapsed time after completion
    print(f"You finally found a set under {final_roll_value} rolls")
    # print("All dice rolled their maximum values!")
    # print(f'Average number of rolls it achieved per run {np.mean(average_rolls):.2f}')
    # print(f'Average number of rolls it achieved per loop {np.mean(loop_average):.2f}')
    print(f"Total time taken: {elapsed_time:.2f} seconds")
    print(f'The final amount of rolls was {cumulative_rolls}')
    human_time = (cumulative_rolls * 1.5)/60/60
    print(f'This would take a human {human_time} HOURS to complete')

if __name__ == "__main__":

    main()


