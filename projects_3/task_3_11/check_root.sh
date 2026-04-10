#!/bin/bash
read -p "COICHE 1-2:" EUID
check_root() {
    if [ "$EUID" == 0 ]; then
        echo "Проверка пройдена: скрипт запущен от имени root (UID: $EUID)"
    else
        echo "Ошибка: Скрипт должен выполняться с правами суперпользователя!"
    fi
}
check_root
