
def check_triangle(side1: int, side2: int, side3: int):
    if side1 + side2 < side3 or side2 + side3 < side1 or side3 + side1 < side2:
        result = "Треугольник не существует"
    elif (side1 == side2) and (side2 == side3) and (side3 == side1): # условие, что треугольник равносторонний
        result = "Равносторонний треугольник"
    elif side1 == side2 or side2 == side3 or side3 == side1: # условие , что треугольник равнобедренный
        result = "Равнобедренный треугольник"
    else:
        result = "Разносторонний треугольник"
    return result
    
triangle = check_triangle(10, 10, 10)
print("Треугольник со сторонами 10, 10, 10:", triangle)
triangle = check_triangle(10, 20, 30)
print("Треугольник со сторонами 10, 20, 30:", triangle)
triangle = check_triangle(10, 10, 20)
print("Треугольник со сторонами 10, 10, 20:", triangle)
triangle = check_triangle(-10, 10, 20)
print("Треугольник со сторонами -10, 10, 20:", triangle)


#side1 + side2 <= side3 or side2 + side3 <= side1 or side3 + side1 <= side2


#elif side1 <= 0 or side2 <= 0 or side3 <= 0 or side1 + side2 <= side3 or side2 + side3 <= side1 or side3 + side1 <= side2: