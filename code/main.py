import timeit
import numpy as np
import os
from node import Distance
from node import Node
from puzzle import Puzzle
import utility
import astar

def get_final_solution_state(initial_state, size, heuristic):
    final_states = utility.get_final_states(initial_state, size)
    final_state_blanks_at_end = final_states[0]
    final_state_blanks_at_beginning = final_states[1]
    initial_state = Node(initial_state)
    final_state_blanks_at_end = Node(final_state_blanks_at_end)
    final_state_blanks_at_beginning = Node(final_state_blanks_at_beginning)

    distance0 = Distance.calculate(
        initial_state.get_current_state(), final_state_blanks_at_end.get_current_state(), heuristic, size)
    distance1 = Distance.calculate(
        initial_state.get_current_state(), final_state_blanks_at_beginning.get_current_state(), heuristic, size)

    if distance1 < distance0:
        distance = distance1
        final_state = final_state_blanks_at_beginning
    else:
        distance = distance0
        final_state = final_state_blanks_at_end
    return initial_state, final_state, distance

def main_function():
    #Initialize
    os.system('cls')
    start = timeit.default_timer()
    # TODO Update to match specified format
    heuristic = int(input("Choose a Heuristic: \n 1. Manhattan Distance \n 2. Manhattan By Weight Distance \n Enter : "))

    # For reading the initial state from csv as matrix
    # Size is an array in the format: [HEIGHT, WIDTH]
    initial_state, size = utility.read_data_csv('./board1.csv')

    # Get final state and update to node format
    initial_state, final_state, distance = get_final_solution_state(initial_state,size, heuristic)
       

    All_states, stop = astar.astar(initial_state, final_state, distance, heuristic, size)
    print("all : ", len(All_states))
    print('Time: ', stop - start)

main_function()