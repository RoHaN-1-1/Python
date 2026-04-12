##inp = int(input())
##for i in range(0,inp,1):
##    N = int(input())
##    S = str(input())



def check(s):
    if s[:len(s)//2] == s[len(s)//2:]:
        return True
    return False


def remove(a,b):
    if (a == "COW" and b == "OWC") or (a == "OWC" and b == "COW"):
        return "C"
    elif (a == "COW" and b == "WCO") or (a == "WCO" and b == "COW"):
        return "W"
    elif (a == "OWC" and b == "WCO") or (a == "WCO" and b == "OWC"):
        return "O"

t,k = list(map(int,input().split()))
for _ in range(t):
    n = int(input())
    s = input()
    if n%2 == 1:
        print(-1)
        continue
    elif check(s) == True:
        print(1)
        print(" ".join(["1"]*len(s)))
        continue
    anslist = [0]*len(s)
    for i in range(n//2):
        a=s[i*3:i*3+3]
        b=s[(i+n//2)*3:(i+n//2)*3+3]
        drop = remove(a,b)
        for j in range(3):
            if a[j] == drop:
                anslist[i*3+j] = 1
            else:
                anslist[i*3+j] = 2
        for j in range(3):
            if b[j] == drop:
                anslist[(i+n//2)*3+j] = 1
            else:
                anslist[(i+n//2)*3+j] = 2
    print(2)
    print(" ".join(map(str,anslist)))

        # if a!=b:
        #     if a[:2]==b[1]:
        #         ans[i*3+2]=ans[(i+n//2)*3]=2
        #     else:
        #         ans[i*3]=ans[(i+n//2)*3+2]=2
        # print(max(ans))
        # for i in range(n*3):
        #     print(ans[i],end=" \n"[i==3*n-1])



        
    
# if len(S) % 2 == 1:
#     print("-1")
# elif len(S) % 2 == 0:
#     half1 = S[:len(S)//2]
#     half2 = S[len(S)//2:]
#     if half1 == half2:
#         print("1")
#         ans = "1 " * len(S)
#         ans = ans.strip()
#         print(ans)
# else:
    
