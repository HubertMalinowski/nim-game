import random


class Nim:
    def __init__(self, stacks: list):
        self.stacks = stacks  # Lista stosów

    def take_from_stack(self, i: int, k: int):
        """Usuwa k elementów ze stosu i"""
        if 0 <= i < len(self.stacks) and 0 < k <= self.stacks[i]:
            self.stacks[i] -= k
            return True
        return False

    def is_empty(self):
        """Sprawdza, czy wszystkie stosy są puste"""
        return all(stack == 0 for stack in self.stacks)

    def print_stacks(self):
        """Wypisuje aktualny stan stosów"""
        for index, count in enumerate(self.stacks):
            print(f"Stos {index}: " + "0 " * count)

    def nim_sum(self):
        """Oblicza XOR wszystkich stosów (kluczowe dla strategii Nim)"""
        result = 0
        for stack in self.stacks:
            result ^= stack
        return result

    def computer_move(self):
        """Komputer wykonuje ruch zgodnie ze strategią Nim"""
        nim_sum = self.nim_sum()

        # Jeśli nim_sum == 0, komputer wykonuje losowy ruch
        if nim_sum == 0:
            non_empty_stacks = [i for i, count in enumerate(self.stacks) if count > 0]
            stack = random.choice(non_empty_stacks)
            remove = random.randint(1, self.stacks[stack])
            self.take_from_stack(stack, remove)
            print(f"Komputer (losowy ruch): Stos {stack}, Usunięto {remove}")
            return

        # Znalezienie optymalnego ruchu
        for i, count in enumerate(self.stacks):
            target = count ^ nim_sum  # Nowa wartość stosu po optymalnym ruchu
            if target < count:  # Jeśli można zmniejszyć stos, wykonaj ruch
                remove = count - target
                self.take_from_stack(i, remove)
                print(f"Komputer (strategiczny ruch): Stos {i}, Usunięto {remove}")
                return
