def buscaBin(vetor, ini, fim, chave):
    if ini > fim:
        return -1
    meio = round((ini + fim)/2);
        
    if chave == vetor[meio]:
        return meio;

    if chave > vetor[meio]:
        meio = meio + 1;
        return buscaBin(vetor, meio, fim, chave);
    
    else:
        meio = meio - 1;
        return buscaBin(vetor, ini, meio, chave);

print("Busca binária. Vetor ordenado 1~10. Ex: Buscar o número 7")
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
print("Vetor:  ",vetor)

n= len(vetor)-1;
print("Posição: ",buscaBin(vetor, 0, n, 7) + 1);

