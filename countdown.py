from time import sleep

#COUNTDOWN ITERATIVO
def countdown(n):
    while n >= 0:
        print(n)
        sleep(0.5)
        n -= 1
#rimango sempre nella stessa riga di debug dentro la stessa istanza del metodo


# COUNTDOWN RICORSIVO
def countdown_recursive(n):
    if n <= 0:  #condizione terminale
        print("stop")
    else: #scompongo il problema
        print(n)
        sleep(0.5) #aspetto 0.5, metto una pausa per vedere meglio il countdown
        counter = n - 1
        countdown_recursive(counter) #chiamo la funzione su questo counter --> n ora ha un valore uguale a counter!!
#quando lanci la funzione ricorsiva lanci proprio più volte il metodo, fai più istanze del metodo countdown_recursive su argomenti diversi,
#non stai ciclando sulla stessa funzione ma stai chiamando più volte il metodo con argomenti diversi
#nei cicli rimani dentro la stessa istanza del metodo, con la ricorsione crei tante istanze diverse dello stesso metodo
#fai crescere lo stack di chiamate
#quando esegui l'ultima chiamata chiude tutte le istanze del metodo aperte prima -> unwinding (per effetto a catena tutte le chiamate fatte prima si chiudono)


#quando faccio soluzione iterativa, rimango dentro l'istanza del metodo e itero su quello
#quando invece faccio ricorsivo --> chiamo TANTE volte lo stesso metodo (creo STACK di chiamate) --> faccio una chiamata per ogni valore di n
#il meccanismo fa accrescere lo stack di chiamate della stessa funzione, quando si arriva al problema piu piccolo possibile, TUTTE le chiamate che abbiamo fatto vengono terminate con effetto a catena (UNWINDING CALL STACK)

if __name__ == '__main__':
    #countdown(10)
    countdown_recursive(10)
