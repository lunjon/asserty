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


def assert_greater_than(a, b):
    testcase_instance.assertGreater(a, b)


def assert_greater_equal_than(a, b):
    testcase_instance.assertGreaterEqual(a, b)


def assert_less_than(a, b):
    testcase_instance.assertLess(a, b)


def assert_less_equal_than(a, b):
    testcase_instance.assertLessEqual(a, b)


def assert_raises(err, func, *args, **kwargs):
    testcase_instance.assertRaises(err, func, *args, **kwargs)


def assert_type(obj, t):
    testcase_instance.assertIsInstance(obj, t)


def assert_not_type(obj, t):
    testcase_instance.assertNotIsInstance(obj, t)


def assert_contains(coll, obj):
    testcase_instance.assertIn(obj, coll)


def assert_not_contains(coll, obj):
    testcase_instance.assertNotIn(obj, coll)


class Assert:
    def __init__(self, value):
        self.value = value

    @property
    def also(self):
        """Make further assertions on this with AND between them."""
        return self

    and_do = also
    and_is = also

    def is_none(self):
        """Assert that this has a value of None."""
        assert_none(self.value)

    def is_not_none(self):
        """Assert that this DO NOT has a value of None."""
        assert_not_none(self.value)

    def equals(self, other):
        """Assert that if this object is equal to the other object."""
        assert_equal(self.value, other)
        return self

    def not_equals(self, other):
        """Check that if this object DO NOT equal to the other object."""
        assert_not_equal(self.value, other)
        return self

    def has_type(self, expected):
        """Assert that this has the expected type."""
        if not isinstance(expected, type):
            expected = type(expected)
        assert_type(self.value, expected)
        return self

    has_same_type_as = has_type
    is_instance = has_type

    def not_has_type(self, other):
        """Assert that this NOT have the expected type."""
        if not isinstance(other, type):
            other = type(other)
        assert_not_type(self.value, other)
        return self

    not_has_same_type_as = not_has_type
    not_is_instance = not_has_type

    def is_in(self, coll):
        """Assert that this is in the given collection."""
        assert_contains(coll, self.value)
        return self

    def is_not_in(self, coll):
        """Assert that this is NOT in the given collection."""
        assert_not_contains(coll, self.value)
        return self

    def has_length(self, expected):
        """Assert that this is of the expected length"""
        if hasattr(expected, "__len__"):
            expected = len(expected)
        assert_equal(len(self.value), expected)
        return self

    def not_has_length(self, expected):
        """Assert that this is NOT of the expected length"""
        if hasattr(expected, "__len__"):
            expected = len(expected)
        assert_not_equal(len(self.value), expected)
        return self

    def is_greater_than(self, other):
        """Assert that this is greater than other."""
        assert_greater_than(self.value, other)
        return self

    def is_greater_or_equal_to(self, other):
        """Assert that this is greater than other."""
        assert_greater_equal_than(self.value, other)
        return self

    def is_less_than(self, other):
        """Assert that this is greater than other."""
        assert_less_than(self.value, other)
        return self

    def is_less_or_equal_to(self, other):
        """Assert that this is greater than other."""
        assert_less_equal_than(self.value, other)
        return self
    
    # Bool Assertions
    
    def is_true(self):
        assert_true(self.value)

    def is_false(self):
        assert_false(self.value)

    is_not_true = is_false
    is_not_false = is_true
    
    # Collection Assertions

    def contains(self, obj):
        """Assert that this contain the given object."""
        assert_contains(self.value, obj)
        return self

    def not_contains(self, obj):
        """Assert that this DO NOT contain the given object."""
        assert_not_contains(self.value, obj)
        return self

    def contains_key(self, key):
        """Assert that this contains the given key."""
        if not hasattr(self.value, "__contains__"):
            raise TypeError("value has no keys")
        assert_contains(self.value, key)
        return self

    def not_contains_key(self, key):
        """Assert that this DO NOT contains the given key."""
        if not hasattr(self.value, "__contains__"):
            raise TypeError("value has no keys")
        assert_not_contains(self.value, key)
        return self

    def has_same_elements(self, other):
        """Assert that this and the other collection has the same elements."""
        assert_equal(sorted(self.value), other)
        return self
    
    # Callable assertions

    @property
    def when_called(self):
        """Assert if called without arguments."""
        self.args = []
        self.kwargs = {}
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

        assert_raises(err, self.value, *self.args, **self.kwargs)

    def returns(self, expected):
        """Assert if called that the given result is returned."""
        actual = self.value(*self.args, **self.kwargs)
        assert_equal(actual, expected)
    
    # HTTP Assertions

    def has_status_ok(self):
        assert_equal(self.value.status_code, 200)
        return self

    def has_status_successful(self):
        assert_less_than(self.value.status_code, 400)
        return self

    def has_status_created(self):
        assert_equal(self.value.status_code, 201)
        return self

    def has_status_no_content(self):
        assert_equal(self.value.status_code, 204)
        return self

    def has_status_bad_request(self):
        assert_equal(self.value.status_code, 400)
        return self

    def has_status_unauthorized(self):
        assert_equal(self.value.status_code, 401)
        return self

    def has_status_forbidden(self):
        assert_equal(self.value.status_code, 403)
        return self

    def has_status_not_found(self):
        assert_equal(self.value.status_code, 404)
        return self

    def has_status_method_not_allowed(self):
        assert_equal(self.value.status_code, 405)
        return self

    def body_equals(self, body: dict):
        assert_equal(self.value.json(), body)
        return self

    def body_contains_key(self, key: str):
        assert_contains(self.value.json(), key)
        return self
