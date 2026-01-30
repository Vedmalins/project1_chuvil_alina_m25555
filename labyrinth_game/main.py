#!/usr/bin/env python3
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    normalize_command,
    show_help,
    solve_puzzle,
)


def process_command(game_state: dict, command_line: str) -> None:
    parts = command_line.split()
    if not parts:
        return

    command = parts[0]
    arg = parts[1] if len(parts) > 1 else ""

    match command:
        case "quit" | "exit":
            game_state["game_over"] = True
            print("Выход из игры.")

        case "look":
            describe_current_room(game_state)

        case "inventory" | "inv":
            show_inventory(game_state)

        case "go":
            if not arg:
                print("Куда идти? Пример: go north")
            else:
                moved = move_player(game_state, arg)
                if moved:
                    describe_current_room(game_state)


        case "take":
            if not arg:
                print("Что взять? Пример: take torch")
            else:
                take_item(game_state, arg)

        case "use":
            if not arg:
                print("Что использовать? Пример: use torch")
            else:
                use_item(game_state, arg)

        case "solve":
            if game_state["current_room"] == "treasure_room":
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)

        case "help":
            show_help()

        case _:
            print("Неизвестная команда. Доступно: look, go, take, use, inventory, quit")




def main() -> None:
    game_state = {
        "player_inventory": [],
        "current_room": "entrance",
        "game_over": False,
        "steps_taken": 0,
    }

    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)

    while not game_state["game_over"]:
        command_line = normalize_command(get_input("> "))
        process_command(game_state, command_line)



if __name__ == "__main__":
    main()


