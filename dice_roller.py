import random


def main():
    # roll = 5
    # roll = random.randint(1, 6)
    dice_rolls = 2
    dice_sums = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1, 6)
        dice_sums += roll
        print(f'Você deu um {roll}')
    print(f'soma dos dados foi { dice_sums }')


if __name__ == "__main__":
    main()
