#Programa que recebe a quantidade de dias, horas, minutos e segundo e calcula
#o total de segundos.

numeroDias = int(input("Digite o número de dias: ")); #Dias diferentes de 0
numeroHoras = int(input("Digite o número de horas: ")); 
numeroMinutos = int(input("Digite o número de minitos: "));
numeroSegundo = int(input("Digite o número de segundos: "));

totalSegundos = numeroDias * 60 * 60 * 24  + ((numeroHoras * 60 * 60) + (numeroMinutos * 60) + numeroSegundo);

print("O total de segundos é: %.4f"% totalSegundos);
