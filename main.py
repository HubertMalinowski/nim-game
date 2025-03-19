from nim import Nim
from utils import computer_vs_computer, human_vs_computer


if __name__ == "__main__":
    print("Choose a mode:")
    print("1 - Human vs Computer game")
    print("2 - Computer vs Computer simulation")
    mode = input("Choice: ")

    if mode == "1":
        human_vs_computer()
    elif mode == "2":
        computer_vs_computer()
    else:
        print("Invalid choice.")
