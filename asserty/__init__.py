from .asserts import Assert
from .expected_error import  expected_error

version = "0.0.3"
name = "asserty"


def assert_that(obj):
    """Make assertions on the given object.

    Args:
        obj (object): The subject to which make assertions on.

    Returns:
        Assert: An object with assertion methods relevant for the type of the object.
    """
    return Assert(obj)


that = assert_that
