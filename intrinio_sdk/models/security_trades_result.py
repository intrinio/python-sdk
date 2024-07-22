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

from intrinio_sdk.models.security_trades import SecurityTrades  # noqa: F401,E501


class SecurityTradesResult(object):
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
        'next_page': 'str',
        'source': 'str',
        'trades': 'list[SecurityTrades]'
    }

    attribute_map = {
        'next_page': 'next_page',
        'source': 'source',
        'trades': 'trades'
    }

    def __init__(self, next_page=None, source=None, trades=None):  # noqa: E501
        """SecurityTradesResult - a model defined in Swagger"""  # noqa: E501

        self._next_page = None
        self._source = None
        self._trades = None
        self.discriminator = None

        if next_page is not None:
            self.next_page = next_page
        if source is not None:
            self.source = source
        if trades is not None:
            self.trades = trades

    @property
    def next_page(self):
        """Gets the next_page of this SecurityTradesResult.  # noqa: E501

        The token required to request the next page of the data. If null, no further results are available.  # noqa: E501

        :return: The next_page of this SecurityTradesResult.  # noqa: E501
        :rtype: str
        """
        return self._next_page
        
    @property
    def next_page_dict(self):
        """Gets the next_page of this SecurityTradesResult.  # noqa: E501

        The token required to request the next page of the data. If null, no further results are available. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The next_page of this SecurityTradesResult.  # noqa: E501
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
        """Sets the next_page of this SecurityTradesResult.

        The token required to request the next page of the data. If null, no further results are available.  # noqa: E501

        :param next_page: The next_page of this SecurityTradesResult.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def source(self):
        """Gets the source of this SecurityTradesResult.  # noqa: E501

        The source of the trades.  # noqa: E501

        :return: The source of this SecurityTradesResult.  # noqa: E501
        :rtype: str
        """
        return self._source
        
    @property
    def source_dict(self):
        """Gets the source of this SecurityTradesResult.  # noqa: E501

        The source of the trades. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The source of this SecurityTradesResult.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.source
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
            result = { 'source': value }

        
        return result
        

    @source.setter
    def source(self, source):
        """Sets the source of this SecurityTradesResult.

        The source of the trades.  # noqa: E501

        :param source: The source of this SecurityTradesResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["iex", "delayed_sip", "utp_delayed", "cta_a_delayed", "cta_b_delayed", "otc_delayed", "nasdaq_basic"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def trades(self):
        """Gets the trades of this SecurityTradesResult.  # noqa: E501

        Array of all the trades in this page of the result.  # noqa: E501

        :return: The trades of this SecurityTradesResult.  # noqa: E501
        :rtype: list[SecurityTrades]
        """
        return self._trades
        
    @property
    def trades_dict(self):
        """Gets the trades of this SecurityTradesResult.  # noqa: E501

        Array of all the trades in this page of the result. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The trades of this SecurityTradesResult.  # noqa: E501
        :rtype: list[SecurityTrades]
        """

        result = None

        value = self.trades
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
            result = { 'trades': value }

        
        return result
        

    @trades.setter
    def trades(self, trades):
        """Sets the trades of this SecurityTradesResult.

        Array of all the trades in this page of the result.  # noqa: E501

        :param trades: The trades of this SecurityTradesResult.  # noqa: E501
        :type: list[SecurityTrades]
        """

        self._trades = trades

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
        if not isinstance(other, SecurityTradesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
