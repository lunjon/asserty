[![Build Status](https://travis-ci.com/lunjon/asserty.svg?branch=master)](https://travis-ci.com/lunjon/asserty)

# Asserty

_Asserty_ is a utility package that provides methods for better assertion in testing.


## Installation

The package can be installed using `pip`:

```bash
$ pip install asserty
```

## Examples

You make assertions by importing the `assert_that` function from the `asserty` package:

```python
from asserty import assert_that

assert_that("str").not_equals("string")
assert_that(5).is_in(range(10)).also.is_less_than(8)

def myfunc(arg):
    if not isinstance(arg, str):
        raise TypeError()
    return arg+"yay"

assert_that(myfunc).if_called_with(1).raises(TypeError)
assert_that(myfunc).if_called_with("Hey-").returns("Hey-yay")
```

Outside a test context that does not handle `AssertionError` you can import the equivalent function called `that`:

```python
from asserty import that

assert that("str").not_equals("string")
assert that(5).is_in(range(10)).also.is_less_than(8)
```
