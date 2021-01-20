# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.18.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.realtime_stock_price_security import RealtimeStockPriceSecurity  # noqa: F401,E501


class RealtimeStockPrice(object):
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
        'last_size': 'float',
        'bid_price': 'float',
        'bid_size': 'float',
        'ask_price': 'float',
        'ask_size': 'float',
        'open_price': 'float',
        'close_price': 'float',
        'high_price': 'float',
        'low_price': 'float',
        'exchange_volume': 'float',
        'market_volume': 'float',
        'updated_on': 'datetime',
        'source': 'str',
        'security': 'RealtimeStockPriceSecurity'
    }

    attribute_map = {
        'last_price': 'last_price',
        'last_time': 'last_time',
        'last_size': 'last_size',
        'bid_price': 'bid_price',
        'bid_size': 'bid_size',
        'ask_price': 'ask_price',
        'ask_size': 'ask_size',
        'open_price': 'open_price',
        'close_price': 'close_price',
        'high_price': 'high_price',
        'low_price': 'low_price',
        'exchange_volume': 'exchange_volume',
        'market_volume': 'market_volume',
        'updated_on': 'updated_on',
        'source': 'source',
        'security': 'security'
    }

    def __init__(self, last_price=None, last_time=None, last_size=None, bid_price=None, bid_size=None, ask_price=None, ask_size=None, open_price=None, close_price=None, high_price=None, low_price=None, exchange_volume=None, market_volume=None, updated_on=None, source=None, security=None):  # noqa: E501
        """RealtimeStockPrice - a model defined in Swagger"""  # noqa: E501

        self._last_price = None
        self._last_time = None
        self._last_size = None
        self._bid_price = None
        self._bid_size = None
        self._ask_price = None
        self._ask_size = None
        self._open_price = None
        self._close_price = None
        self._high_price = None
        self._low_price = None
        self._exchange_volume = None
        self._market_volume = None
        self._updated_on = None
        self._source = None
        self._security = None
        self.discriminator = None

        if last_price is not None:
            self.last_price = last_price
        if last_time is not None:
            self.last_time = last_time
        if last_size is not None:
            self.last_size = last_size
        if bid_price is not None:
            self.bid_price = bid_price
        if bid_size is not None:
            self.bid_size = bid_size
        if ask_price is not None:
            self.ask_price = ask_price
        if ask_size is not None:
            self.ask_size = ask_size
        if open_price is not None:
            self.open_price = open_price
        if close_price is not None:
            self.close_price = close_price
        if high_price is not None:
            self.high_price = high_price
        if low_price is not None:
            self.low_price = low_price
        if exchange_volume is not None:
            self.exchange_volume = exchange_volume
        if market_volume is not None:
            self.market_volume = market_volume
        if updated_on is not None:
            self.updated_on = updated_on
        if source is not None:
            self.source = source
        if security is not None:
            self.security = security

    @property
    def last_price(self):
        """Gets the last_price of this RealtimeStockPrice.  # noqa: E501

        The price of the last trade.  # noqa: E501

        :return: The last_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._last_price
        
    @property
    def last_price_dict(self):
        """Gets the last_price of this RealtimeStockPrice.  # noqa: E501

        The price of the last trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_price of this RealtimeStockPrice.  # noqa: E501
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
        """Sets the last_price of this RealtimeStockPrice.

        The price of the last trade.  # noqa: E501

        :param last_price: The last_price of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._last_price = last_price

    @property
    def last_time(self):
        """Gets the last_time of this RealtimeStockPrice.  # noqa: E501

        The date and time when the last trade occurred.  # noqa: E501

        :return: The last_time of this RealtimeStockPrice.  # noqa: E501
        :rtype: datetime
        """
        return self._last_time
        
    @property
    def last_time_dict(self):
        """Gets the last_time of this RealtimeStockPrice.  # noqa: E501

        The date and time when the last trade occurred. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_time of this RealtimeStockPrice.  # noqa: E501
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
        """Sets the last_time of this RealtimeStockPrice.

        The date and time when the last trade occurred.  # noqa: E501

        :param last_time: The last_time of this RealtimeStockPrice.  # noqa: E501
        :type: datetime
        """

        self._last_time = last_time

    @property
    def last_size(self):
        """Gets the last_size of this RealtimeStockPrice.  # noqa: E501

        The size of the last trade.  # noqa: E501

        :return: The last_size of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._last_size
        
    @property
    def last_size_dict(self):
        """Gets the last_size of this RealtimeStockPrice.  # noqa: E501

        The size of the last trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_size of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.last_size
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
            result = { 'last_size': value }

        
        return result
        

    @last_size.setter
    def last_size(self, last_size):
        """Sets the last_size of this RealtimeStockPrice.

        The size of the last trade.  # noqa: E501

        :param last_size: The last_size of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._last_size = last_size

    @property
    def bid_price(self):
        """Gets the bid_price of this RealtimeStockPrice.  # noqa: E501

        The price of the top bid order.  # noqa: E501

        :return: The bid_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._bid_price
        
    @property
    def bid_price_dict(self):
        """Gets the bid_price of this RealtimeStockPrice.  # noqa: E501

        The price of the top bid order. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.bid_price
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
            result = { 'bid_price': value }

        
        return result
        

    @bid_price.setter
    def bid_price(self, bid_price):
        """Sets the bid_price of this RealtimeStockPrice.

        The price of the top bid order.  # noqa: E501

        :param bid_price: The bid_price of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._bid_price = bid_price

    @property
    def bid_size(self):
        """Gets the bid_size of this RealtimeStockPrice.  # noqa: E501

        The size of the top bid order.  # noqa: E501

        :return: The bid_size of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._bid_size
        
    @property
    def bid_size_dict(self):
        """Gets the bid_size of this RealtimeStockPrice.  # noqa: E501

        The size of the top bid order. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_size of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.bid_size
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
            result = { 'bid_size': value }

        
        return result
        

    @bid_size.setter
    def bid_size(self, bid_size):
        """Sets the bid_size of this RealtimeStockPrice.

        The size of the top bid order.  # noqa: E501

        :param bid_size: The bid_size of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._bid_size = bid_size

    @property
    def ask_price(self):
        """Gets the ask_price of this RealtimeStockPrice.  # noqa: E501

        The price of the top ask order.  # noqa: E501

        :return: The ask_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._ask_price
        
    @property
    def ask_price_dict(self):
        """Gets the ask_price of this RealtimeStockPrice.  # noqa: E501

        The price of the top ask order. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ask_price
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
            result = { 'ask_price': value }

        
        return result
        

    @ask_price.setter
    def ask_price(self, ask_price):
        """Sets the ask_price of this RealtimeStockPrice.

        The price of the top ask order.  # noqa: E501

        :param ask_price: The ask_price of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._ask_price = ask_price

    @property
    def ask_size(self):
        """Gets the ask_size of this RealtimeStockPrice.  # noqa: E501

        The size of the top ask order.  # noqa: E501

        :return: The ask_size of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._ask_size
        
    @property
    def ask_size_dict(self):
        """Gets the ask_size of this RealtimeStockPrice.  # noqa: E501

        The size of the top ask order. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_size of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ask_size
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
            result = { 'ask_size': value }

        
        return result
        

    @ask_size.setter
    def ask_size(self, ask_size):
        """Sets the ask_size of this RealtimeStockPrice.

        The size of the top ask order.  # noqa: E501

        :param ask_size: The ask_size of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._ask_size = ask_size

    @property
    def open_price(self):
        """Gets the open_price of this RealtimeStockPrice.  # noqa: E501

        The price at the open of the trading day.  # noqa: E501

        :return: The open_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._open_price
        
    @property
    def open_price_dict(self):
        """Gets the open_price of this RealtimeStockPrice.  # noqa: E501

        The price at the open of the trading day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.open_price
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
            result = { 'open_price': value }

        
        return result
        

    @open_price.setter
    def open_price(self, open_price):
        """Sets the open_price of this RealtimeStockPrice.

        The price at the open of the trading day.  # noqa: E501

        :param open_price: The open_price of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._open_price = open_price

    @property
    def close_price(self):
        """Gets the close_price of this RealtimeStockPrice.  # noqa: E501

        The price at the close of the trading day.  # noqa: E501

        :return: The close_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._close_price
        
    @property
    def close_price_dict(self):
        """Gets the close_price of this RealtimeStockPrice.  # noqa: E501

        The price at the close of the trading day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.close_price
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
            result = { 'close_price': value }

        
        return result
        

    @close_price.setter
    def close_price(self, close_price):
        """Sets the close_price of this RealtimeStockPrice.

        The price at the close of the trading day.  # noqa: E501

        :param close_price: The close_price of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._close_price = close_price

    @property
    def high_price(self):
        """Gets the high_price of this RealtimeStockPrice.  # noqa: E501

        The high price for the trading day.  # noqa: E501

        :return: The high_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._high_price
        
    @property
    def high_price_dict(self):
        """Gets the high_price of this RealtimeStockPrice.  # noqa: E501

        The high price for the trading day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The high_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.high_price
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
            result = { 'high_price': value }

        
        return result
        

    @high_price.setter
    def high_price(self, high_price):
        """Sets the high_price of this RealtimeStockPrice.

        The high price for the trading day.  # noqa: E501

        :param high_price: The high_price of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._high_price = high_price

    @property
    def low_price(self):
        """Gets the low_price of this RealtimeStockPrice.  # noqa: E501

        The low price for the trading day.  # noqa: E501

        :return: The low_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._low_price
        
    @property
    def low_price_dict(self):
        """Gets the low_price of this RealtimeStockPrice.  # noqa: E501

        The low price for the trading day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The low_price of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.low_price
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
            result = { 'low_price': value }

        
        return result
        

    @low_price.setter
    def low_price(self, low_price):
        """Sets the low_price of this RealtimeStockPrice.

        The low price for the trading day.  # noqa: E501

        :param low_price: The low_price of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._low_price = low_price

    @property
    def exchange_volume(self):
        """Gets the exchange_volume of this RealtimeStockPrice.  # noqa: E501

        The number of shares exchanged during the trading day on the exchange.  # noqa: E501

        :return: The exchange_volume of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._exchange_volume
        
    @property
    def exchange_volume_dict(self):
        """Gets the exchange_volume of this RealtimeStockPrice.  # noqa: E501

        The number of shares exchanged during the trading day on the exchange. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The exchange_volume of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.exchange_volume
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
            result = { 'exchange_volume': value }

        
        return result
        

    @exchange_volume.setter
    def exchange_volume(self, exchange_volume):
        """Sets the exchange_volume of this RealtimeStockPrice.

        The number of shares exchanged during the trading day on the exchange.  # noqa: E501

        :param exchange_volume: The exchange_volume of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._exchange_volume = exchange_volume

    @property
    def market_volume(self):
        """Gets the market_volume of this RealtimeStockPrice.  # noqa: E501

        The number of shares exchanged during the trading day for the whole market.  # noqa: E501

        :return: The market_volume of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._market_volume
        
    @property
    def market_volume_dict(self):
        """Gets the market_volume of this RealtimeStockPrice.  # noqa: E501

        The number of shares exchanged during the trading day for the whole market. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The market_volume of this RealtimeStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.market_volume
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
            result = { 'market_volume': value }

        
        return result
        

    @market_volume.setter
    def market_volume(self, market_volume):
        """Sets the market_volume of this RealtimeStockPrice.

        The number of shares exchanged during the trading day for the whole market.  # noqa: E501

        :param market_volume: The market_volume of this RealtimeStockPrice.  # noqa: E501
        :type: float
        """

        self._market_volume = market_volume

    @property
    def updated_on(self):
        """Gets the updated_on of this RealtimeStockPrice.  # noqa: E501

        The date and time when the data was last updated.  # noqa: E501

        :return: The updated_on of this RealtimeStockPrice.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on
        
    @property
    def updated_on_dict(self):
        """Gets the updated_on of this RealtimeStockPrice.  # noqa: E501

        The date and time when the data was last updated. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The updated_on of this RealtimeStockPrice.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.updated_on
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
            result = { 'updated_on': value }

        
        return result
        

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this RealtimeStockPrice.

        The date and time when the data was last updated.  # noqa: E501

        :param updated_on: The updated_on of this RealtimeStockPrice.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def source(self):
        """Gets the source of this RealtimeStockPrice.  # noqa: E501

        The source of the data.  # noqa: E501

        :return: The source of this RealtimeStockPrice.  # noqa: E501
        :rtype: str
        """
        return self._source
        
    @property
    def source_dict(self):
        """Gets the source of this RealtimeStockPrice.  # noqa: E501

        The source of the data. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The source of this RealtimeStockPrice.  # noqa: E501
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
        """Sets the source of this RealtimeStockPrice.

        The source of the data.  # noqa: E501

        :param source: The source of this RealtimeStockPrice.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def security(self):
        """Gets the security of this RealtimeStockPrice.  # noqa: E501


        :return: The security of this RealtimeStockPrice.  # noqa: E501
        :rtype: RealtimeStockPriceSecurity
        """
        return self._security
        
    @property
    def security_dict(self):
        """Gets the security of this RealtimeStockPrice.  # noqa: E501


        :return: The security of this RealtimeStockPrice.  # noqa: E501
        :rtype: RealtimeStockPriceSecurity
        """

        result = None

        value = self.security
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
            result = { 'security': value }

        
        return result
        

    @security.setter
    def security(self, security):
        """Sets the security of this RealtimeStockPrice.


        :param security: The security of this RealtimeStockPrice.  # noqa: E501
        :type: RealtimeStockPriceSecurity
        """

        self._security = security

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
        if not isinstance(other, RealtimeStockPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
