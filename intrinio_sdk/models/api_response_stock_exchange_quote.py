# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.76.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.api_response_security_quote import ApiResponseSecurityQuote  # noqa: F401,E501
from intrinio_sdk.models.stock_exchange import StockExchange  # noqa: F401,E501


class ApiResponseStockExchangeQuote(object):
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
        'quotes': 'list[ApiResponseSecurityQuote]',
        'stock_exchange': 'StockExchange'
    }

    attribute_map = {
        'quotes': 'quotes',
        'stock_exchange': 'stock_exchange'
    }

    def __init__(self, quotes=None, stock_exchange=None):  # noqa: E501
        """ApiResponseStockExchangeQuote - a model defined in Swagger"""  # noqa: E501

        self._quotes = None
        self._stock_exchange = None
        self.discriminator = None

        if quotes is not None:
            self.quotes = quotes
        if stock_exchange is not None:
            self.stock_exchange = stock_exchange

    @property
    def quotes(self):
        """Gets the quotes of this ApiResponseStockExchangeQuote.  # noqa: E501

        The realtime stock prices for all Securities traded on the Stock Exchange  # noqa: E501

        :return: The quotes of this ApiResponseStockExchangeQuote.  # noqa: E501
        :rtype: list[ApiResponseSecurityQuote]
        """
        return self._quotes
        
    @property
    def quotes_dict(self):
        """Gets the quotes of this ApiResponseStockExchangeQuote.  # noqa: E501

        The realtime stock prices for all Securities traded on the Stock Exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The quotes of this ApiResponseStockExchangeQuote.  # noqa: E501
        :rtype: list[ApiResponseSecurityQuote]
        """

        result = None

        value = self.quotes
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
            result = { 'quotes': value }

        
        return result
        

    @quotes.setter
    def quotes(self, quotes):
        """Sets the quotes of this ApiResponseStockExchangeQuote.

        The realtime stock prices for all Securities traded on the Stock Exchange  # noqa: E501

        :param quotes: The quotes of this ApiResponseStockExchangeQuote.  # noqa: E501
        :type: list[ApiResponseSecurityQuote]
        """

        self._quotes = quotes

    @property
    def stock_exchange(self):
        """Gets the stock_exchange of this ApiResponseStockExchangeQuote.  # noqa: E501

        The Stock Exchange resolved from the given identifier  # noqa: E501

        :return: The stock_exchange of this ApiResponseStockExchangeQuote.  # noqa: E501
        :rtype: StockExchange
        """
        return self._stock_exchange
        
    @property
    def stock_exchange_dict(self):
        """Gets the stock_exchange of this ApiResponseStockExchangeQuote.  # noqa: E501

        The Stock Exchange resolved from the given identifier as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The stock_exchange of this ApiResponseStockExchangeQuote.  # noqa: E501
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
        """Sets the stock_exchange of this ApiResponseStockExchangeQuote.

        The Stock Exchange resolved from the given identifier  # noqa: E501

        :param stock_exchange: The stock_exchange of this ApiResponseStockExchangeQuote.  # noqa: E501
        :type: StockExchange
        """

        self._stock_exchange = stock_exchange

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
        if not isinstance(other, ApiResponseStockExchangeQuote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
