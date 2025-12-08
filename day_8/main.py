import math
class Junction_Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __eq__(self, other):
        if not isinstance(other, Junction_Box):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z

class Vertex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.dist = distance(a, b)
    def __repr__(self):
        return f"{self.a} --{math.floor(self.dist)}-> {self.b}"


def distance(a, b):
    return math.dist((a.x, a.y, a.z), (b.x, b.y, b.z))

def main():
    junction_boxes = []
    vertecies = []
    with open("advent-of-code-2025\day_8\data.txt", mode="r") as file:
        for line in file:
            junction_boxes.append(Junction_Box(*[int(n) for n in line.strip().split(",")]))
    for i, jb in enumerate(junction_boxes):
        for j in range(i+1, len(junction_boxes)):
            vertecies.append(Vertex(jb, junction_boxes[j]))
    vertecies.sort(key = lambda x: x.dist)
    circuits = []
    connected = []
    v = None
    for i in range(len(vertecies)):
        v = vertecies[i]

        if not any(v.a in x or v.b in x for x in circuits):
            circuits.append([v.a, v.b])
            connected.append(v.a)
            connected.append(v.b)
            continue
        if v.a not in connected:
            connected.append(v.a)
        elif v.b not in connected:
            connected.append(v.b)
        if len(connected) == len(junction_boxes):
            print(v.a.x*v.b.x)
            break
        prev = None
        for circuit in circuits:
            if v.a in circuit and v.b not in circuit:
                if prev is not None:
                    prev.extend([c for c in circuit.copy() if c not in prev])
                    circuits.remove(circuit)
                    continue
                circuit.append(v.b)
                prev = circuit
            elif v.b in circuit and v.a not in circuit:
                if prev is not None:
                    prev.extend([c for c in circuit.copy() if c not in prev])
                    circuits.remove(circuit)
                    continue
                circuit.append(v.a)
                prev = circuit

if __name__ == "__main__":
    main()