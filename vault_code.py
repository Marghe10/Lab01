import random

# Costanti del gioco
CODICE_MIN = 1
CODICE_MAX = 50
TENTATIVI_INIZIO = 6
TENTATIVI_MIN = 3
MAX_LIVELLO = 3


def dai_indizio(tentativo, codice):
    """Restituisce un indizio confrontando il tentativo con il codice segreto"""
    # TODO


def stampa_tentativi(tentativi_disponibili, usati):
    """Stampa la riga dei tentativi: O = disponibile, X = già usato"""
    # TODO
    print("tentativi disponibili:")
    for y in range(0,usati):
        print("X", end=" ")
    for x in range(0,tentativi_disponibili):
        print("O",end=" ")
    print()


def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco.
    Ritorna:
    * True se il giocatore indovina il codice
    * False se il giocatore esaurisce i tentativi.

    NB: Le funzioni dai_indizio() e stampa_tentativi() vanno chiamate dentro questa funzione
    """

    # Inizializzazioni
    tentativi_tot_disponibili = TENTATIVI_INIZIO - livello
    if tentativi_tot_disponibili < TENTATIVI_MIN:
        tentativi_tot_disponibili = TENTATIVI_MIN

    codice = random.randint(CODICE_MIN, CODICE_MAX)
    usati = 0
    tentativi_rimanenti=tentativi_tot_disponibili

    # TODO
    stampa_tentativi(tentativi_rimanenti,usati)
    in_gioco=input("inserire il numero da giocare")
    if in_gioco == codice:
        return True
    else:
        indizio=dai_indizio(tentativo, codice)


def main():
    print("=== Benvenuto in Vault Code ===")
    livello = 0

    while livello <= MAX_LIVELLO:
        completato = gestisci_livello(livello)
        if completato is True:
            livello += 1
        else:
            break


if __name__ == "__main__":
    main()
