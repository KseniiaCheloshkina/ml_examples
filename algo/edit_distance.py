import sys
import numpy as np

def EditDistance(a, b):
    n = len(a)
    m = len(b)
    D = np.zeros((n + 1, m + 1))
    D[:, 0] = np.linspace(0, n, n + 1)
    D[0, :] = np.linspace(0, m, m + 1)
    for i in range(0, n):
        for j in range(0, m):
            c = 1 - int(a[i] == b[j])
            D[i + 1, j + 1] = min(D[i, j + 1] + 1, D[i + 1, j] + 1, D[i, j] + c)
    return int(D[-1, -1])

def main():
    reader = (line.rstrip() for line in sys.stdin)
    a = next(reader)
    b = next(reader)
    k = EditDistance(a, b)
    print(k)

def test():
    assert EditDistance('', '') == 0
    assert EditDistance('ab', 'ab') == 0
    assert EditDistance('ab', 'a') == 1
    assert EditDistance('short', 'ports') == 3
    
if __name__ == "__main__":
    main()