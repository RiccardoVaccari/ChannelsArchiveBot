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
- [ ] Cerca con query:
    ...


## States:
- HOME
- RECCOMEND_CHANNEL
    - DESCRIPTION_CHANNEL
    - TAGS_CHANNEL
    - LANGUAGE_CHANNEL
- SEARCH_QUERY
