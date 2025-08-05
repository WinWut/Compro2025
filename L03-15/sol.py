gridsize=str(input("Grid Size: "))
nmine=int(input(""))
minecoord=[]
for i in range(nmine):
    mine=str(input(f"Mine#{i+1}: "))
    minetup=[int(x) for x in mine.split()]
    
    minecoord.append(tuple(minetup))

for i in range(int(gridsize[-1])):
    for j in range(int(gridsize[0])):
        print(i,j)