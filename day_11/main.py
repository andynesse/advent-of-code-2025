def count_paths(graph, curr, dest, memo=None):
    if memo is None:
        memo = {}
    if curr in memo:
        return memo[curr]
    if curr == dest:
        return 1
    tot_paths = 0
    for neighbor in graph.get(curr, []):
        tot_paths += count_paths(graph, neighbor, dest, memo)
    memo[curr] = tot_paths
    return tot_paths

def main():
    graph = {}
    with open("day_11/data.txt", mode="r") as file:
        for line in file:
            line = line.strip().split(":")
            graph[line[0].strip()] = line[1].strip().split()
    print("Part_1:", count_paths(graph, "you", "out"))
    print("Part_2:", count_paths(graph, "svr", "fft")*count_paths(graph, "fft", "dac")*count_paths(graph, "dac", "out"))

if __name__ == "__main__":
    main()