def main():
    data = []
    with open("data.txt", mode="r") as f:
        res = 0
        for line in f:
            data.append(line)
        
        nums = ["" for i in range(4)]
        operator = ""
        for i in range(len(data[0])):
            col = ""
            if operator == "":
                operator = data[-1][i]
            for j in range(len(data)-1):
                col += data[j][i]
            if col.strip() == "":
                if operator == "+":
                    res += sum([int(n) for n in nums if not n == ""])
                else:
                    mr = 1
                    for num in nums:
                        if num == "":
                            continue
                        mr *= int(num)
                    res += mr
                nums = ["" for i in range(4)]
                operator = ""
                continue
            nums[i%4] = col
        print(res)




if __name__ == "__main__":
    main()