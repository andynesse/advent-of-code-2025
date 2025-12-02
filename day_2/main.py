def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def main():
    inv_ids = []
    with open("ids.txt", "r") as file:
        ids = file.read().strip().split(",")
        for id_range in ids:
            start, stop = [int(id) for id in id_range.split("-")]
            for i in range(start, stop+1):
                id_str = str(i)
                if id_str[0] == "0":
                    inv_ids.append(i)
                    continue
                len_factors = find_factors(len(id_str))[:-1]
                valid = True
                for factor in len_factors:
                    section = id_str[:factor]
                    for j in range(factor, len(id_str), factor):
                        if id_str[j:j+factor] != section:
                            break
                        if j + factor >= len(id_str):
                            valid = False
                    if not valid:
                        inv_ids.append(i)
                        break

    print(sum(inv_ids))
if __name__ == "__main__":
    main()
