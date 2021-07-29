import argparse
import random
from typing import Dict

GOAT = "goat"
CAR = "car"
Doors = Dict[int, str]

random.seed()


class MontyHall:
    def __init__(self, door_count: int):
        self._door_count = door_count
        self._doors: Doors = {}
        for i in range(door_count):
            self._doors[i] = "GOAT"

        # Randomly put a car behind one of the doors
        self._doors[random.randrange(0, door_count)] = CAR

    def pick_door(self, choice: int) -> None:
        self._choice: int = choice

    def reveal_goat(self) -> None:
        for door_number, prize in self._doors.items():
            if door_number != self._choice and prize != CAR:
                del self._doors[door_number]
                break

    def keep_choice(self) -> None:
        # We do nothing
        pass

    def change_choice(self) -> None:
        while True:
            choice: int = random.choice(list(self._doors.keys()))
            if choice != self._choice:
                self._choice = choice
                break

    def are_you_a_winner(self) -> bool:
        return True if self._doors[self._choice] == CAR else False


parser = argparse.ArgumentParser(
    description="Simulate Monty Hall game N number of times",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "--choice",
    type=str,
    choices=["keep_door", "change_door"],
    default="keep_door",
    help="Keep or change your original door",
)
parser.add_argument(
    "--number-of-games", type=int, default=10000, help="How many games shall we play"
)
parser.add_argument("--door-count", type=int, default=3, help="number of doors to choose from")

args = parser.parse_args()

door_count = args.door_count
number_of_games = args.number_of_games
choice = args.choice

lost = 0
won = 0

for count in range(number_of_games):
    game = MontyHall(door_count)
    game.pick_door(random.randrange(0, door_count))
    game.reveal_goat()
    if choice == "keep_door":
        game.keep_choice()
    elif choice == "change_door":
        game.change_choice()

    if game.are_you_a_winner():
        won += 1
    else:
        lost += 1

print("MONTY HALL GAME")
print("===============")
print(f"Games Played: {number_of_games}")
print(f"Choice: {choice}")
print(f"Number Of Doors: {door_count}")
print(f"Won: {won}")
print(f"Lost: {lost}")
print(f"Choosing {choice} resulted in winning {(won / number_of_games) * 100:.2f}% of the time")
