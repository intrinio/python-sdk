# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.56.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InstitutionalOwnership(object):
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
        'owner_cik': 'str',
        'owner_name': 'str',
        'period_ended': 'date',
        'value': 'float',
        'amount': 'float',
        'sole_voting_authority': 'float',
        'shared_voting_authority': 'float',
        'no_voting_authority': 'float',
        'previous_amount': 'float',
        'amount_change': 'float',
        'amount_percent_change': 'float'
    }

    attribute_map = {
        'owner_cik': 'owner_cik',
        'owner_name': 'owner_name',
        'period_ended': 'period_ended',
        'value': 'value',
        'amount': 'amount',
        'sole_voting_authority': 'sole_voting_authority',
        'shared_voting_authority': 'shared_voting_authority',
        'no_voting_authority': 'no_voting_authority',
        'previous_amount': 'previous_amount',
        'amount_change': 'amount_change',
        'amount_percent_change': 'amount_percent_change'
    }

    def __init__(self, owner_cik=None, owner_name=None, period_ended=None, value=None, amount=None, sole_voting_authority=None, shared_voting_authority=None, no_voting_authority=None, previous_amount=None, amount_change=None, amount_percent_change=None):  # noqa: E501
        """InstitutionalOwnership - a model defined in Swagger"""  # noqa: E501

        self._owner_cik = None
        self._owner_name = None
        self._period_ended = None
        self._value = None
        self._amount = None
        self._sole_voting_authority = None
        self._shared_voting_authority = None
        self._no_voting_authority = None
        self._previous_amount = None
        self._amount_change = None
        self._amount_percent_change = None
        self.discriminator = None

        if owner_cik is not None:
            self.owner_cik = owner_cik
        if owner_name is not None:
            self.owner_name = owner_name
        if period_ended is not None:
            self.period_ended = period_ended
        if value is not None:
            self.value = value
        if amount is not None:
            self.amount = amount
        if sole_voting_authority is not None:
            self.sole_voting_authority = sole_voting_authority
        if shared_voting_authority is not None:
            self.shared_voting_authority = shared_voting_authority
        if no_voting_authority is not None:
            self.no_voting_authority = no_voting_authority
        if previous_amount is not None:
            self.previous_amount = previous_amount
        if amount_change is not None:
            self.amount_change = amount_change
        if amount_percent_change is not None:
            self.amount_percent_change = amount_percent_change

    @property
    def owner_cik(self):
        """Gets the owner_cik of this InstitutionalOwnership.  # noqa: E501

        The Central Index Key issued by the SEC, which is the unique identifier all owner filings  # noqa: E501

        :return: The owner_cik of this InstitutionalOwnership.  # noqa: E501
        :rtype: str
        """
        return self._owner_cik
        
    @property
    def owner_cik_dict(self):
        """Gets the owner_cik of this InstitutionalOwnership.  # noqa: E501

        The Central Index Key issued by the SEC, which is the unique identifier all owner filings as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The owner_cik of this InstitutionalOwnership.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.owner_cik
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
            result = { 'owner_cik': value }

        
        return result
        

    @owner_cik.setter
    def owner_cik(self, owner_cik):
        """Sets the owner_cik of this InstitutionalOwnership.

        The Central Index Key issued by the SEC, which is the unique identifier all owner filings  # noqa: E501

        :param owner_cik: The owner_cik of this InstitutionalOwnership.  # noqa: E501
        :type: str
        """

        self._owner_cik = owner_cik

    @property
    def owner_name(self):
        """Gets the owner_name of this InstitutionalOwnership.  # noqa: E501

        The name of the institutional owner  # noqa: E501

        :return: The owner_name of this InstitutionalOwnership.  # noqa: E501
        :rtype: str
        """
        return self._owner_name
        
    @property
    def owner_name_dict(self):
        """Gets the owner_name of this InstitutionalOwnership.  # noqa: E501

        The name of the institutional owner as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The owner_name of this InstitutionalOwnership.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.owner_name
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
            result = { 'owner_name': value }

        
        return result
        

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this InstitutionalOwnership.

        The name of the institutional owner  # noqa: E501

        :param owner_name: The owner_name of this InstitutionalOwnership.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def period_ended(self):
        """Gets the period_ended of this InstitutionalOwnership.  # noqa: E501

        The date of the latest 13-F filing on record with the SEC.  # noqa: E501

        :return: The period_ended of this InstitutionalOwnership.  # noqa: E501
        :rtype: date
        """
        return self._period_ended
        
    @property
    def period_ended_dict(self):
        """Gets the period_ended of this InstitutionalOwnership.  # noqa: E501

        The date of the latest 13-F filing on record with the SEC. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The period_ended of this InstitutionalOwnership.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.period_ended
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
            result = { 'period_ended': value }

        
        return result
        

    @period_ended.setter
    def period_ended(self, period_ended):
        """Sets the period_ended of this InstitutionalOwnership.

        The date of the latest 13-F filing on record with the SEC.  # noqa: E501

        :param period_ended: The period_ended of this InstitutionalOwnership.  # noqa: E501
        :type: date
        """

        self._period_ended = period_ended

    @property
    def value(self):
        """Gets the value of this InstitutionalOwnership.  # noqa: E501

        The market value in amount of dollars of the holding in the listed security  # noqa: E501

        :return: The value of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """
        return self._value
        
    @property
    def value_dict(self):
        """Gets the value of this InstitutionalOwnership.  # noqa: E501

        The market value in amount of dollars of the holding in the listed security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The value of this InstitutionalOwnership.  # noqa: E501
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
        """Sets the value of this InstitutionalOwnership.

        The market value in amount of dollars of the holding in the listed security  # noqa: E501

        :param value: The value of this InstitutionalOwnership.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def amount(self):
        """Gets the amount of this InstitutionalOwnership.  # noqa: E501

        The number of shares held in the listed security  # noqa: E501

        :return: The amount of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """
        return self._amount
        
    @property
    def amount_dict(self):
        """Gets the amount of this InstitutionalOwnership.  # noqa: E501

        The number of shares held in the listed security as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The amount of this InstitutionalOwnership.  # noqa: E501
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
        """Sets the amount of this InstitutionalOwnership.

        The number of shares held in the listed security  # noqa: E501

        :param amount: The amount of this InstitutionalOwnership.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def sole_voting_authority(self):
        """Gets the sole_voting_authority of this InstitutionalOwnership.  # noqa: E501

        The number of shares where the insitutional holder has sole voting authority  # noqa: E501

        :return: The sole_voting_authority of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """
        return self._sole_voting_authority
        
    @property
    def sole_voting_authority_dict(self):
        """Gets the sole_voting_authority of this InstitutionalOwnership.  # noqa: E501

        The number of shares where the insitutional holder has sole voting authority as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sole_voting_authority of this InstitutionalOwnership.  # noqa: E501
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
        """Sets the sole_voting_authority of this InstitutionalOwnership.

        The number of shares where the insitutional holder has sole voting authority  # noqa: E501

        :param sole_voting_authority: The sole_voting_authority of this InstitutionalOwnership.  # noqa: E501
        :type: float
        """

        self._sole_voting_authority = sole_voting_authority

    @property
    def shared_voting_authority(self):
        """Gets the shared_voting_authority of this InstitutionalOwnership.  # noqa: E501

        The number of shares where the insitutional holder has shared voting authority  # noqa: E501

        :return: The shared_voting_authority of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """
        return self._shared_voting_authority
        
    @property
    def shared_voting_authority_dict(self):
        """Gets the shared_voting_authority of this InstitutionalOwnership.  # noqa: E501

        The number of shares where the insitutional holder has shared voting authority as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The shared_voting_authority of this InstitutionalOwnership.  # noqa: E501
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
        """Sets the shared_voting_authority of this InstitutionalOwnership.

        The number of shares where the insitutional holder has shared voting authority  # noqa: E501

        :param shared_voting_authority: The shared_voting_authority of this InstitutionalOwnership.  # noqa: E501
        :type: float
        """

        self._shared_voting_authority = shared_voting_authority

    @property
    def no_voting_authority(self):
        """Gets the no_voting_authority of this InstitutionalOwnership.  # noqa: E501

        The number of shares where the insitutional holder has no voting authority  # noqa: E501

        :return: The no_voting_authority of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """
        return self._no_voting_authority
        
    @property
    def no_voting_authority_dict(self):
        """Gets the no_voting_authority of this InstitutionalOwnership.  # noqa: E501

        The number of shares where the insitutional holder has no voting authority as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The no_voting_authority of this InstitutionalOwnership.  # noqa: E501
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
        """Sets the no_voting_authority of this InstitutionalOwnership.

        The number of shares where the insitutional holder has no voting authority  # noqa: E501

        :param no_voting_authority: The no_voting_authority of this InstitutionalOwnership.  # noqa: E501
        :type: float
        """

        self._no_voting_authority = no_voting_authority

    @property
    def previous_amount(self):
        """Gets the previous_amount of this InstitutionalOwnership.  # noqa: E501

        The prior quarter number of shares held by the owner  # noqa: E501

        :return: The previous_amount of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """
        return self._previous_amount
        
    @property
    def previous_amount_dict(self):
        """Gets the previous_amount of this InstitutionalOwnership.  # noqa: E501

        The prior quarter number of shares held by the owner as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The previous_amount of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.previous_amount
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
            result = { 'previous_amount': value }

        
        return result
        

    @previous_amount.setter
    def previous_amount(self, previous_amount):
        """Sets the previous_amount of this InstitutionalOwnership.

        The prior quarter number of shares held by the owner  # noqa: E501

        :param previous_amount: The previous_amount of this InstitutionalOwnership.  # noqa: E501
        :type: float
        """

        self._previous_amount = previous_amount

    @property
    def amount_change(self):
        """Gets the amount_change of this InstitutionalOwnership.  # noqa: E501

        The change in number of shares held from the prior quarter  # noqa: E501

        :return: The amount_change of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """
        return self._amount_change
        
    @property
    def amount_change_dict(self):
        """Gets the amount_change of this InstitutionalOwnership.  # noqa: E501

        The change in number of shares held from the prior quarter as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The amount_change of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.amount_change
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
            result = { 'amount_change': value }

        
        return result
        

    @amount_change.setter
    def amount_change(self, amount_change):
        """Sets the amount_change of this InstitutionalOwnership.

        The change in number of shares held from the prior quarter  # noqa: E501

        :param amount_change: The amount_change of this InstitutionalOwnership.  # noqa: E501
        :type: float
        """

        self._amount_change = amount_change

    @property
    def amount_percent_change(self):
        """Gets the amount_percent_change of this InstitutionalOwnership.  # noqa: E501

        The percentage change in the number of shares held from the prior quarter  # noqa: E501

        :return: The amount_percent_change of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """
        return self._amount_percent_change
        
    @property
    def amount_percent_change_dict(self):
        """Gets the amount_percent_change of this InstitutionalOwnership.  # noqa: E501

        The percentage change in the number of shares held from the prior quarter as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The amount_percent_change of this InstitutionalOwnership.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.amount_percent_change
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
            result = { 'amount_percent_change': value }

        
        return result
        

    @amount_percent_change.setter
    def amount_percent_change(self, amount_percent_change):
        """Sets the amount_percent_change of this InstitutionalOwnership.

        The percentage change in the number of shares held from the prior quarter  # noqa: E501

        :param amount_percent_change: The amount_percent_change of this InstitutionalOwnership.  # noqa: E501
        :type: float
        """

        self._amount_percent_change = amount_percent_change

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
        if not isinstance(other, InstitutionalOwnership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
