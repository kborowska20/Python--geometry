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


    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):

        if not isinstance(shape, Shape):
            raise TypeError("Error")
        else:
            self.shapes.append(shape)


    def get_largest_shape_by_perimeter(self):

        if len(self.shapes) > 0:
            largest_shape = self.shapes[0] #
            for shape in self.shapes:
                if shape.get_perimeter() > largest_shape.get_perimeter():
                    largest_shape = shape
            return largest_shape
        else:
            return "You have no shapes added"



    def get_largest_shape_by_area(self):

        if len(self.shapes) > 0:
            largest_shape = self.shapes[0]
            for shape in self.shapes:
                if shape.get_area() > largest_shape.get_area():
                    largest_shape = shape
            return largest_shape
        else:
            return "You have no shapes added"

    def get_shapes_table(self):
        table = []
        title_list = ['idx', 'Class', '__str__ ', 'Perimeter', 'Formula', 'Area', 'Formula']
        for i in range(0, len(self.shapes)):
            table.append([str(i), str(self.shapes[i].__class__.__name__), str(self.shapes[i]),
                          str(round(self.shapes[i].get_perimeter(), 2)), str(self.shapes[i].get_perimeter_formula()),
                          str(round(self.shapes[i].get_area(), 2)), str(self.shapes[i].get_area_formula())])
    def get_shapes_table(self):
        table = []
        title_list = ['idx', 'Class', '__str__ ', 'Perimeter', 'Formula', 'Area', 'Formula']
        for i in range(0, len(self.shapes)):
            table.append([str(i), str(self.shapes[i].__class__.__name__), str(self.shapes[i]),
                          str(round(self.shapes[i].get_perimeter(), 2)), str(self.shapes[i].get_perimeter_formula()),
                          str(round(self.shapes[i].get_area(), 2)), str(self.shapes[i].get_area_formula())])
        return str(ui.print_table(table, title_list))  # table implemented in ui module