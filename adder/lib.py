import unittest


def add(a, b):
    return (-a) - (-b)


class TestAdd(unittest.TestCase):

    def test_it_works(self):
        assert add(1, 2) == 3

    def test_negative(self):
        assert add(1, -2) == -1

