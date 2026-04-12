##inp = "21"
##N = len(inp)

inp = int(input())
for i in range(0,inp,1):
    inp2 = input()
    x = list(map(int,input().split()))
    majority= []

    for i in range(0,len(x)-1,1):
        if x[i] == x[i+1]:
            majority.append(x[i])
        elif len(x)>= 3 and i < len(x)-2:
            if x[i] == x[i+2]:
                majority.append(x[i])

    if len(majority) == 0:
        print("-1")
    else:
        lst = list(set(majority))
        lst.sort()
        for i in range(0,len(lst),1):
            if i == len(lst)-1:
                print(lst[i])
            else:
                print(lst[i],end=" ")

        
        
    
        
    
