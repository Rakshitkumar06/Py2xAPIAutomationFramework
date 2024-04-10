import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code, \
    verify_json_key_for_not_null
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util


class TestCreateBooking(object):

    @pytest.mark.postive
    def test_create_booking_tc_1(self):
        payload= payload_create_booking()
        print(payload)
        # payload.update({"firstname: "pramod","lastname:"dutta})
        payload["firstname"]= "pramod"
        payload["lastname"]="dutta"
        print(payload)
        # response = post_request()(url=APIConstants.url_create_booking(),
        #                         auth=None,
        #                         headers=Util().common_headers_json(),
        #                         payload=payload_create_booking(),
        #                         in_json=False)
        