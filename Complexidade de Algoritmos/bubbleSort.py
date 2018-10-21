def bubbleSort(vetor, n):
    for i in range(n, 0, -1):
        trocou = False;
        for j in range(i):
            if vetor[j] > vetor[j+1]:
                aux = vetor[j];
                vetor[j]= vetor[j+1]
                vetor[j+1] = aux;
                trocou = True;
        if trocou == False:
            return vetor
       

print("Método de ordenação. Método da bolha.");
vetor = [7, 5, 8, 4, 3, 6, 1, 9, 10, 2];
print("Vetor:     ",vetor);

n = len(vetor)-1;
print("Ordenação: ",bubbleSort(vetor, n));
