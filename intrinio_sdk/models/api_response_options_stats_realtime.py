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

from intrinio_sdk.models.option_factors_realtime import OptionFactorsRealtime  # noqa: F401,E501
from intrinio_sdk.models.option_realtime import OptionRealtime  # noqa: F401,E501
from intrinio_sdk.models.option_stats_realtime import OptionStatsRealtime  # noqa: F401,E501


class ApiResponseOptionsStatsRealtime(object):
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
        'stats': 'OptionStatsRealtime',
        'factors': 'OptionFactorsRealtime',
        'option': 'OptionRealtime'
    }

    attribute_map = {
        'stats': 'stats',
        'factors': 'factors',
        'option': 'option'
    }

    def __init__(self, stats=None, factors=None, option=None):  # noqa: E501
        """ApiResponseOptionsStatsRealtime - a model defined in Swagger"""  # noqa: E501

        self._stats = None
        self._factors = None
        self._option = None
        self.discriminator = None

        if stats is not None:
            self.stats = stats
        if factors is not None:
            self.factors = factors
        if option is not None:
            self.option = option

    @property
    def stats(self):
        """Gets the stats of this ApiResponseOptionsStatsRealtime.  # noqa: E501


        :return: The stats of this ApiResponseOptionsStatsRealtime.  # noqa: E501
        :rtype: OptionStatsRealtime
        """
        return self._stats
        
    @property
    def stats_dict(self):
        """Gets the stats of this ApiResponseOptionsStatsRealtime.  # noqa: E501


        :return: The stats of this ApiResponseOptionsStatsRealtime.  # noqa: E501
        :rtype: OptionStatsRealtime
        """

        result = None

        value = self.stats
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
            result = { 'stats': value }

        
        return result
        

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this ApiResponseOptionsStatsRealtime.


        :param stats: The stats of this ApiResponseOptionsStatsRealtime.  # noqa: E501
        :type: OptionStatsRealtime
        """

        self._stats = stats

    @property
    def factors(self):
        """Gets the factors of this ApiResponseOptionsStatsRealtime.  # noqa: E501


        :return: The factors of this ApiResponseOptionsStatsRealtime.  # noqa: E501
        :rtype: OptionFactorsRealtime
        """
        return self._factors
        
    @property
    def factors_dict(self):
        """Gets the factors of this ApiResponseOptionsStatsRealtime.  # noqa: E501


        :return: The factors of this ApiResponseOptionsStatsRealtime.  # noqa: E501
        :rtype: OptionFactorsRealtime
        """

        result = None

        value = self.factors
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
            result = { 'factors': value }

        
        return result
        

    @factors.setter
    def factors(self, factors):
        """Sets the factors of this ApiResponseOptionsStatsRealtime.


        :param factors: The factors of this ApiResponseOptionsStatsRealtime.  # noqa: E501
        :type: OptionFactorsRealtime
        """

        self._factors = factors

    @property
    def option(self):
        """Gets the option of this ApiResponseOptionsStatsRealtime.  # noqa: E501


        :return: The option of this ApiResponseOptionsStatsRealtime.  # noqa: E501
        :rtype: OptionRealtime
        """
        return self._option
        
    @property
    def option_dict(self):
        """Gets the option of this ApiResponseOptionsStatsRealtime.  # noqa: E501


        :return: The option of this ApiResponseOptionsStatsRealtime.  # noqa: E501
        :rtype: OptionRealtime
        """

        result = None

        value = self.option
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
            result = { 'option': value }

        
        return result
        

    @option.setter
    def option(self, option):
        """Sets the option of this ApiResponseOptionsStatsRealtime.


        :param option: The option of this ApiResponseOptionsStatsRealtime.  # noqa: E501
        :type: OptionRealtime
        """

        self._option = option

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
        if not isinstance(other, ApiResponseOptionsStatsRealtime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
