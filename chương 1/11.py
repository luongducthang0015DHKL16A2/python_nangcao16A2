import math

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

class Parallelogram(Polygon):
    def __init__(self, base, side, height):
        super().__init__([base, side, base, side])
        self.height = height

    def area(self):
        return self.sides[0] * self.height

class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, height, height)

    def area(self):
        return self.sides[0] * self.sides[1]

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Tạo một hình vuông với cạnh là 4
square = Square(4)
print("Chu vi của hình vuông:", square.perimeter())
print("Diện tích của hình vuông:", square.area())

# Tạo một hình chữ nhật với chiều rộng là 4 và chiều cao là 2
rectangle = Rectangle(4, 2)
print("Chu vi của hình chữ nhật:", rectangle.perimeter())
print("Diện tích của hình chữ nhật:", rectangle.area())

# Tạo một hình bình hành với cơ sở là 4, cạnh là 3 và chiều cao là 2
parallelogram = Parallelogram(4, 3, 2)
print("Chu vi của hình bình hành:", parallelogram.perimeter())
print("Diện tích của hình bình hành:", parallelogram.area())

# Tạo một đa giác với các cạnh là 3, 4, 5
polygon = Polygon([3, 4, 5])
print("Chu vi của đa giác:", polygon.perimeter())