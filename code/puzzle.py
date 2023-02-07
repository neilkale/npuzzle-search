import numpy as np

class Puzzle:
    def least_fn(fringe):
        fn_fringe = []
        for i in range(len(fringe)):
            fn_fringe.append(fringe[i].get_fn())
        minimum_fn = min(fn_fringe)
        minimum_fn_index = fn_fringe.index(minimum_fn)
        return minimum_fn_index

    def print_state(node, size):
        base = "-------"

        print("g(n) = ", node.get_gn(), " h(n) = ",
              node.get_hn(), " f(n) = ", node.get_fn(), "\n")
        
        print(node.get_node_move())
        print("Branching Factor = ", node.get_branching_factor(),"\n")

        matrix = np.matrix(node.get_current_state()).reshape(size)

        for i in range(size[0]):
            for j in range(size[1]):
                if matrix[i,j] < 10:
                    print("\t", matrix[i, j], end="  |")
                else:
                    print("\t", matrix[i, j], end=" |")
            if i != (size[0]-1):
                print("\n \t", base*size[0])
                

        print("\n----------------------------------------------------------\n")
        return node.get_branching_factor()
    
    def goal_reached(explored_nodes, count, size):
        nodes_expanded = len(explored_nodes) - 1
        path = []
        init = explored_nodes[0]
        current = explored_nodes.pop()

        while init != current:
            path.append(current)
            current = current.get_parent()

        path.append(init)
        path.reverse()

        branching_factor_array = []
        
        for i in path:
            branching_factor = Puzzle.print_state(i, size)
            branching_factor_array.append(branching_factor)
        
        branching_factor_array.pop()
        
        print("Goal Reached! \n")
        print("The number of nodes expanded: ", nodes_expanded, "\n")
        print("The number of nodes generated: ", count, "\n")
        print("Path Cost: ", len(path) - 1, "\n")
        print("Average Branching Factor: ", sum(branching_factor_array)/len(branching_factor_array),"\n")

    def path(explored_nodes):
        explored_nodes.pop()
