def isCorrectRect(points):
    (x1, y1), (x2, y2) = points
    if len(points) == 2 and x1 < x2 and y1 < y2:
        return True
    else: return False
print(isCorrectRect([(-3.4, 1), (-5, -2)]))