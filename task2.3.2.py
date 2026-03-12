operator_name = input("Enter operator name:Ahmad ")
pressure_value = input("Enter current pressure sensor value: 115")
with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write("ОПЕРАТОР\tЗНАЧЕНИЕ\n")
    file.write(f"{operator_name}\t{pressure_value}\n")

print("Данные успешно сохранены в sensor_log.txt")
