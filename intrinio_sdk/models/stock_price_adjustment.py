# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.70.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.security_summary import SecuritySummary  # noqa: F401,E501


class StockPriceAdjustment(object):
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
        'date': 'date',
        'factor': 'float',
        'dividend': 'float',
        'dividend_currency': 'str',
        'split_ratio': 'float',
        'security': 'SecuritySummary'
    }

    attribute_map = {
        'date': 'date',
        'factor': 'factor',
        'dividend': 'dividend',
        'dividend_currency': 'dividend_currency',
        'split_ratio': 'split_ratio',
        'security': 'security'
    }

    def __init__(self, date=None, factor=None, dividend=None, dividend_currency=None, split_ratio=None, security=None):  # noqa: E501
        """StockPriceAdjustment - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._factor = None
        self._dividend = None
        self._dividend_currency = None
        self._split_ratio = None
        self._security = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if factor is not None:
            self.factor = factor
        if dividend is not None:
            self.dividend = dividend
        if dividend_currency is not None:
            self.dividend_currency = dividend_currency
        if split_ratio is not None:
            self.split_ratio = split_ratio
        if security is not None:
            self.security = security

    @property
    def date(self):
        """Gets the date of this StockPriceAdjustment.  # noqa: E501

        The date on which the adjustment occurred. The adjustment should be applied to all stock prices before this date.  # noqa: E501

        :return: The date of this StockPriceAdjustment.  # noqa: E501
        :rtype: date
        """
        return self._date
        
    @property
    def date_dict(self):
        """Gets the date of this StockPriceAdjustment.  # noqa: E501

        The date on which the adjustment occurred. The adjustment should be applied to all stock prices before this date. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date of this StockPriceAdjustment.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.date
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
            result = { 'date': value }

        
        return result
        

    @date.setter
    def date(self, date):
        """Sets the date of this StockPriceAdjustment.

        The date on which the adjustment occurred. The adjustment should be applied to all stock prices before this date.  # noqa: E501

        :param date: The date of this StockPriceAdjustment.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def factor(self):
        """Gets the factor of this StockPriceAdjustment.  # noqa: E501

        The factor by which to multiply stock prices before this date, in order to calculate historically-adjusted stock prices.  # noqa: E501

        :return: The factor of this StockPriceAdjustment.  # noqa: E501
        :rtype: float
        """
        return self._factor
        
    @property
    def factor_dict(self):
        """Gets the factor of this StockPriceAdjustment.  # noqa: E501

        The factor by which to multiply stock prices before this date, in order to calculate historically-adjusted stock prices. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The factor of this StockPriceAdjustment.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.factor
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
            result = { 'factor': value }

        
        return result
        

    @factor.setter
    def factor(self, factor):
        """Sets the factor of this StockPriceAdjustment.

        The factor by which to multiply stock prices before this date, in order to calculate historically-adjusted stock prices.  # noqa: E501

        :param factor: The factor of this StockPriceAdjustment.  # noqa: E501
        :type: float
        """

        self._factor = factor

    @property
    def dividend(self):
        """Gets the dividend of this StockPriceAdjustment.  # noqa: E501

        The dividend amount, if a dividend was paid.  # noqa: E501

        :return: The dividend of this StockPriceAdjustment.  # noqa: E501
        :rtype: float
        """
        return self._dividend
        
    @property
    def dividend_dict(self):
        """Gets the dividend of this StockPriceAdjustment.  # noqa: E501

        The dividend amount, if a dividend was paid. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The dividend of this StockPriceAdjustment.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.dividend
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
            result = { 'dividend': value }

        
        return result
        

    @dividend.setter
    def dividend(self, dividend):
        """Sets the dividend of this StockPriceAdjustment.

        The dividend amount, if a dividend was paid.  # noqa: E501

        :param dividend: The dividend of this StockPriceAdjustment.  # noqa: E501
        :type: float
        """

        self._dividend = dividend

    @property
    def dividend_currency(self):
        """Gets the dividend_currency of this StockPriceAdjustment.  # noqa: E501

        The currency of the dividend, if known.  # noqa: E501

        :return: The dividend_currency of this StockPriceAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._dividend_currency
        
    @property
    def dividend_currency_dict(self):
        """Gets the dividend_currency of this StockPriceAdjustment.  # noqa: E501

        The currency of the dividend, if known. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The dividend_currency of this StockPriceAdjustment.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.dividend_currency
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
            result = { 'dividend_currency': value }

        
        return result
        

    @dividend_currency.setter
    def dividend_currency(self, dividend_currency):
        """Sets the dividend_currency of this StockPriceAdjustment.

        The currency of the dividend, if known.  # noqa: E501

        :param dividend_currency: The dividend_currency of this StockPriceAdjustment.  # noqa: E501
        :type: str
        """

        self._dividend_currency = dividend_currency

    @property
    def split_ratio(self):
        """Gets the split_ratio of this StockPriceAdjustment.  # noqa: E501

        The ratio of the stock split, if a stock split occurred.  # noqa: E501

        :return: The split_ratio of this StockPriceAdjustment.  # noqa: E501
        :rtype: float
        """
        return self._split_ratio
        
    @property
    def split_ratio_dict(self):
        """Gets the split_ratio of this StockPriceAdjustment.  # noqa: E501

        The ratio of the stock split, if a stock split occurred. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The split_ratio of this StockPriceAdjustment.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.split_ratio
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
            result = { 'split_ratio': value }

        
        return result
        

    @split_ratio.setter
    def split_ratio(self, split_ratio):
        """Sets the split_ratio of this StockPriceAdjustment.

        The ratio of the stock split, if a stock split occurred.  # noqa: E501

        :param split_ratio: The split_ratio of this StockPriceAdjustment.  # noqa: E501
        :type: float
        """

        self._split_ratio = split_ratio

    @property
    def security(self):
        """Gets the security of this StockPriceAdjustment.  # noqa: E501

        The Security of the stock price  # noqa: E501

        :return: The security of this StockPriceAdjustment.  # noqa: E501
        :rtype: SecuritySummary
        """
        return self._security
        
    @property
    def security_dict(self):
        """Gets the security of this StockPriceAdjustment.  # noqa: E501

        The Security of the stock price as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The security of this StockPriceAdjustment.  # noqa: E501
        :rtype: SecuritySummary
        """

        result = None

        value = self.security
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
            result = { 'security': value }

        
        return result
        

    @security.setter
    def security(self, security):
        """Sets the security of this StockPriceAdjustment.

        The Security of the stock price  # noqa: E501

        :param security: The security of this StockPriceAdjustment.  # noqa: E501
        :type: SecuritySummary
        """

        self._security = security

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
        if not isinstance(other, StockPriceAdjustment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
