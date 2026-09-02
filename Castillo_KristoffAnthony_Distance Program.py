import math


point_x1 = float(input("enter the x1: "))
point_x2 = float(input("enter the x2: "))
point_y1 = float(input("enter the y1: "))
point_y2 = float(input("enter the y2: "))

point_a = pow(point_x2-point_x1, 2)
point_b = pow(point_y2-point_y1, 2)

results = point_a + point_b
distance = math.sqrt(results)

print("/nThe distance is", distance)