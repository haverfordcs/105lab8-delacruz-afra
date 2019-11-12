# YOU MUST MAKE USE OF RECURSION
# Read the TwoPlayerGame.py carefully
# After reading the script you may have figured out the following
# The program simulates a two player game
# The player gets alternate chance to play
# Game gets started by a randomly chosen player
# The strategy the players play the game with is given below:
# ----Player1 always removes two pebbles
# ----Player2 removes two pebbles if an even number of pebbles is on the table, and one otherwise
# A total of five sets of experiments run, during each experiment, 2000 games are played

# What you are supposed to do is the following:

# Keeping everything same, you have to extend the game for three players
# Each player after playing for their turn should handover the turn to the next player
# Mutually recursive calls will be made in the following order Player1->Player2->Player3->Player1 
# The game should be started by a randomly chosen player -- already implemented
# The most important thing that you have to make sure that THE GAME IS NOT BIASED
# In an unbiased game, no matter who starts the game with whatever number of pebbles, the number of wins for all
# the players should be ALMOST SAME after playing significant number of games. This is the most important part of this problem
# In short, you have to come up with a STRATEGY (see the strategy for TwoPlayerGame) such that the game remains unbiased. 
# It is also important to make sure that the games finishes at some point.
# If you do everything correctly, all five graphs will show similar (may not be the same) heights of bars for all possible cases.
# For TwoPlayerGame its four cases, P1StartsP1Wins, P1StartsP2Wins, P2StartsP1Wins, and P2StartsP2Wins. Do you already know 
# how many cases would be there for ThreePlayerGame? Find out and make the changes accrodingly. 
