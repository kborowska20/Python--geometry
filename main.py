import sys
from geometry import *
from ui import *


def main():

    shapes = ShapeList()  # object containing all shapes added by the user
    while True:
        Printing.first_menu()
        option = input("Select an option: ")

        if option == "1":

            Printing.add_shape_menu()
            option = input("Select an option: ")

            if option == "1":
                print("You choose circle")
                r = float(input("Please specify a radius: "))
                shapes.add_shape(Circle(r))
                print("Shape added")

            elif option == "2":
                print("You choose triangle")
                a = float(input("Please specify side a: "))
                b = float(input("Please specify side b: "))
                c = float(input("Please specify side c: "))
                shapes.add_shape(Triangle(a, b, c))
                print("Shape added")

            elif option == "3":
                print("You choose equiteral triangle")
                a = float(input("Please specify side length: "))
                shapes.add_shape(EquilateralTriangle(a))
                print("Shape added")

            elif option == "4":
                print("You choose recktangle")
                a = float(input("Please specify side a length: "))
                b = float(input("Please specify side b length: "))
                shapes.add_shape(Rectangle(a, b))
                print("Shape added")

            elif option == "5":
                print("You choose Square")
                a = float(input("Please specify side length: "))
                shapes.add_shape(Square(a))
                print("Shape added")

            elif option == "6":
                print("You choose regular pentagon")
                a = float(input("Please specify side length: "))
                shapes.add_shape(RegularPentagon(a))
                print("Shape added")

            elif option == "0":
                main()

        elif option == "2":
            print(shapes.get_shapes_table())
            # Show all shapes

        elif option == "3":
            print(str(shapes.get_largest_shape_by_perimeter()))
            # Show shape with the largest perimeter

        elif option == "4":
            print(str(shapes.get_largest_shape_by_area()))
            # Show shape with the largest area

        elif option == "5":
            Printing.view_all()
            option = input("Select an option: ")

            if option == "1":
                print("You choose circle")
                print(Circle.get_perimeter_formula())
                print(Circle.get_area_formula())

            elif option == "2":
                print("You choose triangle")
                print(Triangle.get_perimeter_formula())
                print(Triangle.get_area_formula())

            elif option == "3":
                print("You choose equiteral triangle")
                print(EquilateralTriangle.get_perimeter_formula())
                print(EquilateralTriangle.get_area_formula())

            elif option == "4":
                print("You choose recktangle")
                print(Rectangle.get_perimeter_formula())
                print(Rectangle.get_area_formula())

            elif option == "5":
                print("You choose Square")
                print(Square.get_perimeter_formula())
                print(Square.get_area_formula())

            elif option == "6":
                print("You choose regular pentagon")
                print(RegularPentagon.get_perimeter_formula())
                print(RegularPentagon.get_area_formula())

            elif option == "0":
                main()

            # Show formulas

        elif option == "0":
            sys.exit()

if __name__ == "__main__":
    main()