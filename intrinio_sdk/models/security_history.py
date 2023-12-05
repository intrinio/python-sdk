# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.47.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SecurityHistory(object):
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
        'ticker': 'str',
        'name': 'str',
        'security_code': 'str',
        'figi': 'str',
        'composite_figi': 'str',
        'first_price_date': 'date',
        'last_price_date': 'date'
    }

    attribute_map = {
        'id': 'id',
        'ticker': 'ticker',
        'name': 'name',
        'security_code': 'security_code',
        'figi': 'figi',
        'composite_figi': 'composite_figi',
        'first_price_date': 'first_price_date',
        'last_price_date': 'last_price_date'
    }

    def __init__(self, id=None, ticker=None, name=None, security_code=None, figi=None, composite_figi=None, first_price_date=None, last_price_date=None):  # noqa: E501
        """SecurityHistory - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._ticker = None
        self._name = None
        self._security_code = None
        self._figi = None
        self._composite_figi = None
        self._first_price_date = None
        self._last_price_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ticker is not None:
            self.ticker = ticker
        if name is not None:
            self.name = name
        if security_code is not None:
            self.security_code = security_code
        if figi is not None:
            self.figi = figi
        if composite_figi is not None:
            self.composite_figi = composite_figi
        if first_price_date is not None:
            self.first_price_date = first_price_date
        if last_price_date is not None:
            self.last_price_date = last_price_date

    @property
    def id(self):
        """Gets the id of this SecurityHistory.  # noqa: E501

        The Intrinio ID for the Security  # noqa: E501

        :return: The id of this SecurityHistory.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this SecurityHistory.  # noqa: E501

        The Intrinio ID for the Security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this SecurityHistory.  # noqa: E501
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
        """Sets the id of this SecurityHistory.

        The Intrinio ID for the Security  # noqa: E501

        :param id: The id of this SecurityHistory.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ticker(self):
        """Gets the ticker of this SecurityHistory.  # noqa: E501

        The common ticker  # noqa: E501

        :return: The ticker of this SecurityHistory.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this SecurityHistory.  # noqa: E501

        The common ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this SecurityHistory.  # noqa: E501
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
        """Sets the ticker of this SecurityHistory.

        The common ticker  # noqa: E501

        :param ticker: The ticker of this SecurityHistory.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def name(self):
        """Gets the name of this SecurityHistory.  # noqa: E501

        The name of the Security  # noqa: E501

        :return: The name of this SecurityHistory.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this SecurityHistory.  # noqa: E501

        The name of the Security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this SecurityHistory.  # noqa: E501
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
        """Sets the name of this SecurityHistory.

        The name of the Security  # noqa: E501

        :param name: The name of this SecurityHistory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def security_code(self):
        """Gets the security_code of this SecurityHistory.  # noqa: E501

        A 2-3 digit code classifying the Security (<a href=\"https://docs.intrinio.com/documentation/security_codes\" target=\"_blank\">reference</a>)  # noqa: E501

        :return: The security_code of this SecurityHistory.  # noqa: E501
        :rtype: str
        """
        return self._security_code
        
    @property
    def security_code_dict(self):
        """Gets the security_code of this SecurityHistory.  # noqa: E501

        A 2-3 digit code classifying the Security (<a href=\"https://docs.intrinio.com/documentation/security_codes\" target=\"_blank\">reference</a>) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The security_code of this SecurityHistory.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.security_code
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
            result = { 'security_code': value }

        
        return result
        

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this SecurityHistory.

        A 2-3 digit code classifying the Security (<a href=\"https://docs.intrinio.com/documentation/security_codes\" target=\"_blank\">reference</a>)  # noqa: E501

        :param security_code: The security_code of this SecurityHistory.  # noqa: E501
        :type: str
        """

        self._security_code = security_code

    @property
    def figi(self):
        """Gets the figi of this SecurityHistory.  # noqa: E501

        The exchange-level OpenFIGI identifier  # noqa: E501

        :return: The figi of this SecurityHistory.  # noqa: E501
        :rtype: str
        """
        return self._figi
        
    @property
    def figi_dict(self):
        """Gets the figi of this SecurityHistory.  # noqa: E501

        The exchange-level OpenFIGI identifier as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The figi of this SecurityHistory.  # noqa: E501
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
        """Sets the figi of this SecurityHistory.

        The exchange-level OpenFIGI identifier  # noqa: E501

        :param figi: The figi of this SecurityHistory.  # noqa: E501
        :type: str
        """

        self._figi = figi

    @property
    def composite_figi(self):
        """Gets the composite_figi of this SecurityHistory.  # noqa: E501

        The country-composite OpenFIGI identifier  # noqa: E501

        :return: The composite_figi of this SecurityHistory.  # noqa: E501
        :rtype: str
        """
        return self._composite_figi
        
    @property
    def composite_figi_dict(self):
        """Gets the composite_figi of this SecurityHistory.  # noqa: E501

        The country-composite OpenFIGI identifier as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The composite_figi of this SecurityHistory.  # noqa: E501
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
        """Sets the composite_figi of this SecurityHistory.

        The country-composite OpenFIGI identifier  # noqa: E501

        :param composite_figi: The composite_figi of this SecurityHistory.  # noqa: E501
        :type: str
        """

        self._composite_figi = composite_figi

    @property
    def first_price_date(self):
        """Gets the first_price_date of this SecurityHistory.  # noqa: E501

        The date of the first recorded stock price  # noqa: E501

        :return: The first_price_date of this SecurityHistory.  # noqa: E501
        :rtype: date
        """
        return self._first_price_date
        
    @property
    def first_price_date_dict(self):
        """Gets the first_price_date of this SecurityHistory.  # noqa: E501

        The date of the first recorded stock price as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The first_price_date of this SecurityHistory.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.first_price_date
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
            result = { 'first_price_date': value }

        
        return result
        

    @first_price_date.setter
    def first_price_date(self, first_price_date):
        """Sets the first_price_date of this SecurityHistory.

        The date of the first recorded stock price  # noqa: E501

        :param first_price_date: The first_price_date of this SecurityHistory.  # noqa: E501
        :type: date
        """

        self._first_price_date = first_price_date

    @property
    def last_price_date(self):
        """Gets the last_price_date of this SecurityHistory.  # noqa: E501

        The date of the last recorded stock price (or the most recent trading day)  # noqa: E501

        :return: The last_price_date of this SecurityHistory.  # noqa: E501
        :rtype: date
        """
        return self._last_price_date
        
    @property
    def last_price_date_dict(self):
        """Gets the last_price_date of this SecurityHistory.  # noqa: E501

        The date of the last recorded stock price (or the most recent trading day) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_price_date of this SecurityHistory.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.last_price_date
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
            result = { 'last_price_date': value }

        
        return result
        

    @last_price_date.setter
    def last_price_date(self, last_price_date):
        """Sets the last_price_date of this SecurityHistory.

        The date of the last recorded stock price (or the most recent trading day)  # noqa: E501

        :param last_price_date: The last_price_date of this SecurityHistory.  # noqa: E501
        :type: date
        """

        self._last_price_date = last_price_date

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
        if not isinstance(other, SecurityHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
