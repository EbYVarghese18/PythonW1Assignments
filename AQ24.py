# 24.	Write a menu driven program to calculate the area of a given object.
# a.	Program should contain two classes
# i.	Class 1: MyClass
# ii.	Class 2: Area


class Area:

    def circle(self):
        radius = int(input("Enter the radius: "))
        area = 3.14 * radius * radius
        print("The area of circle is: " + str(area))

    def square(self):
        length = int(input("Enter the length: "))
        area = length * length
        print("The area of square is: " + str(area))

    def rectangle(self):
        length = int(input("Enter the length: "))
        breadth = int(input("Enter the breadth: "))
        area = length * breadth
        print("The area of rectangle: " + str(area))

    def triangle(self):
        base = int(input("Enter the base: "))
        height = int(input("Enter the height: "))
        area = 0.5 * base * height
        print("The area of triangle is : " + str(area))


class MyClass(Area):
    pass


choice = int(input(" 1. Circle\n 2. Square\n 3. Reactangle\n 4. Triangle"))

obj = MyClass()
match choice:
        case 1:
            obj.circle()
        case 2:
            obj.square()
        case 3:
            obj.rectangle()
        case 4:
            obj.triangle()
        case _:
            print("Enter the correct choice: ")
