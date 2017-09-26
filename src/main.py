import sys
import random
import csv
import copy
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

#####################################
### NODE (INDIVIDUO) ################
#####################################

class Node():
    # construtor: determina as variáveis iniciais do nó
    def __init__(self, symbol, depth):
        self.symbol = symbol
        if (symbol == '+' or symbol == '*' or symbol == '/'):
            self.type = Types.OPERATOR
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
            self.branches = []
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
                return safe_division(self.branches[0].get_result(var_values), self.branches[1].get_result(var_values))
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

    def set_fitness(self, data_source):
        self.fitness = self.get_fitness(data_source)

    def choose_random_leaf(self):
        if self.type == Types.OPERATOR:
            return self.branches[random.choice([0, 1])]
        else:
            return self

    def choose_random_node(self):
        if self.type == Types.OPERATOR:
            if random.choice([0, 1]) == 0:
                return self.branches[random.choice([0, 1])]
            else:
                return self
        else:
            return self

    def mutate(self):
        node = self.choose_random_node()
        node.symbol == generate_symbol(True)
        if (node.symbol == '+' or node.symbol == '*' or node.symbol == '/'):
            node.type = Types.OPERATOR
        elif(type(node.symbol) is str):
            node.type = Types.VARIABLE
        else:
            node.type = Types.CONSTANT
        node.extend()

    def print_node(self):
        print(self.symbol)
        if self.type == Types.OPERATOR:
            self.branches[0].print_node()
            self.branches[1].print_node()
            
#####################################
### GERACAO ALEATORIA DE INDIVIDUOS #
#####################################

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

def generate_initial_population(data_source):
    ret = []
    for i in range(POPULATION):
        symbol = random.choice("+*/")
        ret.append(Node(symbol, 0))
        ret[i].extend()
        ret[i].set_fitness(data_source)
    return ret

#####################################
### MÉTODOS DO GP ###################
#####################################

def tournament(sample):
    best = Node(0, 0)
    best_fitness = sys.maxsize
    for it in sample:
        current = it.fitness
        if current < best_fitness:
            best_fitness = current
            best = it
    return best

def crossover(parent1, parent2, data_source):
    ret = []
    if random.uniform(0.0, 1.0) <= PROB_CROSSOVER:
        desc1 = copy.deepcopy(parent1)
        desc2 = copy.deepcopy(parent2)
        leaf1 = desc1.choose_random_leaf()
        leaf2 = desc2.choose_random_leaf()
        leaf1, leaf2 = leaf2, leaf1
        if random.uniform(0.0, 1.0) <= PROB_MUTATION:
            leaf1.mutate()
        if random.uniform(0.0, 1.0) <= PROB_MUTATION:
            leaf2.mutate()
        desc1.set_fitness(data_source)
        desc2.set_fitness(data_source)
        ret.append(desc1)
        ret.append(desc2)
    return ret

#####################################
### MAIN ############################
#####################################

def main():
    if len(sys.argv) < 8:
        print("Erro: sem argumentos para os parametros")
        sys.exit()

    train_data = Data(TRAINING_FILE_NAME)
    test_data = Data(TEST_FILE_NAME)
    for i in range(len(train_data.get_line(0))-1):
        variables.append(chr(i+97))
    ppl = generate_initial_population(train_data)

    for count in range(GENERATIONS):
        new_ppl = []
        accum = 0
        best = sys.maxsize
        best_node = Node(0, 0)
        worst = 0

        for it in ppl:
            accum += it.fitness
            if it.fitness < best:
                best = it.fitness
                best_node = it
            if it.fitness > worst:
                worst = it.fitness

        new_ppl.append(best_node)
        print(count)
        print(best)
        print(worst)
        print(accum/len(ppl))

        while len(new_ppl) < POPULATION:
            parent1 = tournament(random.sample(ppl, TOURNAMENT))
            parent2 = tournament(random.sample(ppl, TOURNAMENT))
            new_ppl.extend(crossover(parent1, parent2, train_data))

        ppl = new_ppl

    best = sys.maxsize
    worst = 0
    for it in ppl:
        fitness = it.get_fitness(test_data)
        if fitness < best:
            best = fitness
        if fitness > worst:
            worst = it.fitness
    return best

if __name__ == '__main__':
    data = []
    average = 0
    for i in range(30):
        experiment = main()
        data.append(experiment)
        average += experiment
    average /= 30
    print("final")
    print(average)
