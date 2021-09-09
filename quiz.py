
from termcolor import colored

print ( '''
           Projeto Semana Nacional da Ciência e Tecnologia 
                        Passa ou Repassa Quiz                
''')

print ('''Questão n°1
       ''')

print ('Qual é o coletivo de cães?')
print ('a) Matilha')
print ('b) Rebanho')
print ('c) Alcateia')
print ('''d) Manada
       ''')

team = input ('Qual time está respondendo? ')
pontos_team1 = 0
pontos_team2 = 0

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'a':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'a':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°2
       ''')

print ('Quantos dias tem um ano bissexto?')
print ('a) 350')
print ('b) 364')
print ('c) 365')
print ('''d) 366
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'd':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'd':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°3
       ''')

print ('Qual foi o último Presidente do período da ditadura militar no Brasil?')
print ('a) Costa e Silva')
print ('b) João Figueiredo')
print ('c) Ernestro Geisel')
print ('''d) Emílio Médici
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°4
       ''')

print ('Qual o maior osso do corpo humano?')
print ('a) Escápula')
print ('b) Braço')
print ('c) Tíbia')
print ('''d) Fêmur
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'd':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'd':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°5
       ''')

print ('Quantos centímetros têm um metro?')
print ('a) 10')
print ('b) 1000')
print ('c) 100')
print ('''d) 10000
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'c':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'c':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°6
       ''')

print ('O que está escrito na bandeira do Brasil?')
print ('a) Ordem em Progresso')
print ('b) Ordem com Progresso')
print ('c) Brasil acima de todos')
print ('''d) Ordem e Progresso
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'd':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'd':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°7
       ''')

print ('Qual é o país conhecido por ter o formato de uma bota?')
print ('a) França')
print ('b) Alemanha')
print ('c) Itália')
print ('''d) Suíça
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'c':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'c':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°8
       ''')

print ('Quais são as cores primárias?')
print ('a) Azul, verde e amarelo')
print ('b) Verde, laranja e vermelho')
print ('c) Azul, vermelho e amarelo')
print ('''d) Vermelho, amarelo e verde
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'c':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'c':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°9
       ''')

print ('Em qual país foi construído o campo de concentração de Auschwitz, maior da Alemanha Nazista?')
print ('a) Alemanha')
print ('b) Áustria')
print ('c) Polônia')
print ('''d) França
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'c':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'c':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°10
       ''')

print ('Qual o idioma falado na Angola?')
print ('a) Inglês')
print ('b) Português')
print ('c) Francês')
print ('''d) Angolano
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°11
       ''')

print ('Quantas consoantes tem a palavra desenvolvimento?')
print ('a) 15')
print ('b) 9')
print ('c) 6')
print ('''d) 8
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print ('''
Questão n°12
       ''')

print ('Qual inseto transmite a doença de Chagas?')
print ('a) Aedes aegypti')
print ('b) Barbeiro')
print ('c) Barata')
print ('''d) Percevejo
       ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print('''
Questão n°13
         ''')

print('Qual o feriado comemorado no dia 15 de novembro?')
print('a) Independência do Brasil')
print('b) Dia de Finados')
print('c) Proclamação da República')
print('''d) Dia da Consciência Negra
      ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'c':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'c':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print('''
Questão n°14
         ''')

print('Qual desses filmes nunca ganhou o Oscar de melhor filme?')
print('a) 12 Anos de Escravidão')
print('b) A Forma Da Água')
print('c) Birdman')
print('''d) Avatar
      ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'd':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'd':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print('''
Questão n°15
         ''')

print('Qual é a capital dos Estados Unidos?')
print('a) Nova York')
print('b) Washington')
print('c) Los Angeles')
print('''d) Chicago
      ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print('''
Questão n°16
         ''')

print('Quais são as cores presentes na bandeira da China?')
print('a) Vermelho e branco')
print('b) Vermelho e amarelo')
print('c) Laranja e amarelo')
print('''d) Vermelho, amarelo e branco
      ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print('''
Questão n°17
         ''')

print('Qual é o maior continente em extensão?')
print('a) Europa')
print('b) Américo')
print('c) África')
print('''d) Ásia
      ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'd':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'd':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print('''
Questão n°18
         ''')

print('Como é o nome da energia gerada pelo vento?')
print('a) Eólica')
print('b) Hídrica')
print('c) Térmica')
print('''d) Química
      ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'a':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'a':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')

print('''
Questão n°19
         ''')

print('Você tem 36 laranjas e joga um terço fora, com quantas você fica?')
print('a) 23')
print('b) 24')
print('c) 12')
print('''d) 18
      ''')

team = input ('Qual time está respondendo? ')

if team == '1':

    resposta = input('Digite uma das opções: ')

    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team1 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team1}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team1}')

elif team == '2':

    resposta = input('Digite uma das opções: ')
    if resposta == 'b':
        print (colored ('Certa resposta!', 'green'))
        pontos_team2 += 10             #pontos = pontos + 10
        print(f'Pontos acumulados até o momento: {pontos_team2}')

    else:
        print (colored ('Você errou!', 'red'))

        print (f'Pontos acumulados até o momento: {pontos_team2}')

skip = input ('Deseja continuar? ')

if skip == 'sim':
    print ('Continuando...')
