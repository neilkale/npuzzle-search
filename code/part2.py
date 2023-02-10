import timeit
import numpy as np
import os
from node2 import Distance
from node2 import Node
from puzzle import Puzzle
import utility
import math
import sys
import random

os.system('clear')

def part2():
    Run_time = int(input(" Enter time in seconds how long to run hill climb search  \n Enter : "))

    start = timeit.default_timer()
    Current_time = start

    """
    1 3 4
    2 B 5
    -----
    1 2 3
    4 5 B
    """

    # For reading the initial state from csv as matrix
    # Size is an array in the format: [HEIGHT, WIDTH]
    initial_state, size = utility.read_data_csv('./board1.csv')
    final_states = utility.get_final_states(initial_state, size)
    # To Do: implement a* for multiple solutions  
    final_state_blanks_at_end = final_states[0]
    final_state_blanks_at_beginning = final_states[1]

    All_states = []
    data = []

    initial_state = Node(initial_state)
    final_state_blanks_at_end = Node(final_state_blanks_at_end)
    final_state_blanks_at_beginning = Node(final_state_blanks_at_beginning)
    explored_nodes = []
    fringe = [initial_state]
    distance0 = Distance.calculate(initial_state.get_current_state(), final_state_blanks_at_end.get_current_state(), size=size)
    distance1 = Distance.calculate(initial_state.get_current_state(), final_state_blanks_at_beginning.get_current_state(), size=size)

    print(distance0,distance1)
    if distance1 < distance0:
        distance = distance1
        final_state = final_state_blanks_at_beginning
    else:
        distance = distance0
        final_state = final_state_blanks_at_end

    fringe[0].update_hn(distance)
    count = 1



    print("---------------Printing Solution Path---------------\n \n")

    # Function to calculate the temperature
    schedule = lambda t: 9000 * math.exp(-0.002 * t) if t < 8000 else 0

    current_node = fringe.pop(0)
    goal_node = np.asarray(final_state.get_current_state())
    g = current_node.get_gn() + 1

    #Function to calculate the probability taking next move, if heuristic of next node is higher than current node
    def probability (chance):
        return chance > random.uniform(0.0,1.0)   

    check = 0

    for t in range(sys.maxsize):   
        temprature = schedule(t)

        
        
        if (temprature == 0):  #If tempratre reaches to zero 
            explored_nodes.append(current_node)
            Puzzle.goal_reached(explored_nodes, count, size)
            break

        else:
            zero = np.where(np.asarray(current_node.get_current_state()) == 0)[0]#[0]
            #print (zero)
            count = Node.expand_node(fringe, explored_nodes, current_node, goal_node, zero, g, count, size,check)
            current_node_distance = Distance.calculate(np.asarray(current_node.get_current_state()), goal_node, size)
            fringe_len= len(fringe)
            herustic_diff = []
            k=0
            
            #Simple hill climbing
            for i in range (0,len(fringe)):

                possible_next_node = fringe[i]
                possible_next_node_distance = possible_next_node.get_hn()
                diff = possible_next_node_distance - current_node_distance
            
                if (np.array_equal(np.asarray(current_node.get_current_state()), np.asarray(possible_next_node.get_current_state()))):
                    k=k+1
                    pass
                else:
                    herustic_diff.append(diff)
        
            minimum_fn = min(herustic_diff)
            minimum_fn_index = herustic_diff.index(minimum_fn)
            next_node = fringe[minimum_fn_index+k]
            delta_e = next_node.get_hn() - current_node_distance

            t = probability(math.exp(-1 *delta_e/temprature)) if temprature>=0.1 else False  

            #Simulated annealing 
            if delta_e < 0 or t :
                current_node = next_node
            
    
                if (np.array_equal(np.asarray(current_node.get_current_state()), goal_node)):
                    distance = Distance.calculate(np.asarray(current_node.get_current_state()), goal_node, size)
                    explored_nodes.append(current_node)
                    
                    Puzzle.goal_reached(explored_nodes, count, size)
                    break
                if type(current_node.child) != list:
                    status = ""
                    All_states.append({'list': current_node.child.tolist(), 'distance': current_node.hn})
                else:
                    All_states.append({'list': current_node.child,'distance': current_node.hn})
            else:

                # For random restarts
                next_node_1 = random.choice(fringe)
                current_node = next_node_1
                pass
                
            fringe = []
            check = 1
        Current_time = timeit.default_timer()
        if (Current_time - start > Run_time ):
            explored_nodes.append(current_node)
            
            Puzzle.goal_reached(explored_nodes, count, size)
            break

    stop = timeit.default_timer()
    print("all : ", len(All_states))
    print('Time: ', stop - start)
