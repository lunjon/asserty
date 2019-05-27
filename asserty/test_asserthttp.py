from . import assert_that
from requests import Response


class MockResponse(Response):
    def __init__(self, status_code: int, body: dict):
        super().__init__()
        self.status_code: int = status_code
        self.body: dict = body

    def json(self) -> dict:
        return self.body


def test_status():
    res = MockResponse(200, {})
    assert_that(res).has_status_ok()
    assert_that(res).has_status_successful()
    res = MockResponse(201, {})
    assert_that(res).has_status_successful()
    assert_that(res).has_status_created().also.has_status_successful()


def test_body():
    res = MockResponse(200, {"a": 1})
    assert_that(res).body_contains_key("a")
    assert_that(res).body_equals({"a": 1})


def test_status_and_body():
    res = MockResponse(200, {"a": 1})
    assert_that(res).has_status_ok().also.body_contains_key("a")
