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


class OptionStatsRealtime(object):
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
        'implied_volatility': 'float',
        'delta': 'float',
        'gamma': 'float',
        'theta': 'float',
        'vega': 'float',
        'underlying_price': 'float'
    }

    attribute_map = {
        'implied_volatility': 'implied_volatility',
        'delta': 'delta',
        'gamma': 'gamma',
        'theta': 'theta',
        'vega': 'vega',
        'underlying_price': 'underlying_price'
    }

    def __init__(self, implied_volatility=None, delta=None, gamma=None, theta=None, vega=None, underlying_price=None):  # noqa: E501
        """OptionStatsRealtime - a model defined in Swagger"""  # noqa: E501

        self._implied_volatility = None
        self._delta = None
        self._gamma = None
        self._theta = None
        self._vega = None
        self._underlying_price = None
        self.discriminator = None

        if implied_volatility is not None:
            self.implied_volatility = implied_volatility
        if delta is not None:
            self.delta = delta
        if gamma is not None:
            self.gamma = gamma
        if theta is not None:
            self.theta = theta
        if vega is not None:
            self.vega = vega
        if underlying_price is not None:
            self.underlying_price = underlying_price

    @property
    def implied_volatility(self):
        """Gets the implied_volatility of this OptionStatsRealtime.  # noqa: E501

        The implied volatility of the contract calculated using the Black-Scholes Model.  # noqa: E501

        :return: The implied_volatility of this OptionStatsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._implied_volatility
        
    @property
    def implied_volatility_dict(self):
        """Gets the implied_volatility of this OptionStatsRealtime.  # noqa: E501

        The implied volatility of the contract calculated using the Black-Scholes Model. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The implied_volatility of this OptionStatsRealtime.  # noqa: E501
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
        """Sets the implied_volatility of this OptionStatsRealtime.

        The implied volatility of the contract calculated using the Black-Scholes Model.  # noqa: E501

        :param implied_volatility: The implied_volatility of this OptionStatsRealtime.  # noqa: E501
        :type: float
        """

        self._implied_volatility = implied_volatility

    @property
    def delta(self):
        """Gets the delta of this OptionStatsRealtime.  # noqa: E501

        Delta represents the rate of change between the option's price and a $1 change in the underlying asset's price.  # noqa: E501

        :return: The delta of this OptionStatsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._delta
        
    @property
    def delta_dict(self):
        """Gets the delta of this OptionStatsRealtime.  # noqa: E501

        Delta represents the rate of change between the option's price and a $1 change in the underlying asset's price. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The delta of this OptionStatsRealtime.  # noqa: E501
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
        """Sets the delta of this OptionStatsRealtime.

        Delta represents the rate of change between the option's price and a $1 change in the underlying asset's price.  # noqa: E501

        :param delta: The delta of this OptionStatsRealtime.  # noqa: E501
        :type: float
        """

        self._delta = delta

    @property
    def gamma(self):
        """Gets the gamma of this OptionStatsRealtime.  # noqa: E501

        Gamma represents the rate of change between an option's delta and the underlying asset's price.  # noqa: E501

        :return: The gamma of this OptionStatsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._gamma
        
    @property
    def gamma_dict(self):
        """Gets the gamma of this OptionStatsRealtime.  # noqa: E501

        Gamma represents the rate of change between an option's delta and the underlying asset's price. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The gamma of this OptionStatsRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.gamma
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
            result = { 'gamma': value }

        
        return result
        

    @gamma.setter
    def gamma(self, gamma):
        """Sets the gamma of this OptionStatsRealtime.

        Gamma represents the rate of change between an option's delta and the underlying asset's price.  # noqa: E501

        :param gamma: The gamma of this OptionStatsRealtime.  # noqa: E501
        :type: float
        """

        self._gamma = gamma

    @property
    def theta(self):
        """Gets the theta of this OptionStatsRealtime.  # noqa: E501

        Theta represents the rate of change between the option price and time, or time sensitivity - sometimes known as an option's time decay.  # noqa: E501

        :return: The theta of this OptionStatsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._theta
        
    @property
    def theta_dict(self):
        """Gets the theta of this OptionStatsRealtime.  # noqa: E501

        Theta represents the rate of change between the option price and time, or time sensitivity - sometimes known as an option's time decay. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The theta of this OptionStatsRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.theta
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
            result = { 'theta': value }

        
        return result
        

    @theta.setter
    def theta(self, theta):
        """Sets the theta of this OptionStatsRealtime.

        Theta represents the rate of change between the option price and time, or time sensitivity - sometimes known as an option's time decay.  # noqa: E501

        :param theta: The theta of this OptionStatsRealtime.  # noqa: E501
        :type: float
        """

        self._theta = theta

    @property
    def vega(self):
        """Gets the vega of this OptionStatsRealtime.  # noqa: E501

        Vega represents the rate of change between an option's value and the underlying asset's implied volatility.  # noqa: E501

        :return: The vega of this OptionStatsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._vega
        
    @property
    def vega_dict(self):
        """Gets the vega of this OptionStatsRealtime.  # noqa: E501

        Vega represents the rate of change between an option's value and the underlying asset's implied volatility. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The vega of this OptionStatsRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.vega
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
            result = { 'vega': value }

        
        return result
        

    @vega.setter
    def vega(self, vega):
        """Sets the vega of this OptionStatsRealtime.

        Vega represents the rate of change between an option's value and the underlying asset's implied volatility.  # noqa: E501

        :param vega: The vega of this OptionStatsRealtime.  # noqa: E501
        :type: float
        """

        self._vega = vega

    @property
    def underlying_price(self):
        """Gets the underlying_price of this OptionStatsRealtime.  # noqa: E501

        The most recent trade price of the underlying asset.  # noqa: E501

        :return: The underlying_price of this OptionStatsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._underlying_price
        
    @property
    def underlying_price_dict(self):
        """Gets the underlying_price of this OptionStatsRealtime.  # noqa: E501

        The most recent trade price of the underlying asset. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The underlying_price of this OptionStatsRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.underlying_price
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
            result = { 'underlying_price': value }

        
        return result
        

    @underlying_price.setter
    def underlying_price(self, underlying_price):
        """Sets the underlying_price of this OptionStatsRealtime.

        The most recent trade price of the underlying asset.  # noqa: E501

        :param underlying_price: The underlying_price of this OptionStatsRealtime.  # noqa: E501
        :type: float
        """

        self._underlying_price = underlying_price

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
        if not isinstance(other, OptionStatsRealtime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
