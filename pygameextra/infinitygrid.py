import math


def issubclass_safe(*args):
    try:
        return issubclass(*args)
    except TypeError:
        return False


class Grid:
    width = 2
    height = 2
    length = 4
    array = []
    truth_table: set
    truth_checker = lambda item: True if item else False
    initiator = None

    def __init__(self, width: int, height: int, initiator: any = None, truth_checker=None):
        self.width = width
        self.height = height
        self.length = width * height
        self.array = [initiator] * self.length
        self.truth_table = set()
        self.initiator = initiator
        self.truth_checker = truth_checker or Grid.truth_checker

    def __getitem__(self, x_y):
        if x_y[0] < 0 or x_y[1] < 0 or x_y[0] > self.width - 1 or x_y[1] > self.height - 1:
            return None
        return self.array[x_y[0] + (x_y[1] * self.width)]

    def __setitem__(self, x_y, value):
        if x_y[0] < 0 or x_y[1] < 0 or x_y[0] > self.width - 1 or x_y[1] > self.height - 1:
            return
        self.array[x_y[0] + (x_y[1] * self.width)] = value
        if self.truth_checker(value):
            self.truth_table.add(x_y)
        else:
            self.truth_table.discard(x_y)
        if issubclass(type(value), GridObject) or issubclass_safe(value, GridObject):
            value.x, value.y = x_y
            value.grid = self

    def graph(self, key: any = None):
        x, y = 0, 0
        while y < self.height:
            while x < self.width:
                if (key and key(x, y)) or (not key and self[x, y]):
                    print('■  ', end='')
                else:
                    print('□  ', end='')
                x += 1
            print('')
            y += 1
            x = 0


class GridObject:
    value = None
    grid = None
    x = 0
    y = 0

    def __init__(self, value: any, grid: Grid, x: int = 1, y: int = 1):
        self.value = value
        self.grid = grid
        self.x = x
        self.y = y

    def left(self):
        return self.grid[self.x - 1, self.y]

    def right(self):
        return self.grid[self.x + 1, self.y]

    def up(self):
        return self.grid[self.x, self.y - 1]

    def down(self):
        return self.grid[self.x - 1, self.y + 1]


class Inf_grid:
    def __init__(self, default: any = None):
        self.data = {}
        self.default = default

    def __getitem__(self, x_y):
        if x_y in self.data:
            return self.data[x_y]
        self.data[x_y] = self.default
        if issubclass(type(self.data[x_y]), GridObject) or issubclass_safe(self.data[x_y], GridObject):
            self.data[x_y].x, self.data[x_y].y = x_y
            self.data[x_y].grid = self
        return self.data[x_y]

    def __setitem__(self, x_y, value):
        self.data[x_y] = value or self.default
        if type(value) == GridObject:
            value.x, value.y = x_y
            value.grid = self

    def __delitem__(self, x_y):
        if x_y in self.data:
            del self.data[x_y]

    def snippet(self, start_x: int, start_y: int, width: int, height: int):
        snip = Grid(width, height, self.default)
        x, y = start_x, start_y
        while x < start_x + width:
            while y < start_y + height:
                snip[x - start_x, y - start_y] = self.get(x, y)
                y += 1
            y = start_y
            x += 1
        return snip

    def copy(self, destination: 'Inf_grid' = None):
        if not destination:
            destination = Inf_grid()
        destination.default = self.default
        destination.data = self.data.copy()
        return destination

    def get_area(self):
        keys = list(self.data.keys())
        list_of_x = [x[0] for x in keys]
        list_of_y = [x[1] for x in keys]
        start = (min(list_of_x), min(list_of_y))
        end = (max(list_of_x), max(list_of_y))
        return *start, end[0] - start[0] + 1, end[1] - start[1] + 1
