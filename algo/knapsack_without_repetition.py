def knapsack_without_repetition(W, n, w_list, c_list, return_max_cost=False):
    
    if return_max_cost:
        sum_arr = c_list
    else:
        sum_arr = w_list
        
    D = [[0] * (W + 1) for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            D[i][w] = D[i - 1][w]
            w_cur = w_list[i - 1]
            if w_cur <= w:
                D[i][w] = max(D[i][w], D[i - 1][w - w_cur] + sum_arr[i - 1])
    return D[n][W]
    
def main():
    W, n = map(int, input().split())
    w_list = list(map(int, input().split()))
    c_list = [1] * n
    print(knapsack_without_repetition(W, n, w_list, c_list))

def test():
    assert knapsack_without_repetition(W=10, n=3, w_list=[1, 4, 8], c_list=[0, 0, 0], return_max_cost=True) == 0
    assert knapsack_without_repetition(W=10, n=1, w_list=[20], c_list=[1], return_max_cost=True) == 0
    assert knapsack_without_repetition(W=10, n=3, w_list=[1, 4, 8], c_list=[1, 1, 1], return_max_cost=True) == 2
    
    assert knapsack_without_repetition(W=10, n=3, w_list=[1, 4, 8], c_list=[0, 0, 0], return_max_cost=False) == 9
    assert knapsack_without_repetition(W=10, n=1, w_list=[20], c_list=[1], return_max_cost=False) == 0
    assert knapsack_without_repetition(W=10, n=3, w_list=[1, 4, 8], c_list=[1, 1, 1], return_max_cost=False) == 9
    
if __name__ == "__main__":
    main()
    
