registered_smooth_objects = []


class Smooth_value:
    value: [tuple[float, ...], float]
    smooth: [tuple[float, ...], float]

    def __init__(self, value: [tuple[float, ...], float]):
        self.value = value
        self.smooth = value

        registered_smooth_objects.append(self)

    def __del__(self):
        registered_smooth_objects.remove(self)

    def __set__(self, instance, value):
        print(instance, value)

    def __add__(self, other: [tuple[float, ...], float]):
        if isinstance(other, (tuple, list)) and isinstance(self.value, (tuple, list)):
            if len(self.value) == len(other):
                self.value = [sv + v for sv, v in zip(self.value, other)]
                return self
        elif isinstance(other, (float, int)) and isinstance(self.value, (float, int)):
            self.value += other
            return self
        raise ValueError(self.generate_value_error(other, 'add'))

    def generate_value_error(self, other: any, operation: str):
        return f"Cannot {operation} type {other.__class__.__name__}" \
               f" to type {self.__class__.__name__}" \
               f"<{self.value.__class__.__name__}" \
               f"{'[' + ', '.join([str(v.__class__.__name__) for v in self.value]) + ']' if isinstance(self.value, (tuple, list)) else ''}" \
               f">"

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.__repr__())
