import random


class Nim:
    def __init__(self, stacks: list):
        self.stacks = stacks  # List of stacks

    def take_from_stack(self, i: int, k: int):
        """Removes k elements from stack i"""
        if 0 <= i < len(self.stacks) and 0 < k <= self.stacks[i]:
            self.stacks[i] -= k
            return True
        return False

    def is_empty(self):
        """Checks if all stacks are empty"""
        return all(stack == 0 for stack in self.stacks)

    def print_stacks(self):
        """Prints the current state of the stacks"""
        for index, count in enumerate(self.stacks):
            print(f"Stack {index}: " + "0 " * count)
        print(f"Nim Sum: {self.nim_sum()}")

    def nim_sum(self):
        """Calculates the XOR of all stacks (crucial for the Nim strategy)"""
        result = 0
        for stack in self.stacks:
            result ^= stack
        return result

    def computer_move(self):
        """Computer makes a move according to the Nim strategy"""
        nim_sum = self.nim_sum()

        # If nim_sum == 0, the computer makes a random move
        if nim_sum == 0:
            non_empty_stacks = [i for i, count in enumerate(self.stacks) if count > 0]
            stack = random.choice(non_empty_stacks)
            remove = random.randint(1, self.stacks[stack])
            self.take_from_stack(stack, remove)
            print(f"Computer (random move): Stack {stack}, Removed {remove}")
            return

        # Finding the optimal move
        for i, count in enumerate(self.stacks):
            target = count ^ nim_sum  # New stack value after the optimal move
            if target < count:  # If the stack can be reduced, make the move
                remove = count - target
                self.take_from_stack(i, remove)
                print(f"Computer (strategic move): Stack {i}, Removed {remove}")
                return
