import math
n = 101
m = 110
b = 100


Special = (n // m) * b 
RemainderQuant = (n % m)

if RemainderQuant < m or RemainderQuant == m:
    Remainder = b * 1
else:
    Remainder = math.ceil(n/m) * b
SpecialOnly = Special + Remainder
print(n%m)
print("Special: ", Special)
print("Remainder: ", Remainder)

print(SpecialOnly)