# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.56.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OptionPrice(object):
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
        'date': 'str',
        'close': 'float',
        'close_bid': 'float',
        'close_ask': 'float',
        'volume': 'int',
        'volume_bid': 'int',
        'volume_ask': 'int',
        'trades': 'int',
        'open_interest': 'int',
        'open_interest_change': 'int',
        'next_day_open_interest': 'int',
        'implied_volatility': 'float',
        'implied_volatility_change': 'float',
        'delta': 'float'
    }

    attribute_map = {
        'date': 'date',
        'close': 'close',
        'close_bid': 'close_bid',
        'close_ask': 'close_ask',
        'volume': 'volume',
        'volume_bid': 'volume_bid',
        'volume_ask': 'volume_ask',
        'trades': 'trades',
        'open_interest': 'open_interest',
        'open_interest_change': 'open_interest_change',
        'next_day_open_interest': 'next_day_open_interest',
        'implied_volatility': 'implied_volatility',
        'implied_volatility_change': 'implied_volatility_change',
        'delta': 'delta'
    }

    def __init__(self, date=None, close=None, close_bid=None, close_ask=None, volume=None, volume_bid=None, volume_ask=None, trades=None, open_interest=None, open_interest_change=None, next_day_open_interest=None, implied_volatility=None, implied_volatility_change=None, delta=None):  # noqa: E501
        """OptionPrice - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._close = None
        self._close_bid = None
        self._close_ask = None
        self._volume = None
        self._volume_bid = None
        self._volume_ask = None
        self._trades = None
        self._open_interest = None
        self._open_interest_change = None
        self._next_day_open_interest = None
        self._implied_volatility = None
        self._implied_volatility_change = None
        self._delta = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if close is not None:
            self.close = close
        if close_bid is not None:
            self.close_bid = close_bid
        if close_ask is not None:
            self.close_ask = close_ask
        if volume is not None:
            self.volume = volume
        if volume_bid is not None:
            self.volume_bid = volume_bid
        if volume_ask is not None:
            self.volume_ask = volume_ask
        if trades is not None:
            self.trades = trades
        if open_interest is not None:
            self.open_interest = open_interest
        if open_interest_change is not None:
            self.open_interest_change = open_interest_change
        if next_day_open_interest is not None:
            self.next_day_open_interest = next_day_open_interest
        if implied_volatility is not None:
            self.implied_volatility = implied_volatility
        if implied_volatility_change is not None:
            self.implied_volatility_change = implied_volatility_change
        if delta is not None:
            self.delta = delta

    @property
    def date(self):
        """Gets the date of this OptionPrice.  # noqa: E501

        The date of the price, in the format YYYY-MM-DD  # noqa: E501

        :return: The date of this OptionPrice.  # noqa: E501
        :rtype: str
        """
        return self._date
        
    @property
    def date_dict(self):
        """Gets the date of this OptionPrice.  # noqa: E501

        The date of the price, in the format YYYY-MM-DD as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date of this OptionPrice.  # noqa: E501
        :rtype: str
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
        """Sets the date of this OptionPrice.

        The date of the price, in the format YYYY-MM-DD  # noqa: E501

        :param date: The date of this OptionPrice.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def close(self):
        """Gets the close of this OptionPrice.  # noqa: E501

        The closing price of the options contract.  # noqa: E501

        :return: The close of this OptionPrice.  # noqa: E501
        :rtype: float
        """
        return self._close
        
    @property
    def close_dict(self):
        """Gets the close of this OptionPrice.  # noqa: E501

        The closing price of the options contract. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close of this OptionPrice.  # noqa: E501
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
        """Sets the close of this OptionPrice.

        The closing price of the options contract.  # noqa: E501

        :param close: The close of this OptionPrice.  # noqa: E501
        :type: float
        """

        self._close = close

    @property
    def close_bid(self):
        """Gets the close_bid of this OptionPrice.  # noqa: E501

        The closing bid price of the options contract.  # noqa: E501

        :return: The close_bid of this OptionPrice.  # noqa: E501
        :rtype: float
        """
        return self._close_bid
        
    @property
    def close_bid_dict(self):
        """Gets the close_bid of this OptionPrice.  # noqa: E501

        The closing bid price of the options contract. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close_bid of this OptionPrice.  # noqa: E501
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
        """Sets the close_bid of this OptionPrice.

        The closing bid price of the options contract.  # noqa: E501

        :param close_bid: The close_bid of this OptionPrice.  # noqa: E501
        :type: float
        """

        self._close_bid = close_bid

    @property
    def close_ask(self):
        """Gets the close_ask of this OptionPrice.  # noqa: E501

        The closing ask price of the options contract.  # noqa: E501

        :return: The close_ask of this OptionPrice.  # noqa: E501
        :rtype: float
        """
        return self._close_ask
        
    @property
    def close_ask_dict(self):
        """Gets the close_ask of this OptionPrice.  # noqa: E501

        The closing ask price of the options contract. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close_ask of this OptionPrice.  # noqa: E501
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
        """Sets the close_ask of this OptionPrice.

        The closing ask price of the options contract.  # noqa: E501

        :param close_ask: The close_ask of this OptionPrice.  # noqa: E501
        :type: float
        """

        self._close_ask = close_ask

    @property
    def volume(self):
        """Gets the volume of this OptionPrice.  # noqa: E501

        The cumulative volume of this options contract that traded that day.  # noqa: E501

        :return: The volume of this OptionPrice.  # noqa: E501
        :rtype: int
        """
        return self._volume
        
    @property
    def volume_dict(self):
        """Gets the volume of this OptionPrice.  # noqa: E501

        The cumulative volume of this options contract that traded that day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The volume of this OptionPrice.  # noqa: E501
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
        """Sets the volume of this OptionPrice.

        The cumulative volume of this options contract that traded that day.  # noqa: E501

        :param volume: The volume of this OptionPrice.  # noqa: E501
        :type: int
        """

        self._volume = volume

    @property
    def volume_bid(self):
        """Gets the volume_bid of this OptionPrice.  # noqa: E501

        The cumulative volume of this options contract that traded on the bid price that day.  # noqa: E501

        :return: The volume_bid of this OptionPrice.  # noqa: E501
        :rtype: int
        """
        return self._volume_bid
        
    @property
    def volume_bid_dict(self):
        """Gets the volume_bid of this OptionPrice.  # noqa: E501

        The cumulative volume of this options contract that traded on the bid price that day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The volume_bid of this OptionPrice.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.volume_bid
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
            result = { 'volume_bid': value }

        
        return result
        

    @volume_bid.setter
    def volume_bid(self, volume_bid):
        """Sets the volume_bid of this OptionPrice.

        The cumulative volume of this options contract that traded on the bid price that day.  # noqa: E501

        :param volume_bid: The volume_bid of this OptionPrice.  # noqa: E501
        :type: int
        """

        self._volume_bid = volume_bid

    @property
    def volume_ask(self):
        """Gets the volume_ask of this OptionPrice.  # noqa: E501

        The cumulative volume of this options contract that traded on the ask price that day.  # noqa: E501

        :return: The volume_ask of this OptionPrice.  # noqa: E501
        :rtype: int
        """
        return self._volume_ask
        
    @property
    def volume_ask_dict(self):
        """Gets the volume_ask of this OptionPrice.  # noqa: E501

        The cumulative volume of this options contract that traded on the ask price that day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The volume_ask of this OptionPrice.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.volume_ask
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
            result = { 'volume_ask': value }

        
        return result
        

    @volume_ask.setter
    def volume_ask(self, volume_ask):
        """Sets the volume_ask of this OptionPrice.

        The cumulative volume of this options contract that traded on the ask price that day.  # noqa: E501

        :param volume_ask: The volume_ask of this OptionPrice.  # noqa: E501
        :type: int
        """

        self._volume_ask = volume_ask

    @property
    def trades(self):
        """Gets the trades of this OptionPrice.  # noqa: E501

        The number of trades executed that for this options contract on that day.  # noqa: E501

        :return: The trades of this OptionPrice.  # noqa: E501
        :rtype: int
        """
        return self._trades
        
    @property
    def trades_dict(self):
        """Gets the trades of this OptionPrice.  # noqa: E501

        The number of trades executed that for this options contract on that day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The trades of this OptionPrice.  # noqa: E501
        :rtype: int
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
        """Sets the trades of this OptionPrice.

        The number of trades executed that for this options contract on that day.  # noqa: E501

        :param trades: The trades of this OptionPrice.  # noqa: E501
        :type: int
        """

        self._trades = trades

    @property
    def open_interest(self):
        """Gets the open_interest of this OptionPrice.  # noqa: E501

        The total number of this options contract that are still open.  # noqa: E501

        :return: The open_interest of this OptionPrice.  # noqa: E501
        :rtype: int
        """
        return self._open_interest
        
    @property
    def open_interest_dict(self):
        """Gets the open_interest of this OptionPrice.  # noqa: E501

        The total number of this options contract that are still open. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open_interest of this OptionPrice.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.open_interest
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
            result = { 'open_interest': value }

        
        return result
        

    @open_interest.setter
    def open_interest(self, open_interest):
        """Sets the open_interest of this OptionPrice.

        The total number of this options contract that are still open.  # noqa: E501

        :param open_interest: The open_interest of this OptionPrice.  # noqa: E501
        :type: int
        """

        self._open_interest = open_interest

    @property
    def open_interest_change(self):
        """Gets the open_interest_change of this OptionPrice.  # noqa: E501

        The change in the total number of this options contract that are still open from the previous day.  # noqa: E501

        :return: The open_interest_change of this OptionPrice.  # noqa: E501
        :rtype: int
        """
        return self._open_interest_change
        
    @property
    def open_interest_change_dict(self):
        """Gets the open_interest_change of this OptionPrice.  # noqa: E501

        The change in the total number of this options contract that are still open from the previous day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open_interest_change of this OptionPrice.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.open_interest_change
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
            result = { 'open_interest_change': value }

        
        return result
        

    @open_interest_change.setter
    def open_interest_change(self, open_interest_change):
        """Sets the open_interest_change of this OptionPrice.

        The change in the total number of this options contract that are still open from the previous day.  # noqa: E501

        :param open_interest_change: The open_interest_change of this OptionPrice.  # noqa: E501
        :type: int
        """

        self._open_interest_change = open_interest_change

    @property
    def next_day_open_interest(self):
        """Gets the next_day_open_interest of this OptionPrice.  # noqa: E501

        The total number of this options contract that are still open at the start of the next day.  # noqa: E501

        :return: The next_day_open_interest of this OptionPrice.  # noqa: E501
        :rtype: int
        """
        return self._next_day_open_interest
        
    @property
    def next_day_open_interest_dict(self):
        """Gets the next_day_open_interest of this OptionPrice.  # noqa: E501

        The total number of this options contract that are still open at the start of the next day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The next_day_open_interest of this OptionPrice.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.next_day_open_interest
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
            result = { 'next_day_open_interest': value }

        
        return result
        

    @next_day_open_interest.setter
    def next_day_open_interest(self, next_day_open_interest):
        """Sets the next_day_open_interest of this OptionPrice.

        The total number of this options contract that are still open at the start of the next day.  # noqa: E501

        :param next_day_open_interest: The next_day_open_interest of this OptionPrice.  # noqa: E501
        :type: int
        """

        self._next_day_open_interest = next_day_open_interest

    @property
    def implied_volatility(self):
        """Gets the implied_volatility of this OptionPrice.  # noqa: E501

        The estimated volatility of the Security's price. Volatility is a statistical measure of dispersion of returns for the Security. Standard deviation of a Security's returns and a market index is an example of a measurement of volatility. Implied volatility approximates the future value of an option, and the option's current value takes this into consideration.  # noqa: E501

        :return: The implied_volatility of this OptionPrice.  # noqa: E501
        :rtype: float
        """
        return self._implied_volatility
        
    @property
    def implied_volatility_dict(self):
        """Gets the implied_volatility of this OptionPrice.  # noqa: E501

        The estimated volatility of the Security's price. Volatility is a statistical measure of dispersion of returns for the Security. Standard deviation of a Security's returns and a market index is an example of a measurement of volatility. Implied volatility approximates the future value of an option, and the option's current value takes this into consideration. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The implied_volatility of this OptionPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.implied_volatility
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
            result = { 'implied_volatility': value }

        
        return result
        

    @implied_volatility.setter
    def implied_volatility(self, implied_volatility):
        """Sets the implied_volatility of this OptionPrice.

        The estimated volatility of the Security's price. Volatility is a statistical measure of dispersion of returns for the Security. Standard deviation of a Security's returns and a market index is an example of a measurement of volatility. Implied volatility approximates the future value of an option, and the option's current value takes this into consideration.  # noqa: E501

        :param implied_volatility: The implied_volatility of this OptionPrice.  # noqa: E501
        :type: float
        """

        self._implied_volatility = implied_volatility

    @property
    def implied_volatility_change(self):
        """Gets the implied_volatility_change of this OptionPrice.  # noqa: E501

        The change in implied volatility for that day.  # noqa: E501

        :return: The implied_volatility_change of this OptionPrice.  # noqa: E501
        :rtype: float
        """
        return self._implied_volatility_change
        
    @property
    def implied_volatility_change_dict(self):
        """Gets the implied_volatility_change of this OptionPrice.  # noqa: E501

        The change in implied volatility for that day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The implied_volatility_change of this OptionPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.implied_volatility_change
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
            result = { 'implied_volatility_change': value }

        
        return result
        

    @implied_volatility_change.setter
    def implied_volatility_change(self, implied_volatility_change):
        """Sets the implied_volatility_change of this OptionPrice.

        The change in implied volatility for that day.  # noqa: E501

        :param implied_volatility_change: The implied_volatility_change of this OptionPrice.  # noqa: E501
        :type: float
        """

        self._implied_volatility_change = implied_volatility_change

    @property
    def delta(self):
        """Gets the delta of this OptionPrice.  # noqa: E501

        Delta measures the degree to which an options contract is exposed to shifts in the price of the underlying Security. Values of delta range from 0.0 to 1.0 for call options and -1.0 to 0.0 for put options. For example, if a put option has a delta of -0.50, if the price of the underlying Security increases by $1, the price of the put option will decrease by $0.50.  # noqa: E501

        :return: The delta of this OptionPrice.  # noqa: E501
        :rtype: float
        """
        return self._delta
        
    @property
    def delta_dict(self):
        """Gets the delta of this OptionPrice.  # noqa: E501

        Delta measures the degree to which an options contract is exposed to shifts in the price of the underlying Security. Values of delta range from 0.0 to 1.0 for call options and -1.0 to 0.0 for put options. For example, if a put option has a delta of -0.50, if the price of the underlying Security increases by $1, the price of the put option will decrease by $0.50. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The delta of this OptionPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.delta
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
            result = { 'delta': value }

        
        return result
        

    @delta.setter
    def delta(self, delta):
        """Sets the delta of this OptionPrice.

        Delta measures the degree to which an options contract is exposed to shifts in the price of the underlying Security. Values of delta range from 0.0 to 1.0 for call options and -1.0 to 0.0 for put options. For example, if a put option has a delta of -0.50, if the price of the underlying Security increases by $1, the price of the put option will decrease by $0.50.  # noqa: E501

        :param delta: The delta of this OptionPrice.  # noqa: E501
        :type: float
        """

        self._delta = delta

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
        if not isinstance(other, OptionPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
