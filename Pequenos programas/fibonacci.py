print('Vamos calcular a sequencia de Fibonacci')
n = int(input('Digite o valor de n: '))
v1 = 0
v2 = 1
if n == v1:
	print('O valor do Fibonacci de: ',n ,'é: ',v2)
else:
	for i in range(2, n):
		fibo = v1 + v2;
		v1 = v2;
		v2 = fibo;
	print(fibo);