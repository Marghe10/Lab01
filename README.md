# Lab 01

#### Obiettivi

- Ripasso e consolidamento dei concetti base: strutture condizionali e cicli
- Strutture dati base quali variabili e liste
- Approccio modulare alla scrittura del codice (funzioni)
- Gestione interattiva di input utente e logica di gioco.

## Vault Code

Si vuole realizzare un programma in Python per gestire un caveau protetto da una sequenza di codici numerici segreti. 
Il giocatore deve superare una serie di livelli, ognuno dei quali richiede di indovinare un codice segreto con un 
numero limitato di tentativi, ricevendo un indizio ("più alto", "più basso") ad ogni errore.

### Livelli e tentativi

Ogni livello del gioco corrisponde a una porta blindata con un codice segreto, scelto casualmente in un intervallo 
fisso, e un numero di tentativi a disposizione che diminuisce con il crescere del livello:

- **Livello 0** → 6 tentativi disponibili
- **Livello 1** → 5 tentativi disponibili
- **Livello 2** → 4 tentativi disponibili
* … fino al livello massimo definito nel programma (es. livello 3), oltre il quale il numero di tentativi resta fissato a un minimo (es. 3)

Il codice segreto è un numero intero compreso tra 1 e 50, generato casualmente ad ogni livello.

**NB**: Per generare un numero randomico basta importare il modulo [`random`](https://docs.python.org/3.11/library/random.html) 
e usare le funzioni che mette a disposizione. 

### Simboli di avanzamento

I tentativi rimasti vengono mostrati tramite una riga di simboli:

- `O` → tentativo ancora disponibile
- `X` → tentativo già utilizzato (fallito)

### Esempio di avanzamento a un livello con 5 tentativi, dopo 2 tentativi falliti

```
X X O O O
```

### Regole del gioco

1. Il gioco inizia al livello 0.
2. Ad ogni turno il giocatore digita da tastiera un numero come tentativo.
3. Se il tentativo non rientra nell'intervallo consentito (tra 1 e 50), viene consumato un tentativo e segnalato.
4. Se il tentativo è corretto, il giocatore passa al livello successivo.
5. Se il tentativo è sbagliato (ma valido), il programma mostra un indizio:
   - se il tentativo è più basso del codice → "Più alto"
   - se il tentativo è più alto del codice → "Più basso"
6. Il gioco termina in due casi:
   - il giocatore esaurisce i tentativi disponibili senza indovinare → livello perso
   - il giocatore raggiunge il livello massimo superandolo → gioco vinto
7. Il gioco termina quando il giocatore perde oppure vince tutti i livelli.

### Funzioni da implementare

Il programma di base fornito `vault_code.py` contiene già le definizioni delle funzioni principali che dovranno essere implementate:

---

**`gestisci_livello(livello)`**

**Descrizione:** Gestisce un singolo livello del caveau, mostrando i tentativi disponibili e verificando i codici inseriti.

**Parametri:**
* `livello`: un intero rappresentante il numero del livello corrente.

**Valore di ritorno:**
* `True` se il giocatore indovina il codice entro i tentativi disponibili.
* `False` se il giocatore esaurisce i tentativi senza indovinare.

---

**`stampa_tentativi(n, usati)`**

**Descrizione:** Stampa la riga dei tentativi disponibili, con `O` per i tentativi rimasti e `X` per quelli già usati.

**Parametri:**
* `n`: un intero che indica il numero totale di tentativi assegnati al livello.
* `usati`: un intero che indica quanti tentativi sono già stati utilizzati.

**Output:** Stampa la riga di simboli nella console. Nessun valore di ritorno.

---

**`dai_indizio(tentativo, codice)`**

**Descrizione:** Confronta il tentativo con il codice segreto e restituisce il messaggio di indizio appropriato.

**Parametri:**
* `tentativo`: un intero con il numero digitato dal giocatore.
* `codice`: un intero con il codice segreto del livello.

**Valore di ritorno:**
* una stringa contenente l'indizio ("Più alto" o "Più basso").

### Esempio di esecuzione

```console
=== Benvenuto in Vault Code ===

Livello 0) 6 tentativi
O O O O O O
Tentativo: 60
Il codice è tra 1 e 50
X O O O O O
Tentativo: 25
Più basso
X X O O O O
Tentativo: 12
Più alto
X X X O O O
Tentativo: 18
Accesso consentito!

Livello 1) 5 tentativi
O O O O O
Tentativo: 25
Più alto
X O O O O
Tentativo: 40
Più basso
X X O O O
Tentativo: 33
Accesso consentito!

Livello 2) 4 tentativi
O O O O
Tentativo: 25
Più basso
X O O O
Tentativo: 10
Più basso
X X O O
Tentativo: 5
Più alto
X X X O
Tentativo: 7
GAMEOVER: Tentativi esauriti!
X X X X
```


