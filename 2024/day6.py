#!/usr/bin/env python3

with open("day6.input", "r") as file:
    data = file.read().strip().split("\n")


class Grid():
    def __init__(self, grid: list[str]) -> None:

        # Directions for guard
        self.up = "^"
        self.down = "v"
        self.left = "<"
        self.right = ">"

        self.grid = grid
        self.guard_pos = self._get_guard_pos()
        if self.guard_pos:
            self.guard_pos_x = self.guard_pos[0]
            self.guard_pos_y = self.guard_pos[1]

        self.guard_direction = self._get_guard_direction()

    def print_grid(self):
        for i in self.grid:
            print(i)

    def _get_guard_direction(self) -> str | None:
        for row in self.grid:
            match row:
                case _ if self.up in row:
                    return self.up
                case _ if self.down in row:
                    return self.down
                case _ if self.left in row:
                    return self.left
                case _ if self.right in row:
                    return self.right

    def _get_guard_pos(self) -> tuple[int, int] | None:
        for i, row in enumerate(self.grid):
            if self.up in row:
                return (i, row.index("^"))
        return None

    def _get_next_guard_pos(self) -> tuple[int, int] :
        match self.guard_direction:
            case self.up:
                return (self.guard_pos_x - 1, self.guard_pos_y)
            case self.down:
                return (self.guard_pos_x + 1, self.guard_pos_y)
            case self.left:
                return (self.guard_pos_x, self.guard_pos_y - 1)
            case self.right:
                return (self.guard_pos_x, self.guard_pos_y + 1)

    def _validate_pos(self, pos: tuple[int, int]) -> bool:
        if pos != "#":
            return False
        return True

    def walk_guard(self):
        self.next_guard_pos = self._get_next_guard_pos()
        if self._validate_pos(self.next_guard_pos):
            self.guard_pos = self.next_guard_pos

        



g = Grid(data)
print(g.guard_pos)
print(g.guard_direction)
