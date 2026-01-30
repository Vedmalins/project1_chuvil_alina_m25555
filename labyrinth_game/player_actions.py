def show_inventory(inventory: list[str]) -> None:
    """Печатает содержимое инвентаря игрока."""
    if inventory:
        print("Инвентарь:", ", ".join(inventory))
    else:
        print("Инвентарь: пусто")
