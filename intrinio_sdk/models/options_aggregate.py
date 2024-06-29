# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.62.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OptionsAggregate(object):
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
        'ticker': 'str',
        'total_open_interest': 'float',
        'total_volume': 'float'
    }

    attribute_map = {
        'ticker': 'ticker',
        'total_open_interest': 'total_open_interest',
        'total_volume': 'total_volume'
    }

    def __init__(self, ticker=None, total_open_interest=None, total_volume=None):  # noqa: E501
        """OptionsAggregate - a model defined in Swagger"""  # noqa: E501

        self._ticker = None
        self._total_open_interest = None
        self._total_volume = None
        self.discriminator = None

        if ticker is not None:
            self.ticker = ticker
        if total_open_interest is not None:
            self.total_open_interest = total_open_interest
        if total_volume is not None:
            self.total_volume = total_volume

    @property
    def ticker(self):
        """Gets the ticker of this OptionsAggregate.  # noqa: E501

        The ticker symbol of the Security for the Option.  # noqa: E501

        :return: The ticker of this OptionsAggregate.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this OptionsAggregate.  # noqa: E501

        The ticker symbol of the Security for the Option. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this OptionsAggregate.  # noqa: E501
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
        """Sets the ticker of this OptionsAggregate.

        The ticker symbol of the Security for the Option.  # noqa: E501

        :param ticker: The ticker of this OptionsAggregate.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def total_open_interest(self):
        """Gets the total_open_interest of this OptionsAggregate.  # noqa: E501

        Total open interest for the ticker  # noqa: E501

        :return: The total_open_interest of this OptionsAggregate.  # noqa: E501
        :rtype: float
        """
        return self._total_open_interest
        
    @property
    def total_open_interest_dict(self):
        """Gets the total_open_interest of this OptionsAggregate.  # noqa: E501

        Total open interest for the ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_open_interest of this OptionsAggregate.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.total_open_interest
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
            result = { 'total_open_interest': value }

        
        return result
        

    @total_open_interest.setter
    def total_open_interest(self, total_open_interest):
        """Sets the total_open_interest of this OptionsAggregate.

        Total open interest for the ticker  # noqa: E501

        :param total_open_interest: The total_open_interest of this OptionsAggregate.  # noqa: E501
        :type: float
        """

        self._total_open_interest = total_open_interest

    @property
    def total_volume(self):
        """Gets the total_volume of this OptionsAggregate.  # noqa: E501

        Total volume for the ticker  # noqa: E501

        :return: The total_volume of this OptionsAggregate.  # noqa: E501
        :rtype: float
        """
        return self._total_volume
        
    @property
    def total_volume_dict(self):
        """Gets the total_volume of this OptionsAggregate.  # noqa: E501

        Total volume for the ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_volume of this OptionsAggregate.  # noqa: E501
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
        """Sets the total_volume of this OptionsAggregate.

        Total volume for the ticker  # noqa: E501

        :param total_volume: The total_volume of this OptionsAggregate.  # noqa: E501
        :type: float
        """

        self._total_volume = total_volume

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
        if not isinstance(other, OptionsAggregate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
