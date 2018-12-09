print("Cadastro de funcionarios")

funcionarios = []

def cadastro():
    print("Processo de cadastro iniciado")
    nome= str(input("Digite o nome do funcionario: "))
    idade= int(input("Digite a idade: "))
    sexo= str(input("Digite o sexo: "))
    dados = [nome, idade, sexo]
    return dados


print("Deseja cadastrar um novo funcionario? ")
resposta = str(input("Sim ou Não: "))

while resposta == "Sim" or resposta == "sim":
    funcionarios.append(cadastro())
    print("Deseja cadastrar um novo funcionario? ")
    resposta = str(input("Sim ou Não: "))

#print(funcionarios)

tamanhoLista = len(funcionarios)

for i in range(tamanhoLista):
    print(funcionarios[i])


    
