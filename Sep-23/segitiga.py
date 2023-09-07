# Mencari Luas dan Keliling Lingkaran
import math

a = int(input(">>Alas Segitiga :"))
t = int(input(">>Tinggi Segitiga :"))

L = a * t/2
c = math.sqrt(a**2 + t**2)
Kll = a + t + c

print("Luas :", a, "*", t, "/2 :", str(L))
print("Sisi Miring :", str(c))
print("Keliling :", a, "+", t, "+", c, " :", str(Kll))
