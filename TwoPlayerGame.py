# Player1 always removes two pebbles
# Player2 removes two pebbles if an even number of pebbles is on the table, and one otherwise
# Note that the strategy of both players allow the number of pebbles to become zero
# Otherwise, the program will run into infinite loop if the number of pebbles never becomes "zero"
# importing random so we can start with random number of pebbles as well as randomly chose who starts the game
import random
from matplotlib import pyplot as plt
import sys

# Setting the recursion depth to 20000
sys.setrecursionlimit(20000)


# defining how player1 plays the game
def player1(pebble_count):
    # Strategy:
    # Always picks 2
    if pebble_count == 0:
        return "p2won"  # player2 wins
    else:
        return player2(pebble_count - 2)  # handing over to player2 after picking 2 pebbles


# defining how player2 plays the game
def player2(pebble_count):
    # Strategy:
    # pick 2 pebbles if number of pebbles is even otherwise pick 1
    if pebble_count == 0:
        return "p1won"  # player1 wins
    elif pebble_count % 2 == 0:  # Checking for even
        return player1(pebble_count - 2)  # handing over to player1 after picking 2 pebbles
    else:
        return player1(pebble_count - 1)  # # handing over to player1 after picking 1 pebbles


# Playing the game for desired number of times
# Also testing whether the game is biased or not
# Game would not be biased if both players win equal number of times regardless who starts with what number of pebbles
if __name__ == "__main__":
    # Number of experiments
    number_of_experiments = 5
    for experiment_id in range(number_of_experiments):
        # Automate the game play
        # Initializing some required variables
        number_of_players = 2
        howmanytimes_per_player = 1000
        minimum = number_of_players * 3
        maximum = number_of_players * howmanytimes_per_player
        # generating a list of initial pebble counts to start with
        initial_pebble_counts = random.sample(range(minimum, maximum), maximum - minimum)
        # print initial_pebble_counts or debug to see what are initial pebble counts are
        # Creating a blank list, which will keep tuples with elements who starts the game
        # with howmany pebbles and who wins the game
        results = []
        for initial in initial_pebble_counts:  # Play the game for every randomly generated pebble count
            whostarts = random.randint(1, number_of_players)  # decide who starts the game by generating a random number
            if whostarts == 1:  # In case player1 starts the game
                results.append(('p1started', initial, player1(initial)))  # storing who started with how many pebbles along with won the game
            elif whostarts == 2:  # In case player2 starts the game
                results.append(('p2started', initial, player1(initial)))  # storing who started with how many pebbles along with won the game
            else:
                raise ValueError("No such player exists")  # raise an error if player was not recognized

        stat_dict = {}
        for result in results:
            key = result[0] + result[2]  # creating the key using who started and who won
            if key not in stat_dict:
                stat_dict[key] = 1
            else:
                stat_dict[key] += 1

        plt.figure('Experiment'+str(experiment_id))
        plt.bar(stat_dict.keys(), stat_dict.values())
        plt.xlabel('Scenarios')
        plt.xticks(rotation='vertical')
        plt.ylabel("Number of wins")
        plt.title('Game stats')
        plt.tight_layout()

plt.show()
