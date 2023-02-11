import numpy as np
from heuristic import Distance
from movements import Movements
import timeit



class Node:
    # initialize the node with the board config
    def __init__(self, s):
        self.child = s
        self.parent = []
        self.gn = 0  # cost
        self.hn = 0  # heuristic
        self.fn = 0  # evaluator
        self.move = "Start."

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

    def get_node_move(self):
        return self.move

    def update_gn(self, gn):
        self.gn = gn

    def update_hn(self, hn):
        self.hn = hn

    def update_parent(self, parent):
        self.parent = parent
    
    def update_move(self, move):
        self.move = move
    

    @staticmethod
    def update_expanded(goal_node, heuristic, size, current_node, fringe,node_copy, a, g, move_string):
        distance = Distance.calculate(node_copy, goal_node, heuristic, size)    
        if not list(node_copy) in a:
            node_copy = Node(node_copy)
            node_copy.update_gn(g)
            node_copy.update_hn(distance)
            node_copy.update_parent(current_node)
            node_copy.update_move(move_string)
            fringe.append(node_copy)
        
    @staticmethod
    # Expand greedy search nodes using the greedy search heuristic
    def update_expanded_greedy_star(goal_node, heuristic, size, current_node, fringe,node_copy, a, g, move_string):
        import greedy
            
        if not list(node_copy) in a:
            node_copy = Node(node_copy)
            node_copy.update_gn(g)
            distance = greedy.greedy(node_copy, goal_node, heuristic, size)
            node_copy.update_hn(distance)
            node_copy.update_parent(current_node)
            node_copy.update_move(move_string)
            fringe.append(node_copy)

    # exploring the next states
    def expand_node_greedy(current_node, goal_node, blank_spaces, heuristic, size, distance, count):
        current_node_array = np.asarray(current_node.get_current_state())    
        best_node = current_node

        for blank_space_index in blank_spaces : # considered blankspace as a list of index with 0 value  
            #print(distance, current_node)
            
            if blank_space_index+1 > size[1]: #blank space is not on top layer
                if current_node_array[blank_space_index - size[1]] != 0:
                    #print('not on top')
                    switch_tile = current_node_array[blank_space_index - size[1]]
                    node_copy = current_node_array.copy()
                    #print('goal node:', type(goal_node))
                    #print('current: ',type(node_copy))
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move move current up
                    move.move("up", size)
                    move_string = ('Move tile '+str(switch_tile)+" down.")
                    #print(move_string)
                    
                    if Distance.calculate(node_copy, goal_node, heuristic,size) < distance:
                        #print(Distance.calculate(node_copy, goal_node, heuristic,size))
                        distance = Distance.calculate(node_copy, goal_node, heuristic,size)
                        best_node = Node(node_copy)
                        best_node.update_parent(current_node)
                        best_node.update_move(move_string)
                        count = count +1
                        return best_node, distance, count
                                            
            if blank_space_index+1 < size[0]*size[1]+1 - size[1]: #blank space is not on bottom layer
                if current_node_array[blank_space_index + size[1]] != 0:
                    #print('not on bottom')
                    switch_tile = current_node_array[blank_space_index + size[1]]
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move current node down
                    move.move("down", size)
                    move_string = ('Move tile '+str(switch_tile)+" up.")
                    #print(move_string)
                    if Distance.calculate(node_copy, goal_node, heuristic,size) < distance:
                        #print(Distance.calculate(node_copy, goal_node, heuristic,size))
                        #distance = Distance.calculate(node_copy, goal_node, heuristic,size)
                        best_node = Node(node_copy)
                        best_node.update_parent(current_node)
                        best_node.update_move(move_string)
                        count = count +1
                        return best_node, distance, count
                    
            if blank_space_index % size[0] > 0:
                if current_node_array[blank_space_index - 1] != 0:
                    switch_tile = current_node_array[blank_space_index - 1]
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move current node left
                    move.move("left", size)
                    move_string = ('Move tile '+str(switch_tile)+" right.")
                    #print(move_string)
                    if Distance.calculate(node_copy, goal_node, heuristic,size) < distance:
                        #print(Distance.calculate(node_copy, goal_node, heuristic,size))
                        distance = Distance.calculate(node_copy, goal_node, heuristic,size)
                        best_node = Node(node_copy)
                        best_node.update_parent(current_node)
                        best_node.update_move(move_string)
                        count = count +1
                        return best_node, distance, count
                        
            if (blank_space_index + 1) % size[0] != 0:
                if current_node_array[blank_space_index + 1] != 0: 
                    switch_tile = current_node_array[blank_space_index + 1]
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move current node right
                    move.move("right", size)
                    move_string = ("Move tile "+str(switch_tile)+" left.")
                    #print(move_string)
                    #print('current: ',node_copy)
                    if Distance.calculate(node_copy, goal_node, heuristic,size) < distance:
                        #print('current: ',node_copy)
                        #print(Distance.calculate(node_copy, goal_node, heuristic, size))

                        
                        distance = Distance.calculate(node_copy, goal_node, heuristic, size)
                        best_node = Node(node_copy)
                        best_node.update_parent(current_node)
                        best_node.update_move(move_string)
                        count = count +1
                        return best_node, distance, count
                            
        #print('Distance: ', distance)
        #print('Best Node: ',best_node.get_current_state())
        return best_node, distance, count
    
    def expand_node(fringe, explored_nodes, current_node, goal_node, blank_spaces, g, count, heuristic, size, times):
        a = [list(item.get_current_state()) for item in explored_nodes]
        explored_nodes.append(current_node)
        current_node_array = np.asarray(current_node.get_current_state())
        times = []
        for blank_space_index in blank_spaces : # considered blankspace as a list of index with 0 value
            #if item - size[0]*size[1] >=0:   # size is size of matrix
            if blank_space_index+1 > size[1]: #blank space is not on top layer
                if current_node_array[blank_space_index - size[1]] != 0:
                    start = timeit.default_timer()
                    
                    #print('not on top')
                    switch_tile = current_node_array[blank_space_index - size[1]]
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move move current up
                    move.move("up", size)
                    move_string = ('Move tile '+str(switch_tile)+" down.")
                    #print(move_string)
                    Node.update_expanded(goal_node, heuristic, size, current_node, fringe,node_copy, a, g, move_string)
                    count = count + 1
                    stop = timeit.default_timer()
                    #print('Time: ', stop - start)
                    times.append(stop-start)


            if blank_space_index+1 < size[0]*size[1]+1 - size[1]: #blank space is not on bottom layer
                if current_node_array[blank_space_index + size[1]] != 0:
                    start = timeit.default_timer()
                    #print('not on bottom')
                    switch_tile = current_node_array[blank_space_index + size[1]]
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move current node down
                    move.move("down", size)
                    move_string = ('Move tile '+str(switch_tile)+" up.")
                    #print(move_string)
                    Node.update_expanded(goal_node, heuristic, size, current_node, fringe,node_copy, a, g, move_string)
                    count = count + 1
                    stop = timeit.default_timer()
                    #print('Time: ', stop - start)
                    times.append(stop-start)


            if blank_space_index % size[0] > 0:
                if current_node_array[blank_space_index - 1] != 0:
                    start = timeit.default_timer()
                    switch_tile = current_node_array[blank_space_index - 1]
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move current node left
                    move.move("left", size)
                    move_string = ('Move tile '+str(switch_tile)+" right.")
                    #print(move_string)
                    Node.update_expanded(goal_node, heuristic, size, current_node, fringe, node_copy, a, g, move_string)
                    count = count + 1
                    stop = timeit.default_timer()
                    #print('Time: ', stop - start)
                    times.append(stop-start)


            if (blank_space_index + 1) % size[0] != 0:
                if current_node_array[blank_space_index + 1] != 0: 
                    start = timeit.default_timer()
                    switch_tile = current_node_array[blank_space_index + 1]
                    node_copy = current_node_array.copy()
                    move = Movements(node_copy, current_node_array, blank_space_index,size)
                    # move current node right
                    move.move("right", size)
                    move_string = ("Move tile "+str(switch_tile)+" left.")
                    #print(move_string)
                    Node.update_expanded(goal_node, heuristic, size, current_node, fringe, node_copy, a, g, move_string)
                    count = count + 1
                    stop = timeit.default_timer()
                    #print('Time: ', stop - start)
                    times.append(stop-start)

        #print(times)
        return count, times

    def expand_node_greedy_astar(fringe, explored_nodes, current_node, goal_node, blank_spaces, g, count, heuristic, size, times):
            a = [list(item.get_current_state()) for item in explored_nodes]
            explored_nodes.append(current_node)
            current_node_array = np.asarray(current_node.get_current_state())
            #times = []
            for blank_space_index in blank_spaces : # considered blankspace as a list of index with 0 value
                #if item - size[0]*size[1] >=0:   # size is size of matrix
                if blank_space_index+1 > size[1]: #blank space is not on top layer
                    if current_node_array[blank_space_index - size[1]] != 0:
                        start = timeit.default_timer()
                    
                        #print('NOT ON TOP')
                        switch_tile = current_node_array[blank_space_index - size[1]]
                        node_copy = current_node_array.copy()
                        move = Movements(node_copy, current_node_array, blank_space_index,size)
                        # move move current up
                        move.move("up", size)
                        move_string = ('Move tile '+str(switch_tile)+" down.")
                        #print(move_string)
                        Node.update_expanded_greedy_star(goal_node, heuristic, size, current_node, fringe,node_copy, a, g, move_string)
                        count = count + 1
                        stop = timeit.default_timer()
                        #print('Time: ', stop - start)
                        times.append(stop-start)


                if blank_space_index+1 < size[0]*size[1]+1 - size[1]: #blank space is not on bottom layer
                    if current_node_array[blank_space_index + size[1]] != 0:
                        start = timeit.default_timer()
                    
                        #print('NOT ON BOTTOM')
                        switch_tile = current_node_array[blank_space_index + size[1]]
                        node_copy = current_node_array.copy()
                        move = Movements(node_copy, current_node_array, blank_space_index,size)
                        # move current node down
                        move.move("down", size)
                        move_string = ('Move tile '+str(switch_tile)+" up.")
                        #print(move_string)
                        Node.update_expanded_greedy_star(goal_node, heuristic, size, current_node, fringe,node_copy, a, g, move_string)
                        count = count + 1
                        stop = timeit.default_timer()
                        #print('Time: ', stop - start)
                        times.append(stop-start)



                if blank_space_index % size[0] > 0:
                    if current_node_array[blank_space_index - 1] != 0:
                        start = timeit.default_timer()
                    
                        #print('NOT ON LEFT')
                        switch_tile = current_node_array[blank_space_index - 1]
                        node_copy = current_node_array.copy()
                        move = Movements(node_copy, current_node_array, blank_space_index,size)
                        # move current node left
                        move.move("left", size)
                        move_string = ('Move tile '+str(switch_tile)+" right.")
                        #print(move_string)
                        Node.update_expanded_greedy_star(goal_node, heuristic, size, current_node, fringe, node_copy, a, g, move_string)
                        count = count + 1
                        stop = timeit.default_timer()
                        #print('Time: ', stop - start)
                        times.append(stop-start)



                if (blank_space_index + 1) % size[0] != 0:
                    if current_node_array[blank_space_index + 1] != 0:
                        start = timeit.default_timer()
                    
                        #print('NOT ON RIGHT') 
                        switch_tile = current_node_array[blank_space_index + 1]
                        node_copy = current_node_array.copy()
                        move = Movements(node_copy, current_node_array, blank_space_index,size)
                        # move current node right
                        move.move("right", size)
                        move_string = ("Move tile "+str(switch_tile)+" left.")
                        #print(move_string)
                        Node.update_expanded_greedy_star(goal_node, heuristic, size, current_node, fringe, node_copy, a, g, move_string)
                        count = count + 1
                        stop = timeit.default_timer()
                        #print('Time: ', stop - start)
                        times.append(stop-start)

            #print(times)
            return count, times

