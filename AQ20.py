""" Write a program to print the following pattern using for loop
1
2	3
4	5	6
7	8	9	10 """

num = 1
for row in range(1, 5):
    for col in range(0, row):
        print(str(num) + " ", end="")
        num = num + 1
    print()
