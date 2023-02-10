class Heuristic:
    def __init__(self, current_state, goal):
        self.current_state = current_state
        self.goal = goal

    def manhattan(self, distance, size):
        for i in range(0,len(self.current_state)):
            if self.current_state[i] != 0:
        
                tile = self.current_state[i]
                goal_index = self.goal.index(tile)
                goal_x = goal_index % size[1]
                goal_y = int((goal_index - goal_x) / size[1])
                curr_x = i % size[1]
                curr_y = int((i - curr_x) / size[1])
                distance = distance + abs(goal_x - curr_x) + abs(goal_y - curr_y)
                #distance = (abs(goal_x - curr_x) + abs(goal_y - curr_y))*self.current_state[i] + distance
                #distance = (distance * self.current_state[i]) + distance
            
            
        return distance

# Distance Class to Calculate the Manhattan Distance.
class Distance:
    def calculate(current_state, goal, size):
        distance = 0
        if type(current_state) != list:
            current_state = current_state.tolist()
            goal = goal.tolist()
            if(current_state == goal):
                return 0

        obj = Heuristic(current_state, goal)
        distance = obj.manhattan(distance, size)
        return distance
