import sys
import os
from geometry import *
import ui

def main():
    menu_options = ["Add new shape", "Show all shapes", "Show shape with the largest perimeter",
    "Show shape with the largest area", "Show formulas"]
    shapes = ShapeList()  # object containing all shapes added by the user
    while True:
        ui.menu("Geometry Learning",menu_options)
        option = input("\nSelect an option: ")
        ui.cls()
        if option == "1":
            list_shapes = ["Circle", "Triangle", "Equilateral Triangle", "Rectangle", "Square", "Regular Pentagon"]
            while True:
                ui.menu("Choose a shape", list_shapes)
                choosen_shape = input(">")
                if choosen_shape == "1":
                    sh = Circle(ui.multi_input("Input r = ")[0])
                    shapes.add_shape(sh)
                elif choosen_shape == '2':
                        ui.cls()
                        values = ui.multi_input("Input a =  b =  c =  ")
                        sh = Triangle(values[0], values[1], values[2])
                        print(sh)
                        shapes.add_shape(sh)
                elif choosen_shape == '3':
                        ui.cls()
                        sh = EquilateralTriangle(ui.multi_input("Input a = ")[0])
                        shapes.add_shape(sh)
                elif choosen_shape == '4':
                        ui.cls()
                        values = ui.multi_input("Input a = b =")
                        sh = Rectangle(values[0], values[1])
                        shapes.add_shape(sh)
                elif choosen_shape == '5':
                        ui.cls()
                        sh = Square(ui.multi_input("Input a = ")[0])
                        shapes.add_shape(sh)
                elif choosen_shape == '6':
                        ui.cls()
                        sh = Circle(ui.multi_input("Input a = ")[0])
                        shapes.add_shape(sh)
                elif choosen_shape == '0':
                        break
        elif option == "2":
            # Show all shapes
            ui.cls()
            shapes.get_shapes_table()

        elif option == "3":
            # Show shape with the largest perimeter
            ui.cls()
            largest_perimeter = shapes.get_largest_shape_by_perimeter()
            print("Shape that have largest perimeter: {}".format(largest_perimeter))
        elif option == "4":
            # Show shape with the largest area
            ui.cls()
            largest_area = shapes.get_largest_shape_by_area()
            print("Shape that have largest area: {}".format(largest_area))
        elif option == "5":
            ui.cls()
            print("Which shape formulas do you want to see?")
            options = ["Circle", "Triangle", "Equilateral Triangle", "Rectangle", "Square", "Regular Pentagon"]
            ui.menu("Choose option:", options)
            option = input("> ")
            if option == '1':
                ui.cls()
                print("perimeter = " + Circle.get_perimeter_formula() + "\narea = " +
                Circle.get_area_formula())
            elif option == '2':
                ui.cls()
                print("perimeter = " + Triangle.get_perimeter_formula() + "\narea = " +
                Triangle.get_area_formula())
            elif option == '3':
                ui.cls()
                print("perimeter = " + EquilateralTriangle.get_perimeter_formula() + "\narea = " +
                EquilateralTriangle.get_area_formula())
            elif option == '4':
                ui.cls()
                print("perimeter = " + Rectangle.get_perimeter_formula() + "\narea = " +
                Rectangle.get_area_formula())
            elif option == '5':
                ui.cls()
                print("perimeter = " + Square.get_perimeter_formula() + "\narea = " +
                Square.get_area_formula())
            elif option == '6':
                ui.cls()
                print("perimeter = " + RegularPentagon.get_perimeter_formula() + "\narea = " +
                RegularPentagon.get_area_formula())
            elif option == '0':
                break
        elif option == "0":
            sys.exit()

if __name__ == "__main__":
    main()