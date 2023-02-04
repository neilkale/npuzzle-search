import timeit
import numpy as np
import os
from node import Distance
from node import Node
from puzzle import Puzzle
import utility
import math
import sys
import random

os.system('clear')


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
initial_state, size = utility.read_data_csv('../board1.csv')
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


schedule = lambda t: 3000 * math.exp(-0.005 * t) if t < 5000 else 0

current_node = fringe.pop(0)
goal_node = np.asarray(final_state.get_current_state())
g = current_node.get_gn() + 1

#Function to calculate the probability, if heuristic of next node is higher than current node
def probability (chance):     
    if (chance>0.01):               
        return chance > random.uniform(0.0,1.0)
    else:
        return False

for t in range(sys.maxsize):   
    temprature = schedule(t)
    #print ("curret temp =",temprature)
    
    
    if (temprature == 0):  #If tempratre reaches to zero 
        explored_nodes.append(current_node)
        Puzzle.goal_reached(explored_nodes, count, size)
        break
    else:
        zero = np.where(np.asarray(current_node.get_current_state()) == 0)[0]#[0]
        count = Node.expand_node(fringe, explored_nodes, current_node, goal_node, zero, g, count, size)
        current_node_distance = Distance.calculate(np.asarray(current_node.get_current_state()), goal_node, size)
        #print("curr",current_node_distance)
        fringe_len= len(fringe)
        print("fringe",fringe_len)
        herustic_diff = []
        k=0
        print("current",np.asarray(current_node.get_current_state()))
        for i in range (0,len(fringe)):
            possible_next_node = fringe[i]
            print("Possible",np.asarray(possible_next_node.get_current_state()))
            possible_next_node_distance = Distance.calculate(np.asarray(possible_next_node.get_current_state()), goal_node, size)
            #print ("next",possible_next_node_distance)
            diff = possible_next_node_distance - current_node_distance
            #print ("diff",diff)
            if (np.array_equal(np.asarray(current_node.get_current_state()), np.asarray(possible_next_node.get_current_state()))):
                k=k+1
                pass
            else:
                herustic_diff.append(diff)
                #print(herustic_diff)
        minimum_fn = min(herustic_diff)
        minimum_fn_index = herustic_diff.index(minimum_fn)
        #print("index",minimum_fn_index)
        next_node = fringe[minimum_fn_index+k]
        #print(np.asarray(next_node.get_current_state()))
        #print(np.asarray(fringe[3].get_current_state()))

        #random_index = random.choice(range(0,fringe_len))
        #next_node = fringe.pop(random_indexz
        #print("curr",Distance.calculate(np.asarray(current_node.get_current_state()), goal_node, size) )
        #print("next",Distance.calculate(np.asarray(next_node.get_current_state()), goal_node, size) )
        delta_e = Distance.calculate(np.asarray(next_node.get_current_state()), goal_node, size) - Distance.calculate(np.asarray(current_node.get_current_state()), goal_node, size) 
        
        if delta_e <= 0 or probability(math.exp(delta_e/temprature)) if temprature>=0.013 else probability (0.001):
            current_node = next_node
            goal_node = np.asarray(final_state.get_current_state())
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
        fringe = []
    Current_time = timeit.default_timer()
    if (Current_time - start > Run_time ):
        explored_nodes.append(current_node)
        Puzzle.goal_reached(explored_nodes, count, size)
        break

stop = timeit.default_timer()
print("all : ", len(All_states))
print('Time: ', stop - start)
