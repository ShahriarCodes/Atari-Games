import numpy as np
class game_object:
    def bounding_box(self):
        box = '''
        -----------
        |         |
        |         |
        |         |
        -----------'''
        return box

    def create_matrix(self):
        mat = np.full([3,3], None)
        return mat

class game_logic:
    def __init__(self, red_pos = None, zero_pos = None, red_val = None, zero_val = None):
        self.red_pos = red_pos
        self.zero_pos = zero_pos
        self.red_val  = red_val
        self.zero_val = zero_val

    def fill_matrix(self,red_pos = None, red_val = None):
        object = game_object()
        matrix = object.create_matrix()

        index = {
        1 : (0,0),
        2 : (0,1),
        3 : (0,2),
        4 : (1,0),
        5 : (1,1),
        6 : (1,2),
        7 : (2,0),
        8 : (2,1),
        9 : (2,2)
        }

        for i in range(9):
            self.red_pos = int(input())
            self.red_val = input()
            matrix[index[self.red_pos][0], index[self.red_pos][1]] = self.red_val
            print(matrix)
        return matrix


if __name__ == '__main__':
    # object = game_object()
    # print(object.bounding_box()), print(object.bounding_box())
    logic = game_logic()
    print(logic.fill_matrix(1,1))
