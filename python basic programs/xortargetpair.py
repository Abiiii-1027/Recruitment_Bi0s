def get_list():
        arr = list(map(int,input().split()))
        return arr 
def target_pair():
        T = int(input())
        L = get_list()
        found = False
        for i in range(0,len(L)):
                for j in range(i+1,len(L)):
                        if L[i] ^ L[j] == T:
                                values = L[i], L[j]
                                found = True
        if found == True:
            print("The target pair is:", values)
        elif found == False:
            print("Not found")
                            
                        
target_pair()

