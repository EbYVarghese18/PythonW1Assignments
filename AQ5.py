totalMark = float(input('Enter the total mark: '))
if totalMark > 100:
    print('Enter the correct Total Mark!!')
elif totalMark >= 90:
    print('Grade A')
elif totalMark >= 80:
    print('Grade B')
elif totalMark >= 70:
    print('Grade C')
elif totalMark >= 60:
    print('Grade D')
elif totalMark >= 50:
    print('Grade E')
elif totalMark < 50:
    print('Failed')
