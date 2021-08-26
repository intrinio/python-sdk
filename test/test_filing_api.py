# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.25.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.filing_api import FilingApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestFilingApi(unittest.TestCase):
    """FilingApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.filing_api.FilingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_filings(self):
        """Test case for get_all_filings

        All Filings  # noqa: E501
        """
        pass

    def test_get_all_notes(self):
        """Test case for get_all_notes

        All Filing Notes  # noqa: E501
        """
        pass

    def test_get_filing_answers(self):
        """Test case for get_filing_answers

        Filing Answers  # noqa: E501
        """
        pass

    def test_get_filing_by_id(self):
        """Test case for get_filing_by_id

        Lookup Filing  # noqa: E501
        """
        pass

    def test_get_filing_fundamentals(self):
        """Test case for get_filing_fundamentals

        All Fundamentals by Filing  # noqa: E501
        """
        pass

    def test_get_filing_html(self):
        """Test case for get_filing_html

        Filing Html  # noqa: E501
        """
        pass

    def test_get_filing_text(self):
        """Test case for get_filing_text

        Filing Text  # noqa: E501
        """
        pass

    def test_get_note(self):
        """Test case for get_note

        Filing Note by ID  # noqa: E501
        """
        pass

    def test_get_note_html(self):
        """Test case for get_note_html

        Filing Note HTML  # noqa: E501
        """
        pass

    def test_get_note_text(self):
        """Test case for get_note_text

        Filing Note Text  # noqa: E501
        """
        pass

    def test_search_notes(self):
        """Test case for search_notes

        Search Filing Notes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
