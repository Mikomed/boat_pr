class Boat:
    def __init__(self):
        self._speed = 0
        self._direction = 0  # 0-360 градусов
        self._max_speed = 10

    def row(self) -> None:
        """Увеличивает скорость лодки."""
        if self._speed < self._max_speed:
            self._speed += 2

    def stop(self) -> None:
        """Полная остановка лодки."""
        self._speed = 0

    def turn_left(self, degrees: int = 30) -> None:
        """Поворот влево на заданное количество градусов."""
        if self._speed > 0:
            self._direction = (self._direction - degrees) % 360

    def turn_right(self, degrees: int = 30) -> None:
        """Поворот вправо на заданное количество градусов."""
        if self._speed > 0:
            self._direction = (self._direction + degrees) % 360

    def get_speed(self) -> int:
        """Возвращает текущую скорость."""
        return self._speed

    def get_direction(self) -> int:
        """Возвращает текущее направление."""
        return self._direction