import numpy as np
from heuristic2 import Distance
from movements import Movements


class Node:
    # initialize the node with the board config
    def __init__(self, s):
        self.child = s
        self.parent = []
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
        return self.hn

    def get_current_state(self):
        return self.child

    def update_gn(self, gn):
        self.gn = gn

    def update_hn(self, hn):
        self.hn = hn

    def update_parent(self, parent):
        self.parent = parent

    # exploring the next states
    def expand_node(fringe, explored_nodes, current_node, goal_node, blank_spaces, g, count, size,check):
        a = [list(item.get_current_state()) for item in explored_nodes]
        explored_nodes.append(current_node)
        current_node_array = np.asarray(current_node.get_current_state())
        for blank_space_index in blank_spaces : # considered blankspace as a list of index with 0 value
          
            if blank_space_index+1 > size[1]: #blank space is not on top layer
                #print('not on top')
                node_copy = current_node_array.copy()
                move = Movements(node_copy, current_node_array, blank_space_index,size)
                # move move current up
                move.move("up", size)
                distance = Distance.calculate(node_copy, goal_node,size)
                node_copy = Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)
                node_copy.update_parent(current_node)
                
            
                
                if (check == 0):
                    fringe.append(node_copy)
                    count = count + 1
                else:
                    
                    if (np.array_equal(np.asarray(node_copy.get_current_state()), np.asarray((current_node.get_parent()).get_current_state()))):
                        pass
                    else:
                        fringe.append(node_copy)
                        count = count + 1

            if blank_space_index+1 < size[0]*size[1]+1 - size[1]: #blank space is not on bottom layer
                #print('not on bottom')
                node_copy = current_node_array.copy()
                move = Movements(node_copy, current_node_array, blank_space_index,size)
                # move current node down
                move.move("down", size)
                distance = Distance.calculate(node_copy, goal_node,size)
               
                node_copy = Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)
                node_copy.update_parent(current_node)
                
        
                
                
                if (check == 0):
                    fringe.append(node_copy)
                    count = count + 1
                else:
        
                    if (np.array_equal(np.asarray(node_copy.get_current_state()), np.asarray((current_node.get_parent()).get_current_state()))):
                        pass
                    else:
                        fringe.append(node_copy)
                        count = count + 1



            if blank_space_index % size[0] > 0:
                node_copy = current_node_array.copy()
                move = Movements(node_copy, current_node_array, blank_space_index,size)
                # move current node left
                move.move("left", size)
                distance = Distance.calculate(node_copy, goal_node,size)
           
                node_copy = Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)
                node_copy.update_parent(current_node)
               
                if (check == 0):
                    fringe.append(node_copy)
                    count = count + 1
                else:
                 
                    if (np.array_equal(np.asarray(node_copy.get_current_state()), np.asarray((current_node.get_parent()).get_current_state()))):
                        pass
                    else:
                        fringe.append(node_copy)
                        count = count + 1


            if (blank_space_index + 1) % size[0] != 0:
                node_copy = current_node_array.copy()
                move = Movements(node_copy, current_node_array, blank_space_index,size)
                # move current node right
                move.move("right", size)
                distance = Distance.calculate(node_copy, goal_node,size)
                
                node_copy = Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)
                node_copy.update_parent(current_node)

                if (check == 0):
                    fringe.append(node_copy)
                    count = count + 1
                else:
              
                    if (np.array_equal(np.asarray(node_copy.get_current_state()), np.asarray((current_node.get_parent()).get_current_state()))):
                        pass
                    else:
                        fringe.append(node_copy)
                        count = count + 1

        return count