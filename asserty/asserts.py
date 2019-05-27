from unittest import TestCase


testcase_instance = TestCase("__init__")


def assert_true(obj, msg=""):
    testcase_instance.assertTrue(obj, msg)


def assert_false(obj, msg=""):
    testcase_instance.assertFalse(obj, msg)


def assert_none(obj, msg=""):
    testcase_instance.assertIsNone(obj, msg)


def assert_not_none(obj, msg=""):
    testcase_instance.assertIsNotNone(obj, msg)


def assert_equal(a, b, msg=""):
    testcase_instance.assertEqual(a, b, msg)


def assert_not_equal(a, b, msg=""):
    testcase_instance.assertNotEqual(a, b, msg)


def assert_greater_than(a, b, msg=""):
    testcase_instance.assertGreater(a, b, msg)


def assert_greater_equal_than(a, b, msg=""):
    testcase_instance.assertGreaterEqual(a, b, msg)


def assert_less_than(a, b, msg=""):
    testcase_instance.assertLess(a, b, msg)


def assert_less_equal_than(a, b, msg=""):
    testcase_instance.assertLessEqual(a, b, msg)


def assert_raises(err, func, *args, **kwargs):
    testcase_instance.assertRaises(err, func, *args, **kwargs)


def assert_type(obj, t, msg=""):
    testcase_instance.assertIsInstance(obj, t, msg)


def assert_not_type(obj, t, msg=""):
    testcase_instance.assertNotIsInstance(obj, t, msg)


def assert_contains(coll, obj, msg=""):
    testcase_instance.assertIn(obj, coll, msg)


def assert_not_contains(coll, obj, msg=""):
    testcase_instance.assertNotIn(obj, coll, msg)


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
        msg = "Expected {} to be None".format(self.value)
        assert_none(self.value, msg)

    def is_not_none(self):
        """Assert that this DO NOT has a value of None."""
        msg = "Expected {} to be None".format(self.value)
        assert_not_none(self.value, msg)

    def equals(self, other):
        """Assert that if this object is equal to the other object."""
        msg = "Expected {} to equal".format(self.value, other)
        assert_equal(self.value, other, msg)
        return self

    def not_equals(self, other):
        """Check that if this object DO NOT equal to the other object."""
        msg = "Expected {} not to equal".format(self.value, other)
        assert_not_equal(self.value, other, msg)
        return self

    def has_type(self, expected):
        """Assert that this has the expected type."""
        if not isinstance(expected, type):
            expected = type(expected)
        msg = "Expected {} to have type {} but was {}".format(self.value, type(self.value), expected)
        assert_type(self.value, expected, msg)
        return self

    has_same_type_as = has_type
    is_instance = has_type

    def not_has_type(self, expected):
        """Assert that this NOT have the expected type."""
        if not isinstance(expected, type):
            expected = type(expected)
        msg = "Expected {} not to have type {} but was".format(self.value, expected)
        assert_not_type(self.value, expected, msg)
        return self

    not_has_same_type_as = not_has_type
    not_is_instance = not_has_type

    def is_in(self, coll):
        """Assert that this is in the given collection."""
        msg = "Expected {} to be in {} but was not".format(self.value, coll)
        assert_contains(coll, self.value, msg)
        return self

    def is_not_in(self, coll):
        """Assert that this is NOT in the given collection."""
        msg = "Expected {} not to be in {} but was".format(self.value, coll)
        assert_not_contains(coll, self.value, msg)
        return self

    def has_length(self, expected):
        """Assert that this is of the expected length"""
        if hasattr(expected, "__len__"):
            expected = len(expected)
        msg = "Expected {} to have length {} but was {}".format(self.value, expected, len(self.value))
        assert_equal(len(self.value), expected, msg)
        return self

    def not_has_length(self, expected):
        """Assert that this is NOT of the expected length"""
        if hasattr(expected, "__len__"):
            expected = len(expected)
        msg = "Expected {} to have length {} but was".format(self.value, expected)
        assert_not_equal(len(self.value), expected, msg)
        return self

    def is_greater_than(self, other):
        """Assert that this is greater than other."""
        msg = "Expected {} to be greater than {}".format(self.value, other)
        assert_greater_than(self.value, other, msg)
        return self

    def is_greater_or_equal_to(self, other):
        """Assert that this is greater than other."""
        msg = "Expected {} to be greater or equal to {}".format(self.value, other)
        assert_greater_equal_than(self.value, other, msg)
        return self

    def is_less_than(self, other):
        """Assert that this is greater than other."""
        msg = "Expected {} to be less than {}".format(self.value, other)
        assert_less_than(self.value, other, msg)
        return self

    def is_less_or_equal_to(self, other):
        """Assert that this is greater than other."""
        msg = "Expected {} to be less or equal to {}".format(self.value, other)
        assert_less_equal_than(self.value, other, msg)
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
        msg = "Expected {} to contain {}".format(self.value, obj)
        assert_contains(self.value, obj, msg)
        return self

    def not_contains(self, obj):
        """Assert that this DO NOT contain the given object."""
        msg = "Expected {} not to contain {}".format(self.value, obj)
        assert_not_contains(self.value, obj, msg)
        return self

    def contains_key(self, key):
        """Assert that this contains the given key."""
        if not hasattr(self.value, "__contains__"):
            raise TypeError("value has no keys")
        msg = "Expected {} to contain key {}".format(self.value, key)
        assert_contains(self.value, key, msg)
        return self

    def not_contains_key(self, key):
        """Assert that this DO NOT contains the given key."""
        if not hasattr(self.value, "__contains__"):
            raise TypeError("value has no keys")
        msg = "Expected {} not to contain key {}".format(self.value, key)
        assert_not_contains(self.value, key, msg)
        return self

    def has_same_elements(self, other):
        """Assert that this and the other collection has the same elements."""
        msg = "Expected {} and {} to contain the same elements".format(self.value, other)
        assert_equal(sorted(self.value), other, msg)
        return self
    
    # Callable assertions

    @property
    def when_called(self):
        """Assert if called without arguments."""
        if not callable(self.value):
            raise TypeError("object asserted is not callable")
        self.args = []
        self.kwargs = {}
        return self

    if_called = when_called

    def when_called_with(self, *args, **kwargs):
        """Assert if called with the given arguments."""
        if not callable(self.value):
            raise TypeError("object asserted is not callable")
        self.args = args
        self.kwargs = kwargs
        return self

    if_called_with = when_called_with

    def raises(self, err: type):
        """Assert if called that the given error is raised."""
        assert_raises(err, self.value, *self.args, **self.kwargs)

    def returns(self, expected):
        """Assert if called that the given result is returned."""
        actual = self.value(*self.args, **self.kwargs)
        msg = "Expected {} but {} was returned".format(expected, actual)
        assert_equal(actual, expected, msg)
    
    # HTTP Assertions
    
    def has_status_successful(self):
        msg = "Expected successful HTTP status code but was {}".format(self.value.status_code)
        assert_less_than(self.value.status_code, 400, msg)
        return self

    def has_status_ok(self):
        return self._has_status(200)

    def has_status_created(self):
        return self._has_status(201)

    def has_status_no_content(self):
        return self._has_status(204)

    def has_status_bad_request(self):
        return self._has_status(400)

    def has_status_unauthorized(self):
        return self._has_status(401)

    def has_status_forbidden(self):
        return self._has_status(403)

    def has_status_not_found(self):
        return self._has_status(404)

    def has_status_method_not_allowed(self):
        return self._has_status(405)

    def has_status_precondition_failed(self):
        return self._has_status(412)
    
    def _has_status(self, expected: int):
        msg = "Expected HTTP status {} but was {}".format(expected, self.value.status_code)
        assert_equal(self.value.status_code, expected, msg)
        return self

    def body_equals(self, body: dict):
        msg = "Expected body {} to equal {}".format(self.value.json(), body)
        assert_equal(self.value.json(), body, msg)
        return self

    def body_length(self, length: int):
        actual = len(self.value.json())
        msg = "Expected body length to be {} but was {}".format(actual, length)
        assert_equal(actual, length, msg)
        return self

    def body_contains_key(self, key: str):
        msg = "Expected body {} to contain key {}".format(self.value.json(), key)
        assert_contains(self.value.json(), key, msg)
        return self
