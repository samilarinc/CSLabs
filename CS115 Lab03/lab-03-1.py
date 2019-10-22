def dna_strand( dna ):
    antiDna = ''
    for i in dna:
        if i == 'G'or i == 'g':
            antiDna += 'C'
        elif i == 'C' or i == 'c':
            antiDna += 'G'
        elif i == 'A' or i == 'a':
            antiDna += 'T'
        elif i == 'T' or i == 't':
            antiDna += 'A'     
    return antiDna

antiDna = ''
dna = input("Enter dna: ")
antiDna = dna_strand(dna)

print("dna complement : " + antiDna)
