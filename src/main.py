import sys
import random
import csv

TRAINING_FILE_NAME = sys.argv[1]
TEST_FILE_NAME = sys.argv[2]
POPULATION = int(sys.argv[3])

class Types:
    OPERATOR = 1
    CONSTANT = 2
    VARIABLE = 3

class Data():
    def __init__(self, filename):
        with open(filename, "r") as csvfile:
            csvinput = csv.reader(csvfile)
            self.details = list(csvinput)
    def get_value(self, row, col):
        return self.details[row][col]

class Node():
    def __init__(self, symbol, depth):
        self.symbol = symbol
        if (symbol == '+' or symbol == '*'):
            self.type = Types.OPERATOR
            self.branches = []
        elif('a' <= symbol and symbol <= 'h'):
            self.type = Types.VARIABLE
        else:
            self.type = Types.CONSTANT
        self.depth = depth
    def add_branches(self, symbol1, symbol2):
        self.branches.append(Node(symbol1, self.depth+1))
        self.branches.append(Node(symbol2, self.depth+1))

def generate_initial_population():
    ret = []
    for i in range(POPULATION):
        symbol = random.choice("abcdefgh+*")
    return ret

def main():
    if len(sys.argv) != 4:
        print("usage: python3 main.py <training file> <test file> <population size>")
        sys.exit()

    print(Types.OPERATOR)
    print("main")
    train_data = Data(TRAINING_FILE_NAME)

    # gera populacao inicial
    ppl = generate_initial_population()

if __name__ == '__main__':
    main()
