from .asserts import *


class AssertCallable(Assert):
    args = []
    kwargs = {}

    def __init__(self, func):
        super().__init__(func)
        self.func = func

    @property
    def when_called(self):
        """Assert if called without arguments."""
        return self

    if_called = when_called

    def when_called_with(self, *args, **kwargs):
        """Assert if called with the given arguments."""
        self.args = args
        self.kwargs = kwargs
        return self

    if_called_with = when_called_with

    def raises(self, err):
        """Assert if called that the given error is raised."""
        assert_raises(err, self.func, *self.args, **self.kwargs)

    def returns(self, expected):
        """Assert if called that the given result is returned."""
        actual = self.func(*self.args, **self.kwargs)
        assert_equal(actual, expected)
