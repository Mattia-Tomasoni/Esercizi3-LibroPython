'''
Costruisci un dizionario ottenuto da quello dell'esercizio 
precedente invertendo il ruolo di chiave e valore. Usa il
nuovo dizionario per trovare il nome della nazione, noto
il nome della capitale.
'''
capitali = {
    "Roma" : "Italia",
    "Londra" : "Inghilterra",
    "Pechino" : "Cina",
    "Mosca" : "Russia",
    "Washington" : "Stati Uniti",
    "Canberra" : "Australia",
    "Copenaghen" : "Danimarca",
    "Berlino" : "Germania",
    "Parigi" : "Francia"
}

print("Queste sono le capitali: ")

for e in capitali:
    print(e)

e = input("Di quale capitale vuoi sapere la nazione: ")

if e in capitali:
    print(e, " è la nazione di: ", capitali[e])

else:
    print("Errore: ", e, "non è presente")