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

from intrinio_sdk.models.option_interval import OptionInterval  # noqa: F401,E501


class OptionIntervalsResult(object):
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
        'intervals': 'list[OptionInterval]',
        'contract': 'str',
        'size': 'str'
    }

    attribute_map = {
        'intervals': 'intervals',
        'contract': 'contract',
        'size': 'size'
    }

    def __init__(self, intervals=None, contract=None, size=None):  # noqa: E501
        """OptionIntervalsResult - a model defined in Swagger"""  # noqa: E501

        self._intervals = None
        self._contract = None
        self._size = None
        self.discriminator = None

        if intervals is not None:
            self.intervals = intervals
        if contract is not None:
            self.contract = contract
        if size is not None:
            self.size = size

    @property
    def intervals(self):
        """Gets the intervals of this OptionIntervalsResult.  # noqa: E501

        Array of all the intervals in the result.  # noqa: E501

        :return: The intervals of this OptionIntervalsResult.  # noqa: E501
        :rtype: list[OptionInterval]
        """
        return self._intervals
        
    @property
    def intervals_dict(self):
        """Gets the intervals of this OptionIntervalsResult.  # noqa: E501

        Array of all the intervals in the result. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The intervals of this OptionIntervalsResult.  # noqa: E501
        :rtype: list[OptionInterval]
        """

        result = None

        value = self.intervals
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
            result = { 'intervals': value }

        
        return result
        

    @intervals.setter
    def intervals(self, intervals):
        """Sets the intervals of this OptionIntervalsResult.

        Array of all the intervals in the result.  # noqa: E501

        :param intervals: The intervals of this OptionIntervalsResult.  # noqa: E501
        :type: list[OptionInterval]
        """

        self._intervals = intervals

    @property
    def contract(self):
        """Gets the contract of this OptionIntervalsResult.  # noqa: E501

        The option contract for the intervals  # noqa: E501

        :return: The contract of this OptionIntervalsResult.  # noqa: E501
        :rtype: str
        """
        return self._contract
        
    @property
    def contract_dict(self):
        """Gets the contract of this OptionIntervalsResult.  # noqa: E501

        The option contract for the intervals as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The contract of this OptionIntervalsResult.  # noqa: E501
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
        """Sets the contract of this OptionIntervalsResult.

        The option contract for the intervals  # noqa: E501

        :param contract: The contract of this OptionIntervalsResult.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def size(self):
        """Gets the size of this OptionIntervalsResult.  # noqa: E501

        The size of the time span for the interval.  # noqa: E501

        :return: The size of this OptionIntervalsResult.  # noqa: E501
        :rtype: str
        """
        return self._size
        
    @property
    def size_dict(self):
        """Gets the size of this OptionIntervalsResult.  # noqa: E501

        The size of the time span for the interval. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The size of this OptionIntervalsResult.  # noqa: E501
        :rtype: str
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
        """Sets the size of this OptionIntervalsResult.

        The size of the time span for the interval.  # noqa: E501

        :param size: The size of this OptionIntervalsResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["SixtyMinute", "ThirtyMinute", "FifteenMinute", "TenMinute", "FiveMinute", "OneMinute"]  # noqa: E501
        if size not in allowed_values:
            raise ValueError(
                "Invalid value for `size` ({0}), must be one of {1}"  # noqa: E501
                .format(size, allowed_values)
            )

        self._size = size

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
        if not isinstance(other, OptionIntervalsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other