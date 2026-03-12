sequences = ["ATATACGCGTA", "CTTCGGNGGA"]
for seq in sequences:
    print(f"Обработка последовательности: {seq}")
    print("Посимвольный вывод:")
    for nucleotide in seq:
        print(f"\t{nucleotide}")

    print("-" * 20)
print("Цикл выполнен")
