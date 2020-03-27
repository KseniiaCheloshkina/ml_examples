import sys

class MergeSort(object):
    
    def __init__(self):
        self.n_inv = 0
    
    def merge(self, a, b):
        n_inv = 0
        n1, n2 = len(a), len(b)
        i1 = i2 = 0
        res = []
        while (i1 < n1) & (i2 < n2):
            if a[i1] <= b[i2]:
                res.append(a[i1])
                i1 += 1
            else:
                res.append(b[i2])
                n_inv += n1 - i1
                i2 += 1

        if n1 - i1 > 0:
            for i in range(i1, n1):
                res.append(a[i])
        if n2 - i2 > 0:
            for i in range(i2, n2):
                res.append(b[i])
        self.n_inv += n_inv
        return res
    
    def mergesort(self, a):
        if len(a) > 1:
            m = len(a) // 2
            return self.merge(self.mergesort(a[0:m]), self.mergesort(a[m:]))
        else:
            return a    

def main():
   # get input into convinient form 
    msg = sys.stdin.readlines()
    i = 0
    for item in msg:
        if i == 1:
            int_list = list(map(int, item.rstrip().split()))
        i = i + 1
    
    ms = MergeSort()
    ms.mergesort(int_list)
    print(ms.n_inv)    

if __name__ == "__main__":
    main()
    
