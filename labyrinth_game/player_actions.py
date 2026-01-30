from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room


def get_input(prompt: str = "> ") -> str:
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def show_inventory(game_state: dict) -> None:
    inventory = game_state["player_inventory"]

    if inventory:
        print("Инвентарь:", ", ".join(inventory))
    else:
        print("Инвентарь: пусто")


def move_player(game_state: dict[str, object], direction: str) -> None:
    current_room_name = game_state["current_room"]
    current_room = ROOMS[current_room_name]

    exits = current_room["exits"]
    if direction not in exits:
        print("Нельзя пойти в этом направлении.")
        return

    new_room_name = exits[direction]
    game_state["current_room"] = new_room_name
    game_state["steps_taken"] += 1

    describe_current_room(game_state)


def take_item(game_state: dict, item_name: str) -> None:
    current_room_name = game_state["current_room"]
    room = ROOMS[current_room_name]

    items_in_room = room["items"]
    if item_name not in items_in_room:
        print("Такого предмета здесь нет.")
        return

    game_state["player_inventory"].append(item_name)
    items_in_room.remove(item_name)
    print(f"Вы подняли: {item_name}")


def use_item(game_state: dict, item_name: str) -> None:
    inventory = game_state["player_inventory"]

    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Вы зажигаете факел. Вокруг стало светлее.")
        return

    if item_name == "sword":
        print("Вы крепче сжимаете меч и чувствуете уверенность.")
        return

    if item_name == "bronze_box":
        if "rusty_key" not in inventory:
            inventory.append("rusty_key")
            print("Вы открываете бронзовую шкатулку и находите rusty_key!")
        else:
            print("Шкатулка пуста.")
        return

    print("Вы не знаете, как это использовать.")

