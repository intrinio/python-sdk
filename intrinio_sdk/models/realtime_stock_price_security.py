# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.64.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RealtimeStockPriceSecurity(object):
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
        'id': 'str',
        'ticker': 'str',
        'exchange_ticker': 'str',
        'figi': 'str',
        'composite_figi': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ticker': 'ticker',
        'exchange_ticker': 'exchange_ticker',
        'figi': 'figi',
        'composite_figi': 'composite_figi'
    }

    def __init__(self, id=None, ticker=None, exchange_ticker=None, figi=None, composite_figi=None):  # noqa: E501
        """RealtimeStockPriceSecurity - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._ticker = None
        self._exchange_ticker = None
        self._figi = None
        self._composite_figi = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ticker is not None:
            self.ticker = ticker
        if exchange_ticker is not None:
            self.exchange_ticker = exchange_ticker
        if figi is not None:
            self.figi = figi
        if composite_figi is not None:
            self.composite_figi = composite_figi

    @property
    def id(self):
        """Gets the id of this RealtimeStockPriceSecurity.  # noqa: E501

        The Intrinio ID for Security  # noqa: E501

        :return: The id of this RealtimeStockPriceSecurity.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this RealtimeStockPriceSecurity.  # noqa: E501

        The Intrinio ID for Security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this RealtimeStockPriceSecurity.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.id
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
            result = { 'id': value }

        
        return result
        

    @id.setter
    def id(self, id):
        """Sets the id of this RealtimeStockPriceSecurity.

        The Intrinio ID for Security  # noqa: E501

        :param id: The id of this RealtimeStockPriceSecurity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ticker(self):
        """Gets the ticker of this RealtimeStockPriceSecurity.  # noqa: E501

        The common/local ticker of the Security  # noqa: E501

        :return: The ticker of this RealtimeStockPriceSecurity.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this RealtimeStockPriceSecurity.  # noqa: E501

        The common/local ticker of the Security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this RealtimeStockPriceSecurity.  # noqa: E501
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
        """Sets the ticker of this RealtimeStockPriceSecurity.

        The common/local ticker of the Security  # noqa: E501

        :param ticker: The ticker of this RealtimeStockPriceSecurity.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def exchange_ticker(self):
        """Gets the exchange_ticker of this RealtimeStockPriceSecurity.  # noqa: E501

        The exchange-level ticker  # noqa: E501

        :return: The exchange_ticker of this RealtimeStockPriceSecurity.  # noqa: E501
        :rtype: str
        """
        return self._exchange_ticker
        
    @property
    def exchange_ticker_dict(self):
        """Gets the exchange_ticker of this RealtimeStockPriceSecurity.  # noqa: E501

        The exchange-level ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The exchange_ticker of this RealtimeStockPriceSecurity.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.exchange_ticker
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
            result = { 'exchange_ticker': value }

        
        return result
        

    @exchange_ticker.setter
    def exchange_ticker(self, exchange_ticker):
        """Sets the exchange_ticker of this RealtimeStockPriceSecurity.

        The exchange-level ticker  # noqa: E501

        :param exchange_ticker: The exchange_ticker of this RealtimeStockPriceSecurity.  # noqa: E501
        :type: str
        """

        self._exchange_ticker = exchange_ticker

    @property
    def figi(self):
        """Gets the figi of this RealtimeStockPriceSecurity.  # noqa: E501

        The OpenFIGI identifier  # noqa: E501

        :return: The figi of this RealtimeStockPriceSecurity.  # noqa: E501
        :rtype: str
        """
        return self._figi
        
    @property
    def figi_dict(self):
        """Gets the figi of this RealtimeStockPriceSecurity.  # noqa: E501

        The OpenFIGI identifier as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The figi of this RealtimeStockPriceSecurity.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.figi
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
            result = { 'figi': value }

        
        return result
        

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this RealtimeStockPriceSecurity.

        The OpenFIGI identifier  # noqa: E501

        :param figi: The figi of this RealtimeStockPriceSecurity.  # noqa: E501
        :type: str
        """

        self._figi = figi

    @property
    def composite_figi(self):
        """Gets the composite_figi of this RealtimeStockPriceSecurity.  # noqa: E501

        The country-composite OpenFIGI identifier  # noqa: E501

        :return: The composite_figi of this RealtimeStockPriceSecurity.  # noqa: E501
        :rtype: str
        """
        return self._composite_figi
        
    @property
    def composite_figi_dict(self):
        """Gets the composite_figi of this RealtimeStockPriceSecurity.  # noqa: E501

        The country-composite OpenFIGI identifier as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The composite_figi of this RealtimeStockPriceSecurity.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.composite_figi
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
            result = { 'composite_figi': value }

        
        return result
        

    @composite_figi.setter
    def composite_figi(self, composite_figi):
        """Sets the composite_figi of this RealtimeStockPriceSecurity.

        The country-composite OpenFIGI identifier  # noqa: E501

        :param composite_figi: The composite_figi of this RealtimeStockPriceSecurity.  # noqa: E501
        :type: str
        """

        self._composite_figi = composite_figi

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
        if not isinstance(other, RealtimeStockPriceSecurity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
