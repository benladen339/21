import random


opp = random.randint(14, 23)

score = 0

x = 'gg'

while x != "n":
    x = input("Взять еще карту?\n[y / n] >")
    if x == "y":
        rand = random.randint(6, 14)
        if rand == 11:
            print("Вышла карта: Валет")
            score += 2
        elif rand == 12:
            print("Вышла карта: Дама")
            score += 3
        elif rand == 13:
            print("Вышла карта: Король")
            score += 4
        elif rand == 14:
            print("Вышла карта: Туз")
            score += 11
        else:
            print("Вышла карта " + str(rand))
            score += rand
        print("Очки: " + str(score))
        if score > 21:
            x = "n"

    if x == "n":
        print("\n####Итог####\nВаши очки: " + str(score) + "\nОчки противника: " + str(opp))
        if score > opp or opp > 21:
            if score < 22:
                print("\nПобеда")
                exit()
            if score > 21 and opp < 22:
                print("\nПроигрыш")
                exit()
            else:
                print("\nНичья")
        elif opp == score and opp < 22 and score < 22:
            print("\nНичья")
        else:
            print("\nПроигрыш")