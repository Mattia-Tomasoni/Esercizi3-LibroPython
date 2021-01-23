'''
Risolvi il problema precedente partendo da due liste generano
un dizionario con la nazione come chiave e la capitale come
valore. Successivamente interroga il dizionario per 
visuallizare la capitale di una nazione.
'''
stati = {
    "Italia" : "Roma",
    "Inghilterra" : "Londra",
    "Cina" : "Pechino",
    "Russia" : "Mosca",
    "Stati Uniti" : "Washington",
    "Australia" : "Canberra",
    "Danimarca" : "Copenaghen",
    "Germania" : "Berlino",
    "Francia" : "Parigi"
}

print("Queste sono le nazioni: ")
for nazione in stati:
    print(nazione)

nazione = input("Di quale nazione vuoi sapere la capitale: ")

if nazione in stati:
    print(nazione, " ha come capitale: ", stati[nazione])

else:
    print("Errore: ", nazione, "non è presente")