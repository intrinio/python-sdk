# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.63.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.security_summary import SecuritySummary  # noqa: F401,E501
from intrinio_sdk.models.stock_exchange import StockExchange  # noqa: F401,E501


class ApiResponseStockExchangeSecurities(object):
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
        'securities': 'list[SecuritySummary]',
        'stock_exchange': 'StockExchange',
        'next_page': 'str'
    }

    attribute_map = {
        'securities': 'securities',
        'stock_exchange': 'stock_exchange',
        'next_page': 'next_page'
    }

    def __init__(self, securities=None, stock_exchange=None, next_page=None):  # noqa: E501
        """ApiResponseStockExchangeSecurities - a model defined in Swagger"""  # noqa: E501

        self._securities = None
        self._stock_exchange = None
        self._next_page = None
        self.discriminator = None

        if securities is not None:
            self.securities = securities
        if stock_exchange is not None:
            self.stock_exchange = stock_exchange
        if next_page is not None:
            self.next_page = next_page

    @property
    def securities(self):
        """Gets the securities of this ApiResponseStockExchangeSecurities.  # noqa: E501

        The securities traded on the Stock Exchange  # noqa: E501

        :return: The securities of this ApiResponseStockExchangeSecurities.  # noqa: E501
        :rtype: list[SecuritySummary]
        """
        return self._securities
        
    @property
    def securities_dict(self):
        """Gets the securities of this ApiResponseStockExchangeSecurities.  # noqa: E501

        The securities traded on the Stock Exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The securities of this ApiResponseStockExchangeSecurities.  # noqa: E501
        :rtype: list[SecuritySummary]
        """

        result = None

        value = self.securities
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'securities': value }

        
        return result
        

    @securities.setter
    def securities(self, securities):
        """Sets the securities of this ApiResponseStockExchangeSecurities.

        The securities traded on the Stock Exchange  # noqa: E501

        :param securities: The securities of this ApiResponseStockExchangeSecurities.  # noqa: E501
        :type: list[SecuritySummary]
        """

        self._securities = securities

    @property
    def stock_exchange(self):
        """Gets the stock_exchange of this ApiResponseStockExchangeSecurities.  # noqa: E501

        The Stock Exchange resolved from the given identifier  # noqa: E501

        :return: The stock_exchange of this ApiResponseStockExchangeSecurities.  # noqa: E501
        :rtype: StockExchange
        """
        return self._stock_exchange
        
    @property
    def stock_exchange_dict(self):
        """Gets the stock_exchange of this ApiResponseStockExchangeSecurities.  # noqa: E501

        The Stock Exchange resolved from the given identifier as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The stock_exchange of this ApiResponseStockExchangeSecurities.  # noqa: E501
        :rtype: StockExchange
        """

        result = None

        value = self.stock_exchange
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'stock_exchange': value }

        
        return result
        

    @stock_exchange.setter
    def stock_exchange(self, stock_exchange):
        """Sets the stock_exchange of this ApiResponseStockExchangeSecurities.

        The Stock Exchange resolved from the given identifier  # noqa: E501

        :param stock_exchange: The stock_exchange of this ApiResponseStockExchangeSecurities.  # noqa: E501
        :type: StockExchange
        """

        self._stock_exchange = stock_exchange

    @property
    def next_page(self):
        """Gets the next_page of this ApiResponseStockExchangeSecurities.  # noqa: E501

        The token required to request the next page of the data. If null, no further results are available.  # noqa: E501

        :return: The next_page of this ApiResponseStockExchangeSecurities.  # noqa: E501
        :rtype: str
        """
        return self._next_page
        
    @property
    def next_page_dict(self):
        """Gets the next_page of this ApiResponseStockExchangeSecurities.  # noqa: E501

        The token required to request the next page of the data. If null, no further results are available. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The next_page of this ApiResponseStockExchangeSecurities.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.next_page
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'next_page': value }

        
        return result
        

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ApiResponseStockExchangeSecurities.

        The token required to request the next page of the data. If null, no further results are available.  # noqa: E501

        :param next_page: The next_page of this ApiResponseStockExchangeSecurities.  # noqa: E501
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
        if not isinstance(other, ApiResponseStockExchangeSecurities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
