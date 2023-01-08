

fruits = {"Apple":130,
"Avocado":50,
"Banana":110,
"Cherry":50,
"Cantaloupe":50,
"Grapefruit":60,
"Grapes":90,
"Honeydew Melon":50,
"Kiwifruit":90,
"Lemon":15,
"Nectarine":60,
"Lime":20,
"Orange":80,
"Peach":60,
"Watermelon":80,
"Tangerine":50,
"Sweet Cherries":100,
"Strawberries":50,
"Plums":50,
"Pineapple":50,
"Pear":100,
}
fruits_asked = input("Item: ")


for fruit in fruits:
    if fruit.lower() == fruits_asked:
        print("Calories:", fruits[fruit])
      





