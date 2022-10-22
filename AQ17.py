# Write a menu driven program to do the basic mathematical operations such as
# addition, subtraction, multiplication and division (hint: use if else ladder or switch)


number_One = int(input("Enter the first Number: "))
number_Two = int(input("Enter the second Number: "))


def addition():
    print(number_One + number_Two)


def substraction():
    print(number_One - number_Two)


def multiplication():
    print(number_One * number_Two)


def division():
    print(number_One / number_Two)


class SimpleCalculator:
    while 1 > 0:
        choice = int(input("Select the choice: \n "
                           "1. Addition \n "
                           "2. Substraction \n "
                           "3. Multiplication \n "
                           "4. Division \n "
                           "5. Exit \n"))
        match choice:
            case 1:
                addition()
            case 2:
                substraction()
            case 3:
                multiplication()
            case 4:
                division()
            case 5:
                break
            case _:
                print("Enter the correct choice!!!")
