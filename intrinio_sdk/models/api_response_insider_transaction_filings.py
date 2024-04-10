# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.56.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501
from intrinio_sdk.models.insider_transaction_filing import InsiderTransactionFiling  # noqa: F401,E501
from intrinio_sdk.models.owner_summary import OwnerSummary  # noqa: F401,E501


class ApiResponseInsiderTransactionFilings(object):
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
        'transaction_filings': 'list[InsiderTransactionFiling]',
        'owner': 'OwnerSummary',
        'company': 'CompanySummary',
        'next_page': 'str'
    }

    attribute_map = {
        'transaction_filings': 'transaction_filings',
        'owner': 'owner',
        'company': 'company',
        'next_page': 'next_page'
    }

    def __init__(self, transaction_filings=None, owner=None, company=None, next_page=None):  # noqa: E501
        """ApiResponseInsiderTransactionFilings - a model defined in Swagger"""  # noqa: E501

        self._transaction_filings = None
        self._owner = None
        self._company = None
        self._next_page = None
        self.discriminator = None

        if transaction_filings is not None:
            self.transaction_filings = transaction_filings
        if owner is not None:
            self.owner = owner
        if company is not None:
            self.company = company
        if next_page is not None:
            self.next_page = next_page

    @property
    def transaction_filings(self):
        """Gets the transaction_filings of this ApiResponseInsiderTransactionFilings.  # noqa: E501


        :return: The transaction_filings of this ApiResponseInsiderTransactionFilings.  # noqa: E501
        :rtype: list[InsiderTransactionFiling]
        """
        return self._transaction_filings
        
    @property
    def transaction_filings_dict(self):
        """Gets the transaction_filings of this ApiResponseInsiderTransactionFilings.  # noqa: E501


        :return: The transaction_filings of this ApiResponseInsiderTransactionFilings.  # noqa: E501
        :rtype: list[InsiderTransactionFiling]
        """

        result = None

        value = self.transaction_filings
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
            result = { 'transaction_filings': value }

        
        return result
        

    @transaction_filings.setter
    def transaction_filings(self, transaction_filings):
        """Sets the transaction_filings of this ApiResponseInsiderTransactionFilings.


        :param transaction_filings: The transaction_filings of this ApiResponseInsiderTransactionFilings.  # noqa: E501
        :type: list[InsiderTransactionFiling]
        """

        self._transaction_filings = transaction_filings

    @property
    def owner(self):
        """Gets the owner of this ApiResponseInsiderTransactionFilings.  # noqa: E501

        The owner associated with the transaction filing  # noqa: E501

        :return: The owner of this ApiResponseInsiderTransactionFilings.  # noqa: E501
        :rtype: OwnerSummary
        """
        return self._owner
        
    @property
    def owner_dict(self):
        """Gets the owner of this ApiResponseInsiderTransactionFilings.  # noqa: E501

        The owner associated with the transaction filing as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The owner of this ApiResponseInsiderTransactionFilings.  # noqa: E501
        :rtype: OwnerSummary
        """

        result = None

        value = self.owner
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
            result = { 'owner': value }

        
        return result
        

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ApiResponseInsiderTransactionFilings.

        The owner associated with the transaction filing  # noqa: E501

        :param owner: The owner of this ApiResponseInsiderTransactionFilings.  # noqa: E501
        :type: OwnerSummary
        """

        self._owner = owner

    @property
    def company(self):
        """Gets the company of this ApiResponseInsiderTransactionFilings.  # noqa: E501

        The company associated with the transaction filing  # noqa: E501

        :return: The company of this ApiResponseInsiderTransactionFilings.  # noqa: E501
        :rtype: CompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this ApiResponseInsiderTransactionFilings.  # noqa: E501

        The company associated with the transaction filing as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The company of this ApiResponseInsiderTransactionFilings.  # noqa: E501
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
        """Sets the company of this ApiResponseInsiderTransactionFilings.

        The company associated with the transaction filing  # noqa: E501

        :param company: The company of this ApiResponseInsiderTransactionFilings.  # noqa: E501
        :type: CompanySummary
        """

        self._company = company

    @property
    def next_page(self):
        """Gets the next_page of this ApiResponseInsiderTransactionFilings.  # noqa: E501

        The token required to request the next page of the data. If null, no further results are available.  # noqa: E501

        :return: The next_page of this ApiResponseInsiderTransactionFilings.  # noqa: E501
        :rtype: str
        """
        return self._next_page
        
    @property
    def next_page_dict(self):
        """Gets the next_page of this ApiResponseInsiderTransactionFilings.  # noqa: E501

        The token required to request the next page of the data. If null, no further results are available. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The next_page of this ApiResponseInsiderTransactionFilings.  # noqa: E501
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
        """Sets the next_page of this ApiResponseInsiderTransactionFilings.

        The token required to request the next page of the data. If null, no further results are available.  # noqa: E501

        :param next_page: The next_page of this ApiResponseInsiderTransactionFilings.  # noqa: E501
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
        if not isinstance(other, ApiResponseInsiderTransactionFilings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
