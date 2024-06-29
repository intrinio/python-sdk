# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.62.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SecuritySummary(object):
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
        'company_id': 'str',
        'name': 'str',
        'code': 'str',
        'currency': 'str',
        'ticker': 'str',
        'composite_ticker': 'str',
        'figi': 'str',
        'composite_figi': 'str',
        'share_class_figi': 'str',
        'primary_listing': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'company_id': 'company_id',
        'name': 'name',
        'code': 'code',
        'currency': 'currency',
        'ticker': 'ticker',
        'composite_ticker': 'composite_ticker',
        'figi': 'figi',
        'composite_figi': 'composite_figi',
        'share_class_figi': 'share_class_figi',
        'primary_listing': 'primary_listing'
    }

    def __init__(self, id=None, company_id=None, name=None, code=None, currency=None, ticker=None, composite_ticker=None, figi=None, composite_figi=None, share_class_figi=None, primary_listing=None):  # noqa: E501
        """SecuritySummary - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._company_id = None
        self._name = None
        self._code = None
        self._currency = None
        self._ticker = None
        self._composite_ticker = None
        self._figi = None
        self._composite_figi = None
        self._share_class_figi = None
        self._primary_listing = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if company_id is not None:
            self.company_id = company_id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if currency is not None:
            self.currency = currency
        if ticker is not None:
            self.ticker = ticker
        if composite_ticker is not None:
            self.composite_ticker = composite_ticker
        if figi is not None:
            self.figi = figi
        if composite_figi is not None:
            self.composite_figi = composite_figi
        if share_class_figi is not None:
            self.share_class_figi = share_class_figi
        if primary_listing is not None:
            self.primary_listing = primary_listing

    @property
    def id(self):
        """Gets the id of this SecuritySummary.  # noqa: E501

        The Intrinio ID for Security  # noqa: E501

        :return: The id of this SecuritySummary.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this SecuritySummary.  # noqa: E501

        The Intrinio ID for Security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this SecuritySummary.  # noqa: E501
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
        """Sets the id of this SecuritySummary.

        The Intrinio ID for Security  # noqa: E501

        :param id: The id of this SecuritySummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def company_id(self):
        """Gets the company_id of this SecuritySummary.  # noqa: E501

        The Intrinio ID for the Company for which the Security is issued  # noqa: E501

        :return: The company_id of this SecuritySummary.  # noqa: E501
        :rtype: str
        """
        return self._company_id
        
    @property
    def company_id_dict(self):
        """Gets the company_id of this SecuritySummary.  # noqa: E501

        The Intrinio ID for the Company for which the Security is issued as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The company_id of this SecuritySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.company_id
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
            result = { 'company_id': value }

        
        return result
        

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this SecuritySummary.

        The Intrinio ID for the Company for which the Security is issued  # noqa: E501

        :param company_id: The company_id of this SecuritySummary.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def name(self):
        """Gets the name of this SecuritySummary.  # noqa: E501

        The name of the Security  # noqa: E501

        :return: The name of this SecuritySummary.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this SecuritySummary.  # noqa: E501

        The name of the Security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this SecuritySummary.  # noqa: E501
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
        """Sets the name of this SecuritySummary.

        The name of the Security  # noqa: E501

        :param name: The name of this SecuritySummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this SecuritySummary.  # noqa: E501

        A 2-3 digit code classifying the Security (<a href=\"https://docs.intrinio.com/documentation/security_codes\" target=\"_blank\">reference</a>)  # noqa: E501

        :return: The code of this SecuritySummary.  # noqa: E501
        :rtype: str
        """
        return self._code
        
    @property
    def code_dict(self):
        """Gets the code of this SecuritySummary.  # noqa: E501

        A 2-3 digit code classifying the Security (<a href=\"https://docs.intrinio.com/documentation/security_codes\" target=\"_blank\">reference</a>) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The code of this SecuritySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.code
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
            result = { 'code': value }

        
        return result
        

    @code.setter
    def code(self, code):
        """Sets the code of this SecuritySummary.

        A 2-3 digit code classifying the Security (<a href=\"https://docs.intrinio.com/documentation/security_codes\" target=\"_blank\">reference</a>)  # noqa: E501

        :param code: The code of this SecuritySummary.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def currency(self):
        """Gets the currency of this SecuritySummary.  # noqa: E501

        The currency in which the Security is traded on the exchange  # noqa: E501

        :return: The currency of this SecuritySummary.  # noqa: E501
        :rtype: str
        """
        return self._currency
        
    @property
    def currency_dict(self):
        """Gets the currency of this SecuritySummary.  # noqa: E501

        The currency in which the Security is traded on the exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The currency of this SecuritySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.currency
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
            result = { 'currency': value }

        
        return result
        

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SecuritySummary.

        The currency in which the Security is traded on the exchange  # noqa: E501

        :param currency: The currency of this SecuritySummary.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def ticker(self):
        """Gets the ticker of this SecuritySummary.  # noqa: E501

        The common/local ticker of the Security  # noqa: E501

        :return: The ticker of this SecuritySummary.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this SecuritySummary.  # noqa: E501

        The common/local ticker of the Security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this SecuritySummary.  # noqa: E501
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
        """Sets the ticker of this SecuritySummary.

        The common/local ticker of the Security  # noqa: E501

        :param ticker: The ticker of this SecuritySummary.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def composite_ticker(self):
        """Gets the composite_ticker of this SecuritySummary.  # noqa: E501

        The country-composite ticker of the Security  # noqa: E501

        :return: The composite_ticker of this SecuritySummary.  # noqa: E501
        :rtype: str
        """
        return self._composite_ticker
        
    @property
    def composite_ticker_dict(self):
        """Gets the composite_ticker of this SecuritySummary.  # noqa: E501

        The country-composite ticker of the Security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The composite_ticker of this SecuritySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.composite_ticker
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
            result = { 'composite_ticker': value }

        
        return result
        

    @composite_ticker.setter
    def composite_ticker(self, composite_ticker):
        """Sets the composite_ticker of this SecuritySummary.

        The country-composite ticker of the Security  # noqa: E501

        :param composite_ticker: The composite_ticker of this SecuritySummary.  # noqa: E501
        :type: str
        """

        self._composite_ticker = composite_ticker

    @property
    def figi(self):
        """Gets the figi of this SecuritySummary.  # noqa: E501

        The OpenFIGI identifier  # noqa: E501

        :return: The figi of this SecuritySummary.  # noqa: E501
        :rtype: str
        """
        return self._figi
        
    @property
    def figi_dict(self):
        """Gets the figi of this SecuritySummary.  # noqa: E501

        The OpenFIGI identifier as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The figi of this SecuritySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.figi
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
            result = { 'figi': value }

        
        return result
        

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this SecuritySummary.

        The OpenFIGI identifier  # noqa: E501

        :param figi: The figi of this SecuritySummary.  # noqa: E501
        :type: str
        """

        self._figi = figi

    @property
    def composite_figi(self):
        """Gets the composite_figi of this SecuritySummary.  # noqa: E501

        The country-composite OpenFIGI identifier  # noqa: E501

        :return: The composite_figi of this SecuritySummary.  # noqa: E501
        :rtype: str
        """
        return self._composite_figi
        
    @property
    def composite_figi_dict(self):
        """Gets the composite_figi of this SecuritySummary.  # noqa: E501

        The country-composite OpenFIGI identifier as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The composite_figi of this SecuritySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.composite_figi
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
            result = { 'composite_figi': value }

        
        return result
        

    @composite_figi.setter
    def composite_figi(self, composite_figi):
        """Sets the composite_figi of this SecuritySummary.

        The country-composite OpenFIGI identifier  # noqa: E501

        :param composite_figi: The composite_figi of this SecuritySummary.  # noqa: E501
        :type: str
        """

        self._composite_figi = composite_figi

    @property
    def share_class_figi(self):
        """Gets the share_class_figi of this SecuritySummary.  # noqa: E501

        The global-composite OpenFIGI identifier  # noqa: E501

        :return: The share_class_figi of this SecuritySummary.  # noqa: E501
        :rtype: str
        """
        return self._share_class_figi
        
    @property
    def share_class_figi_dict(self):
        """Gets the share_class_figi of this SecuritySummary.  # noqa: E501

        The global-composite OpenFIGI identifier as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The share_class_figi of this SecuritySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.share_class_figi
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
            result = { 'share_class_figi': value }

        
        return result
        

    @share_class_figi.setter
    def share_class_figi(self, share_class_figi):
        """Sets the share_class_figi of this SecuritySummary.

        The global-composite OpenFIGI identifier  # noqa: E501

        :param share_class_figi: The share_class_figi of this SecuritySummary.  # noqa: E501
        :type: str
        """

        self._share_class_figi = share_class_figi

    @property
    def primary_listing(self):
        """Gets the primary_listing of this SecuritySummary.  # noqa: E501

        If true, the Security is the primary issue for the company, otherwise it is a secondary issue on a secondary stock exchange  # noqa: E501

        :return: The primary_listing of this SecuritySummary.  # noqa: E501
        :rtype: bool
        """
        return self._primary_listing
        
    @property
    def primary_listing_dict(self):
        """Gets the primary_listing of this SecuritySummary.  # noqa: E501

        If true, the Security is the primary issue for the company, otherwise it is a secondary issue on a secondary stock exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The primary_listing of this SecuritySummary.  # noqa: E501
        :rtype: bool
        """

        result = None

        value = self.primary_listing
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
            result = { 'primary_listing': value }

        
        return result
        

    @primary_listing.setter
    def primary_listing(self, primary_listing):
        """Sets the primary_listing of this SecuritySummary.

        If true, the Security is the primary issue for the company, otherwise it is a secondary issue on a secondary stock exchange  # noqa: E501

        :param primary_listing: The primary_listing of this SecuritySummary.  # noqa: E501
        :type: bool
        """

        self._primary_listing = primary_listing

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
        if not isinstance(other, SecuritySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
