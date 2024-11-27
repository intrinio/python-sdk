# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.76.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OptionTrades(object):
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
        'contract': 'str',
        'underlying_symbol': 'str',
        'timestamp': 'datetime',
        'price': 'float',
        'size': 'float',
        'total_volume': 'float',
        'ask_price_at_execution': 'float',
        'bid_price_at_execution': 'float',
        'exchange': 'str',
        'conditions': 'str',
        'sequence_id': 'float'
    }

    attribute_map = {
        'contract': 'contract',
        'underlying_symbol': 'underlying_symbol',
        'timestamp': 'timestamp',
        'price': 'price',
        'size': 'size',
        'total_volume': 'total_volume',
        'ask_price_at_execution': 'ask_price_at_execution',
        'bid_price_at_execution': 'bid_price_at_execution',
        'exchange': 'exchange',
        'conditions': 'conditions',
        'sequence_id': 'sequence_id'
    }

    def __init__(self, contract=None, underlying_symbol=None, timestamp=None, price=None, size=None, total_volume=None, ask_price_at_execution=None, bid_price_at_execution=None, exchange=None, conditions=None, sequence_id=None):  # noqa: E501
        """OptionTrades - a model defined in Swagger"""  # noqa: E501

        self._contract = None
        self._underlying_symbol = None
        self._timestamp = None
        self._price = None
        self._size = None
        self._total_volume = None
        self._ask_price_at_execution = None
        self._bid_price_at_execution = None
        self._exchange = None
        self._conditions = None
        self._sequence_id = None
        self.discriminator = None

        if contract is not None:
            self.contract = contract
        if underlying_symbol is not None:
            self.underlying_symbol = underlying_symbol
        if timestamp is not None:
            self.timestamp = timestamp
        if price is not None:
            self.price = price
        if size is not None:
            self.size = size
        if total_volume is not None:
            self.total_volume = total_volume
        if ask_price_at_execution is not None:
            self.ask_price_at_execution = ask_price_at_execution
        if bid_price_at_execution is not None:
            self.bid_price_at_execution = bid_price_at_execution
        if exchange is not None:
            self.exchange = exchange
        if conditions is not None:
            self.conditions = conditions
        if sequence_id is not None:
            self.sequence_id = sequence_id

    @property
    def contract(self):
        """Gets the contract of this OptionTrades.  # noqa: E501

        The option contract  # noqa: E501

        :return: The contract of this OptionTrades.  # noqa: E501
        :rtype: str
        """
        return self._contract
        
    @property
    def contract_dict(self):
        """Gets the contract of this OptionTrades.  # noqa: E501

        The option contract as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The contract of this OptionTrades.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.contract
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
            result = { 'contract': value }

        
        return result
        

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this OptionTrades.

        The option contract  # noqa: E501

        :param contract: The contract of this OptionTrades.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def underlying_symbol(self):
        """Gets the underlying_symbol of this OptionTrades.  # noqa: E501

        The ticker symbol  # noqa: E501

        :return: The underlying_symbol of this OptionTrades.  # noqa: E501
        :rtype: str
        """
        return self._underlying_symbol
        
    @property
    def underlying_symbol_dict(self):
        """Gets the underlying_symbol of this OptionTrades.  # noqa: E501

        The ticker symbol as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The underlying_symbol of this OptionTrades.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.underlying_symbol
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
            result = { 'underlying_symbol': value }

        
        return result
        

    @underlying_symbol.setter
    def underlying_symbol(self, underlying_symbol):
        """Sets the underlying_symbol of this OptionTrades.

        The ticker symbol  # noqa: E501

        :param underlying_symbol: The underlying_symbol of this OptionTrades.  # noqa: E501
        :type: str
        """

        self._underlying_symbol = underlying_symbol

    @property
    def timestamp(self):
        """Gets the timestamp of this OptionTrades.  # noqa: E501

        The UTC timestamp at the time of the trade.  # noqa: E501

        :return: The timestamp of this OptionTrades.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp
        
    @property
    def timestamp_dict(self):
        """Gets the timestamp of this OptionTrades.  # noqa: E501

        The UTC timestamp at the time of the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The timestamp of this OptionTrades.  # noqa: E501
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
        """Sets the timestamp of this OptionTrades.

        The UTC timestamp at the time of the trade.  # noqa: E501

        :param timestamp: The timestamp of this OptionTrades.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def price(self):
        """Gets the price of this OptionTrades.  # noqa: E501

        The price of the trade.  # noqa: E501

        :return: The price of this OptionTrades.  # noqa: E501
        :rtype: float
        """
        return self._price
        
    @property
    def price_dict(self):
        """Gets the price of this OptionTrades.  # noqa: E501

        The price of the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The price of this OptionTrades.  # noqa: E501
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
        """Sets the price of this OptionTrades.

        The price of the trade.  # noqa: E501

        :param price: The price of this OptionTrades.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def size(self):
        """Gets the size of this OptionTrades.  # noqa: E501

        The size of the trade.  # noqa: E501

        :return: The size of this OptionTrades.  # noqa: E501
        :rtype: float
        """
        return self._size
        
    @property
    def size_dict(self):
        """Gets the size of this OptionTrades.  # noqa: E501

        The size of the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The size of this OptionTrades.  # noqa: E501
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
        """Sets the size of this OptionTrades.

        The size of the trade.  # noqa: E501

        :param size: The size of this OptionTrades.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def total_volume(self):
        """Gets the total_volume of this OptionTrades.  # noqa: E501

        The total volume of the symbol for the day up to the timestamp point in time.  # noqa: E501

        :return: The total_volume of this OptionTrades.  # noqa: E501
        :rtype: float
        """
        return self._total_volume
        
    @property
    def total_volume_dict(self):
        """Gets the total_volume of this OptionTrades.  # noqa: E501

        The total volume of the symbol for the day up to the timestamp point in time. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_volume of this OptionTrades.  # noqa: E501
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
        """Sets the total_volume of this OptionTrades.

        The total volume of the symbol for the day up to the timestamp point in time.  # noqa: E501

        :param total_volume: The total_volume of this OptionTrades.  # noqa: E501
        :type: float
        """

        self._total_volume = total_volume

    @property
    def ask_price_at_execution(self):
        """Gets the ask_price_at_execution of this OptionTrades.  # noqa: E501

        The price of ask quote at the time of the trade.  # noqa: E501

        :return: The ask_price_at_execution of this OptionTrades.  # noqa: E501
        :rtype: float
        """
        return self._ask_price_at_execution
        
    @property
    def ask_price_at_execution_dict(self):
        """Gets the ask_price_at_execution of this OptionTrades.  # noqa: E501

        The price of ask quote at the time of the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_price_at_execution of this OptionTrades.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ask_price_at_execution
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
            result = { 'ask_price_at_execution': value }

        
        return result
        

    @ask_price_at_execution.setter
    def ask_price_at_execution(self, ask_price_at_execution):
        """Sets the ask_price_at_execution of this OptionTrades.

        The price of ask quote at the time of the trade.  # noqa: E501

        :param ask_price_at_execution: The ask_price_at_execution of this OptionTrades.  # noqa: E501
        :type: float
        """

        self._ask_price_at_execution = ask_price_at_execution

    @property
    def bid_price_at_execution(self):
        """Gets the bid_price_at_execution of this OptionTrades.  # noqa: E501

        The price of bid quote at the time of the trade.  # noqa: E501

        :return: The bid_price_at_execution of this OptionTrades.  # noqa: E501
        :rtype: float
        """
        return self._bid_price_at_execution
        
    @property
    def bid_price_at_execution_dict(self):
        """Gets the bid_price_at_execution of this OptionTrades.  # noqa: E501

        The price of bid quote at the time of the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_price_at_execution of this OptionTrades.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.bid_price_at_execution
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
            result = { 'bid_price_at_execution': value }

        
        return result
        

    @bid_price_at_execution.setter
    def bid_price_at_execution(self, bid_price_at_execution):
        """Sets the bid_price_at_execution of this OptionTrades.

        The price of bid quote at the time of the trade.  # noqa: E501

        :param bid_price_at_execution: The bid_price_at_execution of this OptionTrades.  # noqa: E501
        :type: float
        """

        self._bid_price_at_execution = bid_price_at_execution

    @property
    def exchange(self):
        """Gets the exchange of this OptionTrades.  # noqa: E501

        The exchange for the trade.  # noqa: E501

        :return: The exchange of this OptionTrades.  # noqa: E501
        :rtype: str
        """
        return self._exchange
        
    @property
    def exchange_dict(self):
        """Gets the exchange of this OptionTrades.  # noqa: E501

        The exchange for the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The exchange of this OptionTrades.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.exchange
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
            result = { 'exchange': value }

        
        return result
        

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this OptionTrades.

        The exchange for the trade.  # noqa: E501

        :param exchange: The exchange of this OptionTrades.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def conditions(self):
        """Gets the conditions of this OptionTrades.  # noqa: E501

        The condition of the trade.  # noqa: E501

        :return: The conditions of this OptionTrades.  # noqa: E501
        :rtype: str
        """
        return self._conditions
        
    @property
    def conditions_dict(self):
        """Gets the conditions of this OptionTrades.  # noqa: E501

        The condition of the trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The conditions of this OptionTrades.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.conditions
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
            result = { 'conditions': value }

        
        return result
        

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this OptionTrades.

        The condition of the trade.  # noqa: E501

        :param conditions: The conditions of this OptionTrades.  # noqa: E501
        :type: str
        """

        self._conditions = conditions

    @property
    def sequence_id(self):
        """Gets the sequence_id of this OptionTrades.  # noqa: E501

        The sequential ID for the trade, ordered as temporally received from the exchange.  # noqa: E501

        :return: The sequence_id of this OptionTrades.  # noqa: E501
        :rtype: float
        """
        return self._sequence_id
        
    @property
    def sequence_id_dict(self):
        """Gets the sequence_id of this OptionTrades.  # noqa: E501

        The sequential ID for the trade, ordered as temporally received from the exchange. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sequence_id of this OptionTrades.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.sequence_id
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
            result = { 'sequence_id': value }

        
        return result
        

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """Sets the sequence_id of this OptionTrades.

        The sequential ID for the trade, ordered as temporally received from the exchange.  # noqa: E501

        :param sequence_id: The sequence_id of this OptionTrades.  # noqa: E501
        :type: float
        """

        self._sequence_id = sequence_id

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
        if not isinstance(other, OptionTrades):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other