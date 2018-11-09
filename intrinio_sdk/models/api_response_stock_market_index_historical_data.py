# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Marketplace, we offer a wide selection of financial data feeds sourced by our own proprietary processes as well as from many data vendors. The primary application of the Intrinio API is for use in third-party applications and integrations or for end-users utilizing the Excel add-in and Google Sheets add-on. The Intrinio API uses HTTPS verbs and a RESTful endpoint structure, which makes it easy to request data from Intrinio. Responses are delivered in JSON format. If you need additional help in using the API, go to our home page (https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.historical_data import HistoricalData  # noqa: F401,E501
from intrinio_sdk.models.stock_market_index_summary import StockMarketIndexSummary  # noqa: F401,E501


class ApiResponseStockMarketIndexHistoricalData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'historical_data': 'list[HistoricalData]',
        'index': 'StockMarketIndexSummary',
        'next_page': 'str'
    }

    attribute_map = {
        'historical_data': 'historical_data',
        'index': 'index',
        'next_page': 'next_page'
    }

    def __init__(self, historical_data=None, index=None, next_page=None):  # noqa: E501
        """ApiResponseStockMarketIndexHistoricalData - a model defined in Swagger"""  # noqa: E501

        self._historical_data = None
        self._index = None
        self._next_page = None
        self.discriminator = None

        if historical_data is not None:
            self.historical_data = historical_data
        if index is not None:
            self.index = index
        if next_page is not None:
            self.next_page = next_page

    @property
    def historical_data(self):
        """Gets the historical_data of this ApiResponseStockMarketIndexHistoricalData.  # noqa: E501


        :return: The historical_data of this ApiResponseStockMarketIndexHistoricalData.  # noqa: E501
        :rtype: list[HistoricalData]
        """
        return self._historical_data

    @historical_data.setter
    def historical_data(self, historical_data):
        """Sets the historical_data of this ApiResponseStockMarketIndexHistoricalData.


        :param historical_data: The historical_data of this ApiResponseStockMarketIndexHistoricalData.  # noqa: E501
        :type: list[HistoricalData]
        """

        self._historical_data = historical_data

    @property
    def index(self):
        """Gets the index of this ApiResponseStockMarketIndexHistoricalData.  # noqa: E501


        :return: The index of this ApiResponseStockMarketIndexHistoricalData.  # noqa: E501
        :rtype: StockMarketIndexSummary
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ApiResponseStockMarketIndexHistoricalData.


        :param index: The index of this ApiResponseStockMarketIndexHistoricalData.  # noqa: E501
        :type: StockMarketIndexSummary
        """

        self._index = index

    @property
    def next_page(self):
        """Gets the next_page of this ApiResponseStockMarketIndexHistoricalData.  # noqa: E501

        The token required to request the next page of the data  # noqa: E501

        :return: The next_page of this ApiResponseStockMarketIndexHistoricalData.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ApiResponseStockMarketIndexHistoricalData.

        The token required to request the next page of the data  # noqa: E501

        :param next_page: The next_page of this ApiResponseStockMarketIndexHistoricalData.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiResponseStockMarketIndexHistoricalData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
