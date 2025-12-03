def main():
    total_joltage = 0
    with open("battery_banks.txt", mode="r") as file:
        for line in file:
            line = line.strip()
            batteries = []
            for num_char in line:
                num = int(num_char)
                if len(batteries) < 12:
                    batteries.append(num)
                    continue
                compare_swap = False
                for i in range(1, len(batteries)):
                    curr = batteries[i]
                    prev = batteries[i-1]
                    if curr > prev:
                        compare_swap = True
                        batteries.pop(i-1)
                        batteries.append(num)
                        break
                if not compare_swap:
                    min_num = min(batteries)
                    if num > min_num:
                        batteries.remove(min_num)
                        batteries.append(num)
            print(line, batteries)
            total_joltage += int("".join([str(b) for b in batteries]))

    print(total_joltage)


    
if __name__ == "__main__":
    main()