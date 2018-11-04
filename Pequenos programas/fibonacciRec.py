def fibonacciRec(numero):
    if numero == 0 or numero == 1:
        return numero;
    else:
        return fibonacciRec(numero-1) + fibonacciRec(numero-2);

numero = int(input("Digite um número inteiro para calcular Fibonacci: "));
print(fibonacciRec(numero));
