# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.80.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OptionsAggregate(object):
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
        'date': 'str',
        'total_open_interest': 'int',
        'total_volume': 'int',
        'total_put_volume': 'int',
        'total_call_volume': 'int',
        'put_call_volume_ratio': 'float',
        'contract_count': 'int'
    }

    attribute_map = {
        'ticker': 'ticker',
        'date': 'date',
        'total_open_interest': 'total_open_interest',
        'total_volume': 'total_volume',
        'total_put_volume': 'total_put_volume',
        'total_call_volume': 'total_call_volume',
        'put_call_volume_ratio': 'put_call_volume_ratio',
        'contract_count': 'contract_count'
    }

    def __init__(self, ticker=None, date=None, total_open_interest=None, total_volume=None, total_put_volume=None, total_call_volume=None, put_call_volume_ratio=None, contract_count=None):  # noqa: E501
        """OptionsAggregate - a model defined in Swagger"""  # noqa: E501

        self._ticker = None
        self._date = None
        self._total_open_interest = None
        self._total_volume = None
        self._total_put_volume = None
        self._total_call_volume = None
        self._put_call_volume_ratio = None
        self._contract_count = None
        self.discriminator = None

        if ticker is not None:
            self.ticker = ticker
        if date is not None:
            self.date = date
        if total_open_interest is not None:
            self.total_open_interest = total_open_interest
        if total_volume is not None:
            self.total_volume = total_volume
        if total_put_volume is not None:
            self.total_put_volume = total_put_volume
        if total_call_volume is not None:
            self.total_call_volume = total_call_volume
        if put_call_volume_ratio is not None:
            self.put_call_volume_ratio = put_call_volume_ratio
        if contract_count is not None:
            self.contract_count = contract_count

    @property
    def ticker(self):
        """Gets the ticker of this OptionsAggregate.  # noqa: E501

        The ticker symbol of the Security for the Option.  # noqa: E501

        :return: The ticker of this OptionsAggregate.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this OptionsAggregate.  # noqa: E501

        The ticker symbol of the Security for the Option. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this OptionsAggregate.  # noqa: E501
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
        """Sets the ticker of this OptionsAggregate.

        The ticker symbol of the Security for the Option.  # noqa: E501

        :param ticker: The ticker of this OptionsAggregate.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def date(self):
        """Gets the date of this OptionsAggregate.  # noqa: E501

        The date of the data.  # noqa: E501

        :return: The date of this OptionsAggregate.  # noqa: E501
        :rtype: str
        """
        return self._date
        
    @property
    def date_dict(self):
        """Gets the date of this OptionsAggregate.  # noqa: E501

        The date of the data. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date of this OptionsAggregate.  # noqa: E501
        :rtype: str
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
        """Sets the date of this OptionsAggregate.

        The date of the data.  # noqa: E501

        :param date: The date of this OptionsAggregate.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def total_open_interest(self):
        """Gets the total_open_interest of this OptionsAggregate.  # noqa: E501

        Total open interest for the ticker  # noqa: E501

        :return: The total_open_interest of this OptionsAggregate.  # noqa: E501
        :rtype: int
        """
        return self._total_open_interest
        
    @property
    def total_open_interest_dict(self):
        """Gets the total_open_interest of this OptionsAggregate.  # noqa: E501

        Total open interest for the ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_open_interest of this OptionsAggregate.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.total_open_interest
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
            result = { 'total_open_interest': value }

        
        return result
        

    @total_open_interest.setter
    def total_open_interest(self, total_open_interest):
        """Sets the total_open_interest of this OptionsAggregate.

        Total open interest for the ticker  # noqa: E501

        :param total_open_interest: The total_open_interest of this OptionsAggregate.  # noqa: E501
        :type: int
        """

        self._total_open_interest = total_open_interest

    @property
    def total_volume(self):
        """Gets the total_volume of this OptionsAggregate.  # noqa: E501

        Total volume for the ticker  # noqa: E501

        :return: The total_volume of this OptionsAggregate.  # noqa: E501
        :rtype: int
        """
        return self._total_volume
        
    @property
    def total_volume_dict(self):
        """Gets the total_volume of this OptionsAggregate.  # noqa: E501

        Total volume for the ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_volume of this OptionsAggregate.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.total_volume
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
            result = { 'total_volume': value }

        
        return result
        

    @total_volume.setter
    def total_volume(self, total_volume):
        """Sets the total_volume of this OptionsAggregate.

        Total volume for the ticker  # noqa: E501

        :param total_volume: The total_volume of this OptionsAggregate.  # noqa: E501
        :type: int
        """

        self._total_volume = total_volume

    @property
    def total_put_volume(self):
        """Gets the total_put_volume of this OptionsAggregate.  # noqa: E501

        Total put volume for the ticker  # noqa: E501

        :return: The total_put_volume of this OptionsAggregate.  # noqa: E501
        :rtype: int
        """
        return self._total_put_volume
        
    @property
    def total_put_volume_dict(self):
        """Gets the total_put_volume of this OptionsAggregate.  # noqa: E501

        Total put volume for the ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_put_volume of this OptionsAggregate.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.total_put_volume
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
            result = { 'total_put_volume': value }

        
        return result
        

    @total_put_volume.setter
    def total_put_volume(self, total_put_volume):
        """Sets the total_put_volume of this OptionsAggregate.

        Total put volume for the ticker  # noqa: E501

        :param total_put_volume: The total_put_volume of this OptionsAggregate.  # noqa: E501
        :type: int
        """

        self._total_put_volume = total_put_volume

    @property
    def total_call_volume(self):
        """Gets the total_call_volume of this OptionsAggregate.  # noqa: E501

        Total call volume for the ticker  # noqa: E501

        :return: The total_call_volume of this OptionsAggregate.  # noqa: E501
        :rtype: int
        """
        return self._total_call_volume
        
    @property
    def total_call_volume_dict(self):
        """Gets the total_call_volume of this OptionsAggregate.  # noqa: E501

        Total call volume for the ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_call_volume of this OptionsAggregate.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.total_call_volume
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
            result = { 'total_call_volume': value }

        
        return result
        

    @total_call_volume.setter
    def total_call_volume(self, total_call_volume):
        """Sets the total_call_volume of this OptionsAggregate.

        Total call volume for the ticker  # noqa: E501

        :param total_call_volume: The total_call_volume of this OptionsAggregate.  # noqa: E501
        :type: int
        """

        self._total_call_volume = total_call_volume

    @property
    def put_call_volume_ratio(self):
        """Gets the put_call_volume_ratio of this OptionsAggregate.  # noqa: E501

        Total put volume to total call volume ratio for the ticker  # noqa: E501

        :return: The put_call_volume_ratio of this OptionsAggregate.  # noqa: E501
        :rtype: float
        """
        return self._put_call_volume_ratio
        
    @property
    def put_call_volume_ratio_dict(self):
        """Gets the put_call_volume_ratio of this OptionsAggregate.  # noqa: E501

        Total put volume to total call volume ratio for the ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The put_call_volume_ratio of this OptionsAggregate.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.put_call_volume_ratio
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
            result = { 'put_call_volume_ratio': value }

        
        return result
        

    @put_call_volume_ratio.setter
    def put_call_volume_ratio(self, put_call_volume_ratio):
        """Sets the put_call_volume_ratio of this OptionsAggregate.

        Total put volume to total call volume ratio for the ticker  # noqa: E501

        :param put_call_volume_ratio: The put_call_volume_ratio of this OptionsAggregate.  # noqa: E501
        :type: float
        """

        self._put_call_volume_ratio = put_call_volume_ratio

    @property
    def contract_count(self):
        """Gets the contract_count of this OptionsAggregate.  # noqa: E501

        Total number of active contracts for the ticker  # noqa: E501

        :return: The contract_count of this OptionsAggregate.  # noqa: E501
        :rtype: int
        """
        return self._contract_count
        
    @property
    def contract_count_dict(self):
        """Gets the contract_count of this OptionsAggregate.  # noqa: E501

        Total number of active contracts for the ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The contract_count of this OptionsAggregate.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.contract_count
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
            result = { 'contract_count': value }

        
        return result
        

    @contract_count.setter
    def contract_count(self, contract_count):
        """Sets the contract_count of this OptionsAggregate.

        Total number of active contracts for the ticker  # noqa: E501

        :param contract_count: The contract_count of this OptionsAggregate.  # noqa: E501
        :type: int
        """

        self._contract_count = contract_count

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
        if not isinstance(other, OptionsAggregate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
