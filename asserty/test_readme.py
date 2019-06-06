from . import assert_that


def test_readme_examples():
    assert_that("str").not_equals("string")
    assert_that(5).is_in(range(10)).also.is_less_than(8)

    def func(arg):
        if not isinstance(arg, str):
            raise TypeError()
        return arg + "yay"

    assert_that(func).if_called_with(1).raises(TypeError)
    assert_that(func).if_called_with("Hey-").returns("Hey-yay")
