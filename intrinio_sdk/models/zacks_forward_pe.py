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


class ZacksForwardPE(object):
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
        'forward_pe_year1': 'float',
        'forward_pe_year2': 'float',
        'forward_pe_year3': 'float',
        'forward_pe_year4': 'float',
        'forward_pe_year5': 'float',
        'forward_peg_ratio_year1': 'float',
        'last_ttm_eps': 'float'
    }

    attribute_map = {
        'ticker': 'ticker',
        'company_name': 'company_name',
        'forward_pe_year1': 'forward_pe_year1',
        'forward_pe_year2': 'forward_pe_year2',
        'forward_pe_year3': 'forward_pe_year3',
        'forward_pe_year4': 'forward_pe_year4',
        'forward_pe_year5': 'forward_pe_year5',
        'forward_peg_ratio_year1': 'forward_peg_ratio_year1',
        'last_ttm_eps': 'last_ttm_eps'
    }

    def __init__(self, ticker=None, company_name=None, forward_pe_year1=None, forward_pe_year2=None, forward_pe_year3=None, forward_pe_year4=None, forward_pe_year5=None, forward_peg_ratio_year1=None, last_ttm_eps=None):  # noqa: E501
        """ZacksForwardPE - a model defined in Swagger"""  # noqa: E501

        self._ticker = None
        self._company_name = None
        self._forward_pe_year1 = None
        self._forward_pe_year2 = None
        self._forward_pe_year3 = None
        self._forward_pe_year4 = None
        self._forward_pe_year5 = None
        self._forward_peg_ratio_year1 = None
        self._last_ttm_eps = None
        self.discriminator = None

        if ticker is not None:
            self.ticker = ticker
        if company_name is not None:
            self.company_name = company_name
        if forward_pe_year1 is not None:
            self.forward_pe_year1 = forward_pe_year1
        if forward_pe_year2 is not None:
            self.forward_pe_year2 = forward_pe_year2
        if forward_pe_year3 is not None:
            self.forward_pe_year3 = forward_pe_year3
        if forward_pe_year4 is not None:
            self.forward_pe_year4 = forward_pe_year4
        if forward_pe_year5 is not None:
            self.forward_pe_year5 = forward_pe_year5
        if forward_peg_ratio_year1 is not None:
            self.forward_peg_ratio_year1 = forward_peg_ratio_year1
        if last_ttm_eps is not None:
            self.last_ttm_eps = last_ttm_eps

    @property
    def ticker(self):
        """Gets the ticker of this ZacksForwardPE.  # noqa: E501

        The Zacks common exchange ticker  # noqa: E501

        :return: The ticker of this ZacksForwardPE.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this ZacksForwardPE.  # noqa: E501

        The Zacks common exchange ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this ZacksForwardPE.  # noqa: E501
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
        """Sets the ticker of this ZacksForwardPE.

        The Zacks common exchange ticker  # noqa: E501

        :param ticker: The ticker of this ZacksForwardPE.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def company_name(self):
        """Gets the company_name of this ZacksForwardPE.  # noqa: E501

        The company name  # noqa: E501

        :return: The company_name of this ZacksForwardPE.  # noqa: E501
        :rtype: str
        """
        return self._company_name
        
    @property
    def company_name_dict(self):
        """Gets the company_name of this ZacksForwardPE.  # noqa: E501

        The company name as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The company_name of this ZacksForwardPE.  # noqa: E501
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
        """Sets the company_name of this ZacksForwardPE.

        The company name  # noqa: E501

        :param company_name: The company_name of this ZacksForwardPE.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def forward_pe_year1(self):
        """Gets the forward_pe_year1 of this ZacksForwardPE.  # noqa: E501

        The forward PE estimate for the first year  # noqa: E501

        :return: The forward_pe_year1 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """
        return self._forward_pe_year1
        
    @property
    def forward_pe_year1_dict(self):
        """Gets the forward_pe_year1 of this ZacksForwardPE.  # noqa: E501

        The forward PE estimate for the first year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The forward_pe_year1 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.forward_pe_year1
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
            result = { 'forward_pe_year1': value }

        
        return result
        

    @forward_pe_year1.setter
    def forward_pe_year1(self, forward_pe_year1):
        """Sets the forward_pe_year1 of this ZacksForwardPE.

        The forward PE estimate for the first year  # noqa: E501

        :param forward_pe_year1: The forward_pe_year1 of this ZacksForwardPE.  # noqa: E501
        :type: float
        """

        self._forward_pe_year1 = forward_pe_year1

    @property
    def forward_pe_year2(self):
        """Gets the forward_pe_year2 of this ZacksForwardPE.  # noqa: E501

        The forward PE estimate for the second year  # noqa: E501

        :return: The forward_pe_year2 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """
        return self._forward_pe_year2
        
    @property
    def forward_pe_year2_dict(self):
        """Gets the forward_pe_year2 of this ZacksForwardPE.  # noqa: E501

        The forward PE estimate for the second year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The forward_pe_year2 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.forward_pe_year2
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
            result = { 'forward_pe_year2': value }

        
        return result
        

    @forward_pe_year2.setter
    def forward_pe_year2(self, forward_pe_year2):
        """Sets the forward_pe_year2 of this ZacksForwardPE.

        The forward PE estimate for the second year  # noqa: E501

        :param forward_pe_year2: The forward_pe_year2 of this ZacksForwardPE.  # noqa: E501
        :type: float
        """

        self._forward_pe_year2 = forward_pe_year2

    @property
    def forward_pe_year3(self):
        """Gets the forward_pe_year3 of this ZacksForwardPE.  # noqa: E501

        The forward PE estimate for the third year  # noqa: E501

        :return: The forward_pe_year3 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """
        return self._forward_pe_year3
        
    @property
    def forward_pe_year3_dict(self):
        """Gets the forward_pe_year3 of this ZacksForwardPE.  # noqa: E501

        The forward PE estimate for the third year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The forward_pe_year3 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.forward_pe_year3
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
            result = { 'forward_pe_year3': value }

        
        return result
        

    @forward_pe_year3.setter
    def forward_pe_year3(self, forward_pe_year3):
        """Sets the forward_pe_year3 of this ZacksForwardPE.

        The forward PE estimate for the third year  # noqa: E501

        :param forward_pe_year3: The forward_pe_year3 of this ZacksForwardPE.  # noqa: E501
        :type: float
        """

        self._forward_pe_year3 = forward_pe_year3

    @property
    def forward_pe_year4(self):
        """Gets the forward_pe_year4 of this ZacksForwardPE.  # noqa: E501

        The forward PE estimate for the fourth year  # noqa: E501

        :return: The forward_pe_year4 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """
        return self._forward_pe_year4
        
    @property
    def forward_pe_year4_dict(self):
        """Gets the forward_pe_year4 of this ZacksForwardPE.  # noqa: E501

        The forward PE estimate for the fourth year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The forward_pe_year4 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.forward_pe_year4
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
            result = { 'forward_pe_year4': value }

        
        return result
        

    @forward_pe_year4.setter
    def forward_pe_year4(self, forward_pe_year4):
        """Sets the forward_pe_year4 of this ZacksForwardPE.

        The forward PE estimate for the fourth year  # noqa: E501

        :param forward_pe_year4: The forward_pe_year4 of this ZacksForwardPE.  # noqa: E501
        :type: float
        """

        self._forward_pe_year4 = forward_pe_year4

    @property
    def forward_pe_year5(self):
        """Gets the forward_pe_year5 of this ZacksForwardPE.  # noqa: E501

        The forward PE estimate for the fifth year  # noqa: E501

        :return: The forward_pe_year5 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """
        return self._forward_pe_year5
        
    @property
    def forward_pe_year5_dict(self):
        """Gets the forward_pe_year5 of this ZacksForwardPE.  # noqa: E501

        The forward PE estimate for the fifth year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The forward_pe_year5 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.forward_pe_year5
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
            result = { 'forward_pe_year5': value }

        
        return result
        

    @forward_pe_year5.setter
    def forward_pe_year5(self, forward_pe_year5):
        """Sets the forward_pe_year5 of this ZacksForwardPE.

        The forward PE estimate for the fifth year  # noqa: E501

        :param forward_pe_year5: The forward_pe_year5 of this ZacksForwardPE.  # noqa: E501
        :type: float
        """

        self._forward_pe_year5 = forward_pe_year5

    @property
    def forward_peg_ratio_year1(self):
        """Gets the forward_peg_ratio_year1 of this ZacksForwardPE.  # noqa: E501

        The forward PEG ratio for the first year  # noqa: E501

        :return: The forward_peg_ratio_year1 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """
        return self._forward_peg_ratio_year1
        
    @property
    def forward_peg_ratio_year1_dict(self):
        """Gets the forward_peg_ratio_year1 of this ZacksForwardPE.  # noqa: E501

        The forward PEG ratio for the first year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The forward_peg_ratio_year1 of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.forward_peg_ratio_year1
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
            result = { 'forward_peg_ratio_year1': value }

        
        return result
        

    @forward_peg_ratio_year1.setter
    def forward_peg_ratio_year1(self, forward_peg_ratio_year1):
        """Sets the forward_peg_ratio_year1 of this ZacksForwardPE.

        The forward PEG ratio for the first year  # noqa: E501

        :param forward_peg_ratio_year1: The forward_peg_ratio_year1 of this ZacksForwardPE.  # noqa: E501
        :type: float
        """

        self._forward_peg_ratio_year1 = forward_peg_ratio_year1

    @property
    def last_ttm_eps(self):
        """Gets the last_ttm_eps of this ZacksForwardPE.  # noqa: E501

        Trailing twelve months earnings per share  # noqa: E501

        :return: The last_ttm_eps of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """
        return self._last_ttm_eps
        
    @property
    def last_ttm_eps_dict(self):
        """Gets the last_ttm_eps of this ZacksForwardPE.  # noqa: E501

        Trailing twelve months earnings per share as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_ttm_eps of this ZacksForwardPE.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.last_ttm_eps
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
            result = { 'last_ttm_eps': value }

        
        return result
        

    @last_ttm_eps.setter
    def last_ttm_eps(self, last_ttm_eps):
        """Sets the last_ttm_eps of this ZacksForwardPE.

        Trailing twelve months earnings per share  # noqa: E501

        :param last_ttm_eps: The last_ttm_eps of this ZacksForwardPE.  # noqa: E501
        :type: float
        """

        self._last_ttm_eps = last_ttm_eps

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
        if not isinstance(other, ZacksForwardPE):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
