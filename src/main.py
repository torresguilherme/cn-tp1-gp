import sys
import random
import csv
from math import sqrt

TRAINING_FILE_NAME = sys.argv[1]
TEST_FILE_NAME = sys.argv[2]
POPULATION = int(sys.argv[3])
GENERATIONS = int(sys.argv[4])
PROB_CROSSOVER = float(sys.argv[5])
PROB_MUTATION = float(sys.argv[6])
TOURNAMENT = int(sys.argv[7])
variables = []

def safe_division(val1, val2):
    try:
        return val1 / val2
    except:
        return 0.0

# classe Types -> guarda ints para representar o tipo do nó
class Types:
    OPERATOR = 1
    CONSTANT = 2
    VARIABLE = 3

# classe Data -> le os dados de um arquivo e os guarda na memória
class Data():
    def __init__(self, filename):
        with open(filename, "r") as csvfile:
            csvinput = csv.reader(csvfile)
            self.details = list(csvinput)

    def get_line(self, row):
        return self.details[row]

    def get_details(self):
        return self.details

    def get_lenght(self):
        return len(self.details)

# classe Node -> representa os nós da árvore
class Node():
    # construtor: determina as variáveis iniciais do nó
    def __init__(self, symbol, depth):
        self.symbol = symbol
        if (symbol == '+' or symbol == '*' or symbol == '/'):
            self.type = Types.OPERATOR
            self.branches = []
        elif(type(symbol) is str):
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
                symbol1 = generate_symbol(False)
                symbol2 = generate_symbol(False)
            else:
                symbol1 = generate_symbol(True)
                symbol2 = generate_symbol(True)
            self.add_branches(symbol1, symbol2)
            for i in range(2):
                self.branches[i].extend()

    def get_result(self, var_values):
        c_type = self.type
        c_value = self.symbol
        if c_type == Types.OPERATOR:
            if c_value == '+':
                return self.branches[0].get_result(var_values) + self.branches[1].get_result(var_values)
            elif c_value == '*':
                return self.branches[0].get_result(var_values) * self.branches[1].get_result(var_values)
            else:
                return safe_division(self.branches[0].get_result(var_values), self.branches[0].get_result(var_values))
        elif c_type == Types.CONSTANT:
            return c_value
        else:
            return float(var_values[ord(c_value)-97])

    def get_fitness(self, data_source):
        data = data_source.get_details()
        accum = 0
        for it in data:
            accum += pow(self.get_result(it) - float(it[len(it)-1]), 2)
        accum = sqrt(accum/len(data))
        return accum

    def print_node(self):
        print(self.symbol)
        if self.type == Types.OPERATOR:
            self.branches[0].print_node()
            self.branches[1].print_node()
            
# gera um símbolo aleatório
def generate_symbol(operators_allowed:bool):
    if operators_allowed:
        typ = random.choice([0, 1, 2, 3])
        if typ == 0:
            return random.choice(variables)
        elif typ == 1:
            return random.uniform(-10.0, 10.0)
        else:
            return random.choice("+*/")
    else:
        if random.choice([0, 1]) == 0:
            return random.choice(variables)
        else:
            return random.uniform(-10.0, 10.0)

# gera a população inicial de indivíduos
def generate_initial_population():
    ret = []
    for i in range(POPULATION):
        symbol = random.choice("+*/")
        ret.append(Node(symbol, 0))
        ret[i].extend()
    return ret

#####################################
### MÉTODOS DO GP ###################
#####################################

# TO DO:
# torneio: parametro = sys.argv[7] indivíduos aleatórios, retorna o que tem a fitness mais alta
# cruzamento: faz dois torneiros, seleciona os pais, se der dentro da probabilidade de cruzamento, gera 2 filhos
# ESTRATÉGIA MAIS SIMPLES: troca duas folhas
# aplica a probabilidade de mutação aos filhos
# MUTAÇÂO: escolhe um ponto aleatório da árvore, deleta os branches a partir dele e re-extende a árvore até o final

#####################################
### MAIN ############################
#####################################
def main():
    if len(sys.argv) != 8:
        sys.exit()

    print("main")
    train_data = Data(TRAINING_FILE_NAME)
    for i in range(len(train_data.get_line(0))-1):
        variables.append(chr(i+97))
    ppl = generate_initial_population()

    #teste = Node('+', 0)
    #teste.add_branches('*', '+')
    #teste.branches[0].add_branches('d', 'g')
    #teste.branches[1].add_branches('c', 'e')
    #ppl[0].print_node()
    print(ppl[0].get_fitness(train_data))

    # loop de execução do GP:
# - faz a seleção até gerar $tamanho_da_população filhos
# ordena
# imprime a fitness do melhor indivíduo, do pior e tira a média

if __name__ == '__main__':
    main()
