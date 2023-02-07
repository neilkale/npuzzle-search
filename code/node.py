import numpy as np
from heuristic import Distance
from movements import Movements


class Node:
    # initialize the node with the board config
    def __init__(self, s):
        self.child = s
        self.parent = None
        self.gn = 0  # cost
        self.hn = 0  # heuristic
        self.fn = 0  # evaluator

    def get_parent(self):
        return self.parent

    def get_hn(self):
        return self.hn

    def get_gn(self):
        return self.gn

    def get_fn(self):
        return self.gn + self.hn

    def get_current_state(self):
        return self.child

    def update_gn(self, gn):
        self.gn = gn

    def update_hn(self, hn):
        self.hn = hn

    def update_parent(self, parent):
        self.parent = parent

    @staticmethod
    def update_expanded(goal_node, heuristic, size, current_node, fringe,node_copy, a, g):
        distance = Distance.calculate(node_copy, goal_node, heuristic,size)    
        if not list(node_copy) in a:
            node_copy = Node(node_copy)
            node_copy.update_gn(g)
            node_copy.update_hn(distance)
            node_copy.update_parent(current_node)
            fringe.append(node_copy)

    # exploring the next states
    def expand_node(fringe, explored_nodes, current_node, goal_node, blank_spaces, g, count, heuristic, size):
        a = [list(item.get_current_state()) for item in explored_nodes]
        explored_nodes.append(current_node)
        current_node_array = np.asarray(current_node.get_current_state())
        
        for blank_space_index in blank_spaces : # considered blankspace as a list of index with 0 value
            #if item - size[0]*size[1] >=0:   # size is size of matrix
            if blank_space_index+1 > size[1]: #blank space is not on top layer
                if current_node_array[blank_space_index - size[1]] != 0:
                    #print('not on top')
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move move current up
                    move.move("up", size)
                    Node.update_expanded(goal_node, heuristic, size, current_node, fringe,node_copy, a, g)
                    count = count + 1

            if blank_space_index+1 < size[0]*size[1]+1 - size[1]: #blank space is not on bottom layer
                if current_node_array[blank_space_index + size[1]] != 0:
                    #print('not on bottom')
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move current node down
                    move.move("down", size)
                    Node.update_expanded(goal_node, heuristic, size, current_node, fringe,node_copy, a, g)
                    count = count + 1

            if blank_space_index % size[0] > 0:
                if current_node_array[blank_space_index - 1] != 0:
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move current node left
                    move.move("left", size)
                    Node.update_expanded(goal_node, heuristic, size, current_node, fringe, node_copy, a, g)
                    count = count + 1

            if (blank_space_index + 1) % size[0] != 0:
                if current_node_array[blank_space_index + 1] != 0: 
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move current node right
                    move.move("right", size)
                    Node.update_expanded(goal_node, heuristic, size, current_node, fringe,node_copy, a, g)
                    count = count + 1
        return count

