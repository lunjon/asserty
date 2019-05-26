from .asserts import *


class AssertBool(Assert):
    def __init__(self, value):
        super().__init__(value)

    def is_true(self):
        assert_true(self.value)

    def is_false(self):
        assert_false(self.value)

    is_not_true = is_false
    is_not_false = is_true
