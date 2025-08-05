filename=str(input("File name: "))
scores=open(filename).read().splitlines()

scores_list=[i.split() for i in scores]
students={}
for i in scores_list:#
    students[i[0]]=[int(x) for x in i[1:]]

for i in students:# remove min and max
    maxn=-9999999
    minn=99999999
    for j in students[i]:
        if j>maxn:
            maxn=j
        if j<minn:
            minn=j
        
    for k in students[i]:
        if k==maxn:
            students[i].remove(maxn)
        if k==minn:
            students[i].remove(minn)
            
# sum each person   
result={}
for i in students:
    sumn=0

    for j in students[i]:
        sumn+=j
        
    result[i]=sumn
    
maxn=-999999
for i in result:
    if result[i]>maxn:
        maxn=result[i]
        
final=[]
for i in result:
    if result[i]==maxn:
        final.append(i)
print(maxn)
for i in final:
    print(i)
