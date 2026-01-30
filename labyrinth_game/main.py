#!/usr/bin/env python3

from labyrinth_game.constants import PROMPT_TEXT, WELCOME_TEXT
from labyrinth_game.player_actions import show_inventory
from labyrinth_game.utils import normalize_command


def main() -> None:
    print(WELCOME_TEXT)

    inventory: list[str] = []

    while True:
        command = normalize_command(input(PROMPT_TEXT))

        if command == "exit":
            break
        if command == "inv":
            show_inventory(inventory)
        else:
            print("Неизвестная команда. Доступно: inv, exit")


if __name__ == "__main__":
    main()
