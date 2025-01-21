from datetime import datetime
import math

# Function to calculate the difference between two dates
def date_difference(date1, date2):
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    delta = d2 - d1
    return delta.days

# Function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Example usage for date difference
date1 = "2023-01-01"
date2 = "2023-12-31"
days_difference = date_difference(date1, date2)
print(f"The difference between {date1} and {date2} is {days_difference} days.")

# Example usage for Euclidean distance
point1 = (1, 2)
point2 = (4, 6)
distance = euclidean_distance(point1, point2)
print(f"The Euclidean distance between points {point1} and {point2} is {distance}.")