# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.56.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ZacksInstitutionalHoldingHistoricalSummary(object):
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
        'as_of_date': 'date',
        'shares_held': 'float'
    }

    attribute_map = {
        'as_of_date': 'as_of_date',
        'shares_held': 'shares_held'
    }

    def __init__(self, as_of_date=None, shares_held=None):  # noqa: E501
        """ZacksInstitutionalHoldingHistoricalSummary - a model defined in Swagger"""  # noqa: E501

        self._as_of_date = None
        self._shares_held = None
        self.discriminator = None

        if as_of_date is not None:
            self.as_of_date = as_of_date
        if shares_held is not None:
            self.shares_held = shares_held

    @property
    def as_of_date(self):
        """Gets the as_of_date of this ZacksInstitutionalHoldingHistoricalSummary.  # noqa: E501

        The date of the institutional holding  # noqa: E501

        :return: The as_of_date of this ZacksInstitutionalHoldingHistoricalSummary.  # noqa: E501
        :rtype: date
        """
        return self._as_of_date
        
    @property
    def as_of_date_dict(self):
        """Gets the as_of_date of this ZacksInstitutionalHoldingHistoricalSummary.  # noqa: E501

        The date of the institutional holding as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The as_of_date of this ZacksInstitutionalHoldingHistoricalSummary.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.as_of_date
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
            result = { 'as_of_date': value }

        
        return result
        

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this ZacksInstitutionalHoldingHistoricalSummary.

        The date of the institutional holding  # noqa: E501

        :param as_of_date: The as_of_date of this ZacksInstitutionalHoldingHistoricalSummary.  # noqa: E501
        :type: date
        """

        self._as_of_date = as_of_date

    @property
    def shares_held(self):
        """Gets the shares_held of this ZacksInstitutionalHoldingHistoricalSummary.  # noqa: E501

        The number of shares held  # noqa: E501

        :return: The shares_held of this ZacksInstitutionalHoldingHistoricalSummary.  # noqa: E501
        :rtype: float
        """
        return self._shares_held
        
    @property
    def shares_held_dict(self):
        """Gets the shares_held of this ZacksInstitutionalHoldingHistoricalSummary.  # noqa: E501

        The number of shares held as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shares_held of this ZacksInstitutionalHoldingHistoricalSummary.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.shares_held
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
            result = { 'shares_held': value }

        
        return result
        

    @shares_held.setter
    def shares_held(self, shares_held):
        """Sets the shares_held of this ZacksInstitutionalHoldingHistoricalSummary.

        The number of shares held  # noqa: E501

        :param shares_held: The shares_held of this ZacksInstitutionalHoldingHistoricalSummary.  # noqa: E501
        :type: float
        """

        self._shares_held = shares_held

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
        if not isinstance(other, ZacksInstitutionalHoldingHistoricalSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
