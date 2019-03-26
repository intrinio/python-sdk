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

from intrinio_sdk.models.detrended_price_oscillator_technical_value import DetrendedPriceOscillatorTechnicalValue  # noqa: F401,E501
from intrinio_sdk.models.security_summary import SecuritySummary  # noqa: F401,E501
from intrinio_sdk.models.technical_indicator import TechnicalIndicator  # noqa: F401,E501


class ApiResponseSecurityDetrendedPriceOscillator(object):
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
        'technicals': 'list[DetrendedPriceOscillatorTechnicalValue]',
        'indicator': 'TechnicalIndicator',
        'security': 'SecuritySummary',
        'next_page': 'str'
    }

    attribute_map = {
        'technicals': 'technicals',
        'indicator': 'indicator',
        'security': 'security',
        'next_page': 'next_page'
    }

    def __init__(self, technicals=None, indicator=None, security=None, next_page=None):  # noqa: E501
        """ApiResponseSecurityDetrendedPriceOscillator - a model defined in Swagger"""  # noqa: E501

        self._technicals = None
        self._indicator = None
        self._security = None
        self._next_page = None
        self.discriminator = None

        if technicals is not None:
            self.technicals = technicals
        if indicator is not None:
            self.indicator = indicator
        if security is not None:
            self.security = security
        if next_page is not None:
            self.next_page = next_page

    @property
    def technicals(self):
        """Gets the technicals of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501


        :return: The technicals of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501
        :rtype: list[DetrendedPriceOscillatorTechnicalValue]
        """
        return self._technicals

    @technicals.setter
    def technicals(self, technicals):
        """Sets the technicals of this ApiResponseSecurityDetrendedPriceOscillator.


        :param technicals: The technicals of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501
        :type: list[DetrendedPriceOscillatorTechnicalValue]
        """

        self._technicals = technicals

    @property
    def indicator(self):
        """Gets the indicator of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501

        The name and symbol of the technical indicator  # noqa: E501

        :return: The indicator of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501
        :rtype: TechnicalIndicator
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this ApiResponseSecurityDetrendedPriceOscillator.

        The name and symbol of the technical indicator  # noqa: E501

        :param indicator: The indicator of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501
        :type: TechnicalIndicator
        """

        self._indicator = indicator

    @property
    def security(self):
        """Gets the security of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501

        The Security of the Stock Price  # noqa: E501

        :return: The security of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501
        :rtype: SecuritySummary
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this ApiResponseSecurityDetrendedPriceOscillator.

        The Security of the Stock Price  # noqa: E501

        :param security: The security of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501
        :type: SecuritySummary
        """

        self._security = security

    @property
    def next_page(self):
        """Gets the next_page of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501

        The token required to request the next page of the data  # noqa: E501

        :return: The next_page of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ApiResponseSecurityDetrendedPriceOscillator.

        The token required to request the next page of the data  # noqa: E501

        :param next_page: The next_page of this ApiResponseSecurityDetrendedPriceOscillator.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

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
        if not isinstance(other, ApiResponseSecurityDetrendedPriceOscillator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
