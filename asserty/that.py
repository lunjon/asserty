from collections.abc import Iterable
from .asserts import Assert
from .assertbool import AssertBool
from .assertcallable import AssertCallable
from .assertcollection import AssertCollection


def assert_that(obj):
    """Make assertions on the given object.

    Args:
        obj (object): The subject to which make assertions on.

    Returns:
        Assert: An object with assertion methods relevant for the type of the object.
    """

    if isinstance(obj, bool):
        # Note: a bool is also an instance of int
        return AssertBool(obj)

    elif (isinstance(obj, str) or
          isinstance(obj, int) or
          isinstance(obj, float)):
        return Assert(obj)

    elif callable(obj):
        return AssertCallable(obj)

    elif isinstance(obj, Iterable):
        return AssertCollection(obj)

    # Default
    return Assert(obj)