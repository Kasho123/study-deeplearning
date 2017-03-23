import perceptron

if __name__ == '__main__':
    myPerceptron = perceptron.Perceptron()
    print(myPerceptron.ANDWithTheta(0, 0))
    print(myPerceptron.ANDWithTheta(1, 0))
    print(myPerceptron.ANDWithTheta(0, 1))
    print(myPerceptron.ANDWithTheta(1, 1))

    print(myPerceptron.AND(0, 0))
    print(myPerceptron.AND(1, 0))
    print(myPerceptron.AND(0, 1))
    print(myPerceptron.AND(1, 1))

    print(myPerceptron.NAND(0, 0))
    print(myPerceptron.NAND(1, 0))
    print(myPerceptron.NAND(0, 1))
    print(myPerceptron.NAND(1, 1))

    print(myPerceptron.OR(0, 0))
    print(myPerceptron.OR(1, 0))
    print(myPerceptron.OR(0, 1))
    print(myPerceptron.OR(1, 1))

    print(myPerceptron.XOR(0, 0))
    print(myPerceptron.XOR(1, 0))
    print(myPerceptron.XOR(0, 1))
    print(myPerceptron.XOR(1, 1))
