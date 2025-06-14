# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.103.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ForexPrice(object):
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
        'occurred_at': 'str',
        'open_bid': 'float',
        'high_bid': 'float',
        'low_bid': 'float',
        'close_bid': 'float',
        'open_ask': 'float',
        'high_ask': 'float',
        'low_ask': 'float',
        'close_ask': 'float',
        'total_ticks': 'int'
    }

    attribute_map = {
        'occurred_at': 'occurred_at',
        'open_bid': 'open_bid',
        'high_bid': 'high_bid',
        'low_bid': 'low_bid',
        'close_bid': 'close_bid',
        'open_ask': 'open_ask',
        'high_ask': 'high_ask',
        'low_ask': 'low_ask',
        'close_ask': 'close_ask',
        'total_ticks': 'total_ticks'
    }

    def __init__(self, occurred_at=None, open_bid=None, high_bid=None, low_bid=None, close_bid=None, open_ask=None, high_ask=None, low_ask=None, close_ask=None, total_ticks=None):  # noqa: E501
        """ForexPrice - a model defined in Swagger"""  # noqa: E501

        self._occurred_at = None
        self._open_bid = None
        self._high_bid = None
        self._low_bid = None
        self._close_bid = None
        self._open_ask = None
        self._high_ask = None
        self._low_ask = None
        self._close_ask = None
        self._total_ticks = None
        self.discriminator = None

        if occurred_at is not None:
            self.occurred_at = occurred_at
        if open_bid is not None:
            self.open_bid = open_bid
        if high_bid is not None:
            self.high_bid = high_bid
        if low_bid is not None:
            self.low_bid = low_bid
        if close_bid is not None:
            self.close_bid = close_bid
        if open_ask is not None:
            self.open_ask = open_ask
        if high_ask is not None:
            self.high_ask = high_ask
        if low_ask is not None:
            self.low_ask = low_ask
        if close_ask is not None:
            self.close_ask = close_ask
        if total_ticks is not None:
            self.total_ticks = total_ticks

    @property
    def occurred_at(self):
        """Gets the occurred_at of this ForexPrice.  # noqa: E501

        The timestamp of the beginning of the timeframe. The open prices would be at this time, while close prices would be at this time plus the timeframe.  # noqa: E501

        :return: The occurred_at of this ForexPrice.  # noqa: E501
        :rtype: str
        """
        return self._occurred_at
        
    @property
    def occurred_at_dict(self):
        """Gets the occurred_at of this ForexPrice.  # noqa: E501

        The timestamp of the beginning of the timeframe. The open prices would be at this time, while close prices would be at this time plus the timeframe. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The occurred_at of this ForexPrice.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.occurred_at
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
            result = { 'occurred_at': value }

        
        return result
        

    @occurred_at.setter
    def occurred_at(self, occurred_at):
        """Sets the occurred_at of this ForexPrice.

        The timestamp of the beginning of the timeframe. The open prices would be at this time, while close prices would be at this time plus the timeframe.  # noqa: E501

        :param occurred_at: The occurred_at of this ForexPrice.  # noqa: E501
        :type: str
        """

        self._occurred_at = occurred_at

    @property
    def open_bid(self):
        """Gets the open_bid of this ForexPrice.  # noqa: E501

        Open bid  # noqa: E501

        :return: The open_bid of this ForexPrice.  # noqa: E501
        :rtype: float
        """
        return self._open_bid
        
    @property
    def open_bid_dict(self):
        """Gets the open_bid of this ForexPrice.  # noqa: E501

        Open bid as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open_bid of this ForexPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.open_bid
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
            result = { 'open_bid': value }

        
        return result
        

    @open_bid.setter
    def open_bid(self, open_bid):
        """Sets the open_bid of this ForexPrice.

        Open bid  # noqa: E501

        :param open_bid: The open_bid of this ForexPrice.  # noqa: E501
        :type: float
        """

        self._open_bid = open_bid

    @property
    def high_bid(self):
        """Gets the high_bid of this ForexPrice.  # noqa: E501

        High bid  # noqa: E501

        :return: The high_bid of this ForexPrice.  # noqa: E501
        :rtype: float
        """
        return self._high_bid
        
    @property
    def high_bid_dict(self):
        """Gets the high_bid of this ForexPrice.  # noqa: E501

        High bid as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The high_bid of this ForexPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.high_bid
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
            result = { 'high_bid': value }

        
        return result
        

    @high_bid.setter
    def high_bid(self, high_bid):
        """Sets the high_bid of this ForexPrice.

        High bid  # noqa: E501

        :param high_bid: The high_bid of this ForexPrice.  # noqa: E501
        :type: float
        """

        self._high_bid = high_bid

    @property
    def low_bid(self):
        """Gets the low_bid of this ForexPrice.  # noqa: E501

        Low bid  # noqa: E501

        :return: The low_bid of this ForexPrice.  # noqa: E501
        :rtype: float
        """
        return self._low_bid
        
    @property
    def low_bid_dict(self):
        """Gets the low_bid of this ForexPrice.  # noqa: E501

        Low bid as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The low_bid of this ForexPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.low_bid
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
            result = { 'low_bid': value }

        
        return result
        

    @low_bid.setter
    def low_bid(self, low_bid):
        """Sets the low_bid of this ForexPrice.

        Low bid  # noqa: E501

        :param low_bid: The low_bid of this ForexPrice.  # noqa: E501
        :type: float
        """

        self._low_bid = low_bid

    @property
    def close_bid(self):
        """Gets the close_bid of this ForexPrice.  # noqa: E501

        Close bid  # noqa: E501

        :return: The close_bid of this ForexPrice.  # noqa: E501
        :rtype: float
        """
        return self._close_bid
        
    @property
    def close_bid_dict(self):
        """Gets the close_bid of this ForexPrice.  # noqa: E501

        Close bid as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close_bid of this ForexPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.close_bid
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
            result = { 'close_bid': value }

        
        return result
        

    @close_bid.setter
    def close_bid(self, close_bid):
        """Sets the close_bid of this ForexPrice.

        Close bid  # noqa: E501

        :param close_bid: The close_bid of this ForexPrice.  # noqa: E501
        :type: float
        """

        self._close_bid = close_bid

    @property
    def open_ask(self):
        """Gets the open_ask of this ForexPrice.  # noqa: E501

        Open ask  # noqa: E501

        :return: The open_ask of this ForexPrice.  # noqa: E501
        :rtype: float
        """
        return self._open_ask
        
    @property
    def open_ask_dict(self):
        """Gets the open_ask of this ForexPrice.  # noqa: E501

        Open ask as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open_ask of this ForexPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.open_ask
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
            result = { 'open_ask': value }

        
        return result
        

    @open_ask.setter
    def open_ask(self, open_ask):
        """Sets the open_ask of this ForexPrice.

        Open ask  # noqa: E501

        :param open_ask: The open_ask of this ForexPrice.  # noqa: E501
        :type: float
        """

        self._open_ask = open_ask

    @property
    def high_ask(self):
        """Gets the high_ask of this ForexPrice.  # noqa: E501

        High ask  # noqa: E501

        :return: The high_ask of this ForexPrice.  # noqa: E501
        :rtype: float
        """
        return self._high_ask
        
    @property
    def high_ask_dict(self):
        """Gets the high_ask of this ForexPrice.  # noqa: E501

        High ask as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The high_ask of this ForexPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.high_ask
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
            result = { 'high_ask': value }

        
        return result
        

    @high_ask.setter
    def high_ask(self, high_ask):
        """Sets the high_ask of this ForexPrice.

        High ask  # noqa: E501

        :param high_ask: The high_ask of this ForexPrice.  # noqa: E501
        :type: float
        """

        self._high_ask = high_ask

    @property
    def low_ask(self):
        """Gets the low_ask of this ForexPrice.  # noqa: E501

        Low ask  # noqa: E501

        :return: The low_ask of this ForexPrice.  # noqa: E501
        :rtype: float
        """
        return self._low_ask
        
    @property
    def low_ask_dict(self):
        """Gets the low_ask of this ForexPrice.  # noqa: E501

        Low ask as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The low_ask of this ForexPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.low_ask
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
            result = { 'low_ask': value }

        
        return result
        

    @low_ask.setter
    def low_ask(self, low_ask):
        """Sets the low_ask of this ForexPrice.

        Low ask  # noqa: E501

        :param low_ask: The low_ask of this ForexPrice.  # noqa: E501
        :type: float
        """

        self._low_ask = low_ask

    @property
    def close_ask(self):
        """Gets the close_ask of this ForexPrice.  # noqa: E501

        Close ask  # noqa: E501

        :return: The close_ask of this ForexPrice.  # noqa: E501
        :rtype: float
        """
        return self._close_ask
        
    @property
    def close_ask_dict(self):
        """Gets the close_ask of this ForexPrice.  # noqa: E501

        Close ask as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close_ask of this ForexPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.close_ask
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
            result = { 'close_ask': value }

        
        return result
        

    @close_ask.setter
    def close_ask(self, close_ask):
        """Sets the close_ask of this ForexPrice.

        Close ask  # noqa: E501

        :param close_ask: The close_ask of this ForexPrice.  # noqa: E501
        :type: float
        """

        self._close_ask = close_ask

    @property
    def total_ticks(self):
        """Gets the total_ticks of this ForexPrice.  # noqa: E501

        Total ticks  # noqa: E501

        :return: The total_ticks of this ForexPrice.  # noqa: E501
        :rtype: int
        """
        return self._total_ticks
        
    @property
    def total_ticks_dict(self):
        """Gets the total_ticks of this ForexPrice.  # noqa: E501

        Total ticks as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_ticks of this ForexPrice.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.total_ticks
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
            result = { 'total_ticks': value }

        
        return result
        

    @total_ticks.setter
    def total_ticks(self, total_ticks):
        """Sets the total_ticks of this ForexPrice.

        Total ticks  # noqa: E501

        :param total_ticks: The total_ticks of this ForexPrice.  # noqa: E501
        :type: int
        """

        self._total_ticks = total_ticks

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
        if not isinstance(other, ForexPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
