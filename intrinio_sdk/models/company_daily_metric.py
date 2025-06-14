# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.103.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501


class CompanyDailyMetric(object):
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
        'date': 'datetime',
        'enterprise_value': 'float',
        'ev_to_ebit': 'float',
        'ev_to_ebitda': 'float',
        'market_cap': 'float',
        'price_to_book': 'float',
        'price_to_earnings': 'float',
        'price_to_revenue': 'float',
        'price_to_tangible_book': 'float',
        'dividend_yield': 'float',
        'earnings_yield': 'float',
        'ev_to_invested_capital': 'float',
        'ev_to_revenue': 'float',
        'ev_to_nopat': 'float',
        'ev_to_ocf': 'float',
        'ev_to_fcff': 'float',
        'company': 'CompanySummary'
    }

    attribute_map = {
        'date': 'date',
        'enterprise_value': 'enterprise_value',
        'ev_to_ebit': 'ev_to_ebit',
        'ev_to_ebitda': 'ev_to_ebitda',
        'market_cap': 'market_cap',
        'price_to_book': 'price_to_book',
        'price_to_earnings': 'price_to_earnings',
        'price_to_revenue': 'price_to_revenue',
        'price_to_tangible_book': 'price_to_tangible_book',
        'dividend_yield': 'dividend_yield',
        'earnings_yield': 'earnings_yield',
        'ev_to_invested_capital': 'ev_to_invested_capital',
        'ev_to_revenue': 'ev_to_revenue',
        'ev_to_nopat': 'ev_to_nopat',
        'ev_to_ocf': 'ev_to_ocf',
        'ev_to_fcff': 'ev_to_fcff',
        'company': 'company'
    }

    def __init__(self, date=None, enterprise_value=None, ev_to_ebit=None, ev_to_ebitda=None, market_cap=None, price_to_book=None, price_to_earnings=None, price_to_revenue=None, price_to_tangible_book=None, dividend_yield=None, earnings_yield=None, ev_to_invested_capital=None, ev_to_revenue=None, ev_to_nopat=None, ev_to_ocf=None, ev_to_fcff=None, company=None):  # noqa: E501
        """CompanyDailyMetric - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._enterprise_value = None
        self._ev_to_ebit = None
        self._ev_to_ebitda = None
        self._market_cap = None
        self._price_to_book = None
        self._price_to_earnings = None
        self._price_to_revenue = None
        self._price_to_tangible_book = None
        self._dividend_yield = None
        self._earnings_yield = None
        self._ev_to_invested_capital = None
        self._ev_to_revenue = None
        self._ev_to_nopat = None
        self._ev_to_ocf = None
        self._ev_to_fcff = None
        self._company = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if enterprise_value is not None:
            self.enterprise_value = enterprise_value
        if ev_to_ebit is not None:
            self.ev_to_ebit = ev_to_ebit
        if ev_to_ebitda is not None:
            self.ev_to_ebitda = ev_to_ebitda
        if market_cap is not None:
            self.market_cap = market_cap
        if price_to_book is not None:
            self.price_to_book = price_to_book
        if price_to_earnings is not None:
            self.price_to_earnings = price_to_earnings
        if price_to_revenue is not None:
            self.price_to_revenue = price_to_revenue
        if price_to_tangible_book is not None:
            self.price_to_tangible_book = price_to_tangible_book
        if dividend_yield is not None:
            self.dividend_yield = dividend_yield
        if earnings_yield is not None:
            self.earnings_yield = earnings_yield
        if ev_to_invested_capital is not None:
            self.ev_to_invested_capital = ev_to_invested_capital
        if ev_to_revenue is not None:
            self.ev_to_revenue = ev_to_revenue
        if ev_to_nopat is not None:
            self.ev_to_nopat = ev_to_nopat
        if ev_to_ocf is not None:
            self.ev_to_ocf = ev_to_ocf
        if ev_to_fcff is not None:
            self.ev_to_fcff = ev_to_fcff
        if company is not None:
            self.company = company

    @property
    def date(self):
        """Gets the date of this CompanyDailyMetric.  # noqa: E501

        The date of the metric  # noqa: E501

        :return: The date of this CompanyDailyMetric.  # noqa: E501
        :rtype: datetime
        """
        return self._date
        
    @property
    def date_dict(self):
        """Gets the date of this CompanyDailyMetric.  # noqa: E501

        The date of the metric as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date of this CompanyDailyMetric.  # noqa: E501
        :rtype: datetime
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
        """Sets the date of this CompanyDailyMetric.

        The date of the metric  # noqa: E501

        :param date: The date of this CompanyDailyMetric.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def enterprise_value(self):
        """Gets the enterprise_value of this CompanyDailyMetric.  # noqa: E501

        The enterprise value.  # noqa: E501

        :return: The enterprise_value of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._enterprise_value
        
    @property
    def enterprise_value_dict(self):
        """Gets the enterprise_value of this CompanyDailyMetric.  # noqa: E501

        The enterprise value. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The enterprise_value of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.enterprise_value
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
            result = { 'enterprise_value': value }

        
        return result
        

    @enterprise_value.setter
    def enterprise_value(self, enterprise_value):
        """Sets the enterprise_value of this CompanyDailyMetric.

        The enterprise value.  # noqa: E501

        :param enterprise_value: The enterprise_value of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._enterprise_value = enterprise_value

    @property
    def ev_to_ebit(self):
        """Gets the ev_to_ebit of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to earnings before interest and taxes ratio.  # noqa: E501

        :return: The ev_to_ebit of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._ev_to_ebit
        
    @property
    def ev_to_ebit_dict(self):
        """Gets the ev_to_ebit of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to earnings before interest and taxes ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ev_to_ebit of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ev_to_ebit
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
            result = { 'ev_to_ebit': value }

        
        return result
        

    @ev_to_ebit.setter
    def ev_to_ebit(self, ev_to_ebit):
        """Sets the ev_to_ebit of this CompanyDailyMetric.

        The enterprise value to earnings before interest and taxes ratio.  # noqa: E501

        :param ev_to_ebit: The ev_to_ebit of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._ev_to_ebit = ev_to_ebit

    @property
    def ev_to_ebitda(self):
        """Gets the ev_to_ebitda of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to earnings before interest, taxes, depreciation, and amoritization ratio.  # noqa: E501

        :return: The ev_to_ebitda of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._ev_to_ebitda
        
    @property
    def ev_to_ebitda_dict(self):
        """Gets the ev_to_ebitda of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to earnings before interest, taxes, depreciation, and amoritization ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ev_to_ebitda of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ev_to_ebitda
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
            result = { 'ev_to_ebitda': value }

        
        return result
        

    @ev_to_ebitda.setter
    def ev_to_ebitda(self, ev_to_ebitda):
        """Sets the ev_to_ebitda of this CompanyDailyMetric.

        The enterprise value to earnings before interest, taxes, depreciation, and amoritization ratio.  # noqa: E501

        :param ev_to_ebitda: The ev_to_ebitda of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._ev_to_ebitda = ev_to_ebitda

    @property
    def market_cap(self):
        """Gets the market_cap of this CompanyDailyMetric.  # noqa: E501

        The market cap.  # noqa: E501

        :return: The market_cap of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._market_cap
        
    @property
    def market_cap_dict(self):
        """Gets the market_cap of this CompanyDailyMetric.  # noqa: E501

        The market cap. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The market_cap of this CompanyDailyMetric.  # noqa: E501
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
        """Sets the market_cap of this CompanyDailyMetric.

        The market cap.  # noqa: E501

        :param market_cap: The market_cap of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._market_cap = market_cap

    @property
    def price_to_book(self):
        """Gets the price_to_book of this CompanyDailyMetric.  # noqa: E501

        The price to book ratio.  # noqa: E501

        :return: The price_to_book of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._price_to_book
        
    @property
    def price_to_book_dict(self):
        """Gets the price_to_book of this CompanyDailyMetric.  # noqa: E501

        The price to book ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The price_to_book of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.price_to_book
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
            result = { 'price_to_book': value }

        
        return result
        

    @price_to_book.setter
    def price_to_book(self, price_to_book):
        """Sets the price_to_book of this CompanyDailyMetric.

        The price to book ratio.  # noqa: E501

        :param price_to_book: The price_to_book of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._price_to_book = price_to_book

    @property
    def price_to_earnings(self):
        """Gets the price_to_earnings of this CompanyDailyMetric.  # noqa: E501

        The price to earnings ratio.  # noqa: E501

        :return: The price_to_earnings of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._price_to_earnings
        
    @property
    def price_to_earnings_dict(self):
        """Gets the price_to_earnings of this CompanyDailyMetric.  # noqa: E501

        The price to earnings ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The price_to_earnings of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.price_to_earnings
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
            result = { 'price_to_earnings': value }

        
        return result
        

    @price_to_earnings.setter
    def price_to_earnings(self, price_to_earnings):
        """Sets the price_to_earnings of this CompanyDailyMetric.

        The price to earnings ratio.  # noqa: E501

        :param price_to_earnings: The price_to_earnings of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._price_to_earnings = price_to_earnings

    @property
    def price_to_revenue(self):
        """Gets the price_to_revenue of this CompanyDailyMetric.  # noqa: E501

        The price to revenue ratio.  # noqa: E501

        :return: The price_to_revenue of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._price_to_revenue
        
    @property
    def price_to_revenue_dict(self):
        """Gets the price_to_revenue of this CompanyDailyMetric.  # noqa: E501

        The price to revenue ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The price_to_revenue of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.price_to_revenue
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
            result = { 'price_to_revenue': value }

        
        return result
        

    @price_to_revenue.setter
    def price_to_revenue(self, price_to_revenue):
        """Sets the price_to_revenue of this CompanyDailyMetric.

        The price to revenue ratio.  # noqa: E501

        :param price_to_revenue: The price_to_revenue of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._price_to_revenue = price_to_revenue

    @property
    def price_to_tangible_book(self):
        """Gets the price_to_tangible_book of this CompanyDailyMetric.  # noqa: E501

        The price to tangible book ratio.  # noqa: E501

        :return: The price_to_tangible_book of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._price_to_tangible_book
        
    @property
    def price_to_tangible_book_dict(self):
        """Gets the price_to_tangible_book of this CompanyDailyMetric.  # noqa: E501

        The price to tangible book ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The price_to_tangible_book of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.price_to_tangible_book
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
            result = { 'price_to_tangible_book': value }

        
        return result
        

    @price_to_tangible_book.setter
    def price_to_tangible_book(self, price_to_tangible_book):
        """Sets the price_to_tangible_book of this CompanyDailyMetric.

        The price to tangible book ratio.  # noqa: E501

        :param price_to_tangible_book: The price_to_tangible_book of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._price_to_tangible_book = price_to_tangible_book

    @property
    def dividend_yield(self):
        """Gets the dividend_yield of this CompanyDailyMetric.  # noqa: E501

        The dividend yield.  # noqa: E501

        :return: The dividend_yield of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._dividend_yield
        
    @property
    def dividend_yield_dict(self):
        """Gets the dividend_yield of this CompanyDailyMetric.  # noqa: E501

        The dividend yield. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The dividend_yield of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.dividend_yield
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
            result = { 'dividend_yield': value }

        
        return result
        

    @dividend_yield.setter
    def dividend_yield(self, dividend_yield):
        """Sets the dividend_yield of this CompanyDailyMetric.

        The dividend yield.  # noqa: E501

        :param dividend_yield: The dividend_yield of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._dividend_yield = dividend_yield

    @property
    def earnings_yield(self):
        """Gets the earnings_yield of this CompanyDailyMetric.  # noqa: E501

        The earnings yield.  # noqa: E501

        :return: The earnings_yield of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._earnings_yield
        
    @property
    def earnings_yield_dict(self):
        """Gets the earnings_yield of this CompanyDailyMetric.  # noqa: E501

        The earnings yield. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The earnings_yield of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.earnings_yield
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
            result = { 'earnings_yield': value }

        
        return result
        

    @earnings_yield.setter
    def earnings_yield(self, earnings_yield):
        """Sets the earnings_yield of this CompanyDailyMetric.

        The earnings yield.  # noqa: E501

        :param earnings_yield: The earnings_yield of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._earnings_yield = earnings_yield

    @property
    def ev_to_invested_capital(self):
        """Gets the ev_to_invested_capital of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to invested capital ratio.  # noqa: E501

        :return: The ev_to_invested_capital of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._ev_to_invested_capital
        
    @property
    def ev_to_invested_capital_dict(self):
        """Gets the ev_to_invested_capital of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to invested capital ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ev_to_invested_capital of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ev_to_invested_capital
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
            result = { 'ev_to_invested_capital': value }

        
        return result
        

    @ev_to_invested_capital.setter
    def ev_to_invested_capital(self, ev_to_invested_capital):
        """Sets the ev_to_invested_capital of this CompanyDailyMetric.

        The enterprise value to invested capital ratio.  # noqa: E501

        :param ev_to_invested_capital: The ev_to_invested_capital of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._ev_to_invested_capital = ev_to_invested_capital

    @property
    def ev_to_revenue(self):
        """Gets the ev_to_revenue of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to revenue ratio.  # noqa: E501

        :return: The ev_to_revenue of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._ev_to_revenue
        
    @property
    def ev_to_revenue_dict(self):
        """Gets the ev_to_revenue of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to revenue ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ev_to_revenue of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ev_to_revenue
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
            result = { 'ev_to_revenue': value }

        
        return result
        

    @ev_to_revenue.setter
    def ev_to_revenue(self, ev_to_revenue):
        """Sets the ev_to_revenue of this CompanyDailyMetric.

        The enterprise value to revenue ratio.  # noqa: E501

        :param ev_to_revenue: The ev_to_revenue of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._ev_to_revenue = ev_to_revenue

    @property
    def ev_to_nopat(self):
        """Gets the ev_to_nopat of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to normalized operating profit after tax ratio.  # noqa: E501

        :return: The ev_to_nopat of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._ev_to_nopat
        
    @property
    def ev_to_nopat_dict(self):
        """Gets the ev_to_nopat of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to normalized operating profit after tax ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ev_to_nopat of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ev_to_nopat
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
            result = { 'ev_to_nopat': value }

        
        return result
        

    @ev_to_nopat.setter
    def ev_to_nopat(self, ev_to_nopat):
        """Sets the ev_to_nopat of this CompanyDailyMetric.

        The enterprise value to normalized operating profit after tax ratio.  # noqa: E501

        :param ev_to_nopat: The ev_to_nopat of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._ev_to_nopat = ev_to_nopat

    @property
    def ev_to_ocf(self):
        """Gets the ev_to_ocf of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to operating cash flow ratio.  # noqa: E501

        :return: The ev_to_ocf of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._ev_to_ocf
        
    @property
    def ev_to_ocf_dict(self):
        """Gets the ev_to_ocf of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to operating cash flow ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ev_to_ocf of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ev_to_ocf
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
            result = { 'ev_to_ocf': value }

        
        return result
        

    @ev_to_ocf.setter
    def ev_to_ocf(self, ev_to_ocf):
        """Sets the ev_to_ocf of this CompanyDailyMetric.

        The enterprise value to operating cash flow ratio.  # noqa: E501

        :param ev_to_ocf: The ev_to_ocf of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._ev_to_ocf = ev_to_ocf

    @property
    def ev_to_fcff(self):
        """Gets the ev_to_fcff of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to free cash flow to the firm ratio.  # noqa: E501

        :return: The ev_to_fcff of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """
        return self._ev_to_fcff
        
    @property
    def ev_to_fcff_dict(self):
        """Gets the ev_to_fcff of this CompanyDailyMetric.  # noqa: E501

        The enterprise value to free cash flow to the firm ratio. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ev_to_fcff of this CompanyDailyMetric.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ev_to_fcff
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
            result = { 'ev_to_fcff': value }

        
        return result
        

    @ev_to_fcff.setter
    def ev_to_fcff(self, ev_to_fcff):
        """Sets the ev_to_fcff of this CompanyDailyMetric.

        The enterprise value to free cash flow to the firm ratio.  # noqa: E501

        :param ev_to_fcff: The ev_to_fcff of this CompanyDailyMetric.  # noqa: E501
        :type: float
        """

        self._ev_to_fcff = ev_to_fcff

    @property
    def company(self):
        """Gets the company of this CompanyDailyMetric.  # noqa: E501


        :return: The company of this CompanyDailyMetric.  # noqa: E501
        :rtype: CompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this CompanyDailyMetric.  # noqa: E501


        :return: The company of this CompanyDailyMetric.  # noqa: E501
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
        """Sets the company of this CompanyDailyMetric.


        :param company: The company of this CompanyDailyMetric.  # noqa: E501
        :type: CompanySummary
        """

        self._company = company

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
        if not isinstance(other, CompanyDailyMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
