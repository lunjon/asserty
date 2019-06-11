from asserty import assert_that


def test_has_length_on_list():
    assert_that([]).has_length(0)
    assert_that([1]).has_length(1)
    assert_that([1, 2]).has_length([2, 5])

    assert_that("str").has_length(3)

    assert_that({}).has_length(0)
    assert_that({"a": 1}).has_length(1)
    assert_that({"a": 1}).has_length({"b": 2})
    assert_that({"a": 1}).not_has_length(2)


def test_not_has_length():
    assert_that([1]).not_has_length(2)
    assert_that([1, 2, 3]).not_has_length(["a"])
    
    assert_that("Hello").not_has_length([1])

    assert_that({"a": 1}).not_has_length(2)
    

def test_has_length_greater():
    assert_that(["a", "b"]).has_length_greater_than(1)
    assert_that(["a", "b"]).has_length_greater_or_equal_to(2)
    assert_that(["a", "b"]).has_length_greater_or_equal_to(0)
    
    assert_that(["a", "b", "c"]).has_length_greater_or_equal_to([1])
    
    assert_that({"a": 1, "b": 2}).has_length_greater_than(1)
    assert_that({"a": 1, "b": 2}).has_length_greater_or_equal_to(2)
    

def test_has_length_less():
    assert_that([1, 2, 3]).has_length_less_than(4)
    assert_that([1, 2, 3]).has_length_less_or_equal_to(3)
    assert_that([1, 2, 3]).has_length_less_or_equal_to(5)


def test_contains():
    assert_that([1, 2, 3]).contains(1)
    assert_that({"a": 1}).contains("a")


def test_not_contains():
    assert_that([1, 2, 3]).not_contains(4)
    assert_that({}).not_contains(4)


def test_contains_key():
    assert_that({"a": 1}).contains_key("a")
    assert_that({"a": 1}).not_contains_key("b")


def test_contains_key_with_value():
    assert_that({"a": 1}).contains_key_with_value("a", 1)
    

def test_contains_subset():
    # list
    assert_that([1, 2, 3]).contains_subset([1])
    assert_that([1, 2, 3]).contains_subset([1])
    assert_that([1, 2, 3]).contains_subset([1, 2, 3])
    
    # dict
    assert_that({"a": 1, "b": 2}).contains_subset({"b": 2})
    assert_that({"a": 1, "b": 2}).contains_subset({"a": 1, "b": 2})
    
    # set
    assert_that({1, 2, 3, 4}).contains_subset({3})
    
    # mixed types
    assert_that({1, 2, 3}).contains_subset([1, 2])
    

def test_is_subset_of():
    # list
    assert_that([1, 3]).is_subset_of([1, 2, 3, 4])
    assert_that([1, 2, 3]).is_subset_of([1, 2, 3])
    
    # dict
    assert_that({"a": 1}).is_subset_of({"a": 1, "b": 2})


def test_has_same_elements_as():
    assert_that([1,2,3]).has_same_elements_as([2,1,3])

