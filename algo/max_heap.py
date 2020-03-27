import sys

class Heap(object):
    
    def __init__(self):
        # dict (index of node: value)
        self.h = {}
    
    def extract_max(self):

        output = self.h[1]
        
        if len(self.h) == 1:
            self.h = {}
        else:
            # insert at root last and check consistency (SiftDown)
            i = len(self.h)
            self.h[1] = self.h[i]
            self.h.pop(i)

            cur_ind = 1
            val = self.h[cur_ind]
            childs_ind = [ch for ch in [cur_ind * 2, cur_ind * 2 + 1] if ch in self.h]
            while len(childs_ind) > 0:   
                if len(childs_ind) == 1:
                    child_ind = childs_ind[0]
                else:
                    child_ind = childs_ind[0] if self.h[childs_ind[0]] > self.h[childs_ind[1]] else childs_ind[1]
                child_val = self.h[child_ind]
                if val < child_val:
                    self.h[child_ind] = val
                    self.h[cur_ind] = child_val
                    cur_ind = child_ind
                    childs_ind = [ch for ch in [cur_ind * 2, cur_ind * 2 + 1] if ch in self.h]
                else:
                    break       
        return output
    
    def insert(self, val):
        
        i = len(self.h)
        cur_ind = i + 1
        self.h[cur_ind] = val
        
        # check consistency with parent (SiftUp)
        while cur_ind > 1:
            par_ind = cur_ind // 2
            par_val = self.h[par_ind]
            if val > par_val:
                self.h[par_ind] = val
                self.h[cur_ind] = par_val
                cur_ind = par_ind
            else:
                break

    def evaluate(self, commands_list):
        for com in commands_list:
            if com.startswith('Insert'):
                val = int(com.rstrip().split()[1])
                self.insert(val)
                
            else:
                output = self.extract_max()
                print(output)


def main():
   # get input into convinient form 
    msg = sys.stdin.readlines()
    commands_list = []
    i = 0
    for item in msg:
        if i > 0:
            commands_list.append(item)
        i = i + 1

    # run function
    Heap().evaluate(commands_list)

if __name__ == "__main__":
    main()
