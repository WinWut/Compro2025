luckynum=str(input("Enter lucky number : "))
candidaten=str(input("Enter amount of candidates : "))

id_list=[]

for i in range(1,int(candidaten)+1):
    idcard=str(input(f"Enter ID card number {i}: "))
    id_list.append(idcard)

c=[x.count(luckynum) for x in id_list]
maxC=sorted(c)[-1]

d= dict()

for i in range(len(id_list)):
    d[id_list[i]]=c[i]

maxId=0
for i in d:
    if d[i]==maxC:
        if int(i)>maxId:
            maxId=int(i)

print(f"Winner: {maxId}")






        

    

