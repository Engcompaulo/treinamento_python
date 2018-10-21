def maximoSeq2(vetor, n):
    max = vetor[0];
    for i in range(1, n):
        if max < vetor[i]:
            max = vetor[i];
    return max; 

print("Valor máximo em um vetor");    
vetor = [5, 7, 8, 4, 3, 6, 1, 9, 10, 2];
print("Vetor: ",vetor);

n = len(vetor);
print("Maior valor: ",maximoSeq2(vetor, n)); 
