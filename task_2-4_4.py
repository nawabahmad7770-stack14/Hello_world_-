total_volume = float(input("Введите требуемый объем раствора (мл): "))
nacl_mass = total_volume * 0.009
water_volume = total_volume
recipe_content = (
    f"--- Рецепт физраствора (0.9%) ---\n"
    f"Общий объем:\t{total_volume} мл\n"
    f"Масса соли (NaCl):\t{nacl_mass:.2f} г\n"
    f"Объем воды:\t\t{water_volume} мл\n"
    f"----------------------------------")
with open("recipe.txt", "w", encoding="utf-8") as f:
    f.write(recipe_content)
print("\nРецепт успешно сохранен в файл recipe.txt:")
print(recipe_content)
