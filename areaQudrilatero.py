print("Vamos calcular a área de um quadrilatero");
unidade = str(input("Primeiramente, digite a unidade de medida. Ex: cm: "));
base = float(input("Inicialmente, digite a base do polígono: "));
altura = float(input("Agora, digite a altura: "));

area = base * altura;
print("A área deste polígono é: %5.2f %s"% (area, unidade));


