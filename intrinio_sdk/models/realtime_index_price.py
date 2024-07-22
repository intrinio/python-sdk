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

from intrinio_sdk.models.realtime_index_price_index import RealtimeIndexPriceIndex  # noqa: F401,E501


class RealtimeIndexPrice(object):
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
        'last_price': 'float',
        'last_time': 'datetime',
        'index': 'RealtimeIndexPriceIndex'
    }

    attribute_map = {
        'last_price': 'last_price',
        'last_time': 'last_time',
        'index': 'index'
    }

    def __init__(self, last_price=None, last_time=None, index=None):  # noqa: E501
        """RealtimeIndexPrice - a model defined in Swagger"""  # noqa: E501

        self._last_price = None
        self._last_time = None
        self._index = None
        self.discriminator = None

        if last_price is not None:
            self.last_price = last_price
        if last_time is not None:
            self.last_time = last_time
        if index is not None:
            self.index = index

    @property
    def last_price(self):
        """Gets the last_price of this RealtimeIndexPrice.  # noqa: E501

        The last price  # noqa: E501

        :return: The last_price of this RealtimeIndexPrice.  # noqa: E501
        :rtype: float
        """
        return self._last_price
        
    @property
    def last_price_dict(self):
        """Gets the last_price of this RealtimeIndexPrice.  # noqa: E501

        The last price as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_price of this RealtimeIndexPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.last_price
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
            result = { 'last_price': value }

        
        return result
        

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this RealtimeIndexPrice.

        The last price  # noqa: E501

        :param last_price: The last_price of this RealtimeIndexPrice.  # noqa: E501
        :type: float
        """

        self._last_price = last_price

    @property
    def last_time(self):
        """Gets the last_time of this RealtimeIndexPrice.  # noqa: E501

        The timestamp of the last price  # noqa: E501

        :return: The last_time of this RealtimeIndexPrice.  # noqa: E501
        :rtype: datetime
        """
        return self._last_time
        
    @property
    def last_time_dict(self):
        """Gets the last_time of this RealtimeIndexPrice.  # noqa: E501

        The timestamp of the last price as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_time of this RealtimeIndexPrice.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.last_time
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
            result = { 'last_time': value }

        
        return result
        

    @last_time.setter
    def last_time(self, last_time):
        """Sets the last_time of this RealtimeIndexPrice.

        The timestamp of the last price  # noqa: E501

        :param last_time: The last_time of this RealtimeIndexPrice.  # noqa: E501
        :type: datetime
        """

        self._last_time = last_time

    @property
    def index(self):
        """Gets the index of this RealtimeIndexPrice.  # noqa: E501


        :return: The index of this RealtimeIndexPrice.  # noqa: E501
        :rtype: RealtimeIndexPriceIndex
        """
        return self._index
        
    @property
    def index_dict(self):
        """Gets the index of this RealtimeIndexPrice.  # noqa: E501


        :return: The index of this RealtimeIndexPrice.  # noqa: E501
        :rtype: RealtimeIndexPriceIndex
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
        """Sets the index of this RealtimeIndexPrice.


        :param index: The index of this RealtimeIndexPrice.  # noqa: E501
        :type: RealtimeIndexPriceIndex
        """

        self._index = index

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
        if not isinstance(other, RealtimeIndexPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
