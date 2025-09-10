
class Validator:
    def __set_name__(self, owner: str, name: str) -> None:
        self._protected_name = name

    def __get__(self, instance: str, owner: str) -> None:
        getattr(instance, self._protected_name)

    def __set__(self, instance: str, value: int) -> None:
        setattr(instance, self._protected_name, value)

    def validate(self, value: int) -> None:
        pass


class Number(Validator):
    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Quantity should be integer.")
        if value < self.min_value or value > self.max_value:
            raise ValueError(f"Quantity should not be less than "
                             f"{self.min_value} and "
                             f"greater than {self.max_value}.")


class OneOf(Validator):
    def __init__(self, options: str) -> None:
        self.options = options

    def validate(self, value: int) -> None:
        if value not in self.options:
            raise ValueError(f"Expected {value} to be one of {self.options}.")


class BurgerRecipe:
    def __init__(self,
                 buns: int,
                 cheese: int,
                 tomatoes: int,
                 cutlets: int,
                 eggs: int,
                 sauce: str) -> None:
        self.buns = buns
        self.cheese = cheese
        self.tomatoes = tomatoes
        self.cutlets = cutlets
        self.eggs = eggs
        self.sauce = sauce
