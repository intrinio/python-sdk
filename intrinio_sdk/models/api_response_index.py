# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.62.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiResponseIndex(object):
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
        'symbol': 'str',
        'name': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'name': 'name'
    }

    def __init__(self, symbol=None, name=None):  # noqa: E501
        """ApiResponseIndex - a model defined in Swagger"""  # noqa: E501

        self._symbol = None
        self._name = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if name is not None:
            self.name = name

    @property
    def symbol(self):
        """Gets the symbol of this ApiResponseIndex.  # noqa: E501

        The index symbol  # noqa: E501

        :return: The symbol of this ApiResponseIndex.  # noqa: E501
        :rtype: str
        """
        return self._symbol
        
    @property
    def symbol_dict(self):
        """Gets the symbol of this ApiResponseIndex.  # noqa: E501

        The index symbol as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The symbol of this ApiResponseIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.symbol
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
            result = { 'symbol': value }

        
        return result
        

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this ApiResponseIndex.

        The index symbol  # noqa: E501

        :param symbol: The symbol of this ApiResponseIndex.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def name(self):
        """Gets the name of this ApiResponseIndex.  # noqa: E501

        The index name  # noqa: E501

        :return: The name of this ApiResponseIndex.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this ApiResponseIndex.  # noqa: E501

        The index name as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this ApiResponseIndex.  # noqa: E501
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
        """Sets the name of this ApiResponseIndex.

        The index name  # noqa: E501

        :param name: The name of this ApiResponseIndex.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, ApiResponseIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other