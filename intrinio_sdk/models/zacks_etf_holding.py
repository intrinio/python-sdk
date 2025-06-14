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


class ZacksETFHolding(object):
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
        'etf_ticker': 'str',
        'etf_name': 'str',
        'holding_symbol': 'str',
        'holding_name': 'str',
        'date_of_holding': 'date',
        'shares': 'float',
        'weight': 'float'
    }

    attribute_map = {
        'etf_ticker': 'etf_ticker',
        'etf_name': 'etf_name',
        'holding_symbol': 'holding_symbol',
        'holding_name': 'holding_name',
        'date_of_holding': 'date_of_holding',
        'shares': 'shares',
        'weight': 'weight'
    }

    def __init__(self, etf_ticker=None, etf_name=None, holding_symbol=None, holding_name=None, date_of_holding=None, shares=None, weight=None):  # noqa: E501
        """ZacksETFHolding - a model defined in Swagger"""  # noqa: E501

        self._etf_ticker = None
        self._etf_name = None
        self._holding_symbol = None
        self._holding_name = None
        self._date_of_holding = None
        self._shares = None
        self._weight = None
        self.discriminator = None

        if etf_ticker is not None:
            self.etf_ticker = etf_ticker
        if etf_name is not None:
            self.etf_name = etf_name
        if holding_symbol is not None:
            self.holding_symbol = holding_symbol
        if holding_name is not None:
            self.holding_name = holding_name
        if date_of_holding is not None:
            self.date_of_holding = date_of_holding
        if shares is not None:
            self.shares = shares
        if weight is not None:
            self.weight = weight

    @property
    def etf_ticker(self):
        """Gets the etf_ticker of this ZacksETFHolding.  # noqa: E501

        The ETF's common ticker  # noqa: E501

        :return: The etf_ticker of this ZacksETFHolding.  # noqa: E501
        :rtype: str
        """
        return self._etf_ticker
        
    @property
    def etf_ticker_dict(self):
        """Gets the etf_ticker of this ZacksETFHolding.  # noqa: E501

        The ETF's common ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The etf_ticker of this ZacksETFHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.etf_ticker
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
            result = { 'etf_ticker': value }

        
        return result
        

    @etf_ticker.setter
    def etf_ticker(self, etf_ticker):
        """Sets the etf_ticker of this ZacksETFHolding.

        The ETF's common ticker  # noqa: E501

        :param etf_ticker: The etf_ticker of this ZacksETFHolding.  # noqa: E501
        :type: str
        """

        self._etf_ticker = etf_ticker

    @property
    def etf_name(self):
        """Gets the etf_name of this ZacksETFHolding.  # noqa: E501

        The ETF's name  # noqa: E501

        :return: The etf_name of this ZacksETFHolding.  # noqa: E501
        :rtype: str
        """
        return self._etf_name
        
    @property
    def etf_name_dict(self):
        """Gets the etf_name of this ZacksETFHolding.  # noqa: E501

        The ETF's name as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The etf_name of this ZacksETFHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.etf_name
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
            result = { 'etf_name': value }

        
        return result
        

    @etf_name.setter
    def etf_name(self, etf_name):
        """Sets the etf_name of this ZacksETFHolding.

        The ETF's name  # noqa: E501

        :param etf_name: The etf_name of this ZacksETFHolding.  # noqa: E501
        :type: str
        """

        self._etf_name = etf_name

    @property
    def holding_symbol(self):
        """Gets the holding_symbol of this ZacksETFHolding.  # noqa: E501

        The holding's common ticker  # noqa: E501

        :return: The holding_symbol of this ZacksETFHolding.  # noqa: E501
        :rtype: str
        """
        return self._holding_symbol
        
    @property
    def holding_symbol_dict(self):
        """Gets the holding_symbol of this ZacksETFHolding.  # noqa: E501

        The holding's common ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The holding_symbol of this ZacksETFHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.holding_symbol
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
            result = { 'holding_symbol': value }

        
        return result
        

    @holding_symbol.setter
    def holding_symbol(self, holding_symbol):
        """Sets the holding_symbol of this ZacksETFHolding.

        The holding's common ticker  # noqa: E501

        :param holding_symbol: The holding_symbol of this ZacksETFHolding.  # noqa: E501
        :type: str
        """

        self._holding_symbol = holding_symbol

    @property
    def holding_name(self):
        """Gets the holding_name of this ZacksETFHolding.  # noqa: E501

        The holding's name  # noqa: E501

        :return: The holding_name of this ZacksETFHolding.  # noqa: E501
        :rtype: str
        """
        return self._holding_name
        
    @property
    def holding_name_dict(self):
        """Gets the holding_name of this ZacksETFHolding.  # noqa: E501

        The holding's name as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The holding_name of this ZacksETFHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.holding_name
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
            result = { 'holding_name': value }

        
        return result
        

    @holding_name.setter
    def holding_name(self, holding_name):
        """Sets the holding_name of this ZacksETFHolding.

        The holding's name  # noqa: E501

        :param holding_name: The holding_name of this ZacksETFHolding.  # noqa: E501
        :type: str
        """

        self._holding_name = holding_name

    @property
    def date_of_holding(self):
        """Gets the date_of_holding of this ZacksETFHolding.  # noqa: E501

        The date of the holding  # noqa: E501

        :return: The date_of_holding of this ZacksETFHolding.  # noqa: E501
        :rtype: date
        """
        return self._date_of_holding
        
    @property
    def date_of_holding_dict(self):
        """Gets the date_of_holding of this ZacksETFHolding.  # noqa: E501

        The date of the holding as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date_of_holding of this ZacksETFHolding.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.date_of_holding
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
            result = { 'date_of_holding': value }

        
        return result
        

    @date_of_holding.setter
    def date_of_holding(self, date_of_holding):
        """Sets the date_of_holding of this ZacksETFHolding.

        The date of the holding  # noqa: E501

        :param date_of_holding: The date_of_holding of this ZacksETFHolding.  # noqa: E501
        :type: date
        """

        self._date_of_holding = date_of_holding

    @property
    def shares(self):
        """Gets the shares of this ZacksETFHolding.  # noqa: E501

        The number of shares  # noqa: E501

        :return: The shares of this ZacksETFHolding.  # noqa: E501
        :rtype: float
        """
        return self._shares
        
    @property
    def shares_dict(self):
        """Gets the shares of this ZacksETFHolding.  # noqa: E501

        The number of shares as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shares of this ZacksETFHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.shares
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
            result = { 'shares': value }

        
        return result
        

    @shares.setter
    def shares(self, shares):
        """Sets the shares of this ZacksETFHolding.

        The number of shares  # noqa: E501

        :param shares: The shares of this ZacksETFHolding.  # noqa: E501
        :type: float
        """

        self._shares = shares

    @property
    def weight(self):
        """Gets the weight of this ZacksETFHolding.  # noqa: E501

        The weight of the holding  # noqa: E501

        :return: The weight of this ZacksETFHolding.  # noqa: E501
        :rtype: float
        """
        return self._weight
        
    @property
    def weight_dict(self):
        """Gets the weight of this ZacksETFHolding.  # noqa: E501

        The weight of the holding as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The weight of this ZacksETFHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.weight
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
            result = { 'weight': value }

        
        return result
        

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ZacksETFHolding.

        The weight of the holding  # noqa: E501

        :param weight: The weight of this ZacksETFHolding.  # noqa: E501
        :type: float
        """

        self._weight = weight

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
        if not isinstance(other, ZacksETFHolding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
