from .asserts import *


class AssertCollection(Assert):
    def __init__(self, value):
        super().__init__(value)
        self.value = value
    
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
        assert_true(self.value.__contains__(key))
        return self
    
    def not_contains_key(self, key):
        """Assert that this DO NOT contains the given key."""
        if not hasattr(self.value, "__contains__"):
            raise TypeError("value has no keys")
        assert_false(self.value.__contains__(key))
        return self
    
    def has_same_elements(self, other):
        """Assert that this and the other collection has the same elements."""
        assert_equal(sorted(self.value), other)
        return self
