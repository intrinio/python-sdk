# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.64.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SecurityIntervalMover(object):
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
        'symbol': 'str',
        'change': 'float',
        'open': 'float',
        'high': 'float',
        'low': 'float',
        'close': 'float',
        'volume': 'float',
        'average': 'float'
    }

    attribute_map = {
        'symbol': 'symbol',
        'change': 'change',
        'open': 'open',
        'high': 'high',
        'low': 'low',
        'close': 'close',
        'volume': 'volume',
        'average': 'average'
    }

    def __init__(self, symbol=None, change=None, open=None, high=None, low=None, close=None, volume=None, average=None):  # noqa: E501
        """SecurityIntervalMover - a model defined in Swagger"""  # noqa: E501

        self._symbol = None
        self._change = None
        self._open = None
        self._high = None
        self._low = None
        self._close = None
        self._volume = None
        self._average = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if change is not None:
            self.change = change
        if open is not None:
            self.open = open
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if close is not None:
            self.close = close
        if volume is not None:
            self.volume = volume
        if average is not None:
            self.average = average

    @property
    def symbol(self):
        """Gets the symbol of this SecurityIntervalMover.  # noqa: E501

        The ticker symbol for the interval  # noqa: E501

        :return: The symbol of this SecurityIntervalMover.  # noqa: E501
        :rtype: str
        """
        return self._symbol
        
    @property
    def symbol_dict(self):
        """Gets the symbol of this SecurityIntervalMover.  # noqa: E501

        The ticker symbol for the interval as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The symbol of this SecurityIntervalMover.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.symbol
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
            result = { 'symbol': value }

        
        return result
        

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this SecurityIntervalMover.

        The ticker symbol for the interval  # noqa: E501

        :param symbol: The symbol of this SecurityIntervalMover.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def change(self):
        """Gets the change of this SecurityIntervalMover.  # noqa: E501

        The ratio of Close minus Open to Open.  # noqa: E501

        :return: The change of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """
        return self._change
        
    @property
    def change_dict(self):
        """Gets the change of this SecurityIntervalMover.  # noqa: E501

        The ratio of Close minus Open to Open. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The change of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.change
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
            result = { 'change': value }

        
        return result
        

    @change.setter
    def change(self, change):
        """Sets the change of this SecurityIntervalMover.

        The ratio of Close minus Open to Open.  # noqa: E501

        :param change: The change of this SecurityIntervalMover.  # noqa: E501
        :type: float
        """

        self._change = change

    @property
    def open(self):
        """Gets the open of this SecurityIntervalMover.  # noqa: E501

        The first traded price in this interval.  # noqa: E501

        :return: The open of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """
        return self._open
        
    @property
    def open_dict(self):
        """Gets the open of this SecurityIntervalMover.  # noqa: E501

        The first traded price in this interval. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.open
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
            result = { 'open': value }

        
        return result
        

    @open.setter
    def open(self, open):
        """Sets the open of this SecurityIntervalMover.

        The first traded price in this interval.  # noqa: E501

        :param open: The open of this SecurityIntervalMover.  # noqa: E501
        :type: float
        """

        self._open = open

    @property
    def high(self):
        """Gets the high of this SecurityIntervalMover.  # noqa: E501

        The highest traded price in this interval.  # noqa: E501

        :return: The high of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """
        return self._high
        
    @property
    def high_dict(self):
        """Gets the high of this SecurityIntervalMover.  # noqa: E501

        The highest traded price in this interval. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The high of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.high
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
            result = { 'high': value }

        
        return result
        

    @high.setter
    def high(self, high):
        """Sets the high of this SecurityIntervalMover.

        The highest traded price in this interval.  # noqa: E501

        :param high: The high of this SecurityIntervalMover.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this SecurityIntervalMover.  # noqa: E501

        The lowest traded price in this interval.  # noqa: E501

        :return: The low of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """
        return self._low
        
    @property
    def low_dict(self):
        """Gets the low of this SecurityIntervalMover.  # noqa: E501

        The lowest traded price in this interval. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The low of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.low
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
            result = { 'low': value }

        
        return result
        

    @low.setter
    def low(self, low):
        """Sets the low of this SecurityIntervalMover.

        The lowest traded price in this interval.  # noqa: E501

        :param low: The low of this SecurityIntervalMover.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def close(self):
        """Gets the close of this SecurityIntervalMover.  # noqa: E501

        The last traded price in this interval.  # noqa: E501

        :return: The close of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """
        return self._close
        
    @property
    def close_dict(self):
        """Gets the close of this SecurityIntervalMover.  # noqa: E501

        The last traded price in this interval. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.close
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
            result = { 'close': value }

        
        return result
        

    @close.setter
    def close(self, close):
        """Sets the close of this SecurityIntervalMover.

        The last traded price in this interval.  # noqa: E501

        :param close: The close of this SecurityIntervalMover.  # noqa: E501
        :type: float
        """

        self._close = close

    @property
    def volume(self):
        """Gets the volume of this SecurityIntervalMover.  # noqa: E501

        The volume of trades in this interval.  # noqa: E501

        :return: The volume of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """
        return self._volume
        
    @property
    def volume_dict(self):
        """Gets the volume of this SecurityIntervalMover.  # noqa: E501

        The volume of trades in this interval. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The volume of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.volume
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
            result = { 'volume': value }

        
        return result
        

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this SecurityIntervalMover.

        The volume of trades in this interval.  # noqa: E501

        :param volume: The volume of this SecurityIntervalMover.  # noqa: E501
        :type: float
        """

        self._volume = volume

    @property
    def average(self):
        """Gets the average of this SecurityIntervalMover.  # noqa: E501

        The volume weighted average price of trades in this interval.  # noqa: E501

        :return: The average of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """
        return self._average
        
    @property
    def average_dict(self):
        """Gets the average of this SecurityIntervalMover.  # noqa: E501

        The volume weighted average price of trades in this interval. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The average of this SecurityIntervalMover.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.average
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
            result = { 'average': value }

        
        return result
        

    @average.setter
    def average(self, average):
        """Sets the average of this SecurityIntervalMover.

        The volume weighted average price of trades in this interval.  # noqa: E501

        :param average: The average of this SecurityIntervalMover.  # noqa: E501
        :type: float
        """

        self._average = average

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
        if not isinstance(other, SecurityIntervalMover):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
