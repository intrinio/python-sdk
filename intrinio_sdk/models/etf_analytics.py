# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.48.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.etf_summary import ETFSummary  # noqa: F401,E501


class ETFAnalytics(object):
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
        'fifty_two_week_high': 'float',
        'fifty_two_week_low': 'float',
        'volume_traded': 'float',
        'average_daily_volume_one_month': 'float',
        'average_daily_volume_three_month': 'float',
        'average_daily_volume_six_month': 'float',
        'market_cap': 'float',
        'shares_outstanding': 'float',
        'etf': 'ETFSummary'
    }

    attribute_map = {
        'date': 'date',
        'fifty_two_week_high': 'fifty_two_week_high',
        'fifty_two_week_low': 'fifty_two_week_low',
        'volume_traded': 'volume_traded',
        'average_daily_volume_one_month': 'average_daily_volume_one_month',
        'average_daily_volume_three_month': 'average_daily_volume_three_month',
        'average_daily_volume_six_month': 'average_daily_volume_six_month',
        'market_cap': 'market_cap',
        'shares_outstanding': 'shares_outstanding',
        'etf': 'etf'
    }

    def __init__(self, date=None, fifty_two_week_high=None, fifty_two_week_low=None, volume_traded=None, average_daily_volume_one_month=None, average_daily_volume_three_month=None, average_daily_volume_six_month=None, market_cap=None, shares_outstanding=None, etf=None):  # noqa: E501
        """ETFAnalytics - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._fifty_two_week_high = None
        self._fifty_two_week_low = None
        self._volume_traded = None
        self._average_daily_volume_one_month = None
        self._average_daily_volume_three_month = None
        self._average_daily_volume_six_month = None
        self._market_cap = None
        self._shares_outstanding = None
        self._etf = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if fifty_two_week_high is not None:
            self.fifty_two_week_high = fifty_two_week_high
        if fifty_two_week_low is not None:
            self.fifty_two_week_low = fifty_two_week_low
        if volume_traded is not None:
            self.volume_traded = volume_traded
        if average_daily_volume_one_month is not None:
            self.average_daily_volume_one_month = average_daily_volume_one_month
        if average_daily_volume_three_month is not None:
            self.average_daily_volume_three_month = average_daily_volume_three_month
        if average_daily_volume_six_month is not None:
            self.average_daily_volume_six_month = average_daily_volume_six_month
        if market_cap is not None:
            self.market_cap = market_cap
        if shares_outstanding is not None:
            self.shares_outstanding = shares_outstanding
        if etf is not None:
            self.etf = etf

    @property
    def date(self):
        """Gets the date of this ETFAnalytics.  # noqa: E501

        The calendar date these analytics represent.  # noqa: E501

        :return: The date of this ETFAnalytics.  # noqa: E501
        :rtype: date
        """
        return self._date
        
    @property
    def date_dict(self):
        """Gets the date of this ETFAnalytics.  # noqa: E501

        The calendar date these analytics represent. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date of this ETFAnalytics.  # noqa: E501
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
        """Sets the date of this ETFAnalytics.

        The calendar date these analytics represent.  # noqa: E501

        :param date: The date of this ETFAnalytics.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def fifty_two_week_high(self):
        """Gets the fifty_two_week_high of this ETFAnalytics.  # noqa: E501

        Highest trading price for the security in the preceding 52 weeks  # noqa: E501

        :return: The fifty_two_week_high of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._fifty_two_week_high
        
    @property
    def fifty_two_week_high_dict(self):
        """Gets the fifty_two_week_high of this ETFAnalytics.  # noqa: E501

        Highest trading price for the security in the preceding 52 weeks as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The fifty_two_week_high of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.fifty_two_week_high
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
            result = { 'fifty_two_week_high': value }

        
        return result
        

    @fifty_two_week_high.setter
    def fifty_two_week_high(self, fifty_two_week_high):
        """Sets the fifty_two_week_high of this ETFAnalytics.

        Highest trading price for the security in the preceding 52 weeks  # noqa: E501

        :param fifty_two_week_high: The fifty_two_week_high of this ETFAnalytics.  # noqa: E501
        :type: float
        """

        self._fifty_two_week_high = fifty_two_week_high

    @property
    def fifty_two_week_low(self):
        """Gets the fifty_two_week_low of this ETFAnalytics.  # noqa: E501

        Lowest trading price for the security in the preceding 52 weeks  # noqa: E501

        :return: The fifty_two_week_low of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._fifty_two_week_low
        
    @property
    def fifty_two_week_low_dict(self):
        """Gets the fifty_two_week_low of this ETFAnalytics.  # noqa: E501

        Lowest trading price for the security in the preceding 52 weeks as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The fifty_two_week_low of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.fifty_two_week_low
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
            result = { 'fifty_two_week_low': value }

        
        return result
        

    @fifty_two_week_low.setter
    def fifty_two_week_low(self, fifty_two_week_low):
        """Sets the fifty_two_week_low of this ETFAnalytics.

        Lowest trading price for the security in the preceding 52 weeks  # noqa: E501

        :param fifty_two_week_low: The fifty_two_week_low of this ETFAnalytics.  # noqa: E501
        :type: float
        """

        self._fifty_two_week_low = fifty_two_week_low

    @property
    def volume_traded(self):
        """Gets the volume_traded of this ETFAnalytics.  # noqa: E501

        The total quantity of shares traded on the latest trading day  # noqa: E501

        :return: The volume_traded of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._volume_traded
        
    @property
    def volume_traded_dict(self):
        """Gets the volume_traded of this ETFAnalytics.  # noqa: E501

        The total quantity of shares traded on the latest trading day as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The volume_traded of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.volume_traded
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
            result = { 'volume_traded': value }

        
        return result
        

    @volume_traded.setter
    def volume_traded(self, volume_traded):
        """Sets the volume_traded of this ETFAnalytics.

        The total quantity of shares traded on the latest trading day  # noqa: E501

        :param volume_traded: The volume_traded of this ETFAnalytics.  # noqa: E501
        :type: float
        """

        self._volume_traded = volume_traded

    @property
    def average_daily_volume_one_month(self):
        """Gets the average_daily_volume_one_month of this ETFAnalytics.  # noqa: E501

        The average quantity of shares traded per day for the last month  # noqa: E501

        :return: The average_daily_volume_one_month of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._average_daily_volume_one_month
        
    @property
    def average_daily_volume_one_month_dict(self):
        """Gets the average_daily_volume_one_month of this ETFAnalytics.  # noqa: E501

        The average quantity of shares traded per day for the last month as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The average_daily_volume_one_month of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.average_daily_volume_one_month
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
            result = { 'average_daily_volume_one_month': value }

        
        return result
        

    @average_daily_volume_one_month.setter
    def average_daily_volume_one_month(self, average_daily_volume_one_month):
        """Sets the average_daily_volume_one_month of this ETFAnalytics.

        The average quantity of shares traded per day for the last month  # noqa: E501

        :param average_daily_volume_one_month: The average_daily_volume_one_month of this ETFAnalytics.  # noqa: E501
        :type: float
        """

        self._average_daily_volume_one_month = average_daily_volume_one_month

    @property
    def average_daily_volume_three_month(self):
        """Gets the average_daily_volume_three_month of this ETFAnalytics.  # noqa: E501

        The average quantity of shares traded per day for the last three months  # noqa: E501

        :return: The average_daily_volume_three_month of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._average_daily_volume_three_month
        
    @property
    def average_daily_volume_three_month_dict(self):
        """Gets the average_daily_volume_three_month of this ETFAnalytics.  # noqa: E501

        The average quantity of shares traded per day for the last three months as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The average_daily_volume_three_month of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.average_daily_volume_three_month
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
            result = { 'average_daily_volume_three_month': value }

        
        return result
        

    @average_daily_volume_three_month.setter
    def average_daily_volume_three_month(self, average_daily_volume_three_month):
        """Sets the average_daily_volume_three_month of this ETFAnalytics.

        The average quantity of shares traded per day for the last three months  # noqa: E501

        :param average_daily_volume_three_month: The average_daily_volume_three_month of this ETFAnalytics.  # noqa: E501
        :type: float
        """

        self._average_daily_volume_three_month = average_daily_volume_three_month

    @property
    def average_daily_volume_six_month(self):
        """Gets the average_daily_volume_six_month of this ETFAnalytics.  # noqa: E501

        The average quantity of shares traded per day for the last six months  # noqa: E501

        :return: The average_daily_volume_six_month of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._average_daily_volume_six_month
        
    @property
    def average_daily_volume_six_month_dict(self):
        """Gets the average_daily_volume_six_month of this ETFAnalytics.  # noqa: E501

        The average quantity of shares traded per day for the last six months as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The average_daily_volume_six_month of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.average_daily_volume_six_month
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
            result = { 'average_daily_volume_six_month': value }

        
        return result
        

    @average_daily_volume_six_month.setter
    def average_daily_volume_six_month(self, average_daily_volume_six_month):
        """Sets the average_daily_volume_six_month of this ETFAnalytics.

        The average quantity of shares traded per day for the last six months  # noqa: E501

        :param average_daily_volume_six_month: The average_daily_volume_six_month of this ETFAnalytics.  # noqa: E501
        :type: float
        """

        self._average_daily_volume_six_month = average_daily_volume_six_month

    @property
    def market_cap(self):
        """Gets the market_cap of this ETFAnalytics.  # noqa: E501

        The market capitalization for the Exchange Traded Fund (ETF)  # noqa: E501

        :return: The market_cap of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._market_cap
        
    @property
    def market_cap_dict(self):
        """Gets the market_cap of this ETFAnalytics.  # noqa: E501

        The market capitalization for the Exchange Traded Fund (ETF) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The market_cap of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.market_cap
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
            result = { 'market_cap': value }

        
        return result
        

    @market_cap.setter
    def market_cap(self, market_cap):
        """Sets the market_cap of this ETFAnalytics.

        The market capitalization for the Exchange Traded Fund (ETF)  # noqa: E501

        :param market_cap: The market_cap of this ETFAnalytics.  # noqa: E501
        :type: float
        """

        self._market_cap = market_cap

    @property
    def shares_outstanding(self):
        """Gets the shares_outstanding of this ETFAnalytics.  # noqa: E501

        The number of shares outstanding for the Exchange Traded Fund (ETF)  # noqa: E501

        :return: The shares_outstanding of this ETFAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._shares_outstanding
        
    @property
    def shares_outstanding_dict(self):
        """Gets the shares_outstanding of this ETFAnalytics.  # noqa: E501

        The number of shares outstanding for the Exchange Traded Fund (ETF) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shares_outstanding of this ETFAnalytics.  # noqa: E501
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
        """Sets the shares_outstanding of this ETFAnalytics.

        The number of shares outstanding for the Exchange Traded Fund (ETF)  # noqa: E501

        :param shares_outstanding: The shares_outstanding of this ETFAnalytics.  # noqa: E501
        :type: float
        """

        self._shares_outstanding = shares_outstanding

    @property
    def etf(self):
        """Gets the etf of this ETFAnalytics.  # noqa: E501


        :return: The etf of this ETFAnalytics.  # noqa: E501
        :rtype: ETFSummary
        """
        return self._etf
        
    @property
    def etf_dict(self):
        """Gets the etf of this ETFAnalytics.  # noqa: E501


        :return: The etf of this ETFAnalytics.  # noqa: E501
        :rtype: ETFSummary
        """

        result = None

        value = self.etf
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
            result = { 'etf': value }

        
        return result
        

    @etf.setter
    def etf(self, etf):
        """Sets the etf of this ETFAnalytics.


        :param etf: The etf of this ETFAnalytics.  # noqa: E501
        :type: ETFSummary
        """

        self._etf = etf

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
        if not isinstance(other, ETFAnalytics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
