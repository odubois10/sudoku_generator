import numpy as np
import random


class Generate:

    def __init__(self):
        self.A = np.random.randint(1, 10, size=(3, 3))
        self.B = np.zeros((9, 9))

    def build_key(self):
        self.B[:2, :2] = self.A
        for i in range(9):
            # iterates through matrix row
            for j in range(9):
                # iterates through matrix column
                if not self.B[i, j]:
                    # checks that the space is not yet filled
                    for k in range(7):
                        # ange of spots left to fill
                        r = random.randint(1, 10)  # generates random number between 1 and 9
                        if r not in self.B[i] and r not in self.B[:, j]:
                            # checks that the number is not already in its row and column
                            self.B[i, j] = r
