class Heuristic:
    def __init__(self, arr, goal):
        self.arr = arr
        self.goal = goal
        self.blank_original = (1,2)

    def manhattan(self, distance, size):
        distance = 0
        for i in range(0,length(self.arr)) 
            goal_x = self.arr[i] % size[1]
            goal_y = (int) (self.arr[i] / size[1])
            curr_x = i % size[1]
            curr_y = (int) (i / size[1])
            distance = distance + abs(goal_x - curr_x) + abs(goal_y - curr_y)
        return distance
        
    def manhattan_by_wieght(self,arr, distance):
        #print(arr)
        return distance

# Distance Class to Calculate the Manhattan and Misplaced Tiles and new Distance.
class Distance:
    def calculate(arr, goal, heuristic, size):
        distance = 0
        if type(arr) != list:
            arr = arr.tolist()
            goal = goal.tolist()
            if(arr == goal):
                return 0

        obj = Heuristic(arr, goal)
        if heuristic == 1:
            distance = obj.manhattan(distance, size)
        elif heuristic == 2:
            distance = obj.manhattan_by_wieght(arr, distance)
        return distance
