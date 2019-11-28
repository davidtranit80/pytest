
from asserter import assert_true, assert_equal
from session import Endpoints, HTTPSession, RequestTypes, StatusCodes
from test_utils import decorate_test, measure_time
PACKAGE_PARENT = '..'


ENDPOINT = Endpoints.LOGIN


class TestLogin:

    @staticmethod
    @decorate_test
    def test_status_code():
        status_code, _ = HTTPSession.send_request(RequestTypes.GET, ENDPOINT)
        assert_equal(status_code, StatusCodes.STATUS_200,
                     f'Status code of {ENDPOINT} enpoint')
