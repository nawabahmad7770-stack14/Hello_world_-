ph = float(input("Enter the pH level (0-14): "))
if ph < 7:
    print("Environment: Acidic (Кислая)")
elif ph == 7:
    print("Environment: Neutral (Нейтральная)")
elif ph <= 14:
    print("Environment: Alkaline (Щелочная)")
else:
    print("Error: pH values typically range from 0 to 14.")
