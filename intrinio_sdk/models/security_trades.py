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


class SecurityTrades(object):
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
        'timestamp': 'datetime',
        'price': 'float',
        'size': 'float',
        'total_volume': 'float',
        'market_center': 'str',
        'condition': 'str',
        'is_darkpool': 'bool'
    }

    attribute_map = {
        'symbol': 'symbol',
        'timestamp': 'timestamp',
        'price': 'price',
        'size': 'size',
        'total_volume': 'total_volume',
        'market_center': 'market_center',
        'condition': 'condition',
        'is_darkpool': 'is_darkpool'
    }

    def __init__(self, symbol=None, timestamp=None, price=None, size=None, total_volume=None, market_center=None, condition=None, is_darkpool=None):  # noqa: E501
        """SecurityTrades - a model defined in Swagger"""  # noqa: E501

        self._symbol = None
        self._timestamp = None
        self._price = None
        self._size = None
        self._total_volume = None
        self._market_center = None
        self._condition = None
        self._is_darkpool = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if timestamp is not None:
            self.timestamp = timestamp
        if price is not None:
            self.price = price
        if size is not None:
            self.size = size
        if total_volume is not None:
            self.total_volume = total_volume
        if market_center is not None:
            self.market_center = market_center
        if condition is not None:
            self.condition = condition
        if is_darkpool is not None:
            self.is_darkpool = is_darkpool

    @property
    def symbol(self):
        """Gets the symbol of this SecurityTrades.  # noqa: E501

        The ticker symbol  # noqa: E501

        :return: The symbol of this SecurityTrades.  # noqa: E501
        :rtype: str
        """
        return self._symbol
        
    @property
    def symbol_dict(self):
        """Gets the symbol of this SecurityTrades.  # noqa: E501

        The ticker symbol as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The symbol of this SecurityTrades.  # noqa: E501
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
        """Sets the symbol of this SecurityTrades.

        The ticker symbol  # noqa: E501

        :param symbol: The symbol of this SecurityTrades.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def timestamp(self):
        """Gets the timestamp of this SecurityTrades.  # noqa: E501

        The UTC timestamp at the time of the trade.  # noqa: E501

        :return: The timestamp of this SecurityTrades.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp
        
    @property
    def timestamp_dict(self):
        """Gets the timestamp of this SecurityTrades.  # noqa: E501

        The UTC timestamp at the time of the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The timestamp of this SecurityTrades.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.timestamp
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
            result = { 'timestamp': value }

        
        return result
        

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SecurityTrades.

        The UTC timestamp at the time of the trade.  # noqa: E501

        :param timestamp: The timestamp of this SecurityTrades.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def price(self):
        """Gets the price of this SecurityTrades.  # noqa: E501

        The price of the trade.  # noqa: E501

        :return: The price of this SecurityTrades.  # noqa: E501
        :rtype: float
        """
        return self._price
        
    @property
    def price_dict(self):
        """Gets the price of this SecurityTrades.  # noqa: E501

        The price of the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The price of this SecurityTrades.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.price
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
            result = { 'price': value }

        
        return result
        

    @price.setter
    def price(self, price):
        """Sets the price of this SecurityTrades.

        The price of the trade.  # noqa: E501

        :param price: The price of this SecurityTrades.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def size(self):
        """Gets the size of this SecurityTrades.  # noqa: E501

        The size of the trade.  # noqa: E501

        :return: The size of this SecurityTrades.  # noqa: E501
        :rtype: float
        """
        return self._size
        
    @property
    def size_dict(self):
        """Gets the size of this SecurityTrades.  # noqa: E501

        The size of the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The size of this SecurityTrades.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.size
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
            result = { 'size': value }

        
        return result
        

    @size.setter
    def size(self, size):
        """Sets the size of this SecurityTrades.

        The size of the trade.  # noqa: E501

        :param size: The size of this SecurityTrades.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def total_volume(self):
        """Gets the total_volume of this SecurityTrades.  # noqa: E501

        The total volume of the symbol for the day up to the timestamp point in time.  # noqa: E501

        :return: The total_volume of this SecurityTrades.  # noqa: E501
        :rtype: float
        """
        return self._total_volume
        
    @property
    def total_volume_dict(self):
        """Gets the total_volume of this SecurityTrades.  # noqa: E501

        The total volume of the symbol for the day up to the timestamp point in time. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_volume of this SecurityTrades.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.total_volume
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
            result = { 'total_volume': value }

        
        return result
        

    @total_volume.setter
    def total_volume(self, total_volume):
        """Sets the total_volume of this SecurityTrades.

        The total volume of the symbol for the day up to the timestamp point in time.  # noqa: E501

        :param total_volume: The total_volume of this SecurityTrades.  # noqa: E501
        :type: float
        """

        self._total_volume = total_volume

    @property
    def market_center(self):
        """Gets the market_center of this SecurityTrades.  # noqa: E501

        The market center for the trade.  # noqa: E501

        :return: The market_center of this SecurityTrades.  # noqa: E501
        :rtype: str
        """
        return self._market_center
        
    @property
    def market_center_dict(self):
        """Gets the market_center of this SecurityTrades.  # noqa: E501

        The market center for the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The market_center of this SecurityTrades.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.market_center
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
            result = { 'market_center': value }

        
        return result
        

    @market_center.setter
    def market_center(self, market_center):
        """Sets the market_center of this SecurityTrades.

        The market center for the trade.  # noqa: E501

        :param market_center: The market_center of this SecurityTrades.  # noqa: E501
        :type: str
        """

        self._market_center = market_center

    @property
    def condition(self):
        """Gets the condition of this SecurityTrades.  # noqa: E501

        The condition of the trade.  # noqa: E501

        :return: The condition of this SecurityTrades.  # noqa: E501
        :rtype: str
        """
        return self._condition
        
    @property
    def condition_dict(self):
        """Gets the condition of this SecurityTrades.  # noqa: E501

        The condition of the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The condition of this SecurityTrades.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.condition
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
            result = { 'condition': value }

        
        return result
        

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this SecurityTrades.

        The condition of the trade.  # noqa: E501

        :param condition: The condition of this SecurityTrades.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def is_darkpool(self):
        """Gets the is_darkpool of this SecurityTrades.  # noqa: E501

        If the trade was darkpool or not.  # noqa: E501

        :return: The is_darkpool of this SecurityTrades.  # noqa: E501
        :rtype: bool
        """
        return self._is_darkpool
        
    @property
    def is_darkpool_dict(self):
        """Gets the is_darkpool of this SecurityTrades.  # noqa: E501

        If the trade was darkpool or not. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The is_darkpool of this SecurityTrades.  # noqa: E501
        :rtype: bool
        """

        result = None

        value = self.is_darkpool
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
            result = { 'is_darkpool': value }

        
        return result
        

    @is_darkpool.setter
    def is_darkpool(self, is_darkpool):
        """Sets the is_darkpool of this SecurityTrades.

        If the trade was darkpool or not.  # noqa: E501

        :param is_darkpool: The is_darkpool of this SecurityTrades.  # noqa: E501
        :type: bool
        """

        self._is_darkpool = is_darkpool

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
        if not isinstance(other, SecurityTrades):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
