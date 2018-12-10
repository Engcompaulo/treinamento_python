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
