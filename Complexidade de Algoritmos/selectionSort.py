def selectionSort(vetor, n):
    n = n - 1;
    for i in range(n, 1, -1):
        im = 0;
        for j in range(n+1):
           if vetor[j] > vetor[im]:
               im = j;
           if im < i:
               aux = vetor[i];
               vetor[i] = vetor[im];
               vetor[im] = aux;
    return vetor
            
            

print("Ordenação por seleção.");
vetor = [5, 7, 8, 4, 3, 6,1, 9, 10, 2];
print("Vetor:     ",vetor);

n = len(vetor);
print("Ordenação: ",selectionSort(vetor, n));
