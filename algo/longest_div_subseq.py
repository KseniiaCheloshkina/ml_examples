import sys

def DivSeq(a, n):
    
    k = 0
    d = [1] * n
    for i in range(n):
        for j in range(i):
            if (a[i] % a[j] == 0)  & (d[j] + 1 > d[i]):
                d[i] += 1
    ans = 0            
    for i in range(n):
        if d[i] > ans:
            ans = d[i]

    return ans

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n = list(next(reader))[0]
    a = list(next(reader))
    k = DivSeq(a, n)
    print(k)

def test():
    assert DivSeq([], 0) == 0
    assert DivSeq([1], 1) == 1
    assert DivSeq([1, 1], 2) == 1
    assert DivSeq([2, 3, 9, 2, 9], 5) == 2
    assert DivSeq([3, 6, 7, 12], 4) == 3

if __name__ == "__main__":
    main()

