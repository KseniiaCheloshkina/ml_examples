from collections import Counter

def update_codes(codes, val, list_upd_keys):
    for k in list_upd_keys:
        if k not in codes:
            codes.update({k: val})
        else:            
            codes.update({k: val + codes[k]})
    return codes

def get_encode(input_str):
    
    # get frequences
    c = Counter()
    for v in input_str.rstrip():
        c[v] += 1
    c_most_com = c.most_common()
    ordered_freq_keys, ordered_freq_values = map(list, zip(*c_most_com))
    k_output = len(ordered_freq_keys)
        
    # build a tree, save frequences and set codes
    codes = {}
    for n_iter in range(2 ** k_output):
        # take first min freq
        k1 = ordered_freq_keys.pop()
        v1 = ordered_freq_values.pop()
        codes = update_codes(codes, '0', list(k1))
        if len(ordered_freq_values) > 0:
            k2 = ordered_freq_keys.pop()
            v2 = ordered_freq_values.pop()        
            codes = update_codes(codes, '1', list(k2))
            # insert new node
            k1, v1 = k1 + k2, v1 + v2
            i = 0
            if len(ordered_freq_values) > 0:
                while ordered_freq_values[i] > v1:
                    i = i + 1
                    if i == len(ordered_freq_values):
                        break

            ordered_freq_keys.insert(i, k1)
            ordered_freq_values.insert(i, v1)
            if len(ordered_freq_values) == 1:
                break
        else:
            break
    # output
    output = "".join([codes[k] for k in input_str.rstrip()])
    l = len(output)

    return k_output, l, codes, output
    
def main():
    input_str = input()
    # run function to get huffman codes
    k, l, codes, output = get_encode(input_str)
    print(k)
    print(l)
    for k, v in codes.items():
        print(k + ': ' + str(v))
    print(output)

if __name__ == "__main__":
    main()
