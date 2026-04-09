#!/bin/bash

printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"

for file in *.fasta; do
    if [ ! -f "$file" ]; then
        echo "Файлы .fasta не найдены"
        break
    fi
    
    if [ ! -s "$file" ]; then
        continue
    fi
    
    sequence=$(grep -v "^>" "$file" | tr -d '\n')

    count_A=$(echo "$sequence" | grep -o -i "A" | wc -l)
    count_T=$(echo "$sequence" | grep -o -i "T" | wc -l)
    count_G=$(echo "$sequence" | grep -o -i "G" | wc -l)
    count_C=$(echo "$sequence" | grep -o -i "C" | wc -l)
    
    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
done
