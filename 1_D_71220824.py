print("="*20, "BARIS ARITMATIKA","="*20)
def arit(ba, sl, n):
    sel = sl - ba
    rumus = n/2*(2*ba + sl*(n-1))
    return rumus
ba = int(input("Masukan bilangan awal : "))
sl = int(input("Masukan selisih bilangan : "))
n = int(input("Masukan banyak nya suku : "))

tot = arit(ba, sl, n)
print("Total dari deret aritmatika tersebut adalah :", tot) 