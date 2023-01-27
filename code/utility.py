import pandas as pd

def write_data(data,file):
    with open(file, 'w') as f:
        for item in data:
            f.write(str(item))
            f.write('\n')


def read_data_csv(file):
    df = pd.read_csv(file, sep=',', header=None)
    df = df.values
    board_dims = [len(df), len(df[0])] #height, width
    board = []

    for i, row in enumerate(df):
        for j, col in enumerate(row):
            if isinstance(col, str):
                try:
                    df[i][j] = int(col)
                    board.append(df[i][j])
                except:
                    board.append(0)
                    continue
            else:
                board.append(col)
    return board, board_dims