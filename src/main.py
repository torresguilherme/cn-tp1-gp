import sys
import random
import csv

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
    def __init__(self, symbol):
        self.symbol = symbol
        if (symbol == '+' or symbol == '-'):
            self.type = Types.OPERATOR
            self.branches = []
        elif('a' <= symbol and symbol <= 'h'):
            self.type = Types.VARIABLE
        else:
            self.type = Types.CONSTANT
    def add_branches(self, symbol1, symbol2):
        self.branches.append(Node(symbol1))
        self.branches.append(Node(symbol2))

def generate_initial_population():
    ret = []
    # gerar populacao inicial aleatoriamente
    return ret

def main():
    if len(sys.argv) != 2:
        print("usage: python3 main.py <csv test file>")
        sys.exit()

    print(Types.OPERATOR)
    print("main")
    train_data = Data(sys.argv[1])

    # gera populacao inicial
    ppl = generate_initial_population()

if __name__ == '__main__':
    main()
