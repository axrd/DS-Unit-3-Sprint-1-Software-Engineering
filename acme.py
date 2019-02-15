#!/usr/bin/env python
"""
A reusable class for acme produts with select properties
"""


class Product:
    """Class for all Acme products.
    """

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        from random import randint

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flamability
        self.identifier = randint(100000, 999999)

    def stealability(self):
        r = self.price / self.weight
        if r < 0.5:
            return "Not so stealable..."
        elif r <= 0.5 <= 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        product = self.flammability * self.weight
        if product < 10:
            return "...fizzle."
        elif product <= 10 <= 50:
            return "...boom!"
        else:
            return "...BABOOM!!"




if __name__ == '__main__':
    import doctest
    doctest.testmod()
