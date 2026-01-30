def normalize_command(command: str) -> str:
    """Приводит команду к удобному виду: убирает пробелы и делает нижний регистр."""
    return command.strip().lower()
