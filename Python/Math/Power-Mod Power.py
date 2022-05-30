import math

a = int(input())
b = int(input())
c = int(input())

result_power = math.floor(math.pow(a,b))
result_modPower = pow(a,b,c)
print(result_power)
print(result_modPower)
