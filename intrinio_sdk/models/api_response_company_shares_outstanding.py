# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.42.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.company_shares_outstanding import CompanySharesOutstanding  # noqa: F401,E501
from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501


class ApiResponseCompanySharesOutstanding(object):
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
        'shares_outstanding': 'list[CompanySharesOutstanding]',
        'company': 'CompanySummary'
    }

    attribute_map = {
        'shares_outstanding': 'shares_outstanding',
        'company': 'company'
    }

    def __init__(self, shares_outstanding=None, company=None):  # noqa: E501
        """ApiResponseCompanySharesOutstanding - a model defined in Swagger"""  # noqa: E501

        self._shares_outstanding = None
        self._company = None
        self.discriminator = None

        if shares_outstanding is not None:
            self.shares_outstanding = shares_outstanding
        if company is not None:
            self.company = company

    @property
    def shares_outstanding(self):
        """Gets the shares_outstanding of this ApiResponseCompanySharesOutstanding.  # noqa: E501


        :return: The shares_outstanding of this ApiResponseCompanySharesOutstanding.  # noqa: E501
        :rtype: list[CompanySharesOutstanding]
        """
        return self._shares_outstanding
        
    @property
    def shares_outstanding_dict(self):
        """Gets the shares_outstanding of this ApiResponseCompanySharesOutstanding.  # noqa: E501


        :return: The shares_outstanding of this ApiResponseCompanySharesOutstanding.  # noqa: E501
        :rtype: list[CompanySharesOutstanding]
        """

        result = None

        value = self.shares_outstanding
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
            result = { 'shares_outstanding': value }

        
        return result
        

    @shares_outstanding.setter
    def shares_outstanding(self, shares_outstanding):
        """Sets the shares_outstanding of this ApiResponseCompanySharesOutstanding.


        :param shares_outstanding: The shares_outstanding of this ApiResponseCompanySharesOutstanding.  # noqa: E501
        :type: list[CompanySharesOutstanding]
        """

        self._shares_outstanding = shares_outstanding

    @property
    def company(self):
        """Gets the company of this ApiResponseCompanySharesOutstanding.  # noqa: E501


        :return: The company of this ApiResponseCompanySharesOutstanding.  # noqa: E501
        :rtype: CompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this ApiResponseCompanySharesOutstanding.  # noqa: E501


        :return: The company of this ApiResponseCompanySharesOutstanding.  # noqa: E501
        :rtype: CompanySummary
        """

        result = None

        value = self.company
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
            result = { 'company': value }

        
        return result
        

    @company.setter
    def company(self, company):
        """Sets the company of this ApiResponseCompanySharesOutstanding.


        :param company: The company of this ApiResponseCompanySharesOutstanding.  # noqa: E501
        :type: CompanySummary
        """

        self._company = company

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
        if not isinstance(other, ApiResponseCompanySharesOutstanding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
