# Write a program to check whether a given number is prime or not


number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")
