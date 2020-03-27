import sys

def binary_search(arr, n, a):
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == a:
            return m + 1
        elif arr[m] > a:
            r = m - 1
        else:
            l = m + 1
    return -1

def main():
   # get input into convinient form 
    msg = sys.stdin.readlines()
    i = 0
    for item in msg:
        if i == 0:
            array_list = list(map(int, item.rstrip().split()))[1:]
        else:
            int_list = list(map(int, item.rstrip().split()))[1:]
        i = i + 1
    
    output_str = ''
    for val in int_list:
        n = len(array_list)
        output_str += ' ' + str(binary_search(array_list, n, val))
    print(output_str)    

if __name__ == "__main__":
    main()
    
