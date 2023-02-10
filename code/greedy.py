import timeit
import numpy as np
import os
from heuristic import Distance
from node import Node
from puzzle import Puzzle


def greedy(initial_state, final_state, heuristic, size):
    current_node = initial_state
    goal_node = np.asarray(final_state.get_current_state())
    count = 0
    # Manhattan Distance from Start to End
    distance = Distance.calculate(current_node.get_current_state(), goal_node, heuristic,size)
    #print('Start greedy - distance: ',distance)
    #print(current_node.get_current_state(), goal_node)
    i = 0
    steps = 0
    number_of_sideways_moves = 10
    while i < number_of_sideways_moves:
        # Utility to get blank space indices
        blank_spaces = np.where(np.asarray(current_node.get_current_state()) == 0)[0]

        new_current_node, distance_new, count = Node.expand_node_greedy(current_node, goal_node, blank_spaces, heuristic, size, distance, count)
                
        # Goal Found
        if distance_new == 0:
            #print(new_current_node.get_current_state())
            return distance+steps
        
        if distance_new == distance:
            #print('local minima')
            i+=1

        if distance_new < distance:
            #print('not local minima')
            i=0   

        if new_current_node != current_node:
            steps += 1
        
        distance = distance_new
        current_node = new_current_node

    return distance+steps
    