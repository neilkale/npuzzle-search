def write_data(data,file):
    with open(file, 'w') as f:
        for item in data:
            f.write(str(item))
            f.write('\n')

