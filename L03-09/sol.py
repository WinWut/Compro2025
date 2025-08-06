w, h = map(int, input("Grid Size: ").split())

grid = [[0 for _ in range(w)] for _ in range(h)]

n = int(input("Number of mine(s): "))

for i in range(n):
    x, y = map(int, input(f"Mine#{i+1}: ").split())
    grid[y][x] = 'X'

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                if grid[ny][nx] != 'X':
                    grid[ny][nx] += 1

for row in grid:
    print(' '.join(str(cell) for cell in row))