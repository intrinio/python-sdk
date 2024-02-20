# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.52.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.company_api import CompanyApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestCompanyApi(unittest.TestCase):
    """CompanyApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.company_api.CompanyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_companies(self):
        """Test case for get_all_companies

        All Companies  # noqa: E501
        """
        pass

    def test_get_all_companies_daily_metrics(self):
        """Test case for get_all_companies_daily_metrics

        All Companies daily metrics  # noqa: E501
        """
        pass

    def test_get_all_company_news(self):
        """Test case for get_all_company_news

        All News  # noqa: E501
        """
        pass

    def test_get_company(self):
        """Test case for get_company

        Lookup Company  # noqa: E501
        """
        pass

    def test_get_company_answers(self):
        """Test case for get_company_answers

        Company Answers  # noqa: E501
        """
        pass

    def test_get_company_daily_metrics(self):
        """Test case for get_company_daily_metrics

        Company metrics by Company  # noqa: E501
        """
        pass

    def test_get_company_data_point_number(self):
        """Test case for get_company_data_point_number

        Data Point (Number) for Company  # noqa: E501
        """
        pass

    def test_get_company_data_point_text(self):
        """Test case for get_company_data_point_text

        Data Point (Text) for Company  # noqa: E501
        """
        pass

    def test_get_company_filings(self):
        """Test case for get_company_filings

        All Filings by Company  # noqa: E501
        """
        pass

    def test_get_company_fundamentals(self):
        """Test case for get_company_fundamentals

        All Fundamentals by Company  # noqa: E501
        """
        pass

    def test_get_company_historical_data(self):
        """Test case for get_company_historical_data

        Historical Data for Company  # noqa: E501
        """
        pass

    def test_get_company_ipos(self):
        """Test case for get_company_ipos

        IPOs  # noqa: E501
        """
        pass

    def test_get_company_news(self):
        """Test case for get_company_news

        All News by Company  # noqa: E501
        """
        pass

    def test_get_company_public_float(self):
        """Test case for get_company_public_float

        Get Company's public float  # noqa: E501
        """
        pass

    def test_get_company_securities(self):
        """Test case for get_company_securities

        All Securities by Company  # noqa: E501
        """
        pass

    def test_insider_transaction_filings_by_company(self):
        """Test case for insider_transaction_filings_by_company

        Insider Transaction Filings by Company  # noqa: E501
        """
        pass

    def test_latest_insider_transaction_filing_by_company(self):
        """Test case for latest_insider_transaction_filing_by_company

        Latest Insider Transaction Filing by Company  # noqa: E501
        """
        pass

    def test_lookup_company_fundamental(self):
        """Test case for lookup_company_fundamental

        Lookup Fundamental by Company  # noqa: E501
        """
        pass

    def test_recognize_company(self):
        """Test case for recognize_company

        Recognize Company  # noqa: E501
        """
        pass

    def test_search_companies(self):
        """Test case for search_companies

        Search Companies  # noqa: E501
        """
        pass

    def test_shares_outstanding_by_company(self):
        """Test case for shares_outstanding_by_company

        Shares Outstanding by Company  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
