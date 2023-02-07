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
    for i in range(2):
        blank_spaces = np.where(np.asarray(current_node.get_current_state()) == 0)[0]
        current_node, distance, count = Node.expand_node_greedy(current_node, goal_node, blank_spaces, heuristic, size, distance,count)
        print(distance)

    