# check even odd number
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("even Number")
else :
    print("Odd number")

# Approach 2
number = int(input("Enter the number : "))
if number & 1 == 0:
    print("Even")
else :
    print("Odd")

    