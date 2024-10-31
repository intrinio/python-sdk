# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.72.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.esg_api import ESGApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestESGApi(unittest.TestCase):
    """ESGApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.esg_api.ESGApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_esg_companies(self):
        """Test case for get_esg_companies

        ESG Companies  # noqa: E501
        """
        pass

    def test_get_esg_company_comprehensive_ratings(self):
        """Test case for get_esg_company_comprehensive_ratings

        ESG Company Comprehensive Ratings History  # noqa: E501
        """
        pass

    def test_get_esg_company_ratings(self):
        """Test case for get_esg_company_ratings

        ESG Company Ratings History  # noqa: E501
        """
        pass

    def test_get_esg_latest(self):
        """Test case for get_esg_latest

        ESG Latest  # noqa: E501
        """
        pass

    def test_get_esg_latest_comprehensive(self):
        """Test case for get_esg_latest_comprehensive

        ESG Latest Comprehensive  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
