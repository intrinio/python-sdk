# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.28.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ZacksInstitutionalHoldingCompanyDetail(object):
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
        'name': 'str',
        'exchange': 'str',
        'shares_outstanding': 'float',
        'last_close_price': 'float',
        'last_close_date': 'date',
        'institutional_shares_held_percent': 'float',
        'institutional_shares_buy': 'float',
        'institutional_shares_sell': 'float',
        'institutional_positions_increase': 'float',
        'institutional_positions_decrease': 'float',
        'institutional_positions_unchanged': 'float',
        'institutional_positions_total': 'float'
    }

    attribute_map = {
        'ticker': 'ticker',
        'name': 'name',
        'exchange': 'exchange',
        'shares_outstanding': 'shares_outstanding',
        'last_close_price': 'last_close_price',
        'last_close_date': 'last_close_date',
        'institutional_shares_held_percent': 'institutional_shares_held_percent',
        'institutional_shares_buy': 'institutional_shares_buy',
        'institutional_shares_sell': 'institutional_shares_sell',
        'institutional_positions_increase': 'institutional_positions_increase',
        'institutional_positions_decrease': 'institutional_positions_decrease',
        'institutional_positions_unchanged': 'institutional_positions_unchanged',
        'institutional_positions_total': 'institutional_positions_total'
    }

    def __init__(self, ticker=None, name=None, exchange=None, shares_outstanding=None, last_close_price=None, last_close_date=None, institutional_shares_held_percent=None, institutional_shares_buy=None, institutional_shares_sell=None, institutional_positions_increase=None, institutional_positions_decrease=None, institutional_positions_unchanged=None, institutional_positions_total=None):  # noqa: E501
        """ZacksInstitutionalHoldingCompanyDetail - a model defined in Swagger"""  # noqa: E501

        self._ticker = None
        self._name = None
        self._exchange = None
        self._shares_outstanding = None
        self._last_close_price = None
        self._last_close_date = None
        self._institutional_shares_held_percent = None
        self._institutional_shares_buy = None
        self._institutional_shares_sell = None
        self._institutional_positions_increase = None
        self._institutional_positions_decrease = None
        self._institutional_positions_unchanged = None
        self._institutional_positions_total = None
        self.discriminator = None

        if ticker is not None:
            self.ticker = ticker
        if name is not None:
            self.name = name
        if exchange is not None:
            self.exchange = exchange
        if shares_outstanding is not None:
            self.shares_outstanding = shares_outstanding
        if last_close_price is not None:
            self.last_close_price = last_close_price
        if last_close_date is not None:
            self.last_close_date = last_close_date
        if institutional_shares_held_percent is not None:
            self.institutional_shares_held_percent = institutional_shares_held_percent
        if institutional_shares_buy is not None:
            self.institutional_shares_buy = institutional_shares_buy
        if institutional_shares_sell is not None:
            self.institutional_shares_sell = institutional_shares_sell
        if institutional_positions_increase is not None:
            self.institutional_positions_increase = institutional_positions_increase
        if institutional_positions_decrease is not None:
            self.institutional_positions_decrease = institutional_positions_decrease
        if institutional_positions_unchanged is not None:
            self.institutional_positions_unchanged = institutional_positions_unchanged
        if institutional_positions_total is not None:
            self.institutional_positions_total = institutional_positions_total

    @property
    def ticker(self):
        """Gets the ticker of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        The Zacks common exchange ticker  # noqa: E501

        :return: The ticker of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        The Zacks common exchange ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
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
        """Sets the ticker of this ZacksInstitutionalHoldingCompanyDetail.

        The Zacks common exchange ticker  # noqa: E501

        :param ticker: The ticker of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def name(self):
        """Gets the name of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        The company name of the stock listed  # noqa: E501

        :return: The name of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        The company name of the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
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
        """Sets the name of this ZacksInstitutionalHoldingCompanyDetail.

        The company name of the stock listed  # noqa: E501

        :param name: The name of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def exchange(self):
        """Gets the exchange of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Exhange where the stock is traded whose shares are held by the institution  # noqa: E501

        :return: The exchange of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: str
        """
        return self._exchange
        
    @property
    def exchange_dict(self):
        """Gets the exchange of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Exhange where the stock is traded whose shares are held by the institution as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The exchange of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.exchange
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
            result = { 'exchange': value }

        
        return result
        

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this ZacksInstitutionalHoldingCompanyDetail.

        Exhange where the stock is traded whose shares are held by the institution  # noqa: E501

        :param exchange: The exchange of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def shares_outstanding(self):
        """Gets the shares_outstanding of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        The number of shares shares outstanding for the stock  # noqa: E501

        :return: The shares_outstanding of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """
        return self._shares_outstanding
        
    @property
    def shares_outstanding_dict(self):
        """Gets the shares_outstanding of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        The number of shares shares outstanding for the stock as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shares_outstanding of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
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
        """Sets the shares_outstanding of this ZacksInstitutionalHoldingCompanyDetail.

        The number of shares shares outstanding for the stock  # noqa: E501

        :param shares_outstanding: The shares_outstanding of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: float
        """

        self._shares_outstanding = shares_outstanding

    @property
    def last_close_price(self):
        """Gets the last_close_price of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        The last close price of the stock listed  # noqa: E501

        :return: The last_close_price of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """
        return self._last_close_price
        
    @property
    def last_close_price_dict(self):
        """Gets the last_close_price of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        The last close price of the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_close_price of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.last_close_price
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
            result = { 'last_close_price': value }

        
        return result
        

    @last_close_price.setter
    def last_close_price(self, last_close_price):
        """Sets the last_close_price of this ZacksInstitutionalHoldingCompanyDetail.

        The last close price of the stock listed  # noqa: E501

        :param last_close_price: The last_close_price of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: float
        """

        self._last_close_price = last_close_price

    @property
    def last_close_date(self):
        """Gets the last_close_date of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Last closing price of the stock listed  # noqa: E501

        :return: The last_close_date of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: date
        """
        return self._last_close_date
        
    @property
    def last_close_date_dict(self):
        """Gets the last_close_date of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Last closing price of the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_close_date of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.last_close_date
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
            result = { 'last_close_date': value }

        
        return result
        

    @last_close_date.setter
    def last_close_date(self, last_close_date):
        """Sets the last_close_date of this ZacksInstitutionalHoldingCompanyDetail.

        Last closing price of the stock listed  # noqa: E501

        :param last_close_date: The last_close_date of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: date
        """

        self._last_close_date = last_close_date

    @property
    def institutional_shares_held_percent(self):
        """Gets the institutional_shares_held_percent of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Percentage of shares outstanding held by institutions in the stock listed  # noqa: E501

        :return: The institutional_shares_held_percent of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """
        return self._institutional_shares_held_percent
        
    @property
    def institutional_shares_held_percent_dict(self):
        """Gets the institutional_shares_held_percent of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Percentage of shares outstanding held by institutions in the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The institutional_shares_held_percent of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.institutional_shares_held_percent
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
            result = { 'institutional_shares_held_percent': value }

        
        return result
        

    @institutional_shares_held_percent.setter
    def institutional_shares_held_percent(self, institutional_shares_held_percent):
        """Sets the institutional_shares_held_percent of this ZacksInstitutionalHoldingCompanyDetail.

        Percentage of shares outstanding held by institutions in the stock listed  # noqa: E501

        :param institutional_shares_held_percent: The institutional_shares_held_percent of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: float
        """

        self._institutional_shares_held_percent = institutional_shares_held_percent

    @property
    def institutional_shares_buy(self):
        """Gets the institutional_shares_buy of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Number of shares bought by institutions in the stock listed  # noqa: E501

        :return: The institutional_shares_buy of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """
        return self._institutional_shares_buy
        
    @property
    def institutional_shares_buy_dict(self):
        """Gets the institutional_shares_buy of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Number of shares bought by institutions in the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The institutional_shares_buy of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.institutional_shares_buy
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
            result = { 'institutional_shares_buy': value }

        
        return result
        

    @institutional_shares_buy.setter
    def institutional_shares_buy(self, institutional_shares_buy):
        """Sets the institutional_shares_buy of this ZacksInstitutionalHoldingCompanyDetail.

        Number of shares bought by institutions in the stock listed  # noqa: E501

        :param institutional_shares_buy: The institutional_shares_buy of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: float
        """

        self._institutional_shares_buy = institutional_shares_buy

    @property
    def institutional_shares_sell(self):
        """Gets the institutional_shares_sell of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Number of shares sold by institutions in the stock listed  # noqa: E501

        :return: The institutional_shares_sell of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """
        return self._institutional_shares_sell
        
    @property
    def institutional_shares_sell_dict(self):
        """Gets the institutional_shares_sell of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Number of shares sold by institutions in the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The institutional_shares_sell of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.institutional_shares_sell
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
            result = { 'institutional_shares_sell': value }

        
        return result
        

    @institutional_shares_sell.setter
    def institutional_shares_sell(self, institutional_shares_sell):
        """Sets the institutional_shares_sell of this ZacksInstitutionalHoldingCompanyDetail.

        Number of shares sold by institutions in the stock listed  # noqa: E501

        :param institutional_shares_sell: The institutional_shares_sell of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: float
        """

        self._institutional_shares_sell = institutional_shares_sell

    @property
    def institutional_positions_increase(self):
        """Gets the institutional_positions_increase of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Number of institutions who increased their shares held in the stock listed  # noqa: E501

        :return: The institutional_positions_increase of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """
        return self._institutional_positions_increase
        
    @property
    def institutional_positions_increase_dict(self):
        """Gets the institutional_positions_increase of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Number of institutions who increased their shares held in the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The institutional_positions_increase of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.institutional_positions_increase
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
            result = { 'institutional_positions_increase': value }

        
        return result
        

    @institutional_positions_increase.setter
    def institutional_positions_increase(self, institutional_positions_increase):
        """Sets the institutional_positions_increase of this ZacksInstitutionalHoldingCompanyDetail.

        Number of institutions who increased their shares held in the stock listed  # noqa: E501

        :param institutional_positions_increase: The institutional_positions_increase of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: float
        """

        self._institutional_positions_increase = institutional_positions_increase

    @property
    def institutional_positions_decrease(self):
        """Gets the institutional_positions_decrease of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Number of institutions who decrease their shares held in the stock listed  # noqa: E501

        :return: The institutional_positions_decrease of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """
        return self._institutional_positions_decrease
        
    @property
    def institutional_positions_decrease_dict(self):
        """Gets the institutional_positions_decrease of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Number of institutions who decrease their shares held in the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The institutional_positions_decrease of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.institutional_positions_decrease
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
            result = { 'institutional_positions_decrease': value }

        
        return result
        

    @institutional_positions_decrease.setter
    def institutional_positions_decrease(self, institutional_positions_decrease):
        """Sets the institutional_positions_decrease of this ZacksInstitutionalHoldingCompanyDetail.

        Number of institutions who decrease their shares held in the stock listed  # noqa: E501

        :param institutional_positions_decrease: The institutional_positions_decrease of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: float
        """

        self._institutional_positions_decrease = institutional_positions_decrease

    @property
    def institutional_positions_unchanged(self):
        """Gets the institutional_positions_unchanged of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Number of institutions who did not change their shares held in the stock listed  # noqa: E501

        :return: The institutional_positions_unchanged of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """
        return self._institutional_positions_unchanged
        
    @property
    def institutional_positions_unchanged_dict(self):
        """Gets the institutional_positions_unchanged of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Number of institutions who did not change their shares held in the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The institutional_positions_unchanged of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.institutional_positions_unchanged
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
            result = { 'institutional_positions_unchanged': value }

        
        return result
        

    @institutional_positions_unchanged.setter
    def institutional_positions_unchanged(self, institutional_positions_unchanged):
        """Sets the institutional_positions_unchanged of this ZacksInstitutionalHoldingCompanyDetail.

        Number of institutions who did not change their shares held in the stock listed  # noqa: E501

        :param institutional_positions_unchanged: The institutional_positions_unchanged of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: float
        """

        self._institutional_positions_unchanged = institutional_positions_unchanged

    @property
    def institutional_positions_total(self):
        """Gets the institutional_positions_total of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Total number of institutions who hold shares in the stock listed  # noqa: E501

        :return: The institutional_positions_total of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """
        return self._institutional_positions_total
        
    @property
    def institutional_positions_total_dict(self):
        """Gets the institutional_positions_total of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501

        Total number of institutions who hold shares in the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The institutional_positions_total of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.institutional_positions_total
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
            result = { 'institutional_positions_total': value }

        
        return result
        

    @institutional_positions_total.setter
    def institutional_positions_total(self, institutional_positions_total):
        """Sets the institutional_positions_total of this ZacksInstitutionalHoldingCompanyDetail.

        Total number of institutions who hold shares in the stock listed  # noqa: E501

        :param institutional_positions_total: The institutional_positions_total of this ZacksInstitutionalHoldingCompanyDetail.  # noqa: E501
        :type: float
        """

        self._institutional_positions_total = institutional_positions_total

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
        if not isinstance(other, ZacksInstitutionalHoldingCompanyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
