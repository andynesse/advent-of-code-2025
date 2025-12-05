def main():
    ranges = []
    fresh = 0
    with open("data.txt", mode="r") as f:
        line = f.readline().strip()
        while len(line) > 0:
            ranges.append([int(n) for n in line.split("-")])
            line = f.readline().strip()
        final_ranges = [ranges[0]]
        for r in ranges[1:]:
            edited = False
            for i, fr in enumerate(final_ranges):
                if (fr[0] <= r[0] <= fr[1] and r[1] > fr[1]) or (fr[0] <= r[1] <= fr[1] and r[0] < fr[0]) or (r[0] <= fr[0] and fr[1] <= r[1]):
                    final_ranges[i] = [min(r[0], fr[0]), max(r[1], fr[1])]
                    edited = True
            if not edited:
                final_ranges.append(r)
            else:
                while True:
                    edited = False
                    for i, r in enumerate(final_ranges):
                        for j, fr in enumerate(final_ranges):
                            if i == j:
                                continue
                            if (fr[0] <= r[0] <= fr[1] and r[1] > fr[1]) or (fr[0] <= r[1] <= fr[1] and r[0] < fr[0]) or (r[0] <= fr[0] and fr[1] <= r[1]):
                                final_ranges[i] = [min(r[0], fr[0]), max(r[1], fr[1])]
                                edited = True
                                final_ranges.pop(j)
                    if not edited:
                        break

        print(final_ranges, ranges[0])
        for r in final_ranges:
            fresh += r[1] - r[0] + 1
    print(fresh)
if __name__ == "__main__":
    main()