from collections import defaultdict
grid = list(map(lambda x: list(x.strip()), open("advent-of-code-2025\day_7\data.txt").readlines()))

def main(grid):
    points = {(0,i):1 for i in range(len(grid[0])) if grid[0][i] == 'S'}
    line = 0
    while line < len(grid)-1:
        new_points = defaultdict(lambda: 0)
        for ((i,j), cnt) in points.items():
            if not in_range_grid(grid, i+1, j):
                continue
            if grid[i+1][j] == '^':
                new_points[(i+1,j-1)] += cnt
                new_points[(i+1,j+1)] += cnt
            else:
                new_points[(i+1,j)] += cnt
        points = new_points
        line += 1
    print(sum(points.values()))

def in_range_grid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

if __name__ == "__main__":
    main(grid)
