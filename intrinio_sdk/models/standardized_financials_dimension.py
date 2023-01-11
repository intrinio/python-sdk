# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.34.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StandardizedFinancialsDimension(object):
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
        'dimension': 'str',
        'value': 'str'
    }

    attribute_map = {
        'dimension': 'dimension',
        'value': 'value'
    }

    def __init__(self, dimension=None, value=None):  # noqa: E501
        """StandardizedFinancialsDimension - a model defined in Swagger"""  # noqa: E501

        self._dimension = None
        self._value = None
        self.discriminator = None

        if dimension is not None:
            self.dimension = dimension
        if value is not None:
            self.value = value

    @property
    def dimension(self):
        """Gets the dimension of this StandardizedFinancialsDimension.  # noqa: E501

        The title of the dimension  # noqa: E501

        :return: The dimension of this StandardizedFinancialsDimension.  # noqa: E501
        :rtype: str
        """
        return self._dimension
        
    @property
    def dimension_dict(self):
        """Gets the dimension of this StandardizedFinancialsDimension.  # noqa: E501

        The title of the dimension as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The dimension of this StandardizedFinancialsDimension.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.dimension
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
            result = { 'dimension': value }

        
        return result
        

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this StandardizedFinancialsDimension.

        The title of the dimension  # noqa: E501

        :param dimension: The dimension of this StandardizedFinancialsDimension.  # noqa: E501
        :type: str
        """

        self._dimension = dimension

    @property
    def value(self):
        """Gets the value of this StandardizedFinancialsDimension.  # noqa: E501

        The value of the dimension  # noqa: E501

        :return: The value of this StandardizedFinancialsDimension.  # noqa: E501
        :rtype: str
        """
        return self._value
        
    @property
    def value_dict(self):
        """Gets the value of this StandardizedFinancialsDimension.  # noqa: E501

        The value of the dimension as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The value of this StandardizedFinancialsDimension.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.value
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
            result = { 'value': value }

        
        return result
        

    @value.setter
    def value(self, value):
        """Sets the value of this StandardizedFinancialsDimension.

        The value of the dimension  # noqa: E501

        :param value: The value of this StandardizedFinancialsDimension.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, StandardizedFinancialsDimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
