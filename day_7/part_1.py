def main():
    res = 0
    with open("advent-of-code-2025\day_7\data.txt", mode="r") as file:
        line = file.readline()
        rays = set()
        rays.add(line.index("S"))
        for line in file:
            start = 0
            next_rays = rays.copy()
            while True:
                splitter = line.find("^", start)
                if splitter == -1:
                    break
                if splitter in rays:
                    next_rays.add(splitter-1)
                    next_rays.add(splitter+1)
                    next_rays.remove(splitter)
                    res += 1
                start = splitter + 1
            rays = next_rays
    print(res)
            


if __name__ == "__main__":
    main()