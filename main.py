from collision import (
    RectCorrectError,
    isCorrectRect,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect
)
# isCorrectRect
print(isCorrectRect([(-3.4, 1),(9.2, 10)])) # Вернет True
print(isCorrectRect([(-7, 9),(3, 6)])) # Вернет False

# isCollisionRect
print(isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)])) # Вернет True
print(isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)])) # Вернет False
print(isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)])) # Вызовет ошибку

# intersectionAreaRect
print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)])) # Вернет некоторое положительное число
print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)])) # Вернет 0
print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)])) # Вызовет ошибку

# intersectionAreaMultiRect
rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
result = intersectionAreaMultiRect(rectangles)
print(f"Уникальная площадь пересечения: {result}")

# Некорректный прямоугольник
incorrect_rectangles = [
    [(-3, 1), (9, 10)],
    [(3, 17), (13, 1)]  # Некорректный прямоугольник
]
intersectionAreaMultiRect(incorrect_rectangles)  # Вызовет ошибку