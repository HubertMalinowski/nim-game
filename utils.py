import random
from nim import Nim


def create_game_from_input():
    """Creates a new game from user input"""
    stacks = list(
        map(int, input(f"Enter stack heights separated by spaces: ").split())
    )
    return Nim(stacks)


def create_random_game():
    """Creates a random game based on parameters from the user"""
    while True:
        try:
            max_stacks = int(input("Enter max number of stacks: "))
            max_height = int(input("Enter max stack height: "))
            break
        except ValueError:
            print("Enter valid numbers!")
    stacks = [random.randint(1, max_height) for _ in range(random.randint(1, max_stacks))]
    return Nim(stacks)


def decide_player():
    """Creates a game based on user input"""
    while True:
        choice = input("Who should start the game, (p)layer or (c)omputer? ").lower()
        if choice in ['p', 'c']:
            break
        print("Invalid input!")
    return 0 if choice == 'p' else 1


def create_game():
    """Queries the user about game parameters"""
    while True:
        choice = input("Should the game be (r)andom or from (i)nput? ")
        if choice in ['r', 'i']:
            break
        print("Invalid input!")
    if choice == 'r':
        return create_random_game()
    if choice == 'i':
        return create_game_from_input()


def human_vs_computer():
    """Human vs Computer game"""
    game = create_game()
    turn = decide_player()

    while not game.is_empty():
        game.print_stacks()
        if turn == 0:  # Player's move
            while True:
                try:
                    stack = int(input("Choose a stack: "))
                    remove = int(input("How many do you want to remove? "))
                    if game.take_from_stack(stack, remove):
                        break
                    else:
                        print("Invalid move, try again.")
                except ValueError:
                    print("Enter valid numbers!")
        else:  # Computer's move
            game.computer_move()

        turn = 1 - turn  # Switch player

    print("Game over! " + ("Player wins!" if turn == 1 else "Computer wins!"))


def computer_vs_computer():
    """Simulation of computer vs computer game"""

    game = create_game()
    turn = 0  # 0 - computer 1, 1 - computer 2

    print("Initial game state:")
    game.print_stacks()
    while not game.is_empty():
        game.computer_move()
        game.print_stacks()
        turn = 1 - turn  # Switch player

    print("Game over! Computer " + ("1" if turn == 1 else "2") + " wins!")
