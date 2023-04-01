import random

opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
ganhou = 'Você ganhou, uhuu'
perdeu = 'Você perdeu, seu noob'

while True:
    sua_escolha = input('Pedra, papel ou tesoura?')
    num = random.randint(1,3)
    escolha_pc = opcoes[num]

    if sua_escolha == 'Pedra' and escolha_pc == 'Tesoura':
        result = ganhou

    elif sua_escolha == 'tesoura' and escolha_pc == 'papel':
        result = ganhou

    elif sua_escolha == 'Papel' and escolha_pc == 'Pedra':
        result = ganhou

    elif sua_escolha == escolha_pc:
        result = 'Empate feio'

    else:
        result = perdeu

    print(f'{result}, você escolheu {sua_escolha} e o pc escolheu {escolha_pc}')
    continua = input('Deseja jogar novamente? (sim ou não)')

    if continua != 'Sim':
        break