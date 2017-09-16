import sys
import random
import csv

TRAINING_FILE_NAME = sys.argv[1]
TEST_FILE_NAME = sys.argv[2]
POPULATION = int(sys.argv[3])

# classe Types -> guarda ints para representar o tipo do nó
class Types:
    OPERATOR = 1
    CONSTANT = 2
    VARIABLE = 3

# classe Data -> le os dados de um arquivo e os guarda na memória
class Data():
    # lê os valores no arquivo e os guarda
    def __init__(self, filename):
        with open(filename, "r") as csvfile:
            csvinput = csv.reader(csvfile)
            self.details = list(csvinput)

    # obtem o valor numérico de uma posição do arquivo
    def get_value(self, row, col):
        return int(self.details[row][col])

# classe Node -> representa os nós da árvore
class Node():
    # construtor: determina as variáveis iniciais do nó
    def __init__(self, symbol, depth):
        self.symbol = symbol
        if (symbol == '+' or symbol == '*'):
            self.type = Types.OPERATOR
            self.branches = []
        elif(type(symbol) is str):
            self.type = Types.VARIABLE
        else:
            self.type = Types.CONSTANT
        self.depth = depth

    # adiciona dois filhos ao nó da árvore
    def add_branches(self, symbol1, symbol2):
        self.branches.append(Node(symbol1, self.depth+1))
        self.branches.append(Node(symbol2, self.depth+1))

    # extende uma árvore recursivamente
    def extend(self):
        if self.type == Types.OPERATOR:
            if self.depth == 5:
                symbol1 = generate_symbol(False)
                symbol2 = generate_symbol(False)
            else:
                symbol1 = generate_symbol(True)
                symbol2 = generate_symbol(True)
            self.add_branches(symbol1, symbol2)
            for i in range(2):
                self.branches[i].extend()

    # encontra o resultado da funçao na árvore aplicada as variaveis
    def get_result(self, var_values):
        c_type = self.type
        c_value = self.value
        if c_type == Types.OPERATOR:
            if c_value == '+':
                return get_result(self.branches[0]) + get_result(self.branches[1])
            else:
                return get_result(self.branches[0]) * get_result(self.branches[1])
        elif c_type == Types.CONSTANT:
            return c_value
        else:
            return var_values[ord(c_value)-97]

# gera um símbolo aleatório
def generate_symbol(operators_allowed:bool):
    if operators_allowed:
        typ = random.choice([0, 1, 2])
        if typ == 0:
            return random.choice("abcdefgh")
        elif typ == 1:
            return random.uniform(-10.0, 10.0)
        else:
            return random.choice("+*")
    else:
        if random.choice([0, 1]) == 0:
            return random.choice("abcdefgh")
        else:
            return random.uniform(-10.0, 10.0)

# gera a população inicial de indivíduos
def generate_initial_population():
    ret = []
    for i in range(POPULATION):
        symbol = generate_symbol(True)
        ret.append(Node(symbol, 0))
        ret[i].extend()
    return ret

#####################################
### MAIN ############################
#####################################

def main():
    if len(sys.argv) != 4:
        print("usage: python3 main.py <training file> <test file> <population size>")
        sys.exit()

    print("main")
    train_data = Data(TRAINING_FILE_NAME)
    ppl = generate_initial_population()

    # loop de execução do GP

if __name__ == '__main__':
    main()
