def main():
    counter = 50
    password = 0
    with open('rotations.txt', mode='r') as file:
        for line in file:
            line = line.strip()
            rotation_value = int(line[1:])
            if line[0] == 'L':
                while rotation_value > 0:
                    counter -= 1
                    rotation_value -= 1
                    if counter < 0:
                        counter = 99
                    if counter == 0:
                        password += 1
            if line[0] == 'R':
                while rotation_value > 0:
                    counter += 1
                    rotation_value -= 1
                    if counter > 99:
                        counter = 0
                    if counter == 0:
                        password += 1

    print(password)
if __name__ == "__main__":
    main()
