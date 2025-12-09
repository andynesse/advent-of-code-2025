from shapely.geometry import Polygon, box
def main():
    points = []
    with open("advent-of-code-2025\day_9\data.txt", mode="r") as file:
        for line in file:
            points.append(tuple([ int(n) for n in line.strip().split(",")]))
    polygon = Polygon(points)
    max_area = 0
    for i, point_a in enumerate(points):
        for point_b in points[i+1:]:
            area = (abs(point_a[0]-point_b[0])+1)*(abs(point_a[1]-point_b[1])+1)
            if area <= max_area:
                continue
            rectangle = box(min(point_a[0], point_b[0]), min(point_a[1], point_b[1]), max(point_a[0], point_b[0]), max(point_a[1], point_b[1]))
            if polygon.contains(rectangle):
                max_area = area
    print(max_area)
if __name__ == "__main__":
    main()