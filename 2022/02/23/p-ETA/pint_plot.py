import ipdb
from bitstring import BitArray
import matplotlib.pyplot as plt
import numpy as np

def toINT(code):
    code = '0b' + code
    bc = BitArray(code)
    return bc.int 


def binary_list(n):
    return ['{:0{}b}'.format(i, n) for i in range(2**n)]

def de(HB):
    if HB[0] == '0':
        for b in HB:
            if b != '0':
                return False
    elif HB[0] == '1':
        for b in HB:
            if b != '1':
                return False
    return True

def PINT_decode(code, k, d):
    flag = code[0]
    SignedINT = code[1:]
    HB = code[1:-d]
    LB = code[-d-1:]
    if flag == '1':
        return toINT(SignedINT) * (2 ** d)
    elif de(HB):
        return toINT(LB)
    else:
        return toINT(SignedINT) * (2 ** (k-2))

def plot_PINT():
    code_list = binary_list(8)
    value_list = []
    for code in code_list:
        value = PINT_decode(code, 8, 3)
        print(code, value)
        value_list.append(value)

    x = [i for i in range(256)]
    y = value_list
    y.sort()
    resolution = [(y[i+1] - y[i])* 10 for i in range(len(y) - 1)]
    resolution.append(resolution[-1])

    plt.figure(figsize=(8, 4))
    plt.scatter(x, y, s=0.5)
    plt.scatter(x, resolution, s=2)
    plt.savefig("PINT_curve.png")
    plt.show()
    

if __name__ == '__main__':
    print('test')
    plot_PINT()