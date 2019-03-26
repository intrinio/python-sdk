# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DataTagSummary(object):
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
        'id': 'str',
        'name': 'str',
        'tag': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tag': 'tag',
        'unit': 'unit'
    }

    def __init__(self, id=None, name=None, tag=None, unit=None):  # noqa: E501
        """DataTagSummary - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._tag = None
        self._unit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tag is not None:
            self.tag = tag
        if unit is not None:
            self.unit = unit

    @property
    def id(self):
        """Gets the id of this DataTagSummary.  # noqa: E501

        The Intrinio ID for the Data Tag  # noqa: E501

        :return: The id of this DataTagSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataTagSummary.

        The Intrinio ID for the Data Tag  # noqa: E501

        :param id: The id of this DataTagSummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataTagSummary.  # noqa: E501

        The readable name of the Data Tag  # noqa: E501

        :return: The name of this DataTagSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataTagSummary.

        The readable name of the Data Tag  # noqa: E501

        :param name: The name of this DataTagSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tag(self):
        """Gets the tag of this DataTagSummary.  # noqa: E501

        The code-name of the Data Tag  # noqa: E501

        :return: The tag of this DataTagSummary.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this DataTagSummary.

        The code-name of the Data Tag  # noqa: E501

        :param tag: The tag of this DataTagSummary.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def unit(self):
        """Gets the unit of this DataTagSummary.  # noqa: E501

        The unit of the Data Tag  # noqa: E501

        :return: The unit of this DataTagSummary.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DataTagSummary.

        The unit of the Data Tag  # noqa: E501

        :param unit: The unit of this DataTagSummary.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if not isinstance(other, DataTagSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
