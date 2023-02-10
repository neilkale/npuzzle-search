import utility
class Heuristic:
    def __init__(self, current_state, goal):
        self.current_state = current_state
        self.goal = goal

    def misplaced_tiles(self):
        tiles_indexs = []
        for i in range(len(self.current_state)):
            if self.current_state[i] != self.goal[i] and self.current_state[i] != 0:
                tiles_indexs.append([i,self.goal.index(self.current_state[i])])
        return tiles_indexs


    def manhattan_pre(self, distance,include_weight = False):
        hs = utility.distances
        missplaced_tiles_index = self.misplaced_tiles()
        for i in missplaced_tiles_index:
            temp = (hs[i[0]]['h'][i[1]])
            distance = distance + temp
            if include_weight:
                distance =  temp * self.current_state[i[0]] + distance

        return distance

    def manhattan(self, distance, size, include_weight = False):
        for i in range(0,len(self.current_state)):
            if self.current_state[i] != 0:
                tile = self.current_state[i]
                goal_index = self.goal.index(tile)
                goal_x = goal_index % size[1]
                goal_y = int((goal_index - goal_x) / size[1])
                curr_x = i % size[1]
                curr_y = int((i - curr_x) / size[1])
                temp = abs(goal_x - curr_x) + abs(goal_y - curr_y)
                distance = distance + temp
                if include_weight:
                    distance = (temp * self.current_state[i]) + distance
<<<<<<< HEAD
        
=======
>>>>>>> part3
        return distance

# Distance Class to Calculate the Manhattan and Misplaced Tiles and new Distance.
class Distance:
    def calculate(current_state, goal, heuristic, size):
        distance = 0
        if type(current_state) != list:
            current_state = current_state.tolist()
        if type(goal) != list:
            goal = goal.tolist()
        if(current_state == goal):
            return 0
        obj = Heuristic(current_state, goal)
        if heuristic == 1:            
            distance = obj.manhattan(distance, size)
        elif heuristic == 2:
            distance = obj.manhattan(distance, size, True)
        elif heuristic == 3:
            distance = obj.manhattan_pre(distance)
        elif heuristic == 4:
            distance = obj.manhattan_pre(distance, True)
        return distance
