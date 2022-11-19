class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ''
        if self.height > 50 or self.width > 50:
            return 'Too big for picture'
        else:
            for i in range(self.height):
                picture += '*' * self.width + '\n'

            return picture

    def get_amount_inside(self):
        return 'WIP'

class Square(Rectangle):
    def __init__(self, length):
        self.set_width(length)
        self.set_height(length)

    def set_side(self, side):
        self.__init__(side)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
