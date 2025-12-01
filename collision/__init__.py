class RectCorrectError(Exception):
    pass

def isCorrectRect(points):
    (x1, y1), (x2, y2) = points
    if len(points) == 2 and x1 < x2 and y1 < y2:
        return True
    else: 
        return False

def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")
    
    x1_left, y1_bottom = rect1[0]
    x1_right, y1_top = rect1[1]
    x2_left, y2_bottom = rect2[0]
    x2_right, y2_top = rect2[1]
    
    return (x1_left <= x2_right and x1_right >= x2_left and
            y1_bottom <= y2_top and y1_top >= y2_bottom)

# Вызовы функций
print(isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]))
print(isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)]))
print(isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)]))