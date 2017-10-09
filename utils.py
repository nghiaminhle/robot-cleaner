from random import randint
def generate_map_random(cols, rows, barrier_no):
    maps = []
    for j in range(rows):
        r = []
        for i in range(cols):
            r.append(0)
        maps.append(r)
    for k in range(barrier_no):
        i = randint(0, rows - 1)
        j = randint(0, cols - 1)
        maps[i][j] = -1
    return maps

def generate_map_random_for_test(cols, rows, barrier_no):
    maps = []
    for j in range(rows):
        r = []
        for i in range(cols):
            r.append(1)
        maps.append(r)
    for k in range(barrier_no):
        i = randint(0, rows - 1)
        j = randint(0, cols - 1)
        maps[i][j] = -1
    for k in range(1):
        i = randint(0, rows - 1)
        j = randint(0, cols - 1)
        maps[i][j] = 0
    return maps

def print_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    steps = 0
    for i in range(rows):
        print(matrix[i])
        for j in range(cols):
            if matrix[i][j]>=0:
                steps += matrix[i][j]
    
    print('step number', steps)

def print_progress_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    positive_number = 0
    nagative_number = 0
    zero_number = 0
    steps = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]>0:
                positive_number += 1
                steps += matrix[i][j]
            if matrix[i][j]<0:
                nagative_number += 1
            if matrix[i][j]==0:
                zero_number += 1
    
    print('positive', positive_number, 'nagative', nagative_number,'zero', zero_number, 'step', steps)