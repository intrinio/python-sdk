# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.72.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TrueStrengthIndexTechnicalValue(object):
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
        'date_time': 'datetime',
        'tsi': 'float'
    }

    attribute_map = {
        'date_time': 'date_time',
        'tsi': 'tsi'
    }

    def __init__(self, date_time=None, tsi=None):  # noqa: E501
        """TrueStrengthIndexTechnicalValue - a model defined in Swagger"""  # noqa: E501

        self._date_time = None
        self._tsi = None
        self.discriminator = None

        if date_time is not None:
            self.date_time = date_time
        if tsi is not None:
            self.tsi = tsi

    @property
    def date_time(self):
        """Gets the date_time of this TrueStrengthIndexTechnicalValue.  # noqa: E501

        The date_time of the observation  # noqa: E501

        :return: The date_time of this TrueStrengthIndexTechnicalValue.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time
        
    @property
    def date_time_dict(self):
        """Gets the date_time of this TrueStrengthIndexTechnicalValue.  # noqa: E501

        The date_time of the observation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date_time of this TrueStrengthIndexTechnicalValue.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.date_time
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
            result = { 'date_time': value }

        
        return result
        

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this TrueStrengthIndexTechnicalValue.

        The date_time of the observation  # noqa: E501

        :param date_time: The date_time of this TrueStrengthIndexTechnicalValue.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def tsi(self):
        """Gets the tsi of this TrueStrengthIndexTechnicalValue.  # noqa: E501

        The True Strength Index calculation value  # noqa: E501

        :return: The tsi of this TrueStrengthIndexTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._tsi
        
    @property
    def tsi_dict(self):
        """Gets the tsi of this TrueStrengthIndexTechnicalValue.  # noqa: E501

        The True Strength Index calculation value as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The tsi of this TrueStrengthIndexTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.tsi
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
            result = { 'tsi': value }

        
        return result
        

    @tsi.setter
    def tsi(self, tsi):
        """Sets the tsi of this TrueStrengthIndexTechnicalValue.

        The True Strength Index calculation value  # noqa: E501

        :param tsi: The tsi of this TrueStrengthIndexTechnicalValue.  # noqa: E501
        :type: float
        """

        self._tsi = tsi

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
        if not isinstance(other, TrueStrengthIndexTechnicalValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
