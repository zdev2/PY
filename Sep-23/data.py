# Menampilkan Data
jk = ""
h = ""
hobi = ""
jenis_kelamin = ""


nama = input("Nama :")

while jk != "A" or "B":

    jk = input("Jenis Kelamin : \n A) Laki - Laki, B) Perempuan [A/B]?\n")
    if jk == "A":
        jenis_kelamin: str = "Laki - Laki"
        break
    elif jk == "B":
        jenis_kelamin: str = "Permpuan"
        break

    else:
        print("Incorrect. Try again!")


h = input("Hobi : \n A) Membaca,  B) Olahraga [A/B/AB]?\n")
while h != "A" or "B":
    if h == "A":
        hobi: str = "Membaca"
        break
    elif h == "B":
        hobi: str = "Olahraga"
        break
    elif h == "AB":
        hobi: str = "Membaca, Olahraga"
        break
    else:
        print("Incorrect. Try again!")

email = input("Email :")
print("==========================================\n")

print("Nama :", nama)
print("Jenis Kelamin :", jenis_kelamin)
print("Hobi : ", hobi)
print("Email :", email)

print("\n==========================================")
