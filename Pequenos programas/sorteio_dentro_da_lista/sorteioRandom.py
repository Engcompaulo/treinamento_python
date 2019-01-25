import random as rd
from time import sleep


lista_participantes = 'participantes.txt'
lista_participantes_no_codigo = []

with open(lista_participantes) as arquivo:
    for linha in arquivo:
        participante = str(linha)
        lista_participantes_no_codigo.append(participante.replace('\n', ''))

for indice, valor in enumerate(lista_participantes_no_codigo):
    print(indice,' ',valor)
#for i in range(20):  #Caso seja mais de um sorteio

print('\nA cima é a lista com os participantes !')
sleep(3)
total_participantes = len(lista_participantes_no_codigo) #Aqui entra o total. Exemplo 100
print('Vai começar o sroterio, boa sorte !!!')
print('Processando...')
sleep(3)
print('Concluido !!!!')
sleep(2)

ganhador = rd.randrange(1, total_participantes)
print(ganhador)
print('E o ganhador é ??????')
sleep(3)
print('Parabéns !!!!! ',lista_participantes_no_codigo[ganhador])
