# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.28.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ForexCurrency(object):
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
        'name': 'str',
        'country': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'country': 'country'
    }

    def __init__(self, code=None, name=None, country=None):  # noqa: E501
        """ForexCurrency - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._name = None
        self._country = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if country is not None:
            self.country = country

    @property
    def code(self):
        """Gets the code of this ForexCurrency.  # noqa: E501

        The ISO 4217 currency code  # noqa: E501

        :return: The code of this ForexCurrency.  # noqa: E501
        :rtype: str
        """
        return self._code
        
    @property
    def code_dict(self):
        """Gets the code of this ForexCurrency.  # noqa: E501

        The ISO 4217 currency code as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The code of this ForexCurrency.  # noqa: E501
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
        """Sets the code of this ForexCurrency.

        The ISO 4217 currency code  # noqa: E501

        :param code: The code of this ForexCurrency.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this ForexCurrency.  # noqa: E501

        The name of the currency  # noqa: E501

        :return: The name of this ForexCurrency.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this ForexCurrency.  # noqa: E501

        The name of the currency as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this ForexCurrency.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.name
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
            result = { 'name': value }

        
        return result
        

    @name.setter
    def name(self, name):
        """Sets the name of this ForexCurrency.

        The name of the currency  # noqa: E501

        :param name: The name of this ForexCurrency.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def country(self):
        """Gets the country of this ForexCurrency.  # noqa: E501

        The country in which the currency is used  # noqa: E501

        :return: The country of this ForexCurrency.  # noqa: E501
        :rtype: str
        """
        return self._country
        
    @property
    def country_dict(self):
        """Gets the country of this ForexCurrency.  # noqa: E501

        The country in which the currency is used as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The country of this ForexCurrency.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.country
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
            result = { 'country': value }

        
        return result
        

    @country.setter
    def country(self, country):
        """Sets the country of this ForexCurrency.

        The country in which the currency is used  # noqa: E501

        :param country: The country of this ForexCurrency.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if not isinstance(other, ForexCurrency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
