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
    def extend(self):
        if self.type == Types.OPERATOR:
            if self.depth == 5:
                symbol1 = random.choice("abcdefgh")
                symbol2 = random.choice("abcdefgh")
            else:
                symbol1 = random.choice("abcdefgh+*")
                symbol2 = random.choice("abcdefgh+*")
            self.add_branches(symbol1, symbol2)
            for i in range(2):
                self.branches[i].extend()

def generate_initial_population():
    ret = []
    for i in range(POPULATION):
        symbol = random.choice("abcdefgh+*")
        ret.append(Node(symbol, 0))
        ret[i].extend()
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

    # loop de execução do GP

if __name__ == '__main__':
    main()
