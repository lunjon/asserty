from pytest import mark
from asserty import assert_that


class MockResponse:

    def __init__(self, status_code: int, body):
        super().__init__()
        self.status_code: int = status_code
        self.body = body

    def json(self) -> dict:
        return self.body

    @property
    def text(self):
        return str(self.body)


def test_status_codes():
    res = MockResponse(200, {})
    assert_that(res).has_status_ok()
    assert_that(res).has_status_successful()

    res = MockResponse(201, {})
    assert_that(res).has_status_created()
    assert_that(res).has_status_successful()

    res = MockResponse(202, {})
    assert_that(res).has_status_accepted()
    assert_that(res).has_status_successful()

    res = MockResponse(204, {})
    assert_that(res).has_status_no_content()
    assert_that(res).has_status_successful()

    res = MockResponse(400, {})
    assert_that(res).has_status_bad_request()
    assert_that(res).has_status_failed()

    res = MockResponse(401, {})
    assert_that(res).has_status_unauthorized()
    assert_that(res).has_status_failed()

    res = MockResponse(403, {})
    assert_that(res).has_status_forbidden()
    assert_that(res).has_status_failed()

    res = MockResponse(404, {})
    assert_that(res).has_status_not_found()
    assert_that(res).has_status_failed()

    res = MockResponse(405, {})
    assert_that(res).has_status_method_not_allowed()
    assert_that(res).has_status_failed()

    res = MockResponse(409, {})
    assert_that(res).has_status_conflict()
    assert_that(res).has_status_failed()

    res = MockResponse(412, {})
    assert_that(res).has_status_precondition_failed()
    assert_that(res).has_status_failed()

    res = MockResponse(500, {})
    assert_that(res).has_status_internal_server_error()
    assert_that(res).has_status_failed()

    res = MockResponse(503, {})
    assert_that(res).has_status_service_unavailable()
    assert_that(res).has_status_failed()

    res = MockResponse(504, {})
    assert_that(res).has_status_gateway_timeout()
    assert_that(res).has_status_failed()


@mark.parametrize("body,length", [({"a": 1}, 1), ([{"a": 1}, {"b": 2}], 2)])
def test_body_length(body: dict, length: int):
    res = MockResponse(200, body)
    assert_that(res).body_length(length)


@mark.parametrize("body,expected", [({"a": 1}, {"a": 1}), ({"a": 1}, "{'a': 1}")])
def test_body_equals(body: dict, expected):
    res = MockResponse(200, body)
    assert_that(res).body_equals(expected)


def test_body_contains_key():
    res = MockResponse(200, {"a": 1})
    assert_that(res).body_contains_key("a")
    assert_that(res).body_contains_key_with_value("a", 1)
