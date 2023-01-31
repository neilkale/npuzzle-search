import numpy as np

def generate_npuzzle(n):
  num_blanks = int(round(n*n*0.2))
  possible_values = [0]*num_blanks + list(range(1, (n*n - num_blanks) + 1))
  np.random.shuffle(possible_values)
  npuzzle = np.array(possible_values).reshape(n,n)
  return npuzzle

print(generate_npuzzle(4))
