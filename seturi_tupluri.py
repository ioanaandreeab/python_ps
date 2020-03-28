# SETURI
setTehnologii2015 = {'Java', 'C', 'Cobol', 'Pascal', 'Go'}
setTehnologii2020 = {'JavaScript', 'Java', 'C', 'Ruby'}

tehnologiiNoi = setTehnologii2020.difference(setTehnologii2015)
print("Tehnologiile noi din 2020 sunt: ", tehnologiiNoi)
tehnologiiComune = setTehnologii2020.intersection(setTehnologii2015)
print("Tehnologiile care s-au pastrat sunt: ", tehnologiiComune)
tehnologiiTotal = setTehnologii2015.union(setTehnologii2020)
print("Totalitatea tehnologiilor este: ", tehnologiiTotal)

# TUPLURI
tehnologiiPreferate = ('Java', 'Java', 'C', 'Ruby', 'C', 'Java')
print("Numarul angajatilor ce prefera Java este de ", tehnologiiPreferate.count('Java'))
