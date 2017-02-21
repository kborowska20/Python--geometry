import math
import ui
class Shape:
    """
    This is a abstract class representing geometrical shape.
    """

    def __init__(self):
        """
         Constructs Shape object
         Raises:
             ValueError: If any of the parameters is below 0.
         """
        pass

    def get_area(self):
        """
        Calculates shape's area.
        Returns:
            float: area of the shape
        """
        pass

    def get_perimeter(self):
        """
        Calculates shape's perimeter.
        Returns:
            float: perimeter of the shape
        """
        pass

    def __str__(self):
        """
        Returns information about the shape as string.
        Returns:
            str: information bout shape
        """
        pass

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the shape as a string.
        Returns:
            str: area formula
        """
        pass

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the shape as a string.
        Returns:
            str: perimeter formula
        """
        pass


class Circle(Shape):

    def __init__(self, r):
        self.r = r
        if r < 0 :
            raise ValueError("Circle cannot have negative radius")


    def get_area(self):
        return math.pi * (self.r ** 2)


    def get_perimeter(self):
        return 2 * math.pi * self.r


    def __str__(self):
        return "Circle, r = " + str(self.r)


    @classmethod
    def get_area_formula(cls):
        return "π×r^2"


    @classmethod
    def get_perimeter_formula(cls):
        return "2×π×r"


class Triangle(Shape):


    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a < 0 or b < 0 or c < 0:
            raise ValueError("Values of the parameters can't be below 0")

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return "Triangle, a=" + str(self.a) + ",b=" + str(self.b) + ",c=" + str(self.c)

    @classmethod
    def get_area_formula(cls):
        return "(s×(s-a)×(s-b)×(s-c))^1/2"

    @classmethod
    def get_perimeter_formula(cls):
        return "a+b+c"


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        Triangle.__init__(self, a, b=a, c=a)

    def __str__(self):
        return "Equilateral Triangle,a = " + str(self.a)


class Rectangle(Shape):


    def __init__(self, a, b):
        self.a = a
        self.b = b
        if a < 0 or b < 0:
            raise ValueError("Values of the parameters can't be below 0")

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * self.a + 2 * self.b

    def __str__(self):
        return "Rectangle, a = " + str(self.a) + ", b = " + str(self.b)

    @classmethod
    def get_area_formula(cls):
        return "a × b"

    @classmethod
    def get_perimeter_formula(cls):
        return "2×a + 2×b"


class Square(Rectangle):


    def __init__(self, a):
        Rectangle.__init__(self, a, b = a)
        if a < 0:
            raise ValueError("Value of the parameter can't be below 0")

    def __str__(self):
        return "Square, a = " + str(self.a)

    @classmethod
    def get_area_formula(cls):
        return "a × a"

    @classmethod
    def get_perimeter_formula(cls):
        return "4×a"


class RegularPentagon(Shape):


    def __init__(self, a):
        self.a = a
        if a < 0:
            raise ValueError("Value of the parameter can't be below 0")

    def get_area(self):
        return (self.a ** 2) * (math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4)

    def get_perimeter(self):
        return (5 * self.a)

    def __str__(self):
        return "Regular Pentagon,a=" + str(self.a)

    @classmethod
    def get_area_formula(cls):
        return "(a^2 × ((5×(5+2×(5)^1/2))^1/2)/4"

    @classmethod
    def get_perimeter_formula(cls):
        return "5×a"


class ShapeList:

    """
    This is a class representing list of shapes.
    """

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            raise TypeError

    def get_shapes_table(self):
        title_list = ["idx", "Class", "__str__", "Perimeter", "Formula", "Area", "Formula"]
        table = []
        for obj in self.shapes:
            line_lst = [str(self.shapes.index(obj)), obj.__class__.__name__, str(obj), str(obj.get_perimeter()), str(
                obj.get_perimeter_formula()), str(obj.get_area()), str(obj.get_area_formula())]
            table.append(line_lst)
        table.insert(0, title_list)
        width_list = []
        for i in range(len(table[0])):
            longest_string = 0
            for row in table:
                if len(row[i]) > longest_string:
                    longest_string = len(row[i])
            width_list.append(longest_string)

        print("╔", end="")
        for column in range(len(table[0])):
            print("{0:═^{w}}".format("═", w=width_list[column] + 2), end="")
            if column + 1 != len(table[0]):
                print("╦", end="")
        print("╗\n", end="")
        '''content'''
        for row_number, row in enumerate(table):
            for column, cell in enumerate(row):
                print("║{0:^{w}}".format(cell, w=width_list[column] + 2), end="")
            print("║\n", end="")
            if row_number + 1 != len(table):
                print("╠", end="")
                for column, cell in enumerate(row):
                    print("{0:═^{w}}".format("═", w=width_list[column] + 2), end="")
                    if column + 1 != len(table[0]):
                        print("╬", end="")
                print("╣\n", end="")
            '''footer'''
            if row_number + 1 == len(table):
                print("╚", end="")
                for column, cell in enumerate(row):
                    print("{0:═^{w}}".format("═", w=width_list[column] + 2), end="")
                    if column + 1 != len(table[0]):
                        print("╩", end="")
                print("╝")
        table.remove(table[0])

    def get_largest_shape_by_perimeter(self):
        largest_obj = Square(0)
        for obj in self.shapes:
            if largest_obj.get_perimeter() < obj.get_perimeter():
                largest_obj = obj
        return largest_obj

    def get_largest_shape_by_area(self):
        largest_obj = Square(0)
        for obj in self.shapes:
            if largest_obj.get_area() < obj.get_area():
                largest_obj = obj
        return largest_obj