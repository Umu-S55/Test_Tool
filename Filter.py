#! python3
#  Filter.py


import os

FILTER_WORD = 'XXX'
START_LINE = 0

if __name__ == "__main__":
    path = os.listdir()
    with open('log.txt', 'w') as t:
        for row in path:
            t.write(row + '\n')
            with open('' + row, 'r') as f:
                row_line = f.readlines()
                for line in row_line:
                    if FILTER_WORD in line:
                        t.write(line[START_LINE:])
