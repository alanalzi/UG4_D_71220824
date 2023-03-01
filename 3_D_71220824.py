kalim = input("Masukan kalimat: ")
def kajang(kalim):
    kaka = kalim.split()
    kajang = ""
    for kata in kaka :
        if len(kata) > len(kajang):
            kajang = kata
    return kajang
ha = kajang(kalim)
print("kata terpanjang dalam kalimat itu adalah:", ha)