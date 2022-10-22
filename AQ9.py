# Write a program to print the following pattern
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

limit = int(input("Enter the limit: "))
for row in range(1, limit + 1):
    for col in range(1, row + 1):
        print(col, end="")
    print()
