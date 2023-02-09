import timeit
import numpy as np
import os
from node import Distance
from node import Node
from puzzle import Puzzle
import greedy
import utility
import astar

# Call utility function to generate arrays for the two possible final states, and pick the closest to the starting position
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

def get_final_solution_state_greedy(initial_state, size, heuristic):
    final_states = utility.get_final_states(initial_state, size)
    final_state_blanks_at_end = final_states[0]
    final_state_blanks_at_beginning = final_states[1]
    initial_state = Node(initial_state)
    final_state_blanks_at_end = Node(final_state_blanks_at_end)
    final_state_blanks_at_beginning = Node(final_state_blanks_at_beginning)

    distance0 = greedy.greedy(initial_state, final_state_blanks_at_end, heuristic, size)
    distance1 = greedy.greedy(initial_state, final_state_blanks_at_beginning, heuristic, size)

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
    
    # TODO Update to match specified format
    heuristic = int(input("Choose a Heuristic: \n 1. Manhattan Distance \n 2. Manhattan By Weight Distance \n Enter : "))

    # For reading the initial state from csv as matrix
    # Size is an array in the format: [HEIGHT, WIDTH]
    initial_state, size = utility.read_data_csv('./board1.csv')

    # Get final state and update to node format
    initial_state_node, final_state_node, distance = get_final_solution_state(initial_state,size, heuristic)
    
    # Run A* Using the sliding tile heuristic
    start = timeit.default_timer()
    astar.astar(initial_state_node, final_state_node, distance, heuristic, size)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    # Run A* with the greedy heuristic
    initial_state_node, final_state_node, distance = get_final_solution_state_greedy(initial_state,size, heuristic)
    start = timeit.default_timer()   
    astar.astar_greedy(initial_state_node, final_state_node, distance, heuristic, size)
    stop = timeit.default_timer()
    print('Time: ', stop - start)
    

main_function()