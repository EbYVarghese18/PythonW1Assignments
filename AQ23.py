# 23.	Write an object oriented program to store and display the values of a 2D array
# a.	Program should contains 3 functions including the main function
# main()
# 1.	Declare an array
# 2.	Call function getArray()
# 3.	Call function displayArray()

size = int(input("Enter the size of the array: "))
array = []


class DisplayArray:

    @staticmethod
    def getArray():
        print("Enter the array elements: ")
        for i in range(size):
            arrayTemp = []
            for j in range(size):
                arrayTemp.append(int(input()))
            array.append(arrayTemp)

    @staticmethod
    def displayArray():
        print("The array elements are: ")
        for i in range(size):
            print(array[i])


obj = DisplayArray
obj.getArray()
obj.displayArray()