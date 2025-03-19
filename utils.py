import random
from nim import Nim


def human_vs_computer():
    """Gra człowiek vs komputer"""
    n = int(input("Podaj liczbę stosów: "))
    stacks = list(
        map(int, input(f"Podaj {n} wysokości stosów oddzielone spacją: ").split())
    )

    game = Nim(stacks)
    turn = 0  # 0 - gracz, 1 - komputer

    while not game.is_empty():
        game.print_stacks()
        if turn == 0:  # Ruch gracza
            while True:
                try:
                    stack = int(input("Wybierz stos: "))
                    remove = int(input("Ile chcesz usunąć? "))
                    if game.take_from_stack(stack, remove):
                        break
                    else:
                        print("Niepoprawny ruch, spróbuj ponownie.")
                except ValueError:
                    print("Podaj poprawne liczby!")
        else:  # Ruch komputera
            game.computer_move()

        turn = 1 - turn  # Zmiana gracza

    print("Koniec gry! " + ("Gracz wygrał!" if turn == 1 else "Komputer wygrał!"))


def computer_vs_computer():
    """Symulacja gry komputer vs komputer"""
    stacks = [random.randint(1, 10) for _ in range(random.randint(3, 6))]
    game = Nim(stacks)

    print("Początkowy stan gry:")
    game.print_stacks()

    turn = 0  # 0 - komputer 1, 1 - komputer 2

    while not game.is_empty():
        game.computer_move()
        game.print_stacks()
        turn = 1 - turn  # Zmiana gracza

    print("Koniec gry! Wygrał komputer " + ("1" if turn == 1 else "2"))
