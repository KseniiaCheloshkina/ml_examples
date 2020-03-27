import sys

def get_decode(output_code, codes):
    
    output_code = output_code.replace('\n', '')
    decode = ''
    i = 1
    cur_code = output_code[0]
    while i < len(output_code):
        if cur_code in codes:
            decode += codes[cur_code]
            cur_code = output_code[i]
        else:
            cur_code += output_code[i]
        i += 1 
    if len(cur_code) > 0:
        decode += codes[cur_code]
    return decode
    
def main():
   # get input into convinient form 
    msg = sys.stdin.readlines()
    int_list = []
    i = 0
    k = 0
    codes = {}
    for item in msg:
        if i == 0:
            k, l = map(int, item.rstrip().split())
        elif (i > 0) & (i < k + 1):
            s, c = item.rstrip().split(":")
            codes.update({c.lstrip(): s})
        else:
            code_output = item
        i = i + 1
    
    decode = get_decode(code_output, codes)
    print(decode)

if __name__ == "__main__":
    main()

