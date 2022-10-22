# Write a program to identify whether a string is a palindrome or not

userInput = input()
userInputCopy = userInput[::-1]
if userInput == userInputCopy:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
