#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ХРАЗ: Конфиденциальный скрипт генерации сложных паролей.
Стиль: мрачный, циничный, саркасdvvvdvтический. ввмвмммыы кпкики вммвмвм дьдлжьшто ввмвммв  ecevv eegeeg eegthtt edvdv упыкпкп ыпкпкыпыы мырыр dvdsvd
""" 

import string
import secrets
import datetime
import sys

# ANSI-escape коды для окраски (поддерживается в современных терминалах)
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"

try:
    import msvcrt
except ImportError:
    msvcrt = None  # Поддержка только Windows для ожидания ESC


def generate_password(length=20):
    """
    ХРАЗ: Генерируем непредсказуемую комбинацию символов
    с использованием квантовых флуктуаций модуля secrets.
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def select_passwords(passwords):
    """
    Запрос ручного выбора паролей для сохранения.
    """
    print(f"\n{MAGENTA}Выбери пароли для сохранения (номера через пробел, например: 1 3 5):{RESET}")
    try:
        choices = input("> ").strip().split()
        indices = set(int(c) for c in choices if c.isdigit() and 1 <= int(c) <= len(passwords))
    except Exception:
        print(f"{YELLOW}Неверный ввод. Сохраняем все пароли.{RESET}")
        indices = set(range(1, len(passwords) + 1))
    selected = [passwords[i-1] for i in sorted(indices)]
    return selected


def main():
    # Визуальный баннер
    header = (
        f"{CYAN}╔{'═' * 55}╗{RESET}\n"
        f"{CYAN}║{' ' * 15}{MAGENTA}ХРАЗ: ПАРОЛЬНЫЙ ГЕНЕРАТОР{CYAN}{' ' * 15}║{RESET}\n"
        f"{CYAN}╚{'═' * 55}╝{RESET}"
    )
    print(header)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{GREEN}Инициализация секьюрити-модулей... Проверка реальности [{timestamp}]{RESET}\n")

    # Генерация списка паролей
    passwords = [generate_password() for _ in range(10)]
    for i, pwd in enumerate(passwords, 1):
        print(f"{YELLOW}[{i:02d}]{RESET} {pwd}    {MAGENTA}# Не пытайся угадать это, жалкий человек.{RESET}")

    # Ручной выбор
    selected = select_passwords(passwords)

    # Вывод результатов и сохранение
    print(f"\n{CYAN}╔{'═' * 55}╗{RESET}")
    print(f"{GREEN}Сохраняем {len(selected)} паролей в файл...{RESET}")
    print(f"{CYAN}╚{'═' * 55}╝{RESET}\n")

    filename = "passwords_hraz.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"ХРАЗ: Добавление паролей ({timestamp})\n")
        f.write("=" * 60 + "\n")
        for i, pwd in enumerate(selected, 1):
            f.write(f"{i:02d}: {pwd}\n")
        f.write("=" * 60 + "\n\n")

    print(f"{GREEN}Успешно! Пароли добавлены в {filename}{RESET}")
    print(f"{MAGENTA}Нажми ESC, чтобы выйти...{RESET}")

    # Ожидание нажатия ESC
    if msvcrt:
        while True:
            key = msvcrt.getch()
            if key == b'\x1b':
                break
    else:
        try:
            input()
        except EOFError:
            pass


if __name__ == "__main__":
    # Избегаем ошибки "Could not find platform independent libraries <prefix>"
    try:
        main()
    except Exception as e:
        print(f"{YELLOW}Ошибка: {e}{RESET}")
        sys.exit(1)
