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
        for i in range(3):
            self.red_pos = input()
            self.red_val = input()
            matrix[0 , self.red_pos] = self.red_val
            
        return matrix


if __name__ == '__main__':
    # object = game_object()
    # print(object.bounding_box()), print(object.bounding_box())
    logic = game_logic()
    print(logic.fill_matrix(1,1))
