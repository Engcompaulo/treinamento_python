#Operadores
print(5+3)
print(5-3)
print(5*3)
print(5/3)
print(5//3)
print(5%3)
print('67 < 10: ',67 < 10)                                       #False
print('11 > 10: ',11 > 10)                                       #True
print('5 > 4 and 6 > 10: ',5 > 4 and 6 > 10)                     #False
print('True or False: ',True or False)                           #Ture
print('True and False: ',True and False)                         #False
print('True or 5 > 45: ',True or 5 > 45)                         #True
print('len("A vida é bela") > 7: ',len('A vida é bela') > 7)     #True

altura = 100
largura = 45
area = altura * largura
msg = 'A altura mede {} m e a largura mede {} m, com isso a área é {} m².'
print(msg.format(altura, largura, area))


mes = {
  'janeiro': 31,
  'fevereiro': 27,
  'março': 31,
  'abril':30,
  'maio':31,
  'junho':30,
  'julho': 31,
  'agosto':31,
  'setembro':30,
  'outubro':31,
  'novembro':30,
  'dezembro':31
}
print(mes)
print(sorted(mes))
print('\n')
print('\n'.join(mes))
print(mes['abril'])
mesNome = sorted(mes)[0]
mesDia = mes['abril']
msg2 = 'O mês {} tem {} dias'
print(msg2.format(mesNome, mesDia))
