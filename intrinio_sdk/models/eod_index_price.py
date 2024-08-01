# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.63.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.api_response_index import ApiResponseIndex  # noqa: F401,E501


class EodIndexPrice(object):
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
        'index': 'ApiResponseIndex',
        'close': 'float',
        'open': 'float',
        'high': 'float',
        'low': 'float',
        'volume': 'int',
        'date': 'date'
    }

    attribute_map = {
        'index': 'index',
        'close': 'close',
        'open': 'open',
        'high': 'high',
        'low': 'low',
        'volume': 'volume',
        'date': 'date'
    }

    def __init__(self, index=None, close=None, open=None, high=None, low=None, volume=None, date=None):  # noqa: E501
        """EodIndexPrice - a model defined in Swagger"""  # noqa: E501

        self._index = None
        self._close = None
        self._open = None
        self._high = None
        self._low = None
        self._volume = None
        self._date = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if close is not None:
            self.close = close
        if open is not None:
            self.open = open
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if volume is not None:
            self.volume = volume
        if date is not None:
            self.date = date

    @property
    def index(self):
        """Gets the index of this EodIndexPrice.  # noqa: E501

        The index  # noqa: E501

        :return: The index of this EodIndexPrice.  # noqa: E501
        :rtype: ApiResponseIndex
        """
        return self._index
        
    @property
    def index_dict(self):
        """Gets the index of this EodIndexPrice.  # noqa: E501

        The index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The index of this EodIndexPrice.  # noqa: E501
        :rtype: ApiResponseIndex
        """

        result = None

        value = self.index
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
            result = { 'index': value }

        
        return result
        

    @index.setter
    def index(self, index):
        """Sets the index of this EodIndexPrice.

        The index  # noqa: E501

        :param index: The index of this EodIndexPrice.  # noqa: E501
        :type: ApiResponseIndex
        """

        self._index = index

    @property
    def close(self):
        """Gets the close of this EodIndexPrice.  # noqa: E501

        The close price  # noqa: E501

        :return: The close of this EodIndexPrice.  # noqa: E501
        :rtype: float
        """
        return self._close
        
    @property
    def close_dict(self):
        """Gets the close of this EodIndexPrice.  # noqa: E501

        The close price as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close of this EodIndexPrice.  # noqa: E501
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
        """Sets the close of this EodIndexPrice.

        The close price  # noqa: E501

        :param close: The close of this EodIndexPrice.  # noqa: E501
        :type: float
        """

        self._close = close

    @property
    def open(self):
        """Gets the open of this EodIndexPrice.  # noqa: E501

        The open price  # noqa: E501

        :return: The open of this EodIndexPrice.  # noqa: E501
        :rtype: float
        """
        return self._open
        
    @property
    def open_dict(self):
        """Gets the open of this EodIndexPrice.  # noqa: E501

        The open price as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open of this EodIndexPrice.  # noqa: E501
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
        """Sets the open of this EodIndexPrice.

        The open price  # noqa: E501

        :param open: The open of this EodIndexPrice.  # noqa: E501
        :type: float
        """

        self._open = open

    @property
    def high(self):
        """Gets the high of this EodIndexPrice.  # noqa: E501

        The high price  # noqa: E501

        :return: The high of this EodIndexPrice.  # noqa: E501
        :rtype: float
        """
        return self._high
        
    @property
    def high_dict(self):
        """Gets the high of this EodIndexPrice.  # noqa: E501

        The high price as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The high of this EodIndexPrice.  # noqa: E501
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
        """Sets the high of this EodIndexPrice.

        The high price  # noqa: E501

        :param high: The high of this EodIndexPrice.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this EodIndexPrice.  # noqa: E501

        The low price  # noqa: E501

        :return: The low of this EodIndexPrice.  # noqa: E501
        :rtype: float
        """
        return self._low
        
    @property
    def low_dict(self):
        """Gets the low of this EodIndexPrice.  # noqa: E501

        The low price as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The low of this EodIndexPrice.  # noqa: E501
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
        """Sets the low of this EodIndexPrice.

        The low price  # noqa: E501

        :param low: The low of this EodIndexPrice.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def volume(self):
        """Gets the volume of this EodIndexPrice.  # noqa: E501

        The volume  # noqa: E501

        :return: The volume of this EodIndexPrice.  # noqa: E501
        :rtype: int
        """
        return self._volume
        
    @property
    def volume_dict(self):
        """Gets the volume of this EodIndexPrice.  # noqa: E501

        The volume as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The volume of this EodIndexPrice.  # noqa: E501
        :rtype: int
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
        """Sets the volume of this EodIndexPrice.

        The volume  # noqa: E501

        :param volume: The volume of this EodIndexPrice.  # noqa: E501
        :type: int
        """

        self._volume = volume

    @property
    def date(self):
        """Gets the date of this EodIndexPrice.  # noqa: E501

        The date of the pricing data.  # noqa: E501

        :return: The date of this EodIndexPrice.  # noqa: E501
        :rtype: date
        """
        return self._date
        
    @property
    def date_dict(self):
        """Gets the date of this EodIndexPrice.  # noqa: E501

        The date of the pricing data. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date of this EodIndexPrice.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.date
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
            result = { 'date': value }

        
        return result
        

    @date.setter
    def date(self, date):
        """Sets the date of this EodIndexPrice.

        The date of the pricing data.  # noqa: E501

        :param date: The date of this EodIndexPrice.  # noqa: E501
        :type: date
        """

        self._date = date

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
        if not isinstance(other, EodIndexPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
