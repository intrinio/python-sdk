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


class OptionRealtime(object):
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
        'code': 'str',
        'ticker': 'str',
        'expiration': 'date',
        'strike': 'float',
        'type': 'str'
    }

    attribute_map = {
        'code': 'code',
        'ticker': 'ticker',
        'expiration': 'expiration',
        'strike': 'strike',
        'type': 'type'
    }

    def __init__(self, code=None, ticker=None, expiration=None, strike=None, type=None):  # noqa: E501
        """OptionRealtime - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._ticker = None
        self._expiration = None
        self._strike = None
        self._type = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if ticker is not None:
            self.ticker = ticker
        if expiration is not None:
            self.expiration = expiration
        if strike is not None:
            self.strike = strike
        if type is not None:
            self.type = type

    @property
    def code(self):
        """Gets the code of this OptionRealtime.  # noqa: E501

        The Intrinio Code for the Option.  # noqa: E501

        :return: The code of this OptionRealtime.  # noqa: E501
        :rtype: str
        """
        return self._code
        
    @property
    def code_dict(self):
        """Gets the code of this OptionRealtime.  # noqa: E501

        The Intrinio Code for the Option. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The code of this OptionRealtime.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.code
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
            result = { 'code': value }

        
        return result
        

    @code.setter
    def code(self, code):
        """Sets the code of this OptionRealtime.

        The Intrinio Code for the Option.  # noqa: E501

        :param code: The code of this OptionRealtime.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def ticker(self):
        """Gets the ticker of this OptionRealtime.  # noqa: E501

        The ticker symbol of the Security for the Option.  # noqa: E501

        :return: The ticker of this OptionRealtime.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this OptionRealtime.  # noqa: E501

        The ticker symbol of the Security for the Option. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this OptionRealtime.  # noqa: E501
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
        """Sets the ticker of this OptionRealtime.

        The ticker symbol of the Security for the Option.  # noqa: E501

        :param ticker: The ticker of this OptionRealtime.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def expiration(self):
        """Gets the expiration of this OptionRealtime.  # noqa: E501

        The date on which the Option expires. The Option becomes invalid after this date and cannot be exercised.  # noqa: E501

        :return: The expiration of this OptionRealtime.  # noqa: E501
        :rtype: date
        """
        return self._expiration
        
    @property
    def expiration_dict(self):
        """Gets the expiration of this OptionRealtime.  # noqa: E501

        The date on which the Option expires. The Option becomes invalid after this date and cannot be exercised. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The expiration of this OptionRealtime.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.expiration
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
            result = { 'expiration': value }

        
        return result
        

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this OptionRealtime.

        The date on which the Option expires. The Option becomes invalid after this date and cannot be exercised.  # noqa: E501

        :param expiration: The expiration of this OptionRealtime.  # noqa: E501
        :type: date
        """

        self._expiration = expiration

    @property
    def strike(self):
        """Gets the strike of this OptionRealtime.  # noqa: E501

        The strike price is the fixed price at which a derivative can be exercised, and refers to the price of the derivative’s underlying asset.  In a call option, the strike price is the price at which the option holder can purchase the underlying security.  For a put option, the strike price is the price at which the option holder can sell the underlying security.  # noqa: E501

        :return: The strike of this OptionRealtime.  # noqa: E501
        :rtype: float
        """
        return self._strike
        
    @property
    def strike_dict(self):
        """Gets the strike of this OptionRealtime.  # noqa: E501

        The strike price is the fixed price at which a derivative can be exercised, and refers to the price of the derivative’s underlying asset.  In a call option, the strike price is the price at which the option holder can purchase the underlying security.  For a put option, the strike price is the price at which the option holder can sell the underlying security. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The strike of this OptionRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.strike
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
            result = { 'strike': value }

        
        return result
        

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this OptionRealtime.

        The strike price is the fixed price at which a derivative can be exercised, and refers to the price of the derivative’s underlying asset.  In a call option, the strike price is the price at which the option holder can purchase the underlying security.  For a put option, the strike price is the price at which the option holder can sell the underlying security.  # noqa: E501

        :param strike: The strike of this OptionRealtime.  # noqa: E501
        :type: float
        """

        self._strike = strike

    @property
    def type(self):
        """Gets the type of this OptionRealtime.  # noqa: E501

        The type of Option (put or call).  # noqa: E501

        :return: The type of this OptionRealtime.  # noqa: E501
        :rtype: str
        """
        return self._type
        
    @property
    def type_dict(self):
        """Gets the type of this OptionRealtime.  # noqa: E501

        The type of Option (put or call). as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The type of this OptionRealtime.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.type
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
            result = { 'type': value }

        
        return result
        

    @type.setter
    def type(self, type):
        """Sets the type of this OptionRealtime.

        The type of Option (put or call).  # noqa: E501

        :param type: The type of this OptionRealtime.  # noqa: E501
        :type: str
        """
        allowed_values = ["put", "call"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, OptionRealtime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
