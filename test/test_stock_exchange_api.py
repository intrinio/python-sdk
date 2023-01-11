# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.34.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.stock_exchange_api import StockExchangeApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestStockExchangeApi(unittest.TestCase):
    """StockExchangeApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.stock_exchange_api.StockExchangeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_stock_exchanges(self):
        """Test case for get_all_stock_exchanges

        All Stock Exchanges  # noqa: E501
        """
        pass

    def test_get_stock_exchange_by_id(self):
        """Test case for get_stock_exchange_by_id

        Lookup Stock Exchange  # noqa: E501
        """
        pass

    def test_get_stock_exchange_price_adjustments(self):
        """Test case for get_stock_exchange_price_adjustments

        Stock Price Adjustments by Exchange  # noqa: E501
        """
        pass

    def test_get_stock_exchange_prices(self):
        """Test case for get_stock_exchange_prices

        Stock Prices by Exchange  # noqa: E501
        """
        pass

    def test_get_stock_exchange_realtime_prices(self):
        """Test case for get_stock_exchange_realtime_prices

        Realtime Stock Prices by Exchange  # noqa: E501
        """
        pass

    def test_get_stock_exchange_securities(self):
        """Test case for get_stock_exchange_securities

        Securities by Exchange  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
