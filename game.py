import random

opcoes = {1: 'pedra', 2: 'papel', 3: 'tesoura'}
ganhou = 'Você ganhou, uhuu'
perdeu = 'Você perdeu, você é muito ruim!'

while True:
    sua_escolha = input('pedra, papel ou tesoura?')
    num = random.randint(1,3)
    escolha_pc = opcoes[num]

    if sua_escolha == 'pedra' and escolha_pc == 'tesoura':
        result = ganhou

    elif sua_escolha == 'tesoura' and escolha_pc == 'papel':
        result = ganhou

    elif sua_escolha == 'papel' and escolha_pc == 'pedra':
        result = ganhou

    elif sua_escolha == escolha_pc:
        result = 'Empate feio'

    else:
        result = perdeu

    print(f'{result}, você escolheu {sua_escolha} e o pc escolheu {escolha_pc}')
    continua = input('Deseja jogar novamente? (sim ou não)')

    if continua != 'sim':
        break
