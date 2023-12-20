# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.48.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StockPriceInterval(object):
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
        'time': 'datetime',
        'open': 'float',
        'close': 'float',
        'high': 'float',
        'low': 'float',
        'volume': 'float',
        'close_time': 'datetime',
        'interval': 'str',
        'average': 'float',
        'change': 'float'
    }

    attribute_map = {
        'time': 'time',
        'open': 'open',
        'close': 'close',
        'high': 'high',
        'low': 'low',
        'volume': 'volume',
        'close_time': 'close_time',
        'interval': 'interval',
        'average': 'average',
        'change': 'change'
    }

    def __init__(self, time=None, open=None, close=None, high=None, low=None, volume=None, close_time=None, interval=None, average=None, change=None):  # noqa: E501
        """StockPriceInterval - a model defined in Swagger"""  # noqa: E501

        self._time = None
        self._open = None
        self._close = None
        self._high = None
        self._low = None
        self._volume = None
        self._close_time = None
        self._interval = None
        self._average = None
        self._change = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if open is not None:
            self.open = open
        if close is not None:
            self.close = close
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if volume is not None:
            self.volume = volume
        if close_time is not None:
            self.close_time = close_time
        if interval is not None:
            self.interval = interval
        if average is not None:
            self.average = average
        if change is not None:
            self.change = change

    @property
    def time(self):
        """Gets the time of this StockPriceInterval.  # noqa: E501

        The timestamp that represents the start of the interval span.  # noqa: E501

        :return: The time of this StockPriceInterval.  # noqa: E501
        :rtype: datetime
        """
        return self._time
        
    @property
    def time_dict(self):
        """Gets the time of this StockPriceInterval.  # noqa: E501

        The timestamp that represents the start of the interval span. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The time of this StockPriceInterval.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.time
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
            result = { 'time': value }

        
        return result
        

    @time.setter
    def time(self, time):
        """Sets the time of this StockPriceInterval.

        The timestamp that represents the start of the interval span.  # noqa: E501

        :param time: The time of this StockPriceInterval.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def open(self):
        """Gets the open of this StockPriceInterval.  # noqa: E501

        The first traded price during the period  # noqa: E501

        :return: The open of this StockPriceInterval.  # noqa: E501
        :rtype: float
        """
        return self._open
        
    @property
    def open_dict(self):
        """Gets the open of this StockPriceInterval.  # noqa: E501

        The first traded price during the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open of this StockPriceInterval.  # noqa: E501
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
        """Sets the open of this StockPriceInterval.

        The first traded price during the period  # noqa: E501

        :param open: The open of this StockPriceInterval.  # noqa: E501
        :type: float
        """

        self._open = open

    @property
    def close(self):
        """Gets the close of this StockPriceInterval.  # noqa: E501

        The last traded price during the period  # noqa: E501

        :return: The close of this StockPriceInterval.  # noqa: E501
        :rtype: float
        """
        return self._close
        
    @property
    def close_dict(self):
        """Gets the close of this StockPriceInterval.  # noqa: E501

        The last traded price during the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close of this StockPriceInterval.  # noqa: E501
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
        """Sets the close of this StockPriceInterval.

        The last traded price during the period  # noqa: E501

        :param close: The close of this StockPriceInterval.  # noqa: E501
        :type: float
        """

        self._close = close

    @property
    def high(self):
        """Gets the high of this StockPriceInterval.  # noqa: E501

        The highest price over the span of the period  # noqa: E501

        :return: The high of this StockPriceInterval.  # noqa: E501
        :rtype: float
        """
        return self._high
        
    @property
    def high_dict(self):
        """Gets the high of this StockPriceInterval.  # noqa: E501

        The highest price over the span of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The high of this StockPriceInterval.  # noqa: E501
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
        """Sets the high of this StockPriceInterval.

        The highest price over the span of the period  # noqa: E501

        :param high: The high of this StockPriceInterval.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this StockPriceInterval.  # noqa: E501

        The lowest price over the span of the period  # noqa: E501

        :return: The low of this StockPriceInterval.  # noqa: E501
        :rtype: float
        """
        return self._low
        
    @property
    def low_dict(self):
        """Gets the low of this StockPriceInterval.  # noqa: E501

        The lowest price over the span of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The low of this StockPriceInterval.  # noqa: E501
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
        """Sets the low of this StockPriceInterval.

        The lowest price over the span of the period  # noqa: E501

        :param low: The low of this StockPriceInterval.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def volume(self):
        """Gets the volume of this StockPriceInterval.  # noqa: E501

        The number of shares exchanged during the period  # noqa: E501

        :return: The volume of this StockPriceInterval.  # noqa: E501
        :rtype: float
        """
        return self._volume
        
    @property
    def volume_dict(self):
        """Gets the volume of this StockPriceInterval.  # noqa: E501

        The number of shares exchanged during the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The volume of this StockPriceInterval.  # noqa: E501
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
        """Sets the volume of this StockPriceInterval.

        The number of shares exchanged during the period  # noqa: E501

        :param volume: The volume of this StockPriceInterval.  # noqa: E501
        :type: float
        """

        self._volume = volume

    @property
    def close_time(self):
        """Gets the close_time of this StockPriceInterval.  # noqa: E501

        The timestamp that represents the end of the interval span.  # noqa: E501

        :return: The close_time of this StockPriceInterval.  # noqa: E501
        :rtype: datetime
        """
        return self._close_time
        
    @property
    def close_time_dict(self):
        """Gets the close_time of this StockPriceInterval.  # noqa: E501

        The timestamp that represents the end of the interval span. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close_time of this StockPriceInterval.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.close_time
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
            result = { 'close_time': value }

        
        return result
        

    @close_time.setter
    def close_time(self, close_time):
        """Sets the close_time of this StockPriceInterval.

        The timestamp that represents the end of the interval span.  # noqa: E501

        :param close_time: The close_time of this StockPriceInterval.  # noqa: E501
        :type: datetime
        """

        self._close_time = close_time

    @property
    def interval(self):
        """Gets the interval of this StockPriceInterval.  # noqa: E501

        The size of the interval.  # noqa: E501

        :return: The interval of this StockPriceInterval.  # noqa: E501
        :rtype: str
        """
        return self._interval
        
    @property
    def interval_dict(self):
        """Gets the interval of this StockPriceInterval.  # noqa: E501

        The size of the interval. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The interval of this StockPriceInterval.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.interval
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
            result = { 'interval': value }

        
        return result
        

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this StockPriceInterval.

        The size of the interval.  # noqa: E501

        :param interval: The interval of this StockPriceInterval.  # noqa: E501
        :type: str
        """
        allowed_values = ["SixtyMinute", "ThirtyMinute", "FifteenMinute", "TenMinute", "FiveMinute", "OneMinute"]  # noqa: E501
        if interval not in allowed_values:
            raise ValueError(
                "Invalid value for `interval` ({0}), must be one of {1}"  # noqa: E501
                .format(interval, allowed_values)
            )

        self._interval = interval

    @property
    def average(self):
        """Gets the average of this StockPriceInterval.  # noqa: E501

        The average trade price of an individual stock during the interval.  # noqa: E501

        :return: The average of this StockPriceInterval.  # noqa: E501
        :rtype: float
        """
        return self._average
        
    @property
    def average_dict(self):
        """Gets the average of this StockPriceInterval.  # noqa: E501

        The average trade price of an individual stock during the interval. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The average of this StockPriceInterval.  # noqa: E501
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
        """Sets the average of this StockPriceInterval.

        The average trade price of an individual stock during the interval.  # noqa: E501

        :param average: The average of this StockPriceInterval.  # noqa: E501
        :type: float
        """

        self._average = average

    @property
    def change(self):
        """Gets the change of this StockPriceInterval.  # noqa: E501

        The change ratio from open to close.  ((Close - Open)/Open).  # noqa: E501

        :return: The change of this StockPriceInterval.  # noqa: E501
        :rtype: float
        """
        return self._change
        
    @property
    def change_dict(self):
        """Gets the change of this StockPriceInterval.  # noqa: E501

        The change ratio from open to close.  ((Close - Open)/Open). as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The change of this StockPriceInterval.  # noqa: E501
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
        """Sets the change of this StockPriceInterval.

        The change ratio from open to close.  ((Close - Open)/Open).  # noqa: E501

        :param change: The change of this StockPriceInterval.  # noqa: E501
        :type: float
        """

        self._change = change

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
        if not isinstance(other, StockPriceInterval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
