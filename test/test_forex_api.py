# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.56.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.forex_api import ForexApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestForexApi(unittest.TestCase):
    """ForexApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.forex_api.ForexApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_forex_currencies(self):
        """Test case for get_forex_currencies

        Forex Currencies  # noqa: E501
        """
        pass

    def test_get_forex_pairs(self):
        """Test case for get_forex_pairs

        Forex Currency Pairs  # noqa: E501
        """
        pass

    def test_get_forex_prices(self):
        """Test case for get_forex_prices

        Forex Currency Prices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
