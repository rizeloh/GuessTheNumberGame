import random

def guess_the_number():
    """
    Игра "Угадай число".
    """
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать его.")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Введите ваше предположение: ")

        # Проверяем, является ли введенное значение числом
        if not guess.isdigit():
            print("Пожалуйста, введите число.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Ваше число меньше загаданного. Попробуйте еще раз.")
        elif guess > number_to_guess:
            print("Ваше число больше загаданного. Попробуйте еще раз.")
        else:
            print(f"Поздравляем! Вы угадали число {number_to_guess} за {attempts} попыток.")
            break

if __name__ == "__main__":
    guess_the_number()
