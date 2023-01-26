import pandas as pd
import numpy as np 

def write_data(data,file):
    with open(file, 'w') as f:
        for item in data:
            f.write(str(item))
            f.write('\n')


def read_data_csv(file):
    board = pd.read_csv(file, sep=',', header=None)
    board = board.values

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if isinstance(col, str):
                try:
                    board[i][j] = int(col)
                except:
                    continue

    return board