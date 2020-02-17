print('\nDigite...\n1 - PARA INICIAR O PROGRAMA\n2 - PARA SAIR')
proc = int(input())
print('_'*130)
if proc == 2:
    print('\nVOCÊ SAIU!')
while proc < 1 or proc >2:
    proc = int(input('Valor Inválido. Digite novamente: '))

while proc == 1:
    lista = []
    id = int(input('Digite seu id:'))
    nome = input('Digite seu nome:')
    sobrenome = input('Digite seu sobrenome:')
    idade = int(input('Digite sua idade:'))
    sexo = input('Digite seu sexo:')
    print('\nDigite...\n1 - PARA CADASTRAR NOVAMENTE\n2 - PARA SAIR')
    proc = int(input())
    print()
    dicionario = {'id':id, 'nome':nome, 'sobrenome':sobrenome, 'idade':idade, 'sexo':sexo}
    lista.append(dicionario)

    with open('C:/Users/900146/Documents/git/TrabalhosPython/AmDev/Amdev.txt', 'a') as arquivo:
        for p in lista:
            arquivo.write(f"{p['id']};{p['nome']};{p['sobrenome']};{p['idade']};{p['sexo']}\n")

    if proc == 2:
        print('Você saiu!')
        break

    while proc < 1 or proc > 2:
        proc = int(input('Valor Inválido. Digite novamente: '))

