#!/usr/bin/python3
import random
import os
from collections import deque


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        if mines >= width * height:
            raise ValueError("Number of mines must be less than board size.")

        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))

        self.revealed = [
            [False for _ in range(width)]
            for _ in range(height)
        ]

        self.flagged = [
            [False for _ in range(width)]
            for _ in range(height)
        ]

    def print_board(self, reveal=False):
        clear_screen()

        print("    " + " ".join(f"{i:2}" for i in range(self.width)))

        for y in range(self.height):
            print(f"{y:2} ", end="")

            for x in range(self.width):
                position = y * self.width + x

                if reveal and position in self.mines:
                    print("* ", end=" ")

                elif self.flagged[y][x] and not reveal:
                    print("F ", end=" ")

                elif self.revealed[y][x]:
                    if position in self.mines:
                        print("* ", end=" ")
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f"{count if count else ' '} ", end=" ")

                else:
                    print(". ", end=" ")

            print()

    def count_mines_nearby(self, x, y):
        count = 0

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1

        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True

        if self.revealed[y][x] or self.flagged[y][x]:
            return True

        if (y * self.width + x) in self.mines:
            return False

        # Iterative flood-fill instead of recursive reveal()
        queue = deque([(x, y)])

        while queue:
            cx, cy = queue.popleft()

            if self.revealed[cy][cx] or self.flagged[cy][cx]:
                continue

            if (cy * self.width + cx) in self.mines:
                continue

            self.revealed[cy][cx] = True

            if self.count_mines_nearby(cx, cy) == 0:
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx = cx + dx
                        ny = cy + dy

                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            if not self.revealed[ny][nx]:
                                queue.append((nx, ny))

        return True

    def toggle_flag(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return

        if self.revealed[y][x]:
            return

        self.flagged[y][x] = not self.flagged[y][x]

    def has_won(self):
        for y in range(self.height):
            for x in range(self.width):
                position = y * self.width + x

                if position not in self.mines and not self.revealed[y][x]:
                    return False

        return True

    def play(self):
        while True:
            self.print_board()

            print("\nCommands:")
            print("  r x y  = reveal")
            print("  f x y  = flag/unflag")
            print("  q      = quit")

            command = input("\n> ").strip().split()

            if not command:
                continue

            if command[0].lower() == "q":
                print("Thanks for playing!")
                break

            if command[0].lower() not in ("r", "f") or len(command) != 3:
                print("Invalid command.")
                input("Press Enter to continue...")
                continue

            try:
                x = int(command[1])
                y = int(command[2])
            except ValueError:
                print("Coordinates must be numbers.")
                input("Press Enter to continue...")
                continue

            if not (0 <= x < self.width and 0 <= y < self.height):
                print("Coordinates are outside the board.")
                input("Press Enter to continue...")
                continue

            if command[0].lower() == "f":
                self.toggle_flag(x, y)

            else:
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("\n Game Over! You hit a mine.")
                    break

                if self.has_won():
                    self.print_board(reveal=True)
                    print("\n Congratulations! You cleared the board!")
                    break


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
