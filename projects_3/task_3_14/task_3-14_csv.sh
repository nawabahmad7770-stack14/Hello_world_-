#!/bin/bash

echo "=== Названия товаров ==="
awk -F ',' '{print $2}' data.csv

echo -e "\n=== Товары дороже 20 ==="
awk -F ',' '$3 > 20 {print $2, "-", $3}' data.csv

echo -e "\n=== Общая стоимость всех товаров ==="
total=$(awk -F ',' '{sum += $3} END {print sum}' data.csv)
echo "Общая стоимость: $total"

