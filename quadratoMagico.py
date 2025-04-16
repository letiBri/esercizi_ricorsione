def quadrato_magico(N):  # N è la dimensione del quadrato magico
    rimanenti = []
    for i in range(N * N):
        rimanenti.append(i)
    ricorsione([], rimanenti, N)

def ricorsione(parziale, rimanenti, N):
    # condizione terminale
    if len(parziale) == N*N: # mi fermo quando ho esaminato tutte le celle del quadrato
        print(parziale)
    # caso ricorsivo
    else:
        for i in range(len(rimanenti)):
            # mancaa il fatto di inserire i vincoli
            numero = rimanenti[i]
            parziale.append(numero)
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]  # salto elemento i
            ricorsione(parziale, nuovi_rimanenti, N)
            parziale.pop()

if __name__ == '__main__':
    quadrato_magico(3)
