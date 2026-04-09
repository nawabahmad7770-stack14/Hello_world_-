#!/bin/bash
#!/bin/bash

read -p "Введите массу тела (кг): " weight
read -p "Введите рост (м): " height

bmi=$(( weight / height))

echo "Ваш индекс массы тела (ИМТ): $bmi"
