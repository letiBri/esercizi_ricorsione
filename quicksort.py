
def quicksort(sequenza):
    if len(sequenza) == 1:
        return sequenza
    else:
        #1) scegliere pivot
        pivot = sequenza[0]
        #2) dividere sequenza in sottosequenze
        # sequenza_smaller = []
        # sequenza_larger = []
        # sequenza_pivot =[]
        # for i in sequenza:
        #     if(i<pivot):
        #         sequenza_smaller.append(i)
        #     elif (i>pivot):
        #         sequenza_larger.append(i)
        #     else:
        #         sequenza_pivot.append(i)

        sequenza_smaller = [n for n in sequenza if n < pivot]
        sequenza_larger = [n for n in sequenza if n > pivot]
        sequenza_pivot = [n for n in sequenza if n == pivot]
        return (quicksort(sequenza_smaller)+
                sequenza_pivot+
                quicksort(sequenza_larger))


if __name__ == '__main__':
    sequenza = [3, 5, 2, 9, 11, 4, 7]
    print(quicksort(sequenza))