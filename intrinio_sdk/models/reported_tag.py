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


class ReportedTag(object):
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
        'tag': 'str',
        'name': 'str',
        'balance': 'str',
        'unit': 'str',
        'abstract': 'bool',
        'sequence': 'int',
        'depth': 'int'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'balance': 'balance',
        'unit': 'unit',
        'abstract': 'abstract',
        'sequence': 'sequence',
        'depth': 'depth'
    }

    def __init__(self, tag=None, name=None, balance=None, unit=None, abstract=None, sequence=None, depth=None):  # noqa: E501
        """ReportedTag - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._name = None
        self._balance = None
        self._unit = None
        self._abstract = None
        self._sequence = None
        self._depth = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if balance is not None:
            self.balance = balance
        if unit is not None:
            self.unit = unit
        if abstract is not None:
            self.abstract = abstract
        if sequence is not None:
            self.sequence = sequence
        if depth is not None:
            self.depth = depth

    @property
    def tag(self):
        """Gets the tag of this ReportedTag.  # noqa: E501

        The tag code  # noqa: E501

        :return: The tag of this ReportedTag.  # noqa: E501
        :rtype: str
        """
        return self._tag
        
    @property
    def tag_dict(self):
        """Gets the tag of this ReportedTag.  # noqa: E501

        The tag code as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The tag of this ReportedTag.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.tag
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
            result = { 'tag': value }

        
        return result
        

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ReportedTag.

        The tag code  # noqa: E501

        :param tag: The tag of this ReportedTag.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this ReportedTag.  # noqa: E501

        The tag name  # noqa: E501

        :return: The name of this ReportedTag.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this ReportedTag.  # noqa: E501

        The tag name as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this ReportedTag.  # noqa: E501
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
        """Sets the name of this ReportedTag.

        The tag name  # noqa: E501

        :param name: The name of this ReportedTag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def balance(self):
        """Gets the balance of this ReportedTag.  # noqa: E501

        Whether the tag represents a credit or debit  # noqa: E501

        :return: The balance of this ReportedTag.  # noqa: E501
        :rtype: str
        """
        return self._balance
        
    @property
    def balance_dict(self):
        """Gets the balance of this ReportedTag.  # noqa: E501

        Whether the tag represents a credit or debit as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The balance of this ReportedTag.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.balance
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
            result = { 'balance': value }

        
        return result
        

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ReportedTag.

        Whether the tag represents a credit or debit  # noqa: E501

        :param balance: The balance of this ReportedTag.  # noqa: E501
        :type: str
        """

        self._balance = balance

    @property
    def unit(self):
        """Gets the unit of this ReportedTag.  # noqa: E501

        The unit of the tag  # noqa: E501

        :return: The unit of this ReportedTag.  # noqa: E501
        :rtype: str
        """
        return self._unit
        
    @property
    def unit_dict(self):
        """Gets the unit of this ReportedTag.  # noqa: E501

        The unit of the tag as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The unit of this ReportedTag.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.unit
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
            result = { 'unit': value }

        
        return result
        

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ReportedTag.

        The unit of the tag  # noqa: E501

        :param unit: The unit of this ReportedTag.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def abstract(self):
        """Gets the abstract of this ReportedTag.  # noqa: E501

        If true, the tag is an abstract and does not represent a nominal value  # noqa: E501

        :return: The abstract of this ReportedTag.  # noqa: E501
        :rtype: bool
        """
        return self._abstract
        
    @property
    def abstract_dict(self):
        """Gets the abstract of this ReportedTag.  # noqa: E501

        If true, the tag is an abstract and does not represent a nominal value as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The abstract of this ReportedTag.  # noqa: E501
        :rtype: bool
        """

        result = None

        value = self.abstract
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
            result = { 'abstract': value }

        
        return result
        

    @abstract.setter
    def abstract(self, abstract):
        """Sets the abstract of this ReportedTag.

        If true, the tag is an abstract and does not represent a nominal value  # noqa: E501

        :param abstract: The abstract of this ReportedTag.  # noqa: E501
        :type: bool
        """

        self._abstract = abstract

    @property
    def sequence(self):
        """Gets the sequence of this ReportedTag.  # noqa: E501

        The vertical sequence of the tag when displayed in the financial statement  # noqa: E501

        :return: The sequence of this ReportedTag.  # noqa: E501
        :rtype: int
        """
        return self._sequence
        
    @property
    def sequence_dict(self):
        """Gets the sequence of this ReportedTag.  # noqa: E501

        The vertical sequence of the tag when displayed in the financial statement as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sequence of this ReportedTag.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.sequence
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
            result = { 'sequence': value }

        
        return result
        

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this ReportedTag.

        The vertical sequence of the tag when displayed in the financial statement  # noqa: E501

        :param sequence: The sequence of this ReportedTag.  # noqa: E501
        :type: int
        """

        self._sequence = sequence

    @property
    def depth(self):
        """Gets the depth of this ReportedTag.  # noqa: E501

        The horizontal depth of the tag when displayed in the financial statement  # noqa: E501

        :return: The depth of this ReportedTag.  # noqa: E501
        :rtype: int
        """
        return self._depth
        
    @property
    def depth_dict(self):
        """Gets the depth of this ReportedTag.  # noqa: E501

        The horizontal depth of the tag when displayed in the financial statement as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The depth of this ReportedTag.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.depth
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
            result = { 'depth': value }

        
        return result
        

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this ReportedTag.

        The horizontal depth of the tag when displayed in the financial statement  # noqa: E501

        :param depth: The depth of this ReportedTag.  # noqa: E501
        :type: int
        """

        self._depth = depth

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
        if not isinstance(other, ReportedTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
