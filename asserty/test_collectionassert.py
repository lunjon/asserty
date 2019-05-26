from .asserts import assert_that


def test_has_length_on_list():
    assert_that([]).has_length(0)
    assert_that([1]).has_length(1)
    assert_that([1]).not_has_length(2)
    assert_that([1]).has_length([2])


def test_has_length_on_dict():
    assert_that({}).has_length(0)
    assert_that({"a":1}).has_length(1)
    assert_that({"a":1}).has_length({"b":2})
    assert_that({"a":1}).not_has_length(2)
