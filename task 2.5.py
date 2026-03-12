print("=== Анализ последовательности ДНК ===\n")

dna = input("Введите последовательность ДНК: ")
dna_upper = dna.upper()
total_len = len(dna_upper)

print(f"\nПоследовательность в верхнем регистре: {dna_upper}")
print("\nПодсчёт нуклеотидов:")

for n in ['A', 'T', 'G', 'C']:
    count = dna_upper.count(n)
    percent = (count / total_len * 100) if total_len > 0 else 0
    print(f"{n}: {count} ({percent:.1f}%)")

print(f"\nОбщая длина: {total_len} нуклеотидов")
