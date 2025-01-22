import random
numero_secreto = random.randint(1 , 20)

for numero in range(1, 6 ):
    numero = int(input('Pense em um número entre 1 e 20:'))

    if numero > numero_secreto:
        print('Seu palpite é muito alto. Tente novamente.')
    elif numero < numero_secreto:
        print('Seu palpite é muito baixo . Tente novamente.')
    elif numero == numero_secreto:
        print(f'Parabéns ! Vc acertou o número secreto, era {numero_secreto}.Vc ganhou!') 
        break
else:
  print(f'Vc perdeu ! O número secreto, era {numero_secreto}.')       
