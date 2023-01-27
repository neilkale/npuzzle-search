class Movements:
    def __init__(self, node_copy, current_node_array, blank_space, size):
        self.current_node_array = current_node_array
        self.node = node_copy
        self.blank_space = blank_space
        self.size = size

    def move(self, direction,size):
        if direction == "up":
            self.up()
            self.size = size
        if direction == "down":
            self.down()
            self.size = size
        if direction == "right":
            self.right()
            self.size = size
        if direction == "left":
            self.left()
            self.size = size

    # movements
    def up(self):
        self.node[self.blank_space - self.size[1]], self.node[self.blank_space] = self.current_node_array[self.blank_space], self.node[self.blank_space - self.size[1]]
        return "successfully moved"

    def down(self):
        self.node[self.blank_space + self.size[1]], self.node[self.blank_space] = self.current_node_array[self.blank_space], self.node[self.blank_space + self.size[1]]
        return "successfully moved"

    def left(self):
        self.node[self.blank_space - 1], self.node[self.blank_space] = self.current_node_array[self.blank_space], self.node[self.blank_space - 1]
        return "successfully moved"

    def right(self):
        self.node[self.blank_space + 1], self.node[self.blank_space] = self.current_node_array[self.blank_space], self.node[self.blank_space + 1]
        return "successfully moved"

