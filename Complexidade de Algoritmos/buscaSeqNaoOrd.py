def buscaSeqNaoOrd(vetor, n, chave):
    for i in range(n):
        if chave == vetor[i]:
            return i
    return -1

print("Busca sequencial não ordenada. Exemplo, buscar o número 1.");
vetor = [5, 7, 8, 4, 3, 6, 1, 9, 0, 2];
print(vetor);

n = len(vetor);
print("Posição: ", buscaSeqNaoOrd(vetor, n, 1) + 1); #Somando um pois o vetor começa em 0.
