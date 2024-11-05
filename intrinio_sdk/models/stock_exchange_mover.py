# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.73.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StockExchangeMover(object):
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
        'security_id': 'str',
        'ticker': 'str',
        'last_price': 'float',
        'change': 'float',
        'percent_change': 'float',
        'market_volume': 'float',
        'source': 'str'
    }

    attribute_map = {
        'security_id': 'security_id',
        'ticker': 'ticker',
        'last_price': 'last_price',
        'change': 'change',
        'percent_change': 'percent_change',
        'market_volume': 'market_volume',
        'source': 'source'
    }

    def __init__(self, security_id=None, ticker=None, last_price=None, change=None, percent_change=None, market_volume=None, source=None):  # noqa: E501
        """StockExchangeMover - a model defined in Swagger"""  # noqa: E501

        self._security_id = None
        self._ticker = None
        self._last_price = None
        self._change = None
        self._percent_change = None
        self._market_volume = None
        self._source = None
        self.discriminator = None

        if security_id is not None:
            self.security_id = security_id
        if ticker is not None:
            self.ticker = ticker
        if last_price is not None:
            self.last_price = last_price
        if change is not None:
            self.change = change
        if percent_change is not None:
            self.percent_change = percent_change
        if market_volume is not None:
            self.market_volume = market_volume
        if source is not None:
            self.source = source

    @property
    def security_id(self):
        """Gets the security_id of this StockExchangeMover.  # noqa: E501

        The Intrinio Identifier for this security.  # noqa: E501

        :return: The security_id of this StockExchangeMover.  # noqa: E501
        :rtype: str
        """
        return self._security_id
        
    @property
    def security_id_dict(self):
        """Gets the security_id of this StockExchangeMover.  # noqa: E501

        The Intrinio Identifier for this security. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The security_id of this StockExchangeMover.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.security_id
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
            result = { 'security_id': value }

        
        return result
        

    @security_id.setter
    def security_id(self, security_id):
        """Sets the security_id of this StockExchangeMover.

        The Intrinio Identifier for this security.  # noqa: E501

        :param security_id: The security_id of this StockExchangeMover.  # noqa: E501
        :type: str
        """

        self._security_id = security_id

    @property
    def ticker(self):
        """Gets the ticker of this StockExchangeMover.  # noqa: E501

        The ticker symbol for this security.  # noqa: E501

        :return: The ticker of this StockExchangeMover.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this StockExchangeMover.  # noqa: E501

        The ticker symbol for this security. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this StockExchangeMover.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.ticker
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
            result = { 'ticker': value }

        
        return result
        

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this StockExchangeMover.

        The ticker symbol for this security.  # noqa: E501

        :param ticker: The ticker of this StockExchangeMover.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def last_price(self):
        """Gets the last_price of this StockExchangeMover.  # noqa: E501

        The last price of the last trade.  # noqa: E501

        :return: The last_price of this StockExchangeMover.  # noqa: E501
        :rtype: float
        """
        return self._last_price
        
    @property
    def last_price_dict(self):
        """Gets the last_price of this StockExchangeMover.  # noqa: E501

        The last price of the last trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_price of this StockExchangeMover.  # noqa: E501
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
        """Sets the last_price of this StockExchangeMover.

        The last price of the last trade.  # noqa: E501

        :param last_price: The last_price of this StockExchangeMover.  # noqa: E501
        :type: float
        """

        self._last_price = last_price

    @property
    def change(self):
        """Gets the change of this StockExchangeMover.  # noqa: E501

        The raw change in price.  # noqa: E501

        :return: The change of this StockExchangeMover.  # noqa: E501
        :rtype: float
        """
        return self._change
        
    @property
    def change_dict(self):
        """Gets the change of this StockExchangeMover.  # noqa: E501

        The raw change in price. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The change of this StockExchangeMover.  # noqa: E501
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
        """Sets the change of this StockExchangeMover.

        The raw change in price.  # noqa: E501

        :param change: The change of this StockExchangeMover.  # noqa: E501
        :type: float
        """

        self._change = change

    @property
    def percent_change(self):
        """Gets the percent_change of this StockExchangeMover.  # noqa: E501

        The percent change in price.  # noqa: E501

        :return: The percent_change of this StockExchangeMover.  # noqa: E501
        :rtype: float
        """
        return self._percent_change
        
    @property
    def percent_change_dict(self):
        """Gets the percent_change of this StockExchangeMover.  # noqa: E501

        The percent change in price. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The percent_change of this StockExchangeMover.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.percent_change
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
            result = { 'percent_change': value }

        
        return result
        

    @percent_change.setter
    def percent_change(self, percent_change):
        """Sets the percent_change of this StockExchangeMover.

        The percent change in price.  # noqa: E501

        :param percent_change: The percent_change of this StockExchangeMover.  # noqa: E501
        :type: float
        """

        self._percent_change = percent_change

    @property
    def market_volume(self):
        """Gets the market_volume of this StockExchangeMover.  # noqa: E501

        The market volume for the most recent (today) trading day.  # noqa: E501

        :return: The market_volume of this StockExchangeMover.  # noqa: E501
        :rtype: float
        """
        return self._market_volume
        
    @property
    def market_volume_dict(self):
        """Gets the market_volume of this StockExchangeMover.  # noqa: E501

        The market volume for the most recent (today) trading day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The market_volume of this StockExchangeMover.  # noqa: E501
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
        """Sets the market_volume of this StockExchangeMover.

        The market volume for the most recent (today) trading day.  # noqa: E501

        :param market_volume: The market_volume of this StockExchangeMover.  # noqa: E501
        :type: float
        """

        self._market_volume = market_volume

    @property
    def source(self):
        """Gets the source of this StockExchangeMover.  # noqa: E501

        The source of the data.  # noqa: E501

        :return: The source of this StockExchangeMover.  # noqa: E501
        :rtype: str
        """
        return self._source
        
    @property
    def source_dict(self):
        """Gets the source of this StockExchangeMover.  # noqa: E501

        The source of the data. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The source of this StockExchangeMover.  # noqa: E501
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
        """Sets the source of this StockExchangeMover.

        The source of the data.  # noqa: E501

        :param source: The source of this StockExchangeMover.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if not isinstance(other, StockExchangeMover):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
