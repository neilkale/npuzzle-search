class Heuristic:
    def __init__(self, current_state, goal):
        self.current_state = current_state
        self.goal = goal

    def manhattan(self, distance, size):
        distance = 0
        for i in range(0,len(self.current_state)): 
            goal_x = self.current_state[i] % size[1]
            goal_y = (int) (self.current_state[i] / size[1])
            curr_x = i % size[1]
            curr_y = (int) (i / size[1])
            distance = distance + abs(goal_x - curr_x) + abs(goal_y - curr_y)
        return distance
        
    def manhattan_by_wieght(self,current_state, distance):
        #print(current_state)
        return distance

# Distance Class to Calculate the Manhattan and Misplaced Tiles and new Distance.
class Distance:
    def calculate(current_state, goal, heuristic, size):
        distance = 0
        if type(current_state) != list:
            current_state = current_state.tolist()
            goal = goal.tolist()
            if(current_state == goal):
                return 0

        obj = Heuristic(current_state, goal)
        if heuristic == 1:
            distance = obj.manhattan(distance, size)
        elif heuristic == 2:
            distance = obj.manhattan_by_wieght(current_state, distance)
        return distance
