media_name = input("Введите название питательной среды:Bact Medium ")
agar_concentration = input("Введите концентрацию агара (%):20 ")
sterilization_temp = input("Введите температуру стерилизации (120°C): ")


with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"Название среды: {media_name}\n")
    file.write(f" - Концентрация агара: {agar_concentration}%\n")
    file.write(f" - Температура стерилизации: {sterilization_temp}°C\n")

print("Файл 'recipe.txt' успешно сформирован!")
