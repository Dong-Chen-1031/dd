temp = input('').split()
k,q,r,str_,list_,ok_list = int(temp[0]),int(temp[1]),int(temp[2]),input(''),[],[]
for i in range(q):list_.append(input('').split())
for i in list_:
    str_temp=[None]*k
    for ind,n in enumerate(i): str_temp[int(n)-1]=list(str_)[ind]
    str_=''
    for i in str_temp:str_+=i
    ok_list.append(str_)
for i in range(r):
    for n in ok_list:print(n[i],end='')
    print()