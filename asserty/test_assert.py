from .asserts import assert_that


def test_equals_str():
    assert_that("str").equals("str")
    assert_that("str").not_equals("yo")


def test_equals_int():
    assert_that(1).equals(1)
    assert_that(2).not_equals(3)


def test_equals_float():
    assert_that(1.2).equals(1.2)
    assert_that(0.1).not_equals(-0.1)


def test_equals_with_same_class():
    class tmp:
        def __init__(self, var):
            self.var = var
    t1 = tmp(1)
    t2 = tmp(2)
    assert_that(t1).equals(t1)
    assert_that(t1).not_equals(t2)


def test_equals_with_different_class():
    class class1:
        def __init__(self, var):
            self.var = var
    class class2:
        def __init__(self, var):
            self.var = var
    
    c1 = class1(1)
    c2 = class2(2)
    assert assert_that(c1).not_equals(c2)


def test_equals_with_list():
    a = [1]
    b = [1]
    assert_that(a).equals(b)
    assert_that(a).not_equals([3])


def test_equals_with_dict():
    a = {"a":1}
    b = {"a":1}
    assert_that(a).equals(b)
    assert_that(a).not_equals({"c":2})


def test_is_none():
    assert_that(None).is_none()
    assert_that("str").is_not_none()


def test_has_type_on_str():
    assert_that("str").has_type(str)
    assert_that("str").has_type("string")
    assert_that("str").not_has_type(int)
    assert_that("str").not_has_same_type_as(int)
