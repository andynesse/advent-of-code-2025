import pulp

class Diagram:
    def __init__(self, ind_l, buttons, joltage):
        self.ind_l = ind_l
        self.buttons = buttons
        self.joltage = joltage

def main():
    diagrams = []
    with open("day_10/data.txt", mode="r") as file:
        for line in file:
            parts = line.strip().split()
            ind_l = parts[0].replace("[", "").replace("]", "")
            buttons = [tuple([int(n) for n in b.replace("(", "").replace(")", "").split(",")]) for b in parts[1:-1]]
            joltage = [int(n) for n in parts[-1].replace("{", "").replace("}", "").split(",")]
            diagrams.append(Diagram(ind_l, buttons, joltage))
    
    res = 0
    for diagram in diagrams:
        prob = pulp.LpProblem("Button_Presses", pulp.LpMinimize)
        
        button_presses = {}
        for i in range(len(diagram.buttons)):
            button_presses[i] = pulp.LpVariable(f"button_{i}", lowBound=0, cat="Integer")
        
        prob += pulp.lpSum([button_presses[i] for i in range(len(diagram.buttons))]), "Total_Presses"
        
        for idx in range(len(diagram.joltage)):
            affecting_buttons = [i for i in range(len(diagram.buttons)) if idx in diagram.buttons[i]]
            if affecting_buttons:
                prob += pulp.lpSum([button_presses[i] for i in affecting_buttons]) == diagram.joltage[idx], f"Index_{idx}"
            else:
                if diagram.joltage[idx] != 0:
                    prob += 0 == 1
        
        prob.solve(pulp.PULP_CBC_CMD(msg=0))
        
        if prob.status == 1:
            min_presses = int(pulp.value(prob.objective))
            res += min_presses
    
    print(res)

if __name__ == "__main__":
    main()