import timeit
import numpy as np
import os
from node import Distance
from node import Node
from puzzle import Puzzle


def greedy(initial_state, final_state, distance, heuristic, size):

    All_states = []
    data = []
    explored_nodes = []
    current_node = initial_state
    goal_node = np.asarray(final_state.get_current_state())
    count = 0
    print(distance)
    print(current_node.get_current_state())
    local_minima = False
    i = 0
    while i < 10:
        blank_spaces = np.where(np.asarray(current_node.get_current_state()) == 0)[0]
        current_node, distance_new, count = Node.expand_node_greedy(current_node, goal_node, blank_spaces, heuristic, size, distance,count)
        #print(distance_new)
        #print(current_node.get_current_state())
        if distance_new == distance:
            print('local minima')
            local_minima = True
            i+=1
        if distance_new < distance:
            print('not local minima')
            local_minima = False
            i=0        
        distance = distance_new
        print(i, distance)
    return distance
    