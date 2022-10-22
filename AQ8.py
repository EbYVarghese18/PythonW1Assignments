# sum of odd numbers for a given limit
limit = int(input('Enter the limit: '))
sum = 0
for x in range(1, limit + 1):
    if x % 2 == 1:
        print(x)
        sum = sum + x
print('The sum of odd numbers for the given limit is: ' + str(sum))