import math

def calculate_slope(point1, point2):
    if point1[0] == point2[0]:
        return "Undefined (vertical line)"
    return (point2[1] - point1[1]) / (point2[0] - point1[0])

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

point1 = tuple(map(float, input("Enter the coordinates of the first point (x1 y1): ").split()))
point2 = tuple(map(float, input("Enter the coordinates of the second point (x2 y2): ").split()))

slope = calculate_slope(point1, point2)
distance = calculate_euclidean_distance(point1, point2)

print(f"The slope between the points {point1} and {point2} is: {slope}")
print(f"The Euclidean distance between the points {point1} and {point2} is: {distance}")