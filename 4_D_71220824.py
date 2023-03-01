bil1 = input("Masukan sekumpulan bilangan (pisahkan dengan koma): ").split(",")
def bil (bil):
    bil = (bil1)
    return bil
g = bil(bil1)
terbesar = max(g, key=lambda a:int(a))
terkecil = min(g, key=lambda a:int(a))
print("Bilangan terbesar dari kumpulan bilangan yang di input adalah ",terbesar)
print("Bilangan terkecil dari kumpulan bilangan yang di input adalah ",terkecil)