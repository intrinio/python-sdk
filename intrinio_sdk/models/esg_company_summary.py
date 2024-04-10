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


class ESGCompanySummary(object):
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
        'id': 'str',
        'name': 'str',
        'ticker': 'str',
        'isin': 'str',
        'primary_industry': 'str',
        'country': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ticker': 'ticker',
        'isin': 'isin',
        'primary_industry': 'primary_industry',
        'country': 'country'
    }

    def __init__(self, id=None, name=None, ticker=None, isin=None, primary_industry=None, country=None):  # noqa: E501
        """ESGCompanySummary - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._ticker = None
        self._isin = None
        self._primary_industry = None
        self._country = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ticker is not None:
            self.ticker = ticker
        if isin is not None:
            self.isin = isin
        if primary_industry is not None:
            self.primary_industry = primary_industry
        if country is not None:
            self.country = country

    @property
    def id(self):
        """Gets the id of this ESGCompanySummary.  # noqa: E501

        The Intrinio ID of the company.  # noqa: E501

        :return: The id of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this ESGCompanySummary.  # noqa: E501

        The Intrinio ID of the company. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.id
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
            result = { 'id': value }

        
        return result
        

    @id.setter
    def id(self, id):
        """Sets the id of this ESGCompanySummary.

        The Intrinio ID of the company.  # noqa: E501

        :param id: The id of this ESGCompanySummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ESGCompanySummary.  # noqa: E501

        The company’s common name.  # noqa: E501

        :return: The name of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this ESGCompanySummary.  # noqa: E501

        The company’s common name. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.name
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
            result = { 'name': value }

        
        return result
        

    @name.setter
    def name(self, name):
        """Sets the name of this ESGCompanySummary.

        The company’s common name.  # noqa: E501

        :param name: The name of this ESGCompanySummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ticker(self):
        """Gets the ticker of this ESGCompanySummary.  # noqa: E501

        The stock market ticker symbol associated with the company’s common stock security.  # noqa: E501

        :return: The ticker of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this ESGCompanySummary.  # noqa: E501

        The stock market ticker symbol associated with the company’s common stock security. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.ticker
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
            result = { 'ticker': value }

        
        return result
        

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this ESGCompanySummary.

        The stock market ticker symbol associated with the company’s common stock security.  # noqa: E501

        :param ticker: The ticker of this ESGCompanySummary.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def isin(self):
        """Gets the isin of this ESGCompanySummary.  # noqa: E501

        The company's common securities identification 12-digit alphanumeric code.  # noqa: E501

        :return: The isin of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._isin
        
    @property
    def isin_dict(self):
        """Gets the isin of this ESGCompanySummary.  # noqa: E501

        The company's common securities identification 12-digit alphanumeric code. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The isin of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.isin
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
            result = { 'isin': value }

        
        return result
        

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this ESGCompanySummary.

        The company's common securities identification 12-digit alphanumeric code.  # noqa: E501

        :param isin: The isin of this ESGCompanySummary.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def primary_industry(self):
        """Gets the primary_industry of this ESGCompanySummary.  # noqa: E501

        The primary industry associated with the company based on their main revenue generating operations.  # noqa: E501

        :return: The primary_industry of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._primary_industry
        
    @property
    def primary_industry_dict(self):
        """Gets the primary_industry of this ESGCompanySummary.  # noqa: E501

        The primary industry associated with the company based on their main revenue generating operations. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The primary_industry of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.primary_industry
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
            result = { 'primary_industry': value }

        
        return result
        

    @primary_industry.setter
    def primary_industry(self, primary_industry):
        """Sets the primary_industry of this ESGCompanySummary.

        The primary industry associated with the company based on their main revenue generating operations.  # noqa: E501

        :param primary_industry: The primary_industry of this ESGCompanySummary.  # noqa: E501
        :type: str
        """

        self._primary_industry = primary_industry

    @property
    def country(self):
        """Gets the country of this ESGCompanySummary.  # noqa: E501

        The country in which the company's headquarters or primary place of business is located.  # noqa: E501

        :return: The country of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._country
        
    @property
    def country_dict(self):
        """Gets the country of this ESGCompanySummary.  # noqa: E501

        The country in which the company's headquarters or primary place of business is located. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The country of this ESGCompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.country
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
            result = { 'country': value }

        
        return result
        

    @country.setter
    def country(self, country):
        """Sets the country of this ESGCompanySummary.

        The country in which the company's headquarters or primary place of business is located.  # noqa: E501

        :param country: The country of this ESGCompanySummary.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if not isinstance(other, ESGCompanySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
