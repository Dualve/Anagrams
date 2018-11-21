"""
Lab №8(Strings and text processing)

Authors: Dubodelov A.V , Lebed A.S.
Version: 1.0
Group: 10701118
Date: 19.11.2018
"""

import Chek as ch
import random

word_tuple = ("привет", 'здравствуйте', "великолепно", "новый", "термопаста", "мерч", "всевластие", "дым", "ваза",
              "бутыль", "ковер", "аппарат", "автомобиль", "танк", "самолет", "корабль", "мичман", "бра", "половик",
              "бегать", "печка", "парк", "парка", "парикмахерская", "ноль", "чашка", "чай", "лестница", "стол", "дверь",
              "ручка",
              "карандаш", "лист", "предприятие", "здоровье", "плагин", "труднопроизносимый", "спутник",
              "предшествовать", "покровительство", "правительство", "журналист", "", "пассажир", "самоотверженность",
              "финансы", "электроэнергия", "мелкокалиберный", "мемориал", "опубликовать")

while True:
    starter = ch.chekInput("If you want to start programme press 1,\nelse press 2 for exit.\n", int)

    if starter == 1:
        word = list(word_tuple[random.randint(0, 50)])
        word1 = "".join(word)
        random.shuffle(word)
        print(" ".join(word))
        word2 = input("Enter your variant of word:\n")

        if word2.lower() == word1:
            print("Awesome! You guessed!")
            continue

        else:
            print("Wrong,right variant is {}".format(word))
            continue

    elif starter == 0:
        print("Goodbye.")
        break

    else:
        print("Wrong menu item.")
        continue
