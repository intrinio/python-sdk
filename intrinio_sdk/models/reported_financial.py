# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.26.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.reported_financial_dimension import ReportedFinancialDimension  # noqa: F401,E501
from intrinio_sdk.models.reported_tag import ReportedTag  # noqa: F401,E501


class ReportedFinancial(object):
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
        'xbrl_tag': 'ReportedTag',
        'value': 'float',
        'dimensions': 'list[ReportedFinancialDimension]'
    }

    attribute_map = {
        'xbrl_tag': 'xbrl_tag',
        'value': 'value',
        'dimensions': 'dimensions'
    }

    def __init__(self, xbrl_tag=None, value=None, dimensions=None):  # noqa: E501
        """ReportedFinancial - a model defined in Swagger"""  # noqa: E501

        self._xbrl_tag = None
        self._value = None
        self._dimensions = None
        self.discriminator = None

        if xbrl_tag is not None:
            self.xbrl_tag = xbrl_tag
        if value is not None:
            self.value = value
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def xbrl_tag(self):
        """Gets the xbrl_tag of this ReportedFinancial.  # noqa: E501


        :return: The xbrl_tag of this ReportedFinancial.  # noqa: E501
        :rtype: ReportedTag
        """
        return self._xbrl_tag
        
    @property
    def xbrl_tag_dict(self):
        """Gets the xbrl_tag of this ReportedFinancial.  # noqa: E501


        :return: The xbrl_tag of this ReportedFinancial.  # noqa: E501
        :rtype: ReportedTag
        """

        result = None

        value = self.xbrl_tag
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
            result = { 'xbrl_tag': value }

        
        return result
        

    @xbrl_tag.setter
    def xbrl_tag(self, xbrl_tag):
        """Sets the xbrl_tag of this ReportedFinancial.


        :param xbrl_tag: The xbrl_tag of this ReportedFinancial.  # noqa: E501
        :type: ReportedTag
        """

        self._xbrl_tag = xbrl_tag

    @property
    def value(self):
        """Gets the value of this ReportedFinancial.  # noqa: E501

        The value reported for the XBRL Tag within the scope of the Fundamental  # noqa: E501

        :return: The value of this ReportedFinancial.  # noqa: E501
        :rtype: float
        """
        return self._value
        
    @property
    def value_dict(self):
        """Gets the value of this ReportedFinancial.  # noqa: E501

        The value reported for the XBRL Tag within the scope of the Fundamental as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The value of this ReportedFinancial.  # noqa: E501
        :rtype: float
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
        """Sets the value of this ReportedFinancial.

        The value reported for the XBRL Tag within the scope of the Fundamental  # noqa: E501

        :param value: The value of this ReportedFinancial.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def dimensions(self):
        """Gets the dimensions of this ReportedFinancial.  # noqa: E501

        The combination of XBRL axis and members that defines the dimensionalization of this fact (if any)  # noqa: E501

        :return: The dimensions of this ReportedFinancial.  # noqa: E501
        :rtype: list[ReportedFinancialDimension]
        """
        return self._dimensions
        
    @property
    def dimensions_dict(self):
        """Gets the dimensions of this ReportedFinancial.  # noqa: E501

        The combination of XBRL axis and members that defines the dimensionalization of this fact (if any) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The dimensions of this ReportedFinancial.  # noqa: E501
        :rtype: list[ReportedFinancialDimension]
        """

        result = None

        value = self.dimensions
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
            result = { 'dimensions': value }

        
        return result
        

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ReportedFinancial.

        The combination of XBRL axis and members that defines the dimensionalization of this fact (if any)  # noqa: E501

        :param dimensions: The dimensions of this ReportedFinancial.  # noqa: E501
        :type: list[ReportedFinancialDimension]
        """

        self._dimensions = dimensions

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
        if not isinstance(other, ReportedFinancial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
