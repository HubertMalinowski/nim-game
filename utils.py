import random
from nim import Nim


def create_game():
    """Creates a new game from user input"""
    stacks = list(
        map(int, input(f"Enter stack heights separated by spaces: ").split())
    )
    return Nim(stacks)


def human_vs_computer():
    """Human vs Computer game"""
    game = create_game()
    turn = 0  # 0 - player, 1 - computer

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
    stacks = [random.randint(1, 10) for _ in range(random.randint(3, 6))]
    game = Nim(stacks)

    print("Initial game state:")
    game.print_stacks()

    turn = 0  # 0 - computer 1, 1 - computer 2

    while not game.is_empty():
        game.computer_move()
        game.print_stacks()
        turn = 1 - turn  # Switch player

    print("Game over! Computer " + ("1" if turn == 1 else "2") + " wins!")
