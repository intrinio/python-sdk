# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.42.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MovingAverageConvergenceDivergenceTechnicalValue(object):
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
        'macd_histogram': 'float',
        'macd_line': 'float',
        'signal_line': 'float'
    }

    attribute_map = {
        'date_time': 'date_time',
        'macd_histogram': 'macd_histogram',
        'macd_line': 'macd_line',
        'signal_line': 'signal_line'
    }

    def __init__(self, date_time=None, macd_histogram=None, macd_line=None, signal_line=None):  # noqa: E501
        """MovingAverageConvergenceDivergenceTechnicalValue - a model defined in Swagger"""  # noqa: E501

        self._date_time = None
        self._macd_histogram = None
        self._macd_line = None
        self._signal_line = None
        self.discriminator = None

        if date_time is not None:
            self.date_time = date_time
        if macd_histogram is not None:
            self.macd_histogram = macd_histogram
        if macd_line is not None:
            self.macd_line = macd_line
        if signal_line is not None:
            self.signal_line = signal_line

    @property
    def date_time(self):
        """Gets the date_time of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501

        The date_time of the observation  # noqa: E501

        :return: The date_time of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time
        
    @property
    def date_time_dict(self):
        """Gets the date_time of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501

        The date_time of the observation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date_time of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
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
        """Sets the date_time of this MovingAverageConvergenceDivergenceTechnicalValue.

        The date_time of the observation  # noqa: E501

        :param date_time: The date_time of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def macd_histogram(self):
        """Gets the macd_histogram of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501

        The histogram value of the Moving Average Convergence Divergence calculation  # noqa: E501

        :return: The macd_histogram of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._macd_histogram
        
    @property
    def macd_histogram_dict(self):
        """Gets the macd_histogram of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501

        The histogram value of the Moving Average Convergence Divergence calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The macd_histogram of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.macd_histogram
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
            result = { 'macd_histogram': value }

        
        return result
        

    @macd_histogram.setter
    def macd_histogram(self, macd_histogram):
        """Sets the macd_histogram of this MovingAverageConvergenceDivergenceTechnicalValue.

        The histogram value of the Moving Average Convergence Divergence calculation  # noqa: E501

        :param macd_histogram: The macd_histogram of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :type: float
        """

        self._macd_histogram = macd_histogram

    @property
    def macd_line(self):
        """Gets the macd_line of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501

        The line value of the Moving Average Convergence Divergence calculation  # noqa: E501

        :return: The macd_line of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._macd_line
        
    @property
    def macd_line_dict(self):
        """Gets the macd_line of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501

        The line value of the Moving Average Convergence Divergence calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The macd_line of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.macd_line
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
            result = { 'macd_line': value }

        
        return result
        

    @macd_line.setter
    def macd_line(self, macd_line):
        """Sets the macd_line of this MovingAverageConvergenceDivergenceTechnicalValue.

        The line value of the Moving Average Convergence Divergence calculation  # noqa: E501

        :param macd_line: The macd_line of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :type: float
        """

        self._macd_line = macd_line

    @property
    def signal_line(self):
        """Gets the signal_line of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501

        The signal line value of the Moving Average Convergence Divergence calculation  # noqa: E501

        :return: The signal_line of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._signal_line
        
    @property
    def signal_line_dict(self):
        """Gets the signal_line of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501

        The signal line value of the Moving Average Convergence Divergence calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The signal_line of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.signal_line
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
            result = { 'signal_line': value }

        
        return result
        

    @signal_line.setter
    def signal_line(self, signal_line):
        """Sets the signal_line of this MovingAverageConvergenceDivergenceTechnicalValue.

        The signal line value of the Moving Average Convergence Divergence calculation  # noqa: E501

        :param signal_line: The signal_line of this MovingAverageConvergenceDivergenceTechnicalValue.  # noqa: E501
        :type: float
        """

        self._signal_line = signal_line

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
        if not isinstance(other, MovingAverageConvergenceDivergenceTechnicalValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
