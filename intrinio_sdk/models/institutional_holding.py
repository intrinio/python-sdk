# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.25.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InstitutionalHolding(object):
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
        'cusip': 'str',
        'ticker': 'str',
        'security_name': 'str',
        'security_type': 'str',
        'title_of_class': 'str',
        'stock_exchange': 'str',
        'filing_date': 'date',
        'value': 'float',
        'amount': 'float',
        'type': 'str',
        'investment_discretion': 'str',
        'other_manager': 'str',
        'sole_voting_authority': 'float',
        'shared_voting_authority': 'float',
        'no_voting_authority': 'float'
    }

    attribute_map = {
        'cusip': 'cusip',
        'ticker': 'ticker',
        'security_name': 'security_name',
        'security_type': 'security_type',
        'title_of_class': 'title_of_class',
        'stock_exchange': 'stock_exchange',
        'filing_date': 'filing_date',
        'value': 'value',
        'amount': 'amount',
        'type': 'type',
        'investment_discretion': 'investment_discretion',
        'other_manager': 'other_manager',
        'sole_voting_authority': 'sole_voting_authority',
        'shared_voting_authority': 'shared_voting_authority',
        'no_voting_authority': 'no_voting_authority'
    }

    def __init__(self, cusip=None, ticker=None, security_name=None, security_type=None, title_of_class=None, stock_exchange=None, filing_date=None, value=None, amount=None, type=None, investment_discretion=None, other_manager=None, sole_voting_authority=None, shared_voting_authority=None, no_voting_authority=None):  # noqa: E501
        """InstitutionalHolding - a model defined in Swagger"""  # noqa: E501

        self._cusip = None
        self._ticker = None
        self._security_name = None
        self._security_type = None
        self._title_of_class = None
        self._stock_exchange = None
        self._filing_date = None
        self._value = None
        self._amount = None
        self._type = None
        self._investment_discretion = None
        self._other_manager = None
        self._sole_voting_authority = None
        self._shared_voting_authority = None
        self._no_voting_authority = None
        self.discriminator = None

        if cusip is not None:
            self.cusip = cusip
        if ticker is not None:
            self.ticker = ticker
        if security_name is not None:
            self.security_name = security_name
        if security_type is not None:
            self.security_type = security_type
        if title_of_class is not None:
            self.title_of_class = title_of_class
        if stock_exchange is not None:
            self.stock_exchange = stock_exchange
        if filing_date is not None:
            self.filing_date = filing_date
        if value is not None:
            self.value = value
        if amount is not None:
            self.amount = amount
        if type is not None:
            self.type = type
        if investment_discretion is not None:
            self.investment_discretion = investment_discretion
        if other_manager is not None:
            self.other_manager = other_manager
        if sole_voting_authority is not None:
            self.sole_voting_authority = sole_voting_authority
        if shared_voting_authority is not None:
            self.shared_voting_authority = shared_voting_authority
        if no_voting_authority is not None:
            self.no_voting_authority = no_voting_authority

    @property
    def cusip(self):
        """Gets the cusip of this InstitutionalHolding.  # noqa: E501

        The CUSIP number for the security report by the Institutional Owner  # noqa: E501

        :return: The cusip of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """
        return self._cusip
        
    @property
    def cusip_dict(self):
        """Gets the cusip of this InstitutionalHolding.  # noqa: E501

        The CUSIP number for the security report by the Institutional Owner as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The cusip of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.cusip
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
            result = { 'cusip': value }

        
        return result
        

    @cusip.setter
    def cusip(self, cusip):
        """Sets the cusip of this InstitutionalHolding.

        The CUSIP number for the security report by the Institutional Owner  # noqa: E501

        :param cusip: The cusip of this InstitutionalHolding.  # noqa: E501
        :type: str
        """

        self._cusip = cusip

    @property
    def ticker(self):
        """Gets the ticker of this InstitutionalHolding.  # noqa: E501

        The ticker symbol for the security  # noqa: E501

        :return: The ticker of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this InstitutionalHolding.  # noqa: E501

        The ticker symbol for the security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this InstitutionalHolding.  # noqa: E501
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
        """Sets the ticker of this InstitutionalHolding.

        The ticker symbol for the security  # noqa: E501

        :param ticker: The ticker of this InstitutionalHolding.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def security_name(self):
        """Gets the security_name of this InstitutionalHolding.  # noqa: E501

        The name of the security  # noqa: E501

        :return: The security_name of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """
        return self._security_name
        
    @property
    def security_name_dict(self):
        """Gets the security_name of this InstitutionalHolding.  # noqa: E501

        The name of the security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The security_name of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.security_name
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
            result = { 'security_name': value }

        
        return result
        

    @security_name.setter
    def security_name(self, security_name):
        """Sets the security_name of this InstitutionalHolding.

        The name of the security  # noqa: E501

        :param security_name: The security_name of this InstitutionalHolding.  # noqa: E501
        :type: str
        """

        self._security_name = security_name

    @property
    def security_type(self):
        """Gets the security_type of this InstitutionalHolding.  # noqa: E501

        The type of the security  # noqa: E501

        :return: The security_type of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """
        return self._security_type
        
    @property
    def security_type_dict(self):
        """Gets the security_type of this InstitutionalHolding.  # noqa: E501

        The type of the security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The security_type of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.security_type
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
            result = { 'security_type': value }

        
        return result
        

    @security_type.setter
    def security_type(self, security_type):
        """Sets the security_type of this InstitutionalHolding.

        The type of the security  # noqa: E501

        :param security_type: The security_type of this InstitutionalHolding.  # noqa: E501
        :type: str
        """

        self._security_type = security_type

    @property
    def title_of_class(self):
        """Gets the title_of_class of this InstitutionalHolding.  # noqa: E501

        The class of stock held  # noqa: E501

        :return: The title_of_class of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """
        return self._title_of_class
        
    @property
    def title_of_class_dict(self):
        """Gets the title_of_class of this InstitutionalHolding.  # noqa: E501

        The class of stock held as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The title_of_class of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.title_of_class
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
            result = { 'title_of_class': value }

        
        return result
        

    @title_of_class.setter
    def title_of_class(self, title_of_class):
        """Sets the title_of_class of this InstitutionalHolding.

        The class of stock held  # noqa: E501

        :param title_of_class: The title_of_class of this InstitutionalHolding.  # noqa: E501
        :type: str
        """

        self._title_of_class = title_of_class

    @property
    def stock_exchange(self):
        """Gets the stock_exchange of this InstitutionalHolding.  # noqa: E501

        The stock exchange where the security is traded  # noqa: E501

        :return: The stock_exchange of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """
        return self._stock_exchange
        
    @property
    def stock_exchange_dict(self):
        """Gets the stock_exchange of this InstitutionalHolding.  # noqa: E501

        The stock exchange where the security is traded as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The stock_exchange of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.stock_exchange
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
            result = { 'stock_exchange': value }

        
        return result
        

    @stock_exchange.setter
    def stock_exchange(self, stock_exchange):
        """Sets the stock_exchange of this InstitutionalHolding.

        The stock exchange where the security is traded  # noqa: E501

        :param stock_exchange: The stock_exchange of this InstitutionalHolding.  # noqa: E501
        :type: str
        """

        self._stock_exchange = stock_exchange

    @property
    def filing_date(self):
        """Gets the filing_date of this InstitutionalHolding.  # noqa: E501

        The date when the filing was submitted to the SEC by the company  # noqa: E501

        :return: The filing_date of this InstitutionalHolding.  # noqa: E501
        :rtype: date
        """
        return self._filing_date
        
    @property
    def filing_date_dict(self):
        """Gets the filing_date of this InstitutionalHolding.  # noqa: E501

        The date when the filing was submitted to the SEC by the company as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The filing_date of this InstitutionalHolding.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.filing_date
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
            result = { 'filing_date': value }

        
        return result
        

    @filing_date.setter
    def filing_date(self, filing_date):
        """Sets the filing_date of this InstitutionalHolding.

        The date when the filing was submitted to the SEC by the company  # noqa: E501

        :param filing_date: The filing_date of this InstitutionalHolding.  # noqa: E501
        :type: date
        """

        self._filing_date = filing_date

    @property
    def value(self):
        """Gets the value of this InstitutionalHolding.  # noqa: E501

        The market value in amount of dollars of the holding in the listed security  # noqa: E501

        :return: The value of this InstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._value
        
    @property
    def value_dict(self):
        """Gets the value of this InstitutionalHolding.  # noqa: E501

        The market value in amount of dollars of the holding in the listed security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The value of this InstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.value
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
            result = { 'value': value }

        
        return result
        

    @value.setter
    def value(self, value):
        """Sets the value of this InstitutionalHolding.

        The market value in amount of dollars of the holding in the listed security  # noqa: E501

        :param value: The value of this InstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def amount(self):
        """Gets the amount of this InstitutionalHolding.  # noqa: E501

        The number of shares held in the listed security  # noqa: E501

        :return: The amount of this InstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._amount
        
    @property
    def amount_dict(self):
        """Gets the amount of this InstitutionalHolding.  # noqa: E501

        The number of shares held in the listed security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The amount of this InstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.amount
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
            result = { 'amount': value }

        
        return result
        

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InstitutionalHolding.

        The number of shares held in the listed security  # noqa: E501

        :param amount: The amount of this InstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def type(self):
        """Gets the type of this InstitutionalHolding.  # noqa: E501

        Shares  # noqa: E501

        :return: The type of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """
        return self._type
        
    @property
    def type_dict(self):
        """Gets the type of this InstitutionalHolding.  # noqa: E501

        Shares as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The type of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.type
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
            result = { 'type': value }

        
        return result
        

    @type.setter
    def type(self, type):
        """Sets the type of this InstitutionalHolding.

        Shares  # noqa: E501

        :param type: The type of this InstitutionalHolding.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def investment_discretion(self):
        """Gets the investment_discretion of this InstitutionalHolding.  # noqa: E501

        Segregate the holdings of securities of a class according to the nature of the investment discretion held by the Manager.  # noqa: E501

        :return: The investment_discretion of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """
        return self._investment_discretion
        
    @property
    def investment_discretion_dict(self):
        """Gets the investment_discretion of this InstitutionalHolding.  # noqa: E501

        Segregate the holdings of securities of a class according to the nature of the investment discretion held by the Manager. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The investment_discretion of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.investment_discretion
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
            result = { 'investment_discretion': value }

        
        return result
        

    @investment_discretion.setter
    def investment_discretion(self, investment_discretion):
        """Sets the investment_discretion of this InstitutionalHolding.

        Segregate the holdings of securities of a class according to the nature of the investment discretion held by the Manager.  # noqa: E501

        :param investment_discretion: The investment_discretion of this InstitutionalHolding.  # noqa: E501
        :type: str
        """

        self._investment_discretion = investment_discretion

    @property
    def other_manager(self):
        """Gets the other_manager of this InstitutionalHolding.  # noqa: E501

        A code for other managerial authority of the securities listed  # noqa: E501

        :return: The other_manager of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """
        return self._other_manager
        
    @property
    def other_manager_dict(self):
        """Gets the other_manager of this InstitutionalHolding.  # noqa: E501

        A code for other managerial authority of the securities listed as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The other_manager of this InstitutionalHolding.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.other_manager
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
            result = { 'other_manager': value }

        
        return result
        

    @other_manager.setter
    def other_manager(self, other_manager):
        """Sets the other_manager of this InstitutionalHolding.

        A code for other managerial authority of the securities listed  # noqa: E501

        :param other_manager: The other_manager of this InstitutionalHolding.  # noqa: E501
        :type: str
        """

        self._other_manager = other_manager

    @property
    def sole_voting_authority(self):
        """Gets the sole_voting_authority of this InstitutionalHolding.  # noqa: E501

        The number of shares where the insitutional holder has sole voting authority  # noqa: E501

        :return: The sole_voting_authority of this InstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._sole_voting_authority
        
    @property
    def sole_voting_authority_dict(self):
        """Gets the sole_voting_authority of this InstitutionalHolding.  # noqa: E501

        The number of shares where the insitutional holder has sole voting authority as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sole_voting_authority of this InstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.sole_voting_authority
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
            result = { 'sole_voting_authority': value }

        
        return result
        

    @sole_voting_authority.setter
    def sole_voting_authority(self, sole_voting_authority):
        """Sets the sole_voting_authority of this InstitutionalHolding.

        The number of shares where the insitutional holder has sole voting authority  # noqa: E501

        :param sole_voting_authority: The sole_voting_authority of this InstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._sole_voting_authority = sole_voting_authority

    @property
    def shared_voting_authority(self):
        """Gets the shared_voting_authority of this InstitutionalHolding.  # noqa: E501

        The number of shares where the insitutional holder has shared voting authority  # noqa: E501

        :return: The shared_voting_authority of this InstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._shared_voting_authority
        
    @property
    def shared_voting_authority_dict(self):
        """Gets the shared_voting_authority of this InstitutionalHolding.  # noqa: E501

        The number of shares where the insitutional holder has shared voting authority as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shared_voting_authority of this InstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.shared_voting_authority
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
            result = { 'shared_voting_authority': value }

        
        return result
        

    @shared_voting_authority.setter
    def shared_voting_authority(self, shared_voting_authority):
        """Sets the shared_voting_authority of this InstitutionalHolding.

        The number of shares where the insitutional holder has shared voting authority  # noqa: E501

        :param shared_voting_authority: The shared_voting_authority of this InstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._shared_voting_authority = shared_voting_authority

    @property
    def no_voting_authority(self):
        """Gets the no_voting_authority of this InstitutionalHolding.  # noqa: E501

        The number of shares where the insitutional holder has no voting authority  # noqa: E501

        :return: The no_voting_authority of this InstitutionalHolding.  # noqa: E501
        :rtype: float
        """
        return self._no_voting_authority
        
    @property
    def no_voting_authority_dict(self):
        """Gets the no_voting_authority of this InstitutionalHolding.  # noqa: E501

        The number of shares where the insitutional holder has no voting authority as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The no_voting_authority of this InstitutionalHolding.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.no_voting_authority
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
            result = { 'no_voting_authority': value }

        
        return result
        

    @no_voting_authority.setter
    def no_voting_authority(self, no_voting_authority):
        """Sets the no_voting_authority of this InstitutionalHolding.

        The number of shares where the insitutional holder has no voting authority  # noqa: E501

        :param no_voting_authority: The no_voting_authority of this InstitutionalHolding.  # noqa: E501
        :type: float
        """

        self._no_voting_authority = no_voting_authority

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
        if not isinstance(other, InstitutionalHolding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
