def fatorialRec(numero):
    if numero == 0 or numero == 1:
        return 1;
    else:
        return numero * fatorialRec(numero - 1);

# import pytest #Para realização de teste
# @pytest.mark.parametrize("entrada, saida_esperada",[
#     (0, 1),
#     (1, 1),
#     (2, 2),
#     (3, 6),
#     (4, 24),
#     (5, 120)
#     ])

def testa_fatorial(entrada, saida_esperada):
    assert fatorialRec(entrada) == saida_esperada



numero = int(input("Digite o número que deseja calcular o fatorial: "));
print(fatorialRec(numero));