from itertools import combinations
class Diagram:
    def __init__(self, ind_l, buttons, joltage):
        self.ind_l = ind_l
        self.buttons = buttons
        self.joltage = joltage
def main():
    diagrams = []
    with open("advent-of-code-2025/day_10/data.txt", mode="r") as file:
        for line in file:
            parts = line.strip().split()
            ind_l = parts[0].replace("[", "").replace("]", "")
            buttons = [tuple([int(n) for n in b.replace("(", "").replace(")", "").split(",")]) for b in parts[1:-1]]
            joltage = [int(n) for n in parts[-1].replace("{", "").replace("}", "").split(",")]
            diagrams.append(Diagram(ind_l, buttons, joltage))
    res = 0
    for diagram in diagrams:
        correct = {n:(True if diagram.ind_l[n] == "#" else False) for n in range(len(diagram.ind_l))}
        lights = {n:False for n in range(len(diagram.ind_l))}
        combos = []
        correct_combos = []
        for r in range(len(diagram.buttons) + 1):
            for combo in combinations(diagram.buttons, r):
                combos.append(combo)
        for combo in combos:
            test_lights = lights.copy()
            for button in combo:
                for n in button:
                    test_lights[n] = not test_lights[n]
            if test_lights == correct:
                correct_combos.append(combo)
        res += min([len(c) for c in correct_combos])
    print(res)
if __name__ == "__main__":
    main()