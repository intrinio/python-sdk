# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.63.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ZacksEBITDAConsensus(object):
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
        'ticker': 'str',
        'company_name': 'str',
        'estimate_year': 'float',
        'estimate_month': 'float',
        'period': 'str',
        'consensus_type': 'str',
        'estimate_count': 'float',
        'high': 'float',
        'low': 'float',
        'mean': 'float',
        'std_dev': 'float'
    }

    attribute_map = {
        'ticker': 'ticker',
        'company_name': 'company_name',
        'estimate_year': 'estimate_year',
        'estimate_month': 'estimate_month',
        'period': 'period',
        'consensus_type': 'consensus_type',
        'estimate_count': 'estimate_count',
        'high': 'high',
        'low': 'low',
        'mean': 'mean',
        'std_dev': 'std_dev'
    }

    def __init__(self, ticker=None, company_name=None, estimate_year=None, estimate_month=None, period=None, consensus_type=None, estimate_count=None, high=None, low=None, mean=None, std_dev=None):  # noqa: E501
        """ZacksEBITDAConsensus - a model defined in Swagger"""  # noqa: E501

        self._ticker = None
        self._company_name = None
        self._estimate_year = None
        self._estimate_month = None
        self._period = None
        self._consensus_type = None
        self._estimate_count = None
        self._high = None
        self._low = None
        self._mean = None
        self._std_dev = None
        self.discriminator = None

        if ticker is not None:
            self.ticker = ticker
        if company_name is not None:
            self.company_name = company_name
        if estimate_year is not None:
            self.estimate_year = estimate_year
        if estimate_month is not None:
            self.estimate_month = estimate_month
        if period is not None:
            self.period = period
        if consensus_type is not None:
            self.consensus_type = consensus_type
        if estimate_count is not None:
            self.estimate_count = estimate_count
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if mean is not None:
            self.mean = mean
        if std_dev is not None:
            self.std_dev = std_dev

    @property
    def ticker(self):
        """Gets the ticker of this ZacksEBITDAConsensus.  # noqa: E501

        The Zacks common exchange ticker  # noqa: E501

        :return: The ticker of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this ZacksEBITDAConsensus.  # noqa: E501

        The Zacks common exchange ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this ZacksEBITDAConsensus.  # noqa: E501
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
        """Sets the ticker of this ZacksEBITDAConsensus.

        The Zacks common exchange ticker  # noqa: E501

        :param ticker: The ticker of this ZacksEBITDAConsensus.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def company_name(self):
        """Gets the company_name of this ZacksEBITDAConsensus.  # noqa: E501

        The company name  # noqa: E501

        :return: The company_name of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: str
        """
        return self._company_name
        
    @property
    def company_name_dict(self):
        """Gets the company_name of this ZacksEBITDAConsensus.  # noqa: E501

        The company name as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The company_name of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.company_name
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
            result = { 'company_name': value }

        
        return result
        

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ZacksEBITDAConsensus.

        The company name  # noqa: E501

        :param company_name: The company_name of this ZacksEBITDAConsensus.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def estimate_year(self):
        """Gets the estimate_year of this ZacksEBITDAConsensus.  # noqa: E501

        Fiscal year of the estimate  # noqa: E501

        :return: The estimate_year of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """
        return self._estimate_year
        
    @property
    def estimate_year_dict(self):
        """Gets the estimate_year of this ZacksEBITDAConsensus.  # noqa: E501

        Fiscal year of the estimate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The estimate_year of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.estimate_year
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
            result = { 'estimate_year': value }

        
        return result
        

    @estimate_year.setter
    def estimate_year(self, estimate_year):
        """Sets the estimate_year of this ZacksEBITDAConsensus.

        Fiscal year of the estimate  # noqa: E501

        :param estimate_year: The estimate_year of this ZacksEBITDAConsensus.  # noqa: E501
        :type: float
        """

        self._estimate_year = estimate_year

    @property
    def estimate_month(self):
        """Gets the estimate_month of this ZacksEBITDAConsensus.  # noqa: E501

        Fiscal month of the estimate  # noqa: E501

        :return: The estimate_month of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """
        return self._estimate_month
        
    @property
    def estimate_month_dict(self):
        """Gets the estimate_month of this ZacksEBITDAConsensus.  # noqa: E501

        Fiscal month of the estimate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The estimate_month of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.estimate_month
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
            result = { 'estimate_month': value }

        
        return result
        

    @estimate_month.setter
    def estimate_month(self, estimate_month):
        """Sets the estimate_month of this ZacksEBITDAConsensus.

        Fiscal month of the estimate  # noqa: E501

        :param estimate_month: The estimate_month of this ZacksEBITDAConsensus.  # noqa: E501
        :type: float
        """

        self._estimate_month = estimate_month

    @property
    def period(self):
        """Gets the period of this ZacksEBITDAConsensus.  # noqa: E501

        Whether the estimate year and month are fiscal year (fy) or quarter (fq)  # noqa: E501

        :return: The period of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: str
        """
        return self._period
        
    @property
    def period_dict(self):
        """Gets the period of this ZacksEBITDAConsensus.  # noqa: E501

        Whether the estimate year and month are fiscal year (fy) or quarter (fq) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The period of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.period
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
            result = { 'period': value }

        
        return result
        

    @period.setter
    def period(self, period):
        """Sets the period of this ZacksEBITDAConsensus.

        Whether the estimate year and month are fiscal year (fy) or quarter (fq)  # noqa: E501

        :param period: The period of this ZacksEBITDAConsensus.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def consensus_type(self):
        """Gets the consensus_type of this ZacksEBITDAConsensus.  # noqa: E501

        The type of estimate (ebitda, ebitda, ebit, enterprise_value, cash_flow_per_share, pretax_income)  # noqa: E501

        :return: The consensus_type of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: str
        """
        return self._consensus_type
        
    @property
    def consensus_type_dict(self):
        """Gets the consensus_type of this ZacksEBITDAConsensus.  # noqa: E501

        The type of estimate (ebitda, ebitda, ebit, enterprise_value, cash_flow_per_share, pretax_income) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The consensus_type of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.consensus_type
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
            result = { 'consensus_type': value }

        
        return result
        

    @consensus_type.setter
    def consensus_type(self, consensus_type):
        """Sets the consensus_type of this ZacksEBITDAConsensus.

        The type of estimate (ebitda, ebitda, ebit, enterprise_value, cash_flow_per_share, pretax_income)  # noqa: E501

        :param consensus_type: The consensus_type of this ZacksEBITDAConsensus.  # noqa: E501
        :type: str
        """

        self._consensus_type = consensus_type

    @property
    def estimate_count(self):
        """Gets the estimate_count of this ZacksEBITDAConsensus.  # noqa: E501

        The number of estimates  # noqa: E501

        :return: The estimate_count of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """
        return self._estimate_count
        
    @property
    def estimate_count_dict(self):
        """Gets the estimate_count of this ZacksEBITDAConsensus.  # noqa: E501

        The number of estimates as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The estimate_count of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.estimate_count
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
            result = { 'estimate_count': value }

        
        return result
        

    @estimate_count.setter
    def estimate_count(self, estimate_count):
        """Sets the estimate_count of this ZacksEBITDAConsensus.

        The number of estimates  # noqa: E501

        :param estimate_count: The estimate_count of this ZacksEBITDAConsensus.  # noqa: E501
        :type: float
        """

        self._estimate_count = estimate_count

    @property
    def high(self):
        """Gets the high of this ZacksEBITDAConsensus.  # noqa: E501

        The highest estimate  # noqa: E501

        :return: The high of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """
        return self._high
        
    @property
    def high_dict(self):
        """Gets the high of this ZacksEBITDAConsensus.  # noqa: E501

        The highest estimate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The high of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.high
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
            result = { 'high': value }

        
        return result
        

    @high.setter
    def high(self, high):
        """Sets the high of this ZacksEBITDAConsensus.

        The highest estimate  # noqa: E501

        :param high: The high of this ZacksEBITDAConsensus.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this ZacksEBITDAConsensus.  # noqa: E501

        The lowest estimate  # noqa: E501

        :return: The low of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """
        return self._low
        
    @property
    def low_dict(self):
        """Gets the low of this ZacksEBITDAConsensus.  # noqa: E501

        The lowest estimate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The low of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.low
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
            result = { 'low': value }

        
        return result
        

    @low.setter
    def low(self, low):
        """Sets the low of this ZacksEBITDAConsensus.

        The lowest estimate  # noqa: E501

        :param low: The low of this ZacksEBITDAConsensus.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def mean(self):
        """Gets the mean of this ZacksEBITDAConsensus.  # noqa: E501

        The mean value of all estimates  # noqa: E501

        :return: The mean of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """
        return self._mean
        
    @property
    def mean_dict(self):
        """Gets the mean of this ZacksEBITDAConsensus.  # noqa: E501

        The mean value of all estimates as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mean of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.mean
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
            result = { 'mean': value }

        
        return result
        

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this ZacksEBITDAConsensus.

        The mean value of all estimates  # noqa: E501

        :param mean: The mean of this ZacksEBITDAConsensus.  # noqa: E501
        :type: float
        """

        self._mean = mean

    @property
    def std_dev(self):
        """Gets the std_dev of this ZacksEBITDAConsensus.  # noqa: E501

        The standard deviation of all estimates  # noqa: E501

        :return: The std_dev of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """
        return self._std_dev
        
    @property
    def std_dev_dict(self):
        """Gets the std_dev of this ZacksEBITDAConsensus.  # noqa: E501

        The standard deviation of all estimates as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The std_dev of this ZacksEBITDAConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.std_dev
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
            result = { 'std_dev': value }

        
        return result
        

    @std_dev.setter
    def std_dev(self, std_dev):
        """Sets the std_dev of this ZacksEBITDAConsensus.

        The standard deviation of all estimates  # noqa: E501

        :param std_dev: The std_dev of this ZacksEBITDAConsensus.  # noqa: E501
        :type: float
        """

        self._std_dev = std_dev

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
        if not isinstance(other, ZacksEBITDAConsensus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
