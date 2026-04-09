#!/bin/bash

echo "Создание файлов:"
for i in {1..10}; do
    touch "test$i.txt"
    echo "Создан test$i.txt"
done

echo  "Удаление файлов в обратном порядке:"
count=10
while [ $count -ge 1 ]; do
    rm "test$counter.txt"
    echo " Удалён test$counter.txt"
    count=$((count - 1))
done

echo "Готово!"
