import random


def main():
    # roll = 5
    # roll = random.randint(1, 6)
    dice_rolls = int(input('Quantosdados você gostaria de lançar?'))
    dice_sums = 0
    dice_size = int(input('Quantos lados são os dados?'))
    for i in range(0, dice_rolls):
        roll = random.randint(1, dice_size)
        dice_sums += roll
        if roll == 1:
            print(f'Você obteve um {roll} : falha critica')
        elif roll == dice_size:
            print(f'Voce você obteve um {roll} : Sucesso critico!')
        else:
            print(f'Você rolou um {roll}')
    print(f'soma dos dados foi { dice_sums }')


if __name__ == "__main__":
    main()
