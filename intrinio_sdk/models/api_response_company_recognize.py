# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.52.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501


class ApiResponseCompanyRecognize(object):
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
        'companies': 'list[CompanySummary]'
    }

    attribute_map = {
        'companies': 'companies'
    }

    def __init__(self, companies=None):  # noqa: E501
        """ApiResponseCompanyRecognize - a model defined in Swagger"""  # noqa: E501

        self._companies = None
        self.discriminator = None

        if companies is not None:
            self.companies = companies

    @property
    def companies(self):
        """Gets the companies of this ApiResponseCompanyRecognize.  # noqa: E501


        :return: The companies of this ApiResponseCompanyRecognize.  # noqa: E501
        :rtype: list[CompanySummary]
        """
        return self._companies
        
    @property
    def companies_dict(self):
        """Gets the companies of this ApiResponseCompanyRecognize.  # noqa: E501


        :return: The companies of this ApiResponseCompanyRecognize.  # noqa: E501
        :rtype: list[CompanySummary]
        """

        result = None

        value = self.companies
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
            result = { 'companies': value }

        
        return result
        

    @companies.setter
    def companies(self, companies):
        """Sets the companies of this ApiResponseCompanyRecognize.


        :param companies: The companies of this ApiResponseCompanyRecognize.  # noqa: E501
        :type: list[CompanySummary]
        """

        self._companies = companies

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
        if not isinstance(other, ApiResponseCompanyRecognize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
