seq = input("Geef een mRNA sequentie: ") #vraagt de gebruiker om een mRNA sequentie
aantal_A = seq.count("A") #berekent aantal 'A' in de sequentie
aantal_C = seq.count("C") #berekent aantal 'C' in de sequentie
aantal_G = seq.count("G") #berekent aantal 'G' in de sequentie
aantal_T = seq.count("T") #berekent aantal 'T' in de sequentie
aantal_C_G = aantal_C + aantal_G #berekent aantal 'C' en 'G' in de sequentie
totaal = aantal_C_G + aantal_T + aantal_A #berekent totaal aantal nucleotiden
GC = aantal_C_G / totaal * 100 #berekent het GC%
print(GC)
 

