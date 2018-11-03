def maxRec(vetor, n):
    if n == 0:
        return vetor[0];
    max = maxRec(vetor, n-1);
    if max > vetor[n]:
        return max;
    else:
        return vetor[n]

print("Valor máximo em um vetor. Versão recursiva");
vetor = [5, 7, 8, 4, 3, 6, 1, 9, 10, 2];
print("Vetor :",vetor);

n = len(vetor)-1
print("Máximo: ",maxRec(vetor, n));
