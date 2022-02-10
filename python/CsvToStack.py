import csv


class CsvToStack:
    def __init__(self, path):
        self.__path = path

    def read_scv(self):
        csv_stack = []
        file = open(self.__path, 'r')
        read = csv.reader(file)
        for line in read:
            csv_stack.append(line)

        return csv_stack
