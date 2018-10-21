def maximoSeq1(vetor, n):
    max = vetor[0];
    #print(max)
    i = 1;

    while i <= n:
        if max < vetor[i]:
            max = vetor[i];
        i = i + 1;
    return max

print("Valor máximo em um vetor");
vetor = [5, 7, 8, 4, 3, 6, 1, 9, 10, 2];
print("Vetor :",vetor);

n = len(vetor)-1
print("Máximo: ",maximoSeq1(vetor, n));
