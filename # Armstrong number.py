# Armstrong number 
number = 153
sum = 0
t1 = number
while t1>0:
    rem = t1%10
    sum+=rem**3
    t1 //= 10
print("Armstrong number ") if sum == number else print("Not Armstrong")