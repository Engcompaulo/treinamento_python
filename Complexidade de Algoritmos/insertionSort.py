def insertionSort(vetor, n):
    for i in range(1, n):
        j = i;
        while (j > 0) and (vetor[j] < vetor[j-1]):
            aux = vetor[j];
            vetor[j] = vetor[j-1];
            vetor[j-1] = aux;
            j = j-1;
    return vetor

print("Ordenação por inserção");
vetor = [5, 7, 8, 4, 3, 6, 1, 9, 10, 2];
print(vetor);

n = len(vetor);
print("Ordenação: ",insertionSort(vetor, n));
