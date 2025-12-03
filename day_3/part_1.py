def main():
    total_joltage = 0
    with open("battery_banks.txt", mode="r") as file:
        for line in file:
            line = line.strip()
            first, second = 0, 0
            for i, num_char in enumerate(line):
                num = int(num_char)
                if num > first and i != len(line) - 1:
                    first = num
                    second = 0
                elif num > second:
                    second = num
            print(line, first * 10 + second)
            total_joltage += first * 10 + second
    print(total_joltage)


    
if __name__ == "__main__":
    main()