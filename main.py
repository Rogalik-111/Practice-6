import random

print("Игра: камень, ножницы, бумага")
print("Введите: камень, ножницы или бумага. Для выхода напишите: выход")

variants = ["камень", "ножницы", "бумага"]

wins = 0
losses = 0
draws = 0

while True:
    player = input("Ваш выбор: ").lower().strip()

    if player == "выход":
        break

    if player not in variants:
        print("Нужно ввести: камень, ножницы или бумага.")
        continue

    computer = random.choice(variants)
    print("Компьютер выбрал:", computer)

    if player == computer:
        print("Ничья!")
        draws = draws + 1
    elif (player == "камень" and computer == "ножницы") or \
         (player == "ножницы" and computer == "бумага") or \
         (player == "бумага" and computer == "камень"):
        print("Вы победили!")
        wins = wins + 1
    else:
        print("Вы проиграли!")
        losses = losses + 1

    print("Счёт: побед -", wins, ", поражений -", losses, ", ничьих -", draws)
    print()

print("Игра окончена.")
print("Итог: побед -", wins, ", поражений -", losses, ", ничьих -", draws)
