def maximoSeq2(vetor, n):
    max = vetor[0];

    for i in range(n):
        if max < vetor[i]:
            max = vetor[1];
    return max;

print("Valor máximo em um vetor");    
vetor = [5, 7, 8, 4, 3, 6, 1, 9, 0, 2];
print(vetor);

n = len(vetor)
print("Posição: ",maximoSeq2(vetor, n) + 1); #Somando um pois o vetor começa em 0.
