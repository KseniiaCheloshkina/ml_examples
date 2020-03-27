import sys

def CountSort(a, n):
    
    b = [0] * 11
    max_el = 0
    for el in a:
        b[el] += 1
        if el > max_el:
            max_el = el
    b = b[:max_el + 1]
    for j in range(1, max_el + 1):
        b[j] += b[j - 1]
    a1 = [0] * n
    for j in range(n - 1, -1, -1):
        a1[b[a[j]] - 1] = a[j]
        b[a[j]] -= 1
    return a1

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n = list(next(reader))[0]
    a = list(next(reader))
    sort_a = CountSort(a, n)
    print(" ".join(map(str, sort_a)))

def test():
    assert CountSort([], 0) == []
    assert CountSort([1], 1) == [1]
    assert CountSort([1, 1], 2) == [1, 1]
    assert CountSort([2, 3, 9, 2, 9], 5) == [2, 2, 3, 9, 9]

if __name__ == "__main__":
    main()

