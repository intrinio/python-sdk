# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.28.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.zacks_api import ZacksApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestZacksApi(unittest.TestCase):
    """ZacksApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.zacks_api.ZacksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_zacks_analyst_ratings(self):
        """Test case for get_zacks_analyst_ratings

        Zacks Analyst Ratings  # noqa: E501
        """
        pass

    def test_get_zacks_eps_estimates(self):
        """Test case for get_zacks_eps_estimates

        Zacks EPS Estimates  # noqa: E501
        """
        pass

    def test_get_zacks_eps_growth_rates(self):
        """Test case for get_zacks_eps_growth_rates

        Zacks EPS Growth Rates  # noqa: E501
        """
        pass

    def test_get_zacks_eps_surprises(self):
        """Test case for get_zacks_eps_surprises

        Zacks EPS Surprises  # noqa: E501
        """
        pass

    def test_get_zacks_etf_holdings(self):
        """Test case for get_zacks_etf_holdings

        Zacks ETF Holdings  # noqa: E501
        """
        pass

    def test_get_zacks_institutional_holding_companies(self):
        """Test case for get_zacks_institutional_holding_companies

        Zacks Institutional Holding Companies  # noqa: E501
        """
        pass

    def test_get_zacks_institutional_holding_owners(self):
        """Test case for get_zacks_institutional_holding_owners

        Zacks Institutional Holding Owners  # noqa: E501
        """
        pass

    def test_get_zacks_institutional_holdings(self):
        """Test case for get_zacks_institutional_holdings

        Zacks Institutional Holdings  # noqa: E501
        """
        pass

    def test_get_zacks_long_term_growth_rates(self):
        """Test case for get_zacks_long_term_growth_rates

        Zacks Long Term Growth Rates  # noqa: E501
        """
        pass

    def test_get_zacks_sales_surprises(self):
        """Test case for get_zacks_sales_surprises

        Zacks Sales Surprises  # noqa: E501
        """
        pass

    def test_get_zacks_target_price_consensuses(self):
        """Test case for get_zacks_target_price_consensuses

        Zacks Target Price Consensuses  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
