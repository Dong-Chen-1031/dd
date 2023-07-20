from itertools import permutations,combinations

O = 10,5

P = 11,10
Q = 4,6
R = 13,3
S = 6,2

A,B,C,D = 0,0,0,0
for T in [P,Q,R,S]:
    x,y = T[0],T[1]
    if x%2==1:
        if (x+y)%4==1 or (x+y)%4==2:
            A = T
        else:
            C = T
    else:
        if (x+y)%4==1 or (x+y)%4==2:
            B = T
        else:
            D = T
            
print("A={}, B={}, C={}, D={}".format(A,B,C,D))

if 0 not in [A,B,C,D]:
    
    def Dt(A,B):
        x,y = abs(A[0]-B[0]),abs(A[1]-B[1])
        if x>=y:
            dt = x+y
        else:
            if (x+y)%2==0:
                dt = 2*y
            else:
                if A[1]<B[1] and (A[0]+A[1])%2==1:
                    dt = 2*y+1
                elif A[1]>B[1] and (A[0]+A[1])%2==0:
                    dt = 2*y+1
                else:
                    dt = 2*y-1
        return dt

    vars = vars()
    L = list(combinations("OABCD",2)) #所有線段組合
    for i in range(len(L)):
        vars[L[i][0]+L[i][1]]=Dt(vars[L[i][0]],vars[L[i][1]])
        vars[L[i][1]+L[i][0]]=Dt(vars[L[i][0]],vars[L[i][1]])
        print(L[i][0]+L[i][1],"=",vars[L[i][0]+L[i][1]])   #顯示各點間距離

    M = list(permutations("ABCD"))  #所有路徑組合
    for i in range(len(M)):
        M[i]="O"+M[i][0]+M[i][1]+M[i][2]+M[i][3]

    N = []
    for i in range(len(M)): #各路徑對應長度
        N.append(0)
        for j in range(4):
            N[i]=N[i]+vars[M[i][j:j+2]]
        #print(M[i],"=",N[i])   #顯示各路徑長度

    s = min(N)  #最短路徑長
    for i in range(len(N)):
        if N[i]==s:
            print("最短路徑：{}→{}→{}→{}→{}，長度：{}。"
                  .format(M[i][0],M[i][1],M[i][2],M[i][3],M[i][4],s))

else:
    print("無解")