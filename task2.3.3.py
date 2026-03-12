full_name = input("Введите ФИО исследователя:")
date = input("Введите дату (): ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод:")
border = "=" * 50
header = "ЭЛЕКТРОННЫЙ ЛАБОРАТОРНЫЙ ЖУРНАЛ"
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(f"{border}\n")
    file.write(f"{header.center(50)}\n")
    file.write(f"{border}\n\n")

    file.write(f"ДАТА: {date}\n")
    file.write(f"ИССЛЕДОВАТЕЛЬ: {full_name}\n")
    file.write(f"ЭКСПЕРИМЕНТ: {experiment_name}\n")

    file.write(f"\nВЫВОД:\n\t{conclusion}\n\n")
    file.write(f"{border}\n")
print("Файл 'journal.txt' успешно сформирован!")
