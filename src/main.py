import sys
import random
import csv

class Data():
    def __init__(self, filename):
        with open(filename, "r") as csvfile:
            csvinput = csv.reader(csvfile)
            self.details = list(csvinput)
    def get_value(self, row, col):
        return self.details[row][col]

def main():
    if len(sys.argv) != 2:
        print("usage: python main.py <csv test file>")
        sys.exit()

    print("main")
    train_data = Data(sys.argv[1])

if __name__ == '__main__':
    main()
