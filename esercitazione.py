import pandas as pd
import numpy as np


# ============================================================
# ESERCIZIO 1 - Indicizzazione avanzata
# ============================================================

# 1. Creiamo un dizionario con i dati degli studenti
dati = {
    "Studente": ["Anna", "Luca", "Marco"],
    "Materia": ["Matematica", "Fisica", "Matematica"],
    "Classe": [1, 2, 3],
    "Eta": [19, 20, 21],
    "Voto": [30, 25, 29]
}

# 2. Convertiamo il dizionario in un DataFrame
df = pd.DataFrame(dati)

print("DATAFRAME INIZIALE")
print(df)


# 3. Creiamo una maschera booleana.
# Selezioniamo gli studenti che studiano Matematica
# E hanno un voto maggiore di 28.
filtro = (
    (df["Materia"] == "Matematica")
    & (df["Voto"] > 28)
)

# 4. Usiamo .loc per selezionare le righe che rispettano il filtro
risultatofiltro = df.loc[filtro]

# 5. Ordiniamo gli studenti per voto decrescente
# ascending=False significa dal più alto al più basso.
risultatofiltro = risultatofiltro.sort_values(
    by="Voto",
    ascending=False
)

print("\nSTUDENTI SELEZIONATI E ORDINATI")
print(risultatofiltro)


# 6. Aggiungiamo la colonna GIUDIZIO.
# Usiamo .loc per assegnare un giudizio alle righe selezionate.
# Attenzione: un'assegnazione successiva può sovrascrivere
# il valore assegnato in precedenza.

df.loc[df["Voto"] >= 28, "GIUDIZIO"] = "BUONO"
df.loc[df["Voto"] < 28, "GIUDIZIO"] = "SUFFICIENTE"

# Il voto almeno pari a 30 deve ricevere OTTIMO.
# Questa istruzione viene dopo BUONO per sovrascrivere
# correttamente il giudizio degli studenti con voto 30.
df.loc[df["Voto"] >= 30, "GIUDIZIO"] = "OTTIMO"

print("\nDATAFRAME CON GIUDIZIO")
print(df)


# 7. Calcoliamo la media dei voti
media = df["Voto"].mean()

print("\nMEDIA DEI VOTI")
print(media)


# 8. Creiamo una colonna booleana.
# True se il voto è strettamente maggiore della media,
# False altrimenti.
df["Sopra Media"] = df["Voto"] > media

print("\nDATAFRAME CON SOPRA MEDIA")
print(df)


# ============================================================
# ESERCIZIO 2 - query, iloc e fatturato
# ============================================================

# 1. Creiamo i dati dei prodotti.
# Generiamo 4 prezzi casuali tra 100 e 300 inclusi.
# I tre prodotti alimentari hanno prezzi fissi.
dati2 = {
    "Prodotto": [
        "laptop", "mouse", "tastiera", "monitor",
        "pane", "pasta", "pomodori"
    ],

    "Categoria": [
        "tecnologia", "tecnologia", "tecnologia",
        "tecnologia", "cibo", "cibo", "cibo"
    ],

    "Prezzo": np.concatenate([
        np.random.randint(100, 301, size=4),
        [1, 0.5, 0.2]
    ]),

    # Generiamo 7 quantità casuali da 1 a 7
    "Quantita": np.random.randint(1, 8, size=7),

    # Ogni valore corrisponde al prodotto nella stessa posizione
    "Disponibilita": [
        True, True, True, True, False, True, False
    ]
}

# 2. Convertiamo il dizionario in DataFrame
df2 = pd.DataFrame(dati2)

print("\nDATAFRAME DEI PRODOTTI")
print(df2)


# 3. Usiamo query() per selezionare i prodotti tecnologici
# con prezzo compreso tra 100 e 300 inclusi.
#
# Dentro query() scriviamo direttamente i nomi delle colonne.
# Usiamo and perché tutte le condizioni devono essere vere.
#
# .copy() crea una copia indipendente del risultato,
# utile quando vogliamo aggiungere o modificare colonne.
selezionati = df2.query(
    "Categoria == 'tecnologia' and Prezzo >= 100 and Prezzo <= 300"
).copy()

print("\nPRODOTTI SELEZIONATI CON QUERY")
print(selezionati)


# 4. Usiamo iloc per visualizzare:
# - le prime tre righe: 0:3
# - le colonne Prodotto e Prezzo: posizioni 0 e 2
#
# Ricorda: il limite finale di 0:3 è escluso.
prime_tre = selezionati.iloc[0:3, [0, 2]]

print("\nPRIME TRE RIGHE: PRODOTTO E PREZZO")
print(prime_tre)


# 5. Calcoliamo il fatturato di ciascun prodotto.
# Formula: Fatturato = Prezzo * Quantita
#
# Pandas moltiplica i valori riga per riga.
selezionati["Fatturato"] = (
    selezionati["Prezzo"] * selezionati["Quantita"]
)

print("\nPRODOTTI CON FATTURATO")
print(selezionati)


# 6. Ordiniamo i prodotti per fatturato decrescente.
# Salviamo il risultato nella stessa variabile.
selezionati = selezionati.sort_values(
    by="Fatturato",
    ascending=False
)

print("\nPRODOTTI ORDINATI PER FATTURATO DECRESCENTE")
print(selezionati)


# 7. Calcoliamo la media del fatturato dei prodotti selezionati.
media_fatturato = selezionati["Fatturato"].mean()

print("\nMEDIA DEL FATTURATO")
print(media_fatturato)

#Esercizio 3

dati3 = {
    "Dipendente" : ["Paolo","Giovanna","Vittoria","Pepe"],
    "Reparto" : ["Biologia","Psicologia","IT","IT"],
    "Eta" : [23,20,19,33],
    "Stipendio" : [2000,2100,3000,2900],
    "AnniServizio" : [1,2,3,4]
    }

df3 = pd.DataFrame(dati3)

print("3 Dataframe")
print(df3)

filtrodipendenti = ((df3["Eta"] > 30) & (df3["Stipendio"] > 2000)) | (df3["Reparto"] == "IT")

print(df3.loc[filtrodipendenti,["Dipendente","Eta","Stipendio"]])

df3.loc[df3["Eta"] < 35, "Categoria"] = "Junior"
df3.loc[df3["Eta"]>=35,"Categoria"] = "Senior"
print(df3)

media3 = df3.groupby(["Reparto","Categoria"])["Stipendio"].mean()

media3 = media3.sort_values(ascending=False)

print(media3)