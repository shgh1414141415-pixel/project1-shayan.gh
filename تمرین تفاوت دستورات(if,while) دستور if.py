import sys
n = int(input(" imput number: "))
power = 1
for i in range(n + 1):
    print(str(i) + ' ' + str(power))
    power *= 2
    