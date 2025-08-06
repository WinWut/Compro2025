gridsize=str(input("Grid Size: "))
nmine=int(input("Number of mine(s): "))
grid=[]
for row in range(int(gridsize[-1])):
    temp=[]
    for col in range(int(gridsize[0])):
        temp.append(0)
    grid.append(temp)
    
for i in range(nmine):
    column,row=map(int,input(f"Mine#{i}: ").split())
    grid[row][column]='X'
    
    for dy in [-1,0,1]:
        for dx in[-1,0,1]:
            ny=row+dy
            nx=column+dx
            if 0<=ny<int(gridsize[0]) and 0<=nx<int(gridsize[-1]):
                if grid[ny][nx]!='X':
                    grid[ny][nx]+=1

for i in grid:
    print(" ".join(str(x) for x in i ))
        