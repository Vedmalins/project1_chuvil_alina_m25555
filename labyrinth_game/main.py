#!/usr/bin/env python3

from labyrinth_game.constants import ROOMS, WELCOME_TEXT


def main() -> None:
    game_state = {
        "player_inventory": [],
        "current_room": "entrance",
        "game_over": False,
        "steps_taken": 0,
    }

    # В этом шаге убеждаемся, что мы есть и стартовая комната существует
    print(WELCOME_TEXT)
    print("Стартовая комната:", game_state["current_room"])
    print("Доступные комнаты:", ", ".join(ROOMS.keys()))


if __name__ == "__main__":
    main()

