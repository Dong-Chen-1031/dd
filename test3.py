import itertools
list_,list_1,list_2,aw=sorted([int(i) for i in input().split()]),[],[],[]
add=bigs=sum(list_)/2
# print(bigs)

for i in list(itertools.permutations(list_,3)):
    if abs(sum(i)-add) == bigs:
        aw.append(i)
    if abs(sum(i)-add) < bigs:
        aw=[i]
        bigs=abs(sum(i)-add)
# print(bigs)
aw2=[]
for a,b,c in aw:
    if not([a,b,c]  in aw2 ) and not([a,c,b]  in aw2 ) and not([b,a,c]  in aw2 ) and not([b,c,a]  in aw2 ) and not([c,a,b]  in aw2 ) and not([c,b,a]  in aw2 ):
        aw2.append([a,b,c])
# print(aw2)
aw3=[]
for i in aw2:
    _=list(set(list_).difference(set(i)))
    if not([_,i] in aw3):
        aw3.append([i,_])
        print(f"({','.join(map(str,i))})-({','.join(map(str,_))})")
