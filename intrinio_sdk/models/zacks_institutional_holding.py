# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.23.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.zacks_institutional_holding_company_summary import ZacksInstitutionalHoldingCompanySummary  # noqa: F401,E501
from intrinio_sdk.models.zacks_institutional_holding_historical_summary import ZacksInstitutionalHoldingHistoricalSummary  # noqa: F401,E501
from intrinio_sdk.models.zacks_institutional_holding_owner_summary import ZacksInstitutionalHoldingOwnerSummary  # noqa: F401,E501


class ZacksInstitutionalHolding(object):
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
        'company': 'ZacksInstitutionalHoldingCompanySummary',
        'owner': 'ZacksInstitutionalHoldingOwnerSummary',
        'as_of_date': 'date',
        'shares_held': 'float',
        'shared_held_percent': 'float',
        'shares_change': 'float',
        'shares_change_percent': 'float',
        'market_value': 'float',
        'market_value_change': 'float',
        'last_sec_filing_type': 'str',
        'last_sec_filing_date': 'date',
        'last_sec_filing_shares': 'float',
        'historical_holdings': 'list[ZacksInstitutionalHoldingHistoricalSummary]'
    }

    attribute_map = {
        'company': 'company',
        'owner': 'owner',
        'as_of_date': 'as_of_date',
        'shares_held': 'shares_held',
        'shared_held_percent': 'shared_held_percent',
        'shares_change': 'shares_change',
        'shares_change_percent': 'shares_change_percent',
        'market_value': 'market_value',
        'market_value_change': 'market_value_change',
        'last_sec_filing_type': 'last_sec_filing_type',
        'last_sec_filing_date': 'last_sec_filing_date',
        'last_sec_filing_shares': 'last_sec_filing_shares',
        'historical_holdings': 'historical_holdings'
    }

    def __init__(self, company=None, owner=None, as_of_date=None, shares_held=None, shared_held_percent=None, shares_change=None, shares_change_percent=None, market_value=None, market_value_change=None, last_sec_filing_type=None, last_sec_filing_date=None, last_sec_filing_shares=None, historical_holdings=None):  # noqa: E501
        """ZacksInstitutionalHolding - a model defined in Swagger"""  # noqa: E501

        self._company = None
        self._owner = None
        self._as_of_date = None
        self._shares_held = None
        self._shared_held_percent = None
        self._shares_change = None
        self._shares_change_percent = None
        self._market_value = None
        self._market_value_change = None
        self._last_sec_filing_type = None
        self._last_sec_filing_date = None
        self._last_sec_filing_shares = None
        self._historical_holdings = None
        self.discriminator = None

        if company is not None:
            self.company = company
        if owner is not None:
            self.owner = owner
        if as_of_date is not None:
            self.as_of_date = as_of_date
        if shares_held is not None:
            self.shares_held = shares_held
        if shared_held_percent is not None:
            self.shared_held_percent = shared_held_percent
        if shares_change is not None:
            self.shares_change = shares_change
        if shares_change_percent is not None:
            self.shares_change_percent = shares_change_percent
        if market_value is not None:
            self.market_value = market_value
        if market_value_change is not None:
            self.market_value_change = market_value_change
        if last_sec_filing_type is not None:
            self.last_sec_filing_type = last_sec_filing_type
        if last_sec_filing_date is not None:
            self.last_sec_filing_date = last_sec_filing_date
        if last_sec_filing_shares is not None:
            self.last_sec_filing_shares = last_sec_filing_shares
        if historical_holdings is not None:
            self.historical_holdings = historical_holdings

    @property
    def company(self):
        """Gets the company of this ZacksInstitutionalHolding.  # noqa: E501


        :return: The company of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: ZacksInstitutionalHoldingCompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this ZacksInstitutionalHolding.  # noqa: E501


        :return: The company of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: ZacksInstitutionalHoldingCompanySummary
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
        """Sets the company of this ZacksInstitutionalHolding.


        :param company: The company of this ZacksInstitutionalHolding.  # noqa: E501
        :type: ZacksInstitutionalHoldingCompanySummary
        """

        self._company = company

    @property
    def owner(self):
        """Gets the owner of this ZacksInstitutionalHolding.  # noqa: E501


        :return: The owner of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: ZacksInstitutionalHoldingOwnerSummary
        """
        return self._owner
        
    @property
    def owner_dict(self):
        """Gets the owner of this ZacksInstitutionalHolding.  # noqa: E501


        :return: The owner of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: ZacksInstitutionalHoldingOwnerSummary
        """

        result = None

        value = self.owner
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
            result = { 'owner': value }

        
        return result
        

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ZacksInstitutionalHolding.


        :param owner: The owner of this ZacksInstitutionalHolding.  # noqa: E501
        :type: ZacksInstitutionalHoldingOwnerSummary
        """

        self._owner = owner

    @property
    def as_of_date(self):
        """Gets the as_of_date of this ZacksInstitutionalHolding.  # noqa: E501

        Quarter end date listed in the most recent 13F report filed by the institution  # noqa: E501

        :return: The as_of_date of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: date
        """
        return self._as_of_date
        
    @property
    def as_of_date_dict(self):
        """Gets the as_of_date of this ZacksInstitutionalHolding.  # noqa: E501

        Quarter end date listed in the most recent 13F report filed by the institution as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The as_of_date of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.as_of_date
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
            result = { 'as_of_date': value }

        
        return result
        

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this ZacksInstitutionalHolding.

        Quarter end date listed in the most recent 13F report filed by the institution  # noqa: E501

        :param as_of_date: The as_of_date of this ZacksInstitutionalHolding.  # noqa: E501
        :type: date
        """

        self._as_of_date = as_of_date

    @property
    def shares_held(self):
        """Gets the shares_held of this ZacksInstitutionalHolding.  # noqa: E501

        Number of shares of the stock listed  # noqa: E501

        :return: The shares_held of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._shares_held
        
    @property
    def shares_held_dict(self):
        """Gets the shares_held of this ZacksInstitutionalHolding.  # noqa: E501

        Number of shares of the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shares_held of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.shares_held
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
            result = { 'shares_held': value }

        
        return result
        

    @shares_held.setter
    def shares_held(self, shares_held):
        """Sets the shares_held of this ZacksInstitutionalHolding.

        Number of shares of the stock listed  # noqa: E501

        :param shares_held: The shares_held of this ZacksInstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._shares_held = shares_held

    @property
    def shared_held_percent(self):
        """Gets the shared_held_percent of this ZacksInstitutionalHolding.  # noqa: E501

        Percent of shares outstanding held of the stock by the institution listed  # noqa: E501

        :return: The shared_held_percent of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._shared_held_percent
        
    @property
    def shared_held_percent_dict(self):
        """Gets the shared_held_percent of this ZacksInstitutionalHolding.  # noqa: E501

        Percent of shares outstanding held of the stock by the institution listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shared_held_percent of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.shared_held_percent
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
            result = { 'shared_held_percent': value }

        
        return result
        

    @shared_held_percent.setter
    def shared_held_percent(self, shared_held_percent):
        """Sets the shared_held_percent of this ZacksInstitutionalHolding.

        Percent of shares outstanding held of the stock by the institution listed  # noqa: E501

        :param shared_held_percent: The shared_held_percent of this ZacksInstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._shared_held_percent = shared_held_percent

    @property
    def shares_change(self):
        """Gets the shares_change of this ZacksInstitutionalHolding.  # noqa: E501

        Change in shares of the stock held by the institution listed  # noqa: E501

        :return: The shares_change of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._shares_change
        
    @property
    def shares_change_dict(self):
        """Gets the shares_change of this ZacksInstitutionalHolding.  # noqa: E501

        Change in shares of the stock held by the institution listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shares_change of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.shares_change
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
            result = { 'shares_change': value }

        
        return result
        

    @shares_change.setter
    def shares_change(self, shares_change):
        """Sets the shares_change of this ZacksInstitutionalHolding.

        Change in shares of the stock held by the institution listed  # noqa: E501

        :param shares_change: The shares_change of this ZacksInstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._shares_change = shares_change

    @property
    def shares_change_percent(self):
        """Gets the shares_change_percent of this ZacksInstitutionalHolding.  # noqa: E501

        Percentage change in shares of the stock held by the institution listed  # noqa: E501

        :return: The shares_change_percent of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._shares_change_percent
        
    @property
    def shares_change_percent_dict(self):
        """Gets the shares_change_percent of this ZacksInstitutionalHolding.  # noqa: E501

        Percentage change in shares of the stock held by the institution listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shares_change_percent of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.shares_change_percent
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
            result = { 'shares_change_percent': value }

        
        return result
        

    @shares_change_percent.setter
    def shares_change_percent(self, shares_change_percent):
        """Sets the shares_change_percent of this ZacksInstitutionalHolding.

        Percentage change in shares of the stock held by the institution listed  # noqa: E501

        :param shares_change_percent: The shares_change_percent of this ZacksInstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._shares_change_percent = shares_change_percent

    @property
    def market_value(self):
        """Gets the market_value of this ZacksInstitutionalHolding.  # noqa: E501

        Market value of shares outstanding held of the stock listed  # noqa: E501

        :return: The market_value of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._market_value
        
    @property
    def market_value_dict(self):
        """Gets the market_value of this ZacksInstitutionalHolding.  # noqa: E501

        Market value of shares outstanding held of the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The market_value of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.market_value
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
            result = { 'market_value': value }

        
        return result
        

    @market_value.setter
    def market_value(self, market_value):
        """Sets the market_value of this ZacksInstitutionalHolding.

        Market value of shares outstanding held of the stock listed  # noqa: E501

        :param market_value: The market_value of this ZacksInstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._market_value = market_value

    @property
    def market_value_change(self):
        """Gets the market_value_change of this ZacksInstitutionalHolding.  # noqa: E501

        Change in market value shares of the stock listed  # noqa: E501

        :return: The market_value_change of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._market_value_change
        
    @property
    def market_value_change_dict(self):
        """Gets the market_value_change of this ZacksInstitutionalHolding.  # noqa: E501

        Change in market value shares of the stock listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The market_value_change of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.market_value_change
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
            result = { 'market_value_change': value }

        
        return result
        

    @market_value_change.setter
    def market_value_change(self, market_value_change):
        """Sets the market_value_change of this ZacksInstitutionalHolding.

        Change in market value shares of the stock listed  # noqa: E501

        :param market_value_change: The market_value_change of this ZacksInstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._market_value_change = market_value_change

    @property
    def last_sec_filing_type(self):
        """Gets the last_sec_filing_type of this ZacksInstitutionalHolding.  # noqa: E501

        The report type of the latest SEC filing  # noqa: E501

        :return: The last_sec_filing_type of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: str
        """
        return self._last_sec_filing_type
        
    @property
    def last_sec_filing_type_dict(self):
        """Gets the last_sec_filing_type of this ZacksInstitutionalHolding.  # noqa: E501

        The report type of the latest SEC filing as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_sec_filing_type of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.last_sec_filing_type
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
            result = { 'last_sec_filing_type': value }

        
        return result
        

    @last_sec_filing_type.setter
    def last_sec_filing_type(self, last_sec_filing_type):
        """Sets the last_sec_filing_type of this ZacksInstitutionalHolding.

        The report type of the latest SEC filing  # noqa: E501

        :param last_sec_filing_type: The last_sec_filing_type of this ZacksInstitutionalHolding.  # noqa: E501
        :type: str
        """

        self._last_sec_filing_type = last_sec_filing_type

    @property
    def last_sec_filing_date(self):
        """Gets the last_sec_filing_date of this ZacksInstitutionalHolding.  # noqa: E501

        The date of the latest SEC filing  # noqa: E501

        :return: The last_sec_filing_date of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: date
        """
        return self._last_sec_filing_date
        
    @property
    def last_sec_filing_date_dict(self):
        """Gets the last_sec_filing_date of this ZacksInstitutionalHolding.  # noqa: E501

        The date of the latest SEC filing as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_sec_filing_date of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.last_sec_filing_date
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
            result = { 'last_sec_filing_date': value }

        
        return result
        

    @last_sec_filing_date.setter
    def last_sec_filing_date(self, last_sec_filing_date):
        """Sets the last_sec_filing_date of this ZacksInstitutionalHolding.

        The date of the latest SEC filing  # noqa: E501

        :param last_sec_filing_date: The last_sec_filing_date of this ZacksInstitutionalHolding.  # noqa: E501
        :type: date
        """

        self._last_sec_filing_date = last_sec_filing_date

    @property
    def last_sec_filing_shares(self):
        """Gets the last_sec_filing_shares of this ZacksInstitutionalHolding.  # noqa: E501

        The  # noqa: E501

        :return: The last_sec_filing_shares of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._last_sec_filing_shares
        
    @property
    def last_sec_filing_shares_dict(self):
        """Gets the last_sec_filing_shares of this ZacksInstitutionalHolding.  # noqa: E501

        The as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_sec_filing_shares of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.last_sec_filing_shares
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
            result = { 'last_sec_filing_shares': value }

        
        return result
        

    @last_sec_filing_shares.setter
    def last_sec_filing_shares(self, last_sec_filing_shares):
        """Sets the last_sec_filing_shares of this ZacksInstitutionalHolding.

        The  # noqa: E501

        :param last_sec_filing_shares: The last_sec_filing_shares of this ZacksInstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._last_sec_filing_shares = last_sec_filing_shares

    @property
    def historical_holdings(self):
        """Gets the historical_holdings of this ZacksInstitutionalHolding.  # noqa: E501


        :return: The historical_holdings of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: list[ZacksInstitutionalHoldingHistoricalSummary]
        """
        return self._historical_holdings
        
    @property
    def historical_holdings_dict(self):
        """Gets the historical_holdings of this ZacksInstitutionalHolding.  # noqa: E501


        :return: The historical_holdings of this ZacksInstitutionalHolding.  # noqa: E501
        :rtype: list[ZacksInstitutionalHoldingHistoricalSummary]
        """

        result = None

        value = self.historical_holdings
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
            result = { 'historical_holdings': value }

        
        return result
        

    @historical_holdings.setter
    def historical_holdings(self, historical_holdings):
        """Sets the historical_holdings of this ZacksInstitutionalHolding.


        :param historical_holdings: The historical_holdings of this ZacksInstitutionalHolding.  # noqa: E501
        :type: list[ZacksInstitutionalHoldingHistoricalSummary]
        """

        self._historical_holdings = historical_holdings

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
        if not isinstance(other, ZacksInstitutionalHolding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
