import numpy as np
import random as rand

def osud(datum_narozeni):
    x = datum_narozeni.split(". ")
    den = x[0]
    den = split(den)
    mesic = x[1]
    mesic = split(mesic)
    rok = x[2]
    rok = split(rok)
    datum = den + mesic + rok

    for i in range(0, len(datum)): 
        datum[i] = int(datum[i]) 
    osudove_cislo = sum(datum) 
    if osudove_cislo == 11 or osudove_cislo == 22:
        return osudove_cislo
    else:
        res = split(str(osudove_cislo))
        for i in range(0, len(res)): 
            res[i] = int(res[i]) 
        res = sum(res)
        return  res

def split(word): 
    return [char for char in word]

def rozdilMatic(N):
    matrix = np.zeros((N,N), int)
    rnd = np.random.choice(matrix.size, rand.randint(0, N*N), replace=False)
    matrix.ravel()[rnd] = 1
    #print(matrix)

    l_matrix = matrix[:, 0::2]
    s_matrix = matrix[:, 1::2]

    res = l_matrix==s_matrix
    percent =100 - (np.sum(res))/(len(res)*(len(res[0])))*100
    print("Rozdil: ",percent, "%")

    return matrix

def spirala(N):
    matrix = np.zeros((N,N), int)
    center_x = N//2
    center_y = N//2
    direction = 1
    counter = 1
    while counter != 5:
        matrix[center_y,center_x] = counter
        center_y = center_y-1
        matrix = np.rot90(matrix)
        counter = counter + 1

    return matrix

if __name__ == "__main__":
    print("Osudové číslo:")
    print(osud("4. 1. 1997"))
    print("Rozdil matic:")
    print(rozdilMatic(4))
    print("Spirala: ")
    print(spirala(5))
