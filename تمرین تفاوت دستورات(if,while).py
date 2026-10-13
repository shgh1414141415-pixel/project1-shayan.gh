import sys
n = int(input(" input number: "))
i = 0 
power = 1
while i <= n:
    print(str(i) + ' ' + str(power))
    i += 1
    power *= 2 
    