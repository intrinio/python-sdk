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

from intrinio_sdk.models.fundamental import Fundamental  # noqa: F401,E501
from intrinio_sdk.models.standardized_financial import StandardizedFinancial  # noqa: F401,E501


class ApiResponseStandardizedFinancials(object):
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
        'standardized_financials': 'list[StandardizedFinancial]',
        'fundamental': 'Fundamental',
        'next_page': 'str'
    }

    attribute_map = {
        'standardized_financials': 'standardized_financials',
        'fundamental': 'fundamental',
        'next_page': 'next_page'
    }

    def __init__(self, standardized_financials=None, fundamental=None, next_page=None):  # noqa: E501
        """ApiResponseStandardizedFinancials - a model defined in Swagger"""  # noqa: E501

        self._standardized_financials = None
        self._fundamental = None
        self._next_page = None
        self.discriminator = None

        if standardized_financials is not None:
            self.standardized_financials = standardized_financials
        if fundamental is not None:
            self.fundamental = fundamental
        if next_page is not None:
            self.next_page = next_page

    @property
    def standardized_financials(self):
        """Gets the standardized_financials of this ApiResponseStandardizedFinancials.  # noqa: E501


        :return: The standardized_financials of this ApiResponseStandardizedFinancials.  # noqa: E501
        :rtype: list[StandardizedFinancial]
        """
        return self._standardized_financials
        
    @property
    def standardized_financials_dict(self):
        """Gets the standardized_financials of this ApiResponseStandardizedFinancials.  # noqa: E501


        :return: The standardized_financials of this ApiResponseStandardizedFinancials.  # noqa: E501
        :rtype: list[StandardizedFinancial]
        """

        result = None

        value = self.standardized_financials
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
            result = { 'standardized_financials': value }

        
        return result
        

    @standardized_financials.setter
    def standardized_financials(self, standardized_financials):
        """Sets the standardized_financials of this ApiResponseStandardizedFinancials.


        :param standardized_financials: The standardized_financials of this ApiResponseStandardizedFinancials.  # noqa: E501
        :type: list[StandardizedFinancial]
        """

        self._standardized_financials = standardized_financials

    @property
    def fundamental(self):
        """Gets the fundamental of this ApiResponseStandardizedFinancials.  # noqa: E501


        :return: The fundamental of this ApiResponseStandardizedFinancials.  # noqa: E501
        :rtype: Fundamental
        """
        return self._fundamental
        
    @property
    def fundamental_dict(self):
        """Gets the fundamental of this ApiResponseStandardizedFinancials.  # noqa: E501


        :return: The fundamental of this ApiResponseStandardizedFinancials.  # noqa: E501
        :rtype: Fundamental
        """

        result = None

        value = self.fundamental
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
            result = { 'fundamental': value }

        
        return result
        

    @fundamental.setter
    def fundamental(self, fundamental):
        """Sets the fundamental of this ApiResponseStandardizedFinancials.


        :param fundamental: The fundamental of this ApiResponseStandardizedFinancials.  # noqa: E501
        :type: Fundamental
        """

        self._fundamental = fundamental

    @property
    def next_page(self):
        """Gets the next_page of this ApiResponseStandardizedFinancials.  # noqa: E501

        The token required to request the next page of the data. If null, no further results are available.  # noqa: E501

        :return: The next_page of this ApiResponseStandardizedFinancials.  # noqa: E501
        :rtype: str
        """
        return self._next_page
        
    @property
    def next_page_dict(self):
        """Gets the next_page of this ApiResponseStandardizedFinancials.  # noqa: E501

        The token required to request the next page of the data. If null, no further results are available. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The next_page of this ApiResponseStandardizedFinancials.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.next_page
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
            result = { 'next_page': value }

        
        return result
        

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ApiResponseStandardizedFinancials.

        The token required to request the next page of the data. If null, no further results are available.  # noqa: E501

        :param next_page: The next_page of this ApiResponseStandardizedFinancials.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

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
        if not isinstance(other, ApiResponseStandardizedFinancials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
