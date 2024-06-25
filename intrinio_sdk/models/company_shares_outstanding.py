# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.62.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CompanySharesOutstanding(object):
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
        'xbrl_axis': 'str',
        'xbrl_member': 'str',
        'end_date': 'date',
        'title_of_security': 'str',
        'trading_symbol': 'str',
        'security_exchange_name': 'str',
        'shares_outstanding': 'float'
    }

    attribute_map = {
        'xbrl_axis': 'xbrl_axis',
        'xbrl_member': 'xbrl_member',
        'end_date': 'end_date',
        'title_of_security': 'title_of_security',
        'trading_symbol': 'trading_symbol',
        'security_exchange_name': 'security_exchange_name',
        'shares_outstanding': 'shares_outstanding'
    }

    def __init__(self, xbrl_axis=None, xbrl_member=None, end_date=None, title_of_security=None, trading_symbol=None, security_exchange_name=None, shares_outstanding=None):  # noqa: E501
        """CompanySharesOutstanding - a model defined in Swagger"""  # noqa: E501

        self._xbrl_axis = None
        self._xbrl_member = None
        self._end_date = None
        self._title_of_security = None
        self._trading_symbol = None
        self._security_exchange_name = None
        self._shares_outstanding = None
        self.discriminator = None

        if xbrl_axis is not None:
            self.xbrl_axis = xbrl_axis
        if xbrl_member is not None:
            self.xbrl_member = xbrl_member
        if end_date is not None:
            self.end_date = end_date
        if title_of_security is not None:
            self.title_of_security = title_of_security
        if trading_symbol is not None:
            self.trading_symbol = trading_symbol
        if security_exchange_name is not None:
            self.security_exchange_name = security_exchange_name
        if shares_outstanding is not None:
            self.shares_outstanding = shares_outstanding

    @property
    def xbrl_axis(self):
        """Gets the xbrl_axis of this CompanySharesOutstanding.  # noqa: E501

        The xbrl concept axis member reported to the SEC.  # noqa: E501

        :return: The xbrl_axis of this CompanySharesOutstanding.  # noqa: E501
        :rtype: str
        """
        return self._xbrl_axis
        
    @property
    def xbrl_axis_dict(self):
        """Gets the xbrl_axis of this CompanySharesOutstanding.  # noqa: E501

        The xbrl concept axis member reported to the SEC. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The xbrl_axis of this CompanySharesOutstanding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.xbrl_axis
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
            result = { 'xbrl_axis': value }

        
        return result
        

    @xbrl_axis.setter
    def xbrl_axis(self, xbrl_axis):
        """Sets the xbrl_axis of this CompanySharesOutstanding.

        The xbrl concept axis member reported to the SEC.  # noqa: E501

        :param xbrl_axis: The xbrl_axis of this CompanySharesOutstanding.  # noqa: E501
        :type: str
        """

        self._xbrl_axis = xbrl_axis

    @property
    def xbrl_member(self):
        """Gets the xbrl_member of this CompanySharesOutstanding.  # noqa: E501

        Provides information about the class of stock as reported in XBRL  # noqa: E501

        :return: The xbrl_member of this CompanySharesOutstanding.  # noqa: E501
        :rtype: str
        """
        return self._xbrl_member
        
    @property
    def xbrl_member_dict(self):
        """Gets the xbrl_member of this CompanySharesOutstanding.  # noqa: E501

        Provides information about the class of stock as reported in XBRL as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The xbrl_member of this CompanySharesOutstanding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.xbrl_member
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
            result = { 'xbrl_member': value }

        
        return result
        

    @xbrl_member.setter
    def xbrl_member(self, xbrl_member):
        """Sets the xbrl_member of this CompanySharesOutstanding.

        Provides information about the class of stock as reported in XBRL  # noqa: E501

        :param xbrl_member: The xbrl_member of this CompanySharesOutstanding.  # noqa: E501
        :type: str
        """

        self._xbrl_member = xbrl_member

    @property
    def end_date(self):
        """Gets the end_date of this CompanySharesOutstanding.  # noqa: E501

        End date of the filing period  # noqa: E501

        :return: The end_date of this CompanySharesOutstanding.  # noqa: E501
        :rtype: date
        """
        return self._end_date
        
    @property
    def end_date_dict(self):
        """Gets the end_date of this CompanySharesOutstanding.  # noqa: E501

        End date of the filing period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The end_date of this CompanySharesOutstanding.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.end_date
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
            result = { 'end_date': value }

        
        return result
        

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CompanySharesOutstanding.

        End date of the filing period  # noqa: E501

        :param end_date: The end_date of this CompanySharesOutstanding.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def title_of_security(self):
        """Gets the title_of_security of this CompanySharesOutstanding.  # noqa: E501

        The description of the security type  # noqa: E501

        :return: The title_of_security of this CompanySharesOutstanding.  # noqa: E501
        :rtype: str
        """
        return self._title_of_security
        
    @property
    def title_of_security_dict(self):
        """Gets the title_of_security of this CompanySharesOutstanding.  # noqa: E501

        The description of the security type as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The title_of_security of this CompanySharesOutstanding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.title_of_security
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
            result = { 'title_of_security': value }

        
        return result
        

    @title_of_security.setter
    def title_of_security(self, title_of_security):
        """Sets the title_of_security of this CompanySharesOutstanding.

        The description of the security type  # noqa: E501

        :param title_of_security: The title_of_security of this CompanySharesOutstanding.  # noqa: E501
        :type: str
        """

        self._title_of_security = title_of_security

    @property
    def trading_symbol(self):
        """Gets the trading_symbol of this CompanySharesOutstanding.  # noqa: E501

        The symbol under which the security is traded in the exchange  # noqa: E501

        :return: The trading_symbol of this CompanySharesOutstanding.  # noqa: E501
        :rtype: str
        """
        return self._trading_symbol
        
    @property
    def trading_symbol_dict(self):
        """Gets the trading_symbol of this CompanySharesOutstanding.  # noqa: E501

        The symbol under which the security is traded in the exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The trading_symbol of this CompanySharesOutstanding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.trading_symbol
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
            result = { 'trading_symbol': value }

        
        return result
        

    @trading_symbol.setter
    def trading_symbol(self, trading_symbol):
        """Sets the trading_symbol of this CompanySharesOutstanding.

        The symbol under which the security is traded in the exchange  # noqa: E501

        :param trading_symbol: The trading_symbol of this CompanySharesOutstanding.  # noqa: E501
        :type: str
        """

        self._trading_symbol = trading_symbol

    @property
    def security_exchange_name(self):
        """Gets the security_exchange_name of this CompanySharesOutstanding.  # noqa: E501

        The name of the secuirty exchange  # noqa: E501

        :return: The security_exchange_name of this CompanySharesOutstanding.  # noqa: E501
        :rtype: str
        """
        return self._security_exchange_name
        
    @property
    def security_exchange_name_dict(self):
        """Gets the security_exchange_name of this CompanySharesOutstanding.  # noqa: E501

        The name of the secuirty exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The security_exchange_name of this CompanySharesOutstanding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.security_exchange_name
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
            result = { 'security_exchange_name': value }

        
        return result
        

    @security_exchange_name.setter
    def security_exchange_name(self, security_exchange_name):
        """Sets the security_exchange_name of this CompanySharesOutstanding.

        The name of the secuirty exchange  # noqa: E501

        :param security_exchange_name: The security_exchange_name of this CompanySharesOutstanding.  # noqa: E501
        :type: str
        """

        self._security_exchange_name = security_exchange_name

    @property
    def shares_outstanding(self):
        """Gets the shares_outstanding of this CompanySharesOutstanding.  # noqa: E501

        The amount of stock currently held by all shareholders  # noqa: E501

        :return: The shares_outstanding of this CompanySharesOutstanding.  # noqa: E501
        :rtype: float
        """
        return self._shares_outstanding
        
    @property
    def shares_outstanding_dict(self):
        """Gets the shares_outstanding of this CompanySharesOutstanding.  # noqa: E501

        The amount of stock currently held by all shareholders as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shares_outstanding of this CompanySharesOutstanding.  # noqa: E501
        :rtype: float
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
        """Sets the shares_outstanding of this CompanySharesOutstanding.

        The amount of stock currently held by all shareholders  # noqa: E501

        :param shares_outstanding: The shares_outstanding of this CompanySharesOutstanding.  # noqa: E501
        :type: float
        """

        self._shares_outstanding = shares_outstanding

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
        if not isinstance(other, CompanySharesOutstanding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
