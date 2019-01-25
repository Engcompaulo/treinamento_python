arquivo = open('teste.html', 'a', encoding='utf-8')

arquivo.write('<html>\n')

arquivo.write('<head>\n')

arquivo.write('</head>\n')

arquivo.write('<body>\n')

arquivo.write('<div>\n')
arquivo.write('<h1>Hello Word</h1>\n')

resp = str(input('Deseja adcionar uma publicação?: '))

while resp == 'sim' or resp == 's':
    categoria = str(input('Digite a categoria: '))
    fonte = str(input('Digite a fonte: '))
    link = str(input('Digite o link: '))
    nome_link = str(input('Digite o nome do link: '))
    arquivo.write('<div>\n')
    arquivo.write('<h2>'+categoria+'</h2>\n')
    arquivo.write('<h4>'+fonte+'</h4>\n')
    arquivo.write('<li><a href="'+link+'">'+nome_link+'</a></li>\n')
    arquivo.write('</div>\n')

    resp = str(input('Deseja adcionar uma publicação?: '))                      


arquivo.write('</div>\n')

arquivo.write('</body>\n')

arquivo.write('</html>\n')

arquivo.close()
