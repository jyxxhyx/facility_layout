from unittest import TestCase

from model.guillotine import Guillotine


class TestGuillotine(TestCase):
    def test__plate_variable_enumeration(self):
        grid = (12, 10)
        shapes = [(5, 7), (7, 5)]
        upper_bound = 46
        model = Guillotine(grid, shapes, upper_bound)
        blocks, cuts = model.solve()
        print(blocks)
        print(cuts)
