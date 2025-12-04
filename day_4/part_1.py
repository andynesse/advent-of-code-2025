def main():
    matrix = []
    with open("data.txt", mode="r") as f:
        for line in f:
            row = []
            line = line.strip()
            for char in line:
                if char == "@":
                    row.append(1)
                    continue
                row.append(0)
            matrix.append(row)
    tot_rolls = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                adjacent = 0
                for y in range(max(i-1, 0), min(i+2, len(matrix))):
                    for x in range(max(j-1, 0), min(j+2, len(matrix[0]))):
                        if y == i and x == j:
                            continue
                        if matrix[y][x] == 1:
                            adjacent += 1
                if adjacent < 4:
                    tot_rolls += 1
    print(tot_rolls)
    with open("test.txt", mode="w"):
        canvas = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    adjacent = 0
                    for y in range(max(i-1, 0), min(i+2, len(matrix))):
                        for x in range(max(j-1, 0), min(j+2, len(matrix[0]))):
                            if y == i and x == j:
                                continue
                            if matrix[y][x] == 1:
                                adjacent += 1
                    if adjacent < 4:
                        canvas += "x"
                        continue
                    canvas += "@"
                    continue
                canvas += "."

        

if __name__ == "__main__":
    main()