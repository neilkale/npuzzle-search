import timeit
import numpy as np
import os
from node import Distance
from node import Node
from puzzle import Puzzle


def astar(initial_state, final_state, distance, heuristic, size):

    All_states = []
    data = []
    explored_nodes = []
    fringe = [initial_state]

    

    fringe[0].update_hn(distance)
    count = 1

    print("---------------Printing Solution Path---------------\n \n")

    while  fringe:
        # select minimum fn for expand
        minimum_fn_index = Puzzle.least_fn(fringe)
        current_node = fringe.pop(minimum_fn_index)
        All_states.append(current_node.child)

        g = current_node.get_gn() + 1
        goal_node = np.asarray(final_state.get_current_state())
        
        # check if we reached goal state or not
        if np.array_equal(np.asarray(current_node.get_current_state()), goal_node):
            distance = Distance.calculate(np.asarray(
                current_node.get_current_state()), goal_node, heuristic, size)
            explored_nodes.append(current_node)
            Puzzle.goal_reached(explored_nodes, count, size)
            fringe = []
        elif not np.array_equal(current_node, goal_node):
            zero = np.where(np.asarray(
                current_node.get_current_state()) == 0)[0]
            #print(zero)
            count = Node.expand_node(
                fringe, explored_nodes, current_node, goal_node, zero, g, count, heuristic, size)

    stop = timeit.default_timer()
    

def astar_greedy(initial_state, final_state, distance, heuristic, size):

    All_states = []
    explored_nodes = []
    fringe = [initial_state]
    
    fringe[0].update_hn(distance)
    count = 1

    print("---------------Printing Solution Path---------------\n \n")

    while  fringe:
        # select minimum fn for expand
        minimum_fn_index = Puzzle.least_fn(fringe)
        current_node = fringe.pop(minimum_fn_index)
        All_states.append(current_node.child)

        g = current_node.get_gn() + 1
        goal_node = np.asarray(final_state.get_current_state())
        
        # check if we reached goal state or not
        if np.array_equal(np.asarray(current_node.get_current_state()), goal_node):
            distance = Distance.calculate(np.asarray(current_node.get_current_state()), goal_node, heuristic, size)
            explored_nodes.append(current_node)
            Puzzle.goal_reached(explored_nodes, count, size)
            fringe = []
        elif not np.array_equal(current_node, goal_node):
            zero = np.where(np.asarray(current_node.get_current_state()) == 0)[0]
            #print(zero)
            count = Node.expand_node_greedy_astar(
                fringe, explored_nodes, current_node, final_state, zero, g, count, heuristic, size)

    
    
