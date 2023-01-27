class Heuristic:
    def __init__(self, arr, goal):
        self.arr = arr
        self.goal = goal
        self.matrix = []
        self.blank_original = (1,2)

    def manhattan(self, distance):
        distance = sum(abs((val - 1) % 3 - i % 3) + abs((val - 1) // 3 - i // 3)
                       for i, val in enumerate(self.arr) if val)
        return distance
        
    def manhattan_by_wieght(self,arr, distance):
        #print(arr)
        return distance

# Distance Class to Calculate the Manhattan and Misplaced Tiles and new Distance.
class Distance:
    def calculate(arr, goal, heuristic):
        distance = 0
        if type(arr) != list:
            arr = arr.tolist()
            goal = goal.tolist()
            if(arr == goal):
                return 0

        obj = Heuristic(arr, goal)
        if heuristic == 1:
            distance = obj.manhattan(distance)
        elif heuristic == 2:
            distance = obj.manhattan_by_wieght(arr, distance)
        return distance
