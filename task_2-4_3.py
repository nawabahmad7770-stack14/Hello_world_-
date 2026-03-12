total_capsules = int(input("Введите общее количество капсул: "))
pack_capacity = int(input("Введите вместимость одной упаковки (шт): "))
full_packs = total_capsules // pack_capacity
remaining_capsules = total_capsules % pack_capacity
print(f"Результат упаковки:")
print(f"\tПолных упаковок: {full_packs}")
print(f"\tОсталось капсул: {remaining_capsules}")
