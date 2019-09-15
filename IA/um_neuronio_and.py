print("Exemplo: Simulação do Operador Lógico AND.\n")

limiar_ativador = 2
print("Limiar de ativação: ", limiar_ativador)
print() #pular linha

#Pesos iniciais.
w1 = 1
w2 = 1
print("Pesos iniciais w1: ",w1," e w2: ",w2) 
print() #pular linha

# Entradas.
x1= [0, 0, 1, 1] 
x2= [0, 1, 0, 1]
print("Entradas.")
print("x1: ", x1)
print("x2: ", x2)

# Para guardar o potencial de ativação.
t = []

# Resultado.
r = []


for i in range(len(x1)):
    t.append(x1[i] * w1 + x2[i] * w2)
    if t[i] >= limiar_ativador:
        r.append(1)
    else:
        r.append(0)

print() #pular linha
print("Resultado: ", r)
