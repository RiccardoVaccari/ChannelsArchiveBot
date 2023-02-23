## TODO
- [x] Aggiunta canale:
    - [x] Messaggio con regole -> testo + (state=RECCOMEND_CHANNEL) 
    - [x] Messaggio per descrizione -> testo + (state=DESCRIPTION_CHANNEL)
    - [x] Messaggio per tags -> testo + (state=TAGS_CHANNEL)
    - [x] Messaggio per linuga -> testo + (state=LANGUAGE_CHANNEL)
    - [x] Scelta categoria -> testo + buttons + (state=HOME)
- [x] Pubblicazione canale:
    ogni giorno alle 9 e alle 19 vengono pubblicati 3 canali alla volta.
    1. Ottengo i canali in base al parametro `added_on`
    2. Per ogni canale genero il testo del messaggio
    3. Keyboard con i ratings
    4. Pubblico i 3 messaggi
    5. Salvo i messaggi nella tabella `messages`
- [x] Recensione canale:
    al click del pulsante (con stella), viene creato un nuovo record con il voto dell'utente, oppure aggiornato il record se l'utente aveva già votato. NON viene aggiornato immediatamente il messaggio del canale ??
- [x] Cerca:
    - [x] Search by query:
        la ricerca avviene nella colonna `name` e `description` 
        1. ottenere risultato con colonna `name` e `description`, sommarli e convertire in set()
        2. ordinare in base al rating
        3. creare keyboard con index della lista
        4. inviare un messaggio unico con 3 canali
    - [x] Search by category:
        1. Messaggio con scelta categorie
        2. Messaggio con conali di quella categoria


## States:
- HOME
- RECCOMEND_CHANNEL
    - DESCRIPTION_CHANNEL
    - TAGS_CHANNEL
    - LANGUAGE_CHANNEL
- SEARCH_QUERY
