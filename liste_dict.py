# LISTE
produse = ["Antivirus Plus", "Total Security", "Family Pack", "Internet Security"]
produse.remove("Family Pack")
print ("Lista de produse dupa eliminarea Family Pack: ", produse)
produse.append("Ultra Security")
print ("Lista de produse dupa adaugarea noului produs: ", produse)
produse.sort()
print ("Lista in ordine alfabetica: ", produse)

# DICTIONARE
dictProduse = {"Antivirus Plus": 100, "Total Security": 75, "Internet Security": 56, "Ultra Security": 120}
dictProduse["Antivirus Plus"] += dictProduse["Antivirus Plus"]*0.25
preturi = dictProduse.values()
pret_mediu = sum(preturi)/len(preturi)
print ("Produsele si preturile asociate sunt: ", dictProduse)
print ("Pretul mediu al unui produs este: ", pret_mediu)
