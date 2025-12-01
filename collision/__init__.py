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

def intersectionAreaRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise ValueError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise ValueError("2й прямоугольник некоректный")
    if not isCollisionRect(rect1, rect2):
        return 0
    x1_left, y1_bottom = rect1[0]
    x1_right, y1_top = rect1[1]
    x2_left, y2_bottom = rect2[0]
    x2_right, y2_top = rect2[1]
    
    intersect_left = max(x1_left, x2_left)
    intersect_right = min(x1_right, x2_right)
    intersect_bottom = max(y1_bottom, y2_bottom)
    intersect_top = min(y1_top, y2_top)
    
    width = intersect_right - intersect_left
    height = intersect_top - intersect_bottom
    area = width * height
    
    return area

def intersectionAreaMultiRect(rectangles):
    if not rectangles:
        return 0
    for i, rect in enumerate(rectangles):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"{i+1}й прямоугольник некоректный")
    def rect_area(rect):
        x1, y1 = rect[0]
        x2, y2 = rect[1]
        return (x2 - x1) * (y2 - y1)
    def rect_intersection(rect1, rect2):
        if not isCollisionRect(rect1, rect2):
            return None
        x1_left, y1_bottom = rect1[0]
        x1_right, y1_top = rect1[1]
        x2_left, y2_bottom = rect2[0]
        x2_right, y2_top = rect2[1]
        
        intersect_left = max(x1_left, x2_left)
        intersect_right = min(x1_right, x2_right)
        intersect_bottom = max(y1_bottom, y2_bottom)
        intersect_top = min(y1_top, y2_top)
        
        return [(intersect_left, intersect_bottom), (intersect_right, intersect_top)]
    all_intersections = []
    # Находим все возможные пересечения разного уровня
    # k-уровень: пересечения k прямоугольников
    for k in range(1, len(rectangles) + 1):
        from itertools import combinations
        
        for combo in combinations(rectangles, k):
            current_intersection = combo[0]
            for rect in combo[1:]:
                current_intersection = rect_intersection(current_intersection, rect)
                if current_intersection is None:
                    break
            if current_intersection is not None:
                all_intersections.append((k, current_intersection))
    if not all_intersections:
        return 0
    max_k = max(k for k, _ in all_intersections)
    for k, intersection in all_intersections:
        if k == max_k:
            return rect_area(intersection)
    return 0