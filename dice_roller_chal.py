import random
'''
    Explicando o game :
    vence que tiver mais pontos no game são três rodadas
    e em cada rodada o jogador tem direito de jogar entre três dados
    se jogar 1 dados seu numero é multiplicado por 6
    se jogar 2 dados seu numero é multiplicado por 3
    se jogar 3 dados seu numero é multiplicado por 1
    vence o jogador que tiver mais pontos no fim das 3 rodadas.
'''


def Dados(quantidade_dados):
    roll_sum = 0

    for i in range(0, quantidade_dados):
        roll = random.randint(1, 6)
        roll_sum += roll
    if quantidade_dados == 1:
        return roll_sum*6
    elif quantidade_dados == 2:
        return roll_sum*3
    elif quantidade_dados == 3:
        return roll_sum*1
    else:
        print('Erro não escolheu nenhuma das opções então leva penalidade...')
        return 0


def main():
    print("Starting... o game 6 3 1")
    jogador1 = input('Qual é seu nome jogador 1 ?')
    jogador2 = input('Qual é seu nome jogador 2 ?)')
    print('Começaremos nossa primeira rodada ----------😁')
    quantidade_dados1 = int(
        input(f'Quantos dados lançara { jogador1 } 1 2 ou 3?'))
    quantidade_dados2 = int(
        input(f'Quantos dados lançara { jogador2 } 1 2 ou 3?'))
    placar_jogador1 = 0
    placar_jogador2 = 0

    placar_jogador1 = Dados(quantidade_dados1)
    placar_jogador2 = Dados(quantidade_dados2)

    print(f'Jogador { jogador1 } seu placar {placar_jogador1}')
    print(f'Jogador { jogador2 } seu placar {placar_jogador2}')


if __name__ == "__main__":
    main()
