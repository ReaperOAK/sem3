import math

class StraightLine:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_distance(self):
        distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        return distance

    def calculate_slope(self):
        if self.x2 - self.x1 == 0:
            return float('inf')  # Slope is infinite for vertical lines
        slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        return slope

    def display(self):
        print(f"Point 1: ({self.x1}, {self.y1})")
        print(f"Point 2: ({self.x2}, {self.y2})")
        print(f"Distance between points: {self.calculate_distance()}")
        print(f"Slope of the line: {self.calculate_slope()}")

# Example usage
line = StraightLine(0, 0, 30, 40)
line.display()