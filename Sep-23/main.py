# Mencari Luas dan Keliling Lingkaran
import math

pi = math.pi
r = int(input(">>Jari - Jari :"))

L = round(pi * r * r)
Kll = round(pi * (2*r))

print("Luas :", str(L))
print("Keliling :", str(Kll))
