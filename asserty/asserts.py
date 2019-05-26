from collections.abc import Iterable
from unittest import TestCase


testcase_instance = TestCase("__init__")


def assert_true(obj):
    testcase_instance.assertTrue(obj)


def assert_false(obj):
    testcase_instance.assertFalse(obj)


def assert_none(obj):
    testcase_instance.assertIsNone(obj)


def assert_not_none(obj):
    testcase_instance.assertIsNotNone(obj)


def assert_equal(a, b):
    testcase_instance.assertEqual(a, b)


def assert_not_equal(a, b):
    testcase_instance.assertNotEqual(a, b)


def assert_raises(err, func, *args, **kwargs):
    testcase_instance.assertRaises(err, func, *args, **kwargs)


def assert_type(obj, t):
    testcase_instance.assertIsInstance(obj, t)


def assert_not_type(obj, t):
    testcase_instance.assertNotIsInstance(obj, t)


class Assert:
    def __init__(self, value):
        self.value = value

    def also(self):
        return self

    def is_none(self):
        assert_none(self.value)

    def is_not_none(self):
        assert_not_none(self.value)

    def equals(self, other):
        """Assert that if this object is equal to the other object."""
        assert_equal(self.value, other)
        return self

    def not_equals(self, other):
        """Check that if this object is NOT equal to the other object."""
        assert_not_equal(self.value, other)
        return self


    def has_type(self, expected):
        """Assert that this type is the expected.

        Args:
            expected (type|object): the type or object to compare the type.
        """
        if not isinstance(expected, type):
            expected = type(expected)
        assert_type(self.value, expected)
        return self

    has_same_type_as = has_type
    is_instance = has_type

    def not_has_type(self, other):
        """Assert that this type is the expected.

        Args:
            expected (type|object): the type or object to compare the type.
        """
        if not isinstance(other, type):
            other = type(other)
        assert_not_type(self.value, other)
        return self

    not_has_same_type_as = not_has_type
    not_is_instance = not_has_type


class AssertBool(Assert):
    def __init__(self, value):
        super().__init__(value)

    def is_true(self):
        assert_true(self.value)

    def is_false(self):
        assert_false(self.value)

    is_not_true = is_false
    is_not_false = is_true


class AssertCollection(Assert):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    def has_length(self, expected):
        """Assert that the length of this object is of the expected value.

        Args:
            expected (int|obj): the expected length. It can be an integer or an object
                that has the __len__ attribute.
        """
        if hasattr(expected, "__len__"):
            expected = len(expected)
        assert_equal(len(self.value), expected)
        return self

    def not_has_length(self, expected):
        """Assert that the length of this object is NOT of the expected value.

        Args:
            expected (int|obj): the expected length. It can be an integer or an object
                that has the __len__ attribute.
        """
        if hasattr(expected, "__len__"):
            expected = len(expected)
        assert_not_equal(len(self.value), expected)
        return self


class AssertCallable(Assert):
    args = []
    kwargs = {}

    def __init__(self, func):
        super().__init__(func)
        self.func = func

    @property
    def when_called(self):
        """Make assertion on a callable.
        """
        return self

    if_called = when_called

    def when_called_with(self, *args, **kwargs):
        """Make assertion on a callable with arguments.

        Returns:
            AssertCallable: A new asserter.
        """
        self.args = args
        self.kwargs = kwargs
        return self

    if_called_with = when_called_with

    def raises(self, err):
        assert_raises(err, self.func, *self.args, **self.kwargs)

    def returns(self, expected):
        actual = self.func(*self.args, **self.kwargs)
        assert_equal(actual, expected)


def assert_that(obj):
    """Returns a new object around the object to assert."""

    if isinstance(obj, bool):
        # A bool is an instance of int, hence the check
        return AssertBool(obj)

    elif (isinstance(obj, str) or
        isinstance(obj, int) or
        isinstance(obj, float)):
        return Assert(obj)


    elif callable(obj):
        return AssertCallable(obj)

    elif isinstance(obj, Iterable):
        return AssertCollection(obj)

    return Assert(obj)


class expected_error:

    def __init__(self, err_type):
        if not isinstance(err_type, type):
            self.err_type = type(err_type)
        else:
            self.err_type = err_type

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        return isinstance(value, self.err_type)
