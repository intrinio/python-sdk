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

from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501
from intrinio_sdk.models.insider_transaction import InsiderTransaction  # noqa: F401,E501
from intrinio_sdk.models.owner_summary import OwnerSummary  # noqa: F401,E501


class InsiderTransactionFiling(object):
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
        'filing_url': 'str',
        'issuer_ticker': 'str',
        'issuer_cik': 'str',
        'issuer_company': 'str',
        'transactions': 'list[InsiderTransaction]',
        'company': 'CompanySummary',
        'owner': 'OwnerSummary'
    }

    attribute_map = {
        'filing_url': 'filing_url',
        'issuer_ticker': 'issuer_ticker',
        'issuer_cik': 'issuer_cik',
        'issuer_company': 'issuer_company',
        'transactions': 'transactions',
        'company': 'company',
        'owner': 'owner'
    }

    def __init__(self, filing_url=None, issuer_ticker=None, issuer_cik=None, issuer_company=None, transactions=None, company=None, owner=None):  # noqa: E501
        """InsiderTransactionFiling - a model defined in Swagger"""  # noqa: E501

        self._filing_url = None
        self._issuer_ticker = None
        self._issuer_cik = None
        self._issuer_company = None
        self._transactions = None
        self._company = None
        self._owner = None
        self.discriminator = None

        if filing_url is not None:
            self.filing_url = filing_url
        if issuer_ticker is not None:
            self.issuer_ticker = issuer_ticker
        if issuer_cik is not None:
            self.issuer_cik = issuer_cik
        if issuer_company is not None:
            self.issuer_company = issuer_company
        if transactions is not None:
            self.transactions = transactions
        if company is not None:
            self.company = company
        if owner is not None:
            self.owner = owner

    @property
    def filing_url(self):
        """Gets the filing_url of this InsiderTransactionFiling.  # noqa: E501

        The URL of the filing with the SEC  # noqa: E501

        :return: The filing_url of this InsiderTransactionFiling.  # noqa: E501
        :rtype: str
        """
        return self._filing_url
        
    @property
    def filing_url_dict(self):
        """Gets the filing_url of this InsiderTransactionFiling.  # noqa: E501

        The URL of the filing with the SEC as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The filing_url of this InsiderTransactionFiling.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.filing_url
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
            result = { 'filing_url': value }

        
        return result
        

    @filing_url.setter
    def filing_url(self, filing_url):
        """Sets the filing_url of this InsiderTransactionFiling.

        The URL of the filing with the SEC  # noqa: E501

        :param filing_url: The filing_url of this InsiderTransactionFiling.  # noqa: E501
        :type: str
        """

        self._filing_url = filing_url

    @property
    def issuer_ticker(self):
        """Gets the issuer_ticker of this InsiderTransactionFiling.  # noqa: E501

        The ticker of the issuing company.  # noqa: E501

        :return: The issuer_ticker of this InsiderTransactionFiling.  # noqa: E501
        :rtype: str
        """
        return self._issuer_ticker
        
    @property
    def issuer_ticker_dict(self):
        """Gets the issuer_ticker of this InsiderTransactionFiling.  # noqa: E501

        The ticker of the issuing company. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The issuer_ticker of this InsiderTransactionFiling.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.issuer_ticker
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
            result = { 'issuer_ticker': value }

        
        return result
        

    @issuer_ticker.setter
    def issuer_ticker(self, issuer_ticker):
        """Sets the issuer_ticker of this InsiderTransactionFiling.

        The ticker of the issuing company.  # noqa: E501

        :param issuer_ticker: The issuer_ticker of this InsiderTransactionFiling.  # noqa: E501
        :type: str
        """

        self._issuer_ticker = issuer_ticker

    @property
    def issuer_cik(self):
        """Gets the issuer_cik of this InsiderTransactionFiling.  # noqa: E501

        The Central Index Key (CIK) of the issuing company.  # noqa: E501

        :return: The issuer_cik of this InsiderTransactionFiling.  # noqa: E501
        :rtype: str
        """
        return self._issuer_cik
        
    @property
    def issuer_cik_dict(self):
        """Gets the issuer_cik of this InsiderTransactionFiling.  # noqa: E501

        The Central Index Key (CIK) of the issuing company. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The issuer_cik of this InsiderTransactionFiling.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.issuer_cik
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
            result = { 'issuer_cik': value }

        
        return result
        

    @issuer_cik.setter
    def issuer_cik(self, issuer_cik):
        """Sets the issuer_cik of this InsiderTransactionFiling.

        The Central Index Key (CIK) of the issuing company.  # noqa: E501

        :param issuer_cik: The issuer_cik of this InsiderTransactionFiling.  # noqa: E501
        :type: str
        """

        self._issuer_cik = issuer_cik

    @property
    def issuer_company(self):
        """Gets the issuer_company of this InsiderTransactionFiling.  # noqa: E501

        The name of the issuing company.  # noqa: E501

        :return: The issuer_company of this InsiderTransactionFiling.  # noqa: E501
        :rtype: str
        """
        return self._issuer_company
        
    @property
    def issuer_company_dict(self):
        """Gets the issuer_company of this InsiderTransactionFiling.  # noqa: E501

        The name of the issuing company. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The issuer_company of this InsiderTransactionFiling.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.issuer_company
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
            result = { 'issuer_company': value }

        
        return result
        

    @issuer_company.setter
    def issuer_company(self, issuer_company):
        """Sets the issuer_company of this InsiderTransactionFiling.

        The name of the issuing company.  # noqa: E501

        :param issuer_company: The issuer_company of this InsiderTransactionFiling.  # noqa: E501
        :type: str
        """

        self._issuer_company = issuer_company

    @property
    def transactions(self):
        """Gets the transactions of this InsiderTransactionFiling.  # noqa: E501

        The insider transactions associated with the filing  # noqa: E501

        :return: The transactions of this InsiderTransactionFiling.  # noqa: E501
        :rtype: list[InsiderTransaction]
        """
        return self._transactions
        
    @property
    def transactions_dict(self):
        """Gets the transactions of this InsiderTransactionFiling.  # noqa: E501

        The insider transactions associated with the filing as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The transactions of this InsiderTransactionFiling.  # noqa: E501
        :rtype: list[InsiderTransaction]
        """

        result = None

        value = self.transactions
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
            result = { 'transactions': value }

        
        return result
        

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this InsiderTransactionFiling.

        The insider transactions associated with the filing  # noqa: E501

        :param transactions: The transactions of this InsiderTransactionFiling.  # noqa: E501
        :type: list[InsiderTransaction]
        """

        self._transactions = transactions

    @property
    def company(self):
        """Gets the company of this InsiderTransactionFiling.  # noqa: E501

        The company associated with the filing  # noqa: E501

        :return: The company of this InsiderTransactionFiling.  # noqa: E501
        :rtype: CompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this InsiderTransactionFiling.  # noqa: E501

        The company associated with the filing as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The company of this InsiderTransactionFiling.  # noqa: E501
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
        """Sets the company of this InsiderTransactionFiling.

        The company associated with the filing  # noqa: E501

        :param company: The company of this InsiderTransactionFiling.  # noqa: E501
        :type: CompanySummary
        """

        self._company = company

    @property
    def owner(self):
        """Gets the owner of this InsiderTransactionFiling.  # noqa: E501

        The owner associated with the filing  # noqa: E501

        :return: The owner of this InsiderTransactionFiling.  # noqa: E501
        :rtype: OwnerSummary
        """
        return self._owner
        
    @property
    def owner_dict(self):
        """Gets the owner of this InsiderTransactionFiling.  # noqa: E501

        The owner associated with the filing as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The owner of this InsiderTransactionFiling.  # noqa: E501
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
        """Sets the owner of this InsiderTransactionFiling.

        The owner associated with the filing  # noqa: E501

        :param owner: The owner of this InsiderTransactionFiling.  # noqa: E501
        :type: OwnerSummary
        """

        self._owner = owner

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
        if not isinstance(other, InsiderTransactionFiling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
