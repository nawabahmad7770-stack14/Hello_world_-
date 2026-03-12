COLLECTION_DATE = "12.03.2026"
sequence = input("Введите последовательность ДНК: ").upper()
total_len = len(sequence)
gc_count = sequence.count('G') + sequence.count('C')
gc_content = (gc_count / total_len) * 100 if total_len > 0 else 0
print(f"\n--- Отчет об анализе ---")
print(f"Дата взятия образца: {COLLECTION_DATE}")
print(f"Длина последовательности: {total_len} bp")
print(f"GC-состав: {gc_content:.2f}%")
print(f"------------------------")
