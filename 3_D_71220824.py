kalim = str(input("Masukan kalimat: ")).split()
def kajang(kalim):
    kaka = kalim
    kajang = ""
    for kata in kaka :
        if len(kata) > len(kajang):
            kajang = kata
    return kajang
ha = kajang(kalim)
print("kata terpanjang dalam kalimat itu adalah:", ha)