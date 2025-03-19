from nim import Nim
from utils import computer_vs_computer, human_vs_computer


if __name__ == "__main__":
    print("Wybierz tryb:")
    print("1 - Gra Człowiek vs Komputer")
    print("2 - Symulacja Komputer vs Komputer")
    mode = input("Wybór: ")

    if mode == "1":
        human_vs_computer()
    elif mode == "2":
        computer_vs_computer()
    else:
        print("Niepoprawny wybór.")
