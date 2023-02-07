import timeit
import numpy as np
import os
from node import Distance
from node import Node
from puzzle import Puzzle


def greedy(initial_state, final_state, distance, heuristic, size):

    
    current_node = initial_state
    goal_node = np.asarray(final_state.get_current_state())
    count = 0
    #print(distance)
    #print(current_node.get_current_state())
    i = 0
    number_of_sideways_moves = 10
    while i < number_of_sideways_moves:
        blank_spaces = np.where(np.asarray(current_node.get_current_state()) == 0)[0]
        current_node, distance_new, count = Node.expand_node_greedy(current_node, goal_node, blank_spaces, heuristic, size, distance,count)
        #print(distance_new)
        #print(current_node.get_current_state())
        if distance_new == distance:
            #print('local minima')
            i+=1
        if distance_new < distance:
            #print('not local minima')
            i=0        
        distance = distance_new
        print(i, distance)
    return distance
    