import math

from labyrinth_game.constants import ROOMS


def normalize_command(command: str) -> str:
    """Приводит команду к удобному виду: убирает пробелы и делает нижний регистр."""
    return command.strip().lower()


def describe_current_room(game_state: dict) -> None:
    current_room_name = game_state["current_room"]
    room = ROOMS[current_room_name]

    print(f"\n== {current_room_name.upper()} ==")
    print(room["description"])

    items = room["items"]
    if items:
        print("Заметные предметы:", ", ".join(items))

    exits = room["exits"]
    print("Выходы:", ", ".join(exits.keys()))

    if room["puzzle"] is not None:
        print("Кажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state: dict) -> None:
    room_name = game_state["current_room"]
    room = ROOMS[room_name]

    puzzle = room["puzzle"]
    if puzzle is None:
        print("Загадок здесь нет.")
        return

    question, answer = puzzle
    print(question)
    user_answer = input("Ваш ответ: ").strip().lower()

    if user_answer == answer.strip().lower():
        print("Верно! Загадка решена.")
        room["puzzle"] = None

        # награда: выдадим ключ (минимально, чтобы появилась победа)
        if "treasure_key" not in game_state["player_inventory"]:
            game_state["player_inventory"].append("treasure_key")
            print("Вы получаете награду: treasure_key!")
    else:
        print("Неверно. Попробуйте снова.")


def pseudo_random(seed: int, modulo: int) -> int:
    if modulo <= 0:
        return 0

    x = math.sin(seed * 12.9898) * 43758.5453
    frac = x - math.floor(x)
    return int(frac * modulo)        


def attempt_open_treasure(game_state: dict) -> None:
    room_name = game_state["current_room"]
    room = ROOMS[room_name]

    if room_name != "treasure_room":
        print("Здесь нет сокровищницы.")
        return

    if "treasure_chest" not in room["items"]:
        print("Сундук уже открыт.")
        return

    inventory = game_state["player_inventory"]

    if "treasure_key" in inventory:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room["items"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
        return

    choice = input("Сундук заперт. Ввести код? (да/нет): ").strip().lower()
    if choice != "да":
        print("Вы отступаете от сундука.")
        return

    code = input("Введите код: ").strip().lower()
    puzzle = room["puzzle"]
    if puzzle is None:
        print("Похоже, кода больше не требуется.")
        return

    _, correct = puzzle
    if code == correct.strip().lower():
        print("Код верный! Замок открыт!")
        room["items"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
    else:
        print("Код неверный.")


def show_help() -> None:
    print("\nДоступные команды:")
    print("  go <direction>  - перейти (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")
