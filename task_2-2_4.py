reagent_name = input("Введите название нового реактива: ")
reagent_quantity = int(input("Введите его количество (целое число): "))
report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."
print(report)
with open("inventory.txt", "a", encoding="utf-8") as f:print(report, file=f)
