# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.26.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501


class ZacksEPSEstimate(object):
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
        'company': 'CompanySummary',
        'date': 'date',
        'fiscal_year': 'int',
        'fiscal_quarter': 'str',
        'calendar_year': 'int',
        'calendar_quarter': 'str',
        'count': 'int',
        'mean': 'float',
        'median': 'float',
        'high': 'float',
        'low': 'float',
        'standard_deviation': 'float',
        'percent_change': 'float',
        'mean_7_days_ago': 'float',
        'mean_30_days_ago': 'float',
        'mean_60_days_ago': 'float',
        'mean_90_days_ago': 'float'
    }

    attribute_map = {
        'company': 'company',
        'date': 'date',
        'fiscal_year': 'fiscal_year',
        'fiscal_quarter': 'fiscal_quarter',
        'calendar_year': 'calendar_year',
        'calendar_quarter': 'calendar_quarter',
        'count': 'count',
        'mean': 'mean',
        'median': 'median',
        'high': 'high',
        'low': 'low',
        'standard_deviation': 'standard_deviation',
        'percent_change': 'percent_change',
        'mean_7_days_ago': 'mean_7_days_ago',
        'mean_30_days_ago': 'mean_30_days_ago',
        'mean_60_days_ago': 'mean_60_days_ago',
        'mean_90_days_ago': 'mean_90_days_ago'
    }

    def __init__(self, company=None, date=None, fiscal_year=None, fiscal_quarter=None, calendar_year=None, calendar_quarter=None, count=None, mean=None, median=None, high=None, low=None, standard_deviation=None, percent_change=None, mean_7_days_ago=None, mean_30_days_ago=None, mean_60_days_ago=None, mean_90_days_ago=None):  # noqa: E501
        """ZacksEPSEstimate - a model defined in Swagger"""  # noqa: E501

        self._company = None
        self._date = None
        self._fiscal_year = None
        self._fiscal_quarter = None
        self._calendar_year = None
        self._calendar_quarter = None
        self._count = None
        self._mean = None
        self._median = None
        self._high = None
        self._low = None
        self._standard_deviation = None
        self._percent_change = None
        self._mean_7_days_ago = None
        self._mean_30_days_ago = None
        self._mean_60_days_ago = None
        self._mean_90_days_ago = None
        self.discriminator = None

        if company is not None:
            self.company = company
        if date is not None:
            self.date = date
        if fiscal_year is not None:
            self.fiscal_year = fiscal_year
        if fiscal_quarter is not None:
            self.fiscal_quarter = fiscal_quarter
        if calendar_year is not None:
            self.calendar_year = calendar_year
        if calendar_quarter is not None:
            self.calendar_quarter = calendar_quarter
        if count is not None:
            self.count = count
        if mean is not None:
            self.mean = mean
        if median is not None:
            self.median = median
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if standard_deviation is not None:
            self.standard_deviation = standard_deviation
        if percent_change is not None:
            self.percent_change = percent_change
        if mean_7_days_ago is not None:
            self.mean_7_days_ago = mean_7_days_ago
        if mean_30_days_ago is not None:
            self.mean_30_days_ago = mean_30_days_ago
        if mean_60_days_ago is not None:
            self.mean_60_days_ago = mean_60_days_ago
        if mean_90_days_ago is not None:
            self.mean_90_days_ago = mean_90_days_ago

    @property
    def company(self):
        """Gets the company of this ZacksEPSEstimate.  # noqa: E501


        :return: The company of this ZacksEPSEstimate.  # noqa: E501
        :rtype: CompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this ZacksEPSEstimate.  # noqa: E501


        :return: The company of this ZacksEPSEstimate.  # noqa: E501
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
        """Sets the company of this ZacksEPSEstimate.


        :param company: The company of this ZacksEPSEstimate.  # noqa: E501
        :type: CompanySummary
        """

        self._company = company

    @property
    def date(self):
        """Gets the date of this ZacksEPSEstimate.  # noqa: E501

        The period end date  # noqa: E501

        :return: The date of this ZacksEPSEstimate.  # noqa: E501
        :rtype: date
        """
        return self._date
        
    @property
    def date_dict(self):
        """Gets the date of this ZacksEPSEstimate.  # noqa: E501

        The period end date as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date of this ZacksEPSEstimate.  # noqa: E501
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
        """Sets the date of this ZacksEPSEstimate.

        The period end date  # noqa: E501

        :param date: The date of this ZacksEPSEstimate.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def fiscal_year(self):
        """Gets the fiscal_year of this ZacksEPSEstimate.  # noqa: E501

        The company’s fiscal year for the reported period  # noqa: E501

        :return: The fiscal_year of this ZacksEPSEstimate.  # noqa: E501
        :rtype: int
        """
        return self._fiscal_year
        
    @property
    def fiscal_year_dict(self):
        """Gets the fiscal_year of this ZacksEPSEstimate.  # noqa: E501

        The company’s fiscal year for the reported period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The fiscal_year of this ZacksEPSEstimate.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.fiscal_year
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
            result = { 'fiscal_year': value }

        
        return result
        

    @fiscal_year.setter
    def fiscal_year(self, fiscal_year):
        """Sets the fiscal_year of this ZacksEPSEstimate.

        The company’s fiscal year for the reported period  # noqa: E501

        :param fiscal_year: The fiscal_year of this ZacksEPSEstimate.  # noqa: E501
        :type: int
        """

        self._fiscal_year = fiscal_year

    @property
    def fiscal_quarter(self):
        """Gets the fiscal_quarter of this ZacksEPSEstimate.  # noqa: E501

        The company’s fiscal quarter for the reported period  # noqa: E501

        :return: The fiscal_quarter of this ZacksEPSEstimate.  # noqa: E501
        :rtype: str
        """
        return self._fiscal_quarter
        
    @property
    def fiscal_quarter_dict(self):
        """Gets the fiscal_quarter of this ZacksEPSEstimate.  # noqa: E501

        The company’s fiscal quarter for the reported period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The fiscal_quarter of this ZacksEPSEstimate.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.fiscal_quarter
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
            result = { 'fiscal_quarter': value }

        
        return result
        

    @fiscal_quarter.setter
    def fiscal_quarter(self, fiscal_quarter):
        """Sets the fiscal_quarter of this ZacksEPSEstimate.

        The company’s fiscal quarter for the reported period  # noqa: E501

        :param fiscal_quarter: The fiscal_quarter of this ZacksEPSEstimate.  # noqa: E501
        :type: str
        """

        self._fiscal_quarter = fiscal_quarter

    @property
    def calendar_year(self):
        """Gets the calendar_year of this ZacksEPSEstimate.  # noqa: E501

        The closest calendar year for the company’s fiscal year  # noqa: E501

        :return: The calendar_year of this ZacksEPSEstimate.  # noqa: E501
        :rtype: int
        """
        return self._calendar_year
        
    @property
    def calendar_year_dict(self):
        """Gets the calendar_year of this ZacksEPSEstimate.  # noqa: E501

        The closest calendar year for the company’s fiscal year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The calendar_year of this ZacksEPSEstimate.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.calendar_year
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
            result = { 'calendar_year': value }

        
        return result
        

    @calendar_year.setter
    def calendar_year(self, calendar_year):
        """Sets the calendar_year of this ZacksEPSEstimate.

        The closest calendar year for the company’s fiscal year  # noqa: E501

        :param calendar_year: The calendar_year of this ZacksEPSEstimate.  # noqa: E501
        :type: int
        """

        self._calendar_year = calendar_year

    @property
    def calendar_quarter(self):
        """Gets the calendar_quarter of this ZacksEPSEstimate.  # noqa: E501

        The closest calendar quarter for the company’s fiscal year  # noqa: E501

        :return: The calendar_quarter of this ZacksEPSEstimate.  # noqa: E501
        :rtype: str
        """
        return self._calendar_quarter
        
    @property
    def calendar_quarter_dict(self):
        """Gets the calendar_quarter of this ZacksEPSEstimate.  # noqa: E501

        The closest calendar quarter for the company’s fiscal year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The calendar_quarter of this ZacksEPSEstimate.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.calendar_quarter
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
            result = { 'calendar_quarter': value }

        
        return result
        

    @calendar_quarter.setter
    def calendar_quarter(self, calendar_quarter):
        """Sets the calendar_quarter of this ZacksEPSEstimate.

        The closest calendar quarter for the company’s fiscal year  # noqa: E501

        :param calendar_quarter: The calendar_quarter of this ZacksEPSEstimate.  # noqa: E501
        :type: str
        """

        self._calendar_quarter = calendar_quarter

    @property
    def count(self):
        """Gets the count of this ZacksEPSEstimate.  # noqa: E501

        The number of estimates for the period  # noqa: E501

        :return: The count of this ZacksEPSEstimate.  # noqa: E501
        :rtype: int
        """
        return self._count
        
    @property
    def count_dict(self):
        """Gets the count of this ZacksEPSEstimate.  # noqa: E501

        The number of estimates for the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The count of this ZacksEPSEstimate.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.count
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
            result = { 'count': value }

        
        return result
        

    @count.setter
    def count(self, count):
        """Sets the count of this ZacksEPSEstimate.

        The number of estimates for the period  # noqa: E501

        :param count: The count of this ZacksEPSEstimate.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def mean(self):
        """Gets the mean of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) mean estimate for the period  # noqa: E501

        :return: The mean of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """
        return self._mean
        
    @property
    def mean_dict(self):
        """Gets the mean of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) mean estimate for the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mean of this ZacksEPSEstimate.  # noqa: E501
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
        """Sets the mean of this ZacksEPSEstimate.

        The earnings per share (EPS) mean estimate for the period  # noqa: E501

        :param mean: The mean of this ZacksEPSEstimate.  # noqa: E501
        :type: float
        """

        self._mean = mean

    @property
    def median(self):
        """Gets the median of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) median estimate for the period  # noqa: E501

        :return: The median of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """
        return self._median
        
    @property
    def median_dict(self):
        """Gets the median of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) median estimate for the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The median of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.median
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
            result = { 'median': value }

        
        return result
        

    @median.setter
    def median(self, median):
        """Sets the median of this ZacksEPSEstimate.

        The earnings per share (EPS) median estimate for the period  # noqa: E501

        :param median: The median of this ZacksEPSEstimate.  # noqa: E501
        :type: float
        """

        self._median = median

    @property
    def high(self):
        """Gets the high of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) high estimate for the period  # noqa: E501

        :return: The high of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """
        return self._high
        
    @property
    def high_dict(self):
        """Gets the high of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) high estimate for the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The high of this ZacksEPSEstimate.  # noqa: E501
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
        """Sets the high of this ZacksEPSEstimate.

        The earnings per share (EPS) high estimate for the period  # noqa: E501

        :param high: The high of this ZacksEPSEstimate.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) low estimate for the period  # noqa: E501

        :return: The low of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """
        return self._low
        
    @property
    def low_dict(self):
        """Gets the low of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) low estimate for the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The low of this ZacksEPSEstimate.  # noqa: E501
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
        """Sets the low of this ZacksEPSEstimate.

        The earnings per share (EPS) low estimate for the period  # noqa: E501

        :param low: The low of this ZacksEPSEstimate.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def standard_deviation(self):
        """Gets the standard_deviation of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) standard deviation estimate for the period  # noqa: E501

        :return: The standard_deviation of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """
        return self._standard_deviation
        
    @property
    def standard_deviation_dict(self):
        """Gets the standard_deviation of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) standard deviation estimate for the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The standard_deviation of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.standard_deviation
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
            result = { 'standard_deviation': value }

        
        return result
        

    @standard_deviation.setter
    def standard_deviation(self, standard_deviation):
        """Sets the standard_deviation of this ZacksEPSEstimate.

        The earnings per share (EPS) standard deviation estimate for the period  # noqa: E501

        :param standard_deviation: The standard_deviation of this ZacksEPSEstimate.  # noqa: E501
        :type: float
        """

        self._standard_deviation = standard_deviation

    @property
    def percent_change(self):
        """Gets the percent_change of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) percent change in estimate for the period  # noqa: E501

        :return: The percent_change of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """
        return self._percent_change
        
    @property
    def percent_change_dict(self):
        """Gets the percent_change of this ZacksEPSEstimate.  # noqa: E501

        The earnings per share (EPS) percent change in estimate for the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The percent_change of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.percent_change
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
            result = { 'percent_change': value }

        
        return result
        

    @percent_change.setter
    def percent_change(self, percent_change):
        """Sets the percent_change of this ZacksEPSEstimate.

        The earnings per share (EPS) percent change in estimate for the period  # noqa: E501

        :param percent_change: The percent_change of this ZacksEPSEstimate.  # noqa: E501
        :type: float
        """

        self._percent_change = percent_change

    @property
    def mean_7_days_ago(self):
        """Gets the mean_7_days_ago of this ZacksEPSEstimate.  # noqa: E501

        The long term growth mean estimate - 7 Days Ago  # noqa: E501

        :return: The mean_7_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """
        return self._mean_7_days_ago
        
    @property
    def mean_7_days_ago_dict(self):
        """Gets the mean_7_days_ago of this ZacksEPSEstimate.  # noqa: E501

        The long term growth mean estimate - 7 Days Ago as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mean_7_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.mean_7_days_ago
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
            result = { 'mean_7_days_ago': value }

        
        return result
        

    @mean_7_days_ago.setter
    def mean_7_days_ago(self, mean_7_days_ago):
        """Sets the mean_7_days_ago of this ZacksEPSEstimate.

        The long term growth mean estimate - 7 Days Ago  # noqa: E501

        :param mean_7_days_ago: The mean_7_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :type: float
        """

        self._mean_7_days_ago = mean_7_days_ago

    @property
    def mean_30_days_ago(self):
        """Gets the mean_30_days_ago of this ZacksEPSEstimate.  # noqa: E501

        The long term growth mean estimate - 30 Days Ago  # noqa: E501

        :return: The mean_30_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """
        return self._mean_30_days_ago
        
    @property
    def mean_30_days_ago_dict(self):
        """Gets the mean_30_days_ago of this ZacksEPSEstimate.  # noqa: E501

        The long term growth mean estimate - 30 Days Ago as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mean_30_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.mean_30_days_ago
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
            result = { 'mean_30_days_ago': value }

        
        return result
        

    @mean_30_days_ago.setter
    def mean_30_days_ago(self, mean_30_days_ago):
        """Sets the mean_30_days_ago of this ZacksEPSEstimate.

        The long term growth mean estimate - 30 Days Ago  # noqa: E501

        :param mean_30_days_ago: The mean_30_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :type: float
        """

        self._mean_30_days_ago = mean_30_days_ago

    @property
    def mean_60_days_ago(self):
        """Gets the mean_60_days_ago of this ZacksEPSEstimate.  # noqa: E501

        The long term growth mean estimate - 60 Days Ago  # noqa: E501

        :return: The mean_60_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """
        return self._mean_60_days_ago
        
    @property
    def mean_60_days_ago_dict(self):
        """Gets the mean_60_days_ago of this ZacksEPSEstimate.  # noqa: E501

        The long term growth mean estimate - 60 Days Ago as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mean_60_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.mean_60_days_ago
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
            result = { 'mean_60_days_ago': value }

        
        return result
        

    @mean_60_days_ago.setter
    def mean_60_days_ago(self, mean_60_days_ago):
        """Sets the mean_60_days_ago of this ZacksEPSEstimate.

        The long term growth mean estimate - 60 Days Ago  # noqa: E501

        :param mean_60_days_ago: The mean_60_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :type: float
        """

        self._mean_60_days_ago = mean_60_days_ago

    @property
    def mean_90_days_ago(self):
        """Gets the mean_90_days_ago of this ZacksEPSEstimate.  # noqa: E501

        The long term growth mean estimate - 90 Days Ago  # noqa: E501

        :return: The mean_90_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """
        return self._mean_90_days_ago
        
    @property
    def mean_90_days_ago_dict(self):
        """Gets the mean_90_days_ago of this ZacksEPSEstimate.  # noqa: E501

        The long term growth mean estimate - 90 Days Ago as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mean_90_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.mean_90_days_ago
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
            result = { 'mean_90_days_ago': value }

        
        return result
        

    @mean_90_days_ago.setter
    def mean_90_days_ago(self, mean_90_days_ago):
        """Sets the mean_90_days_ago of this ZacksEPSEstimate.

        The long term growth mean estimate - 90 Days Ago  # noqa: E501

        :param mean_90_days_ago: The mean_90_days_ago of this ZacksEPSEstimate.  # noqa: E501
        :type: float
        """

        self._mean_90_days_ago = mean_90_days_ago

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
        if not isinstance(other, ZacksEPSEstimate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
