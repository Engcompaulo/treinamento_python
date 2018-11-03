def maxRec2(vetor, ini, fim):
    if ini == fim:
        return vetor[ini];
    meio = round((ini + fim)/2);
    max1 = maxRec2(vetor, ini, meio);
    max2 = maxRec2(vetor, meio+1, fim);
    if max1 > max2:
        return max1;
    else:
        return max2;

print("Valor máximo em um vetor. Versão recursiva");
vetor = [5, 7, 8, 4, 3, 6, 1, 9, 10, 2];
print("Vetor :",vetor);

ini = 0;
fim = len(vetor)-1
print("Máximo: ",maxRec2(vetor, ini, fim));
