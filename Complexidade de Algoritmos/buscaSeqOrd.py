def buscaSeqOrd(vetor, n, chave):
    for i in range(1 ,n):
        if chave <= vetor[i]:
            if chave == vetor[i]:
                return i
            else:
                return -1
    return -1

print("Busca em vetor ordenado. Exemplo, buscar o número 8.");
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
print(vetor);

n = len(vetor);
print("Posição: ", buscaSeqOrd(vetor, n, 8) + 1);
