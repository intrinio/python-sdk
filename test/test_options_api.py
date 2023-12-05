# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.47.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.options_api import OptionsApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestOptionsApi(unittest.TestCase):
    """OptionsApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.options_api.OptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_options_tickers(self):
        """Test case for get_all_options_tickers

        Options Tickers  # noqa: E501
        """
        pass

    def test_get_option_expirations_realtime(self):
        """Test case for get_option_expirations_realtime

        Options Expirations  # noqa: E501
        """
        pass

    def test_get_option_strikes_realtime(self):
        """Test case for get_option_strikes_realtime

        Option Strikes Realtime  # noqa: E501
        """
        pass

    def test_get_options(self):
        """Test case for get_options

        Options  # noqa: E501
        """
        pass

    def test_get_options_by_symbol_realtime(self):
        """Test case for get_options_by_symbol_realtime

        Options by Symbol Realtime  # noqa: E501
        """
        pass

    def test_get_options_chain(self):
        """Test case for get_options_chain

        Options Chain  # noqa: E501
        """
        pass

    def test_get_options_chain_eod(self):
        """Test case for get_options_chain_eod

        Options Chain EOD  # noqa: E501
        """
        pass

    def test_get_options_chain_realtime(self):
        """Test case for get_options_chain_realtime

        Options Chain Realtime  # noqa: E501
        """
        pass

    def test_get_options_expirations(self):
        """Test case for get_options_expirations

        Options Expirations  # noqa: E501
        """
        pass

    def test_get_options_expirations_eod(self):
        """Test case for get_options_expirations_eod

        Options Expirations  # noqa: E501
        """
        pass

    def test_get_options_interval_by_contract(self):
        """Test case for get_options_interval_by_contract

        Options Intervals By Contract  # noqa: E501
        """
        pass

    def test_get_options_interval_movers(self):
        """Test case for get_options_interval_movers

        Options Intervals Movers  # noqa: E501
        """
        pass

    def test_get_options_interval_movers_change(self):
        """Test case for get_options_interval_movers_change

        Options Intervals Movers By Change  # noqa: E501
        """
        pass

    def test_get_options_interval_movers_volume(self):
        """Test case for get_options_interval_movers_volume

        Options Intervals Movers By Volume  # noqa: E501
        """
        pass

    def test_get_options_prices(self):
        """Test case for get_options_prices

        Option Prices  # noqa: E501
        """
        pass

    def test_get_options_prices_batch_realtime(self):
        """Test case for get_options_prices_batch_realtime

        Option Prices Batch Realtime  # noqa: E501
        """
        pass

    def test_get_options_prices_eod(self):
        """Test case for get_options_prices_eod

        Option Prices EOD  # noqa: E501
        """
        pass

    def test_get_options_prices_realtime(self):
        """Test case for get_options_prices_realtime

        Option Prices Realtime  # noqa: E501
        """
        pass

    def test_get_options_snapshots(self):
        """Test case for get_options_snapshots

        Option Prices Realtime Snapshot  # noqa: E501
        """
        pass

    def test_get_options_stats_realtime(self):
        """Test case for get_options_stats_realtime

        Option Stats Realtime  # noqa: E501
        """
        pass

    def test_get_unusual_activity(self):
        """Test case for get_unusual_activity

        Options Unusual Activity  # noqa: E501
        """
        pass

    def test_get_unusual_activity_intraday(self):
        """Test case for get_unusual_activity_intraday

        Options Unusual Activity Intraday  # noqa: E501
        """
        pass

    def test_get_unusual_activity_universal(self):
        """Test case for get_unusual_activity_universal

        Options Unusual Activity Universal  # noqa: E501
        """
        pass

    def test_get_unusual_activity_universal_intraday(self):
        """Test case for get_unusual_activity_universal_intraday

        Options Unusual Activity Universal Intraday  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
