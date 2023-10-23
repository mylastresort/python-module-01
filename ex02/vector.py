class Vector:
    pass


class Vector:
    def __init__(self, values: list[float] | list[list[float]] | int | tuple[int, int]):
        if not values or (type(values) is tuple and len(values) != 2) \
                or (type(values) is list and type(values[0]) is list and len(values) > 1
                    and any([len(row) != 1 for row in values])):
            raise Exception('only 2 dimention values are excepted')
        self.values = values
        self.shape = (len(values), len(values[0]))

    def __str__(self) -> str:
        return str(self.shape)

    def dot(self, vec2) -> int:
        return sum([a * b for a, b in zip(self.values, vec2.values)])

    def T(self):
        if (self.shape[0] == 1):
            return Vector([[val] for val in self.values[0]])
        return Vector([val for [val] in self.values])

    def __add__(self, vec2: Vector):
        if vec2.shape != self.shape:
            raise Exception('operation performs on different vector shapes')
        if self.shape[0] == 1:
            return Vector([[a + b for a, b in zip(self.values[0], vec2.values[0])]])
        return Vector([[a + b] for [a], [b] in zip(self.values, vec2.values)])

    def __radd__(self, vec2):
        return self.__add__(vec2)

    def __sub__(self, vec2: Vector):
        if vec2.shape != self.shape:
            raise Exception('operation performs on different vector shapes')
        if self.shape == 1:
            return Vector([[a - b for a, b in zip(self.values[0], vec2.values[0])]])
        return Vector([[a - b] for [a], [b] in zip(self.values, vec2.values)])

    def __rsub__(self, vec2):
        return self.__sub__(vec2)

    def __truediv__(self, scalar: int or Vector):
        if self.shape[0] == 1:
            ret = [[val / scalar for val in self.values[0]]]
            print(ret)
            return Vector(ret)
        return Vector([[val / scalar] for val, in self.values])

    def __rtruediv__(self, scalar: int or Vector):
        if type(scalar) in (int, float):
            raise NotImplementedError(
                "Division of a scalar by a Vector is not defined here.")

    def __mul__(self, scalar: int):
        if self.shape[0] == 1:
            return Vector([[val * scalar for val in self.values[0]]])
        return Vector([[val * scalar] for val, in self.values])

    def __rmul__(self, scalar: int):
        return self.__mul__(scalar)

    def __str__(self):
        return self.values

    def __repr__(self):
        return self.values
