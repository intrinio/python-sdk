# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.52.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MarketStatusResult(object):
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
        'timestamp': 'datetime',
        'is_open': 'bool'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'is_open': 'is_open'
    }

    def __init__(self, timestamp=None, is_open=None):  # noqa: E501
        """MarketStatusResult - a model defined in Swagger"""  # noqa: E501

        self._timestamp = None
        self._is_open = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if is_open is not None:
            self.is_open = is_open

    @property
    def timestamp(self):
        """Gets the timestamp of this MarketStatusResult.  # noqa: E501

        The UTC timestamp.  # noqa: E501

        :return: The timestamp of this MarketStatusResult.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp
        
    @property
    def timestamp_dict(self):
        """Gets the timestamp of this MarketStatusResult.  # noqa: E501

        The UTC timestamp. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The timestamp of this MarketStatusResult.  # noqa: E501
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
        """Sets the timestamp of this MarketStatusResult.

        The UTC timestamp.  # noqa: E501

        :param timestamp: The timestamp of this MarketStatusResult.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def is_open(self):
        """Gets the is_open of this MarketStatusResult.  # noqa: E501

        Whether the market is open or not.  # noqa: E501

        :return: The is_open of this MarketStatusResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_open
        
    @property
    def is_open_dict(self):
        """Gets the is_open of this MarketStatusResult.  # noqa: E501

        Whether the market is open or not. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The is_open of this MarketStatusResult.  # noqa: E501
        :rtype: bool
        """

        result = None

        value = self.is_open
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
            result = { 'is_open': value }

        
        return result
        

    @is_open.setter
    def is_open(self, is_open):
        """Sets the is_open of this MarketStatusResult.

        Whether the market is open or not.  # noqa: E501

        :param is_open: The is_open of this MarketStatusResult.  # noqa: E501
        :type: bool
        """

        self._is_open = is_open

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
        if not isinstance(other, MarketStatusResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
