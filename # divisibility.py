# divisibility
# check divisibility by 3 and 5
# number = int(input("Enter your number: "))
# if number % 3 & number % 5:
#     print("Number is divisible by 3 and 5")
# else :
#     print("Not divisible")

# # print numbers from 1 to N
# N = int(input("Enter the value of N: "))
# for i in range (1,N+1):
#     print(i)

# print 1 to 40 ==> even odd different 
for i in range (1,41):
    if i % 2:
        print("even numbers are:",i)
    else :
        print("Odd numbers are",i)

# different lists of odd even 
for i in range (1,41):
    if i % 2 == 0 :
        print(i,"even number")
for i in range (1,41):
    if i % 2 != 0:
        print(i,"odd")

