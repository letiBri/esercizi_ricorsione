from time import time
from functools import lru_cache


class Fibonacci:

    def __init__(self):
        self.cache = {0: 0, 1: 1}  # F(0) = 0 e F(1) = 1

    # metodo 1
    def calcola_elemento(self, n):
        # deve calcolare l'elemento di n, quindi restituire la sequenza di fibonacci fino a quel valore
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcola_elemento(n - 1) + self.calcola_elemento(n - 2)

    # metodo 2 con tecnica MEMORIZATION è più rapido
    def calcola_elemento_cache(self, n):
        if self.cache.get(n) is not None:  # adesso il problema semplice è "è già dentro la cache o no?"
            # se questa chiave di n è già presente nella mia cache di risultati, posso fare il return del risultato già presente
            return self.cache[n]
        else:
            self.cache[n] = (self.calcola_elemento_cache(n-1) + self.calcola_elemento_cache(n - 2))
            return self.cache[n]

    # metodo 3 con la cache di Python è ancora più rapido
    @lru_cache(maxsize=None)  # mettendo il decoratore, posso implementare il metodo come se non avessi la cache,
    # tanto Python memorizza da solo nella sua cache e non ricalcola se è gia presente nella cache
    def calcola_elemento_lru(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcola_elemento_lru(n-1) + self.calcola_elemento_lru(n-2)


if __name__ == '__main__':
    fib = Fibonacci()  # creo l'oggetto

    # provo il metodo 1
    start_time = time()
    print(fib.calcola_elemento(40))
    end_time = time()
    print(f"Elapsed time senza cache: {end_time-start_time}") # ci mette tanto

    # provo il metodo 2
    start_time = time()
    print(fib.calcola_elemento_cache(40))
    end_time = time()
    print(f"Elapsed time con cache: {end_time - start_time}") # non ci mette nulla

    # provo il metodo 3
    start_time = time()
    print(fib.calcola_elemento_lru(40))
    end_time = time()
    print(f"Elapsed time lru_cache: {end_time - start_time}") # non ci mette nulla
