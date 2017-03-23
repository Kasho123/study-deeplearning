import numpy as np

class Perceptron:

    def ANDWithTheta(self, x1, x2):
        w1, w2, theta = 0.5, 0.5, 0.7
        result = x1*w1 + x2*w2
        if result <= theta:
            return 0
        elif result > theta:
            return 1

    def AND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.7
        result = np.sum(x*w) + b
        if result <= 0:
            return 0
        else:
            return 1

    def NAND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([-0.5, -0.5])
        b = 0.7
        result = np.sum(x*w) + b
        if result <= 0:
            return 0
        else:
            return 1

    def OR(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.2
        result = np.sum(x*w) + b
        if result <= 0:
            return 0
        else:
            return 1

    def XOR(self, x1, x2):
        nandResult = self.NAND(x1, x2)
        orResult = self.OR(x1, x2)
        return self.AND(nandResult, orResult)
