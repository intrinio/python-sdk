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

from intrinio_sdk.models.security_summary import SecuritySummary  # noqa: F401,E501


class Beta(object):
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
        'period_type': 'str',
        'one_year_beta': 'float',
        'three_year_beta': 'float',
        'five_year_beta': 'float',
        'seven_year_beta': 'float',
        'ten_year_beta': 'float',
        'security': 'SecuritySummary'
    }

    attribute_map = {
        'period_type': 'period_type',
        'one_year_beta': 'one_year_beta',
        'three_year_beta': 'three_year_beta',
        'five_year_beta': 'five_year_beta',
        'seven_year_beta': 'seven_year_beta',
        'ten_year_beta': 'ten_year_beta',
        'security': 'security'
    }

    def __init__(self, period_type=None, one_year_beta=None, three_year_beta=None, five_year_beta=None, seven_year_beta=None, ten_year_beta=None, security=None):  # noqa: E501
        """Beta - a model defined in Swagger"""  # noqa: E501

        self._period_type = None
        self._one_year_beta = None
        self._three_year_beta = None
        self._five_year_beta = None
        self._seven_year_beta = None
        self._ten_year_beta = None
        self._security = None
        self.discriminator = None

        if period_type is not None:
            self.period_type = period_type
        if one_year_beta is not None:
            self.one_year_beta = one_year_beta
        if three_year_beta is not None:
            self.three_year_beta = three_year_beta
        if five_year_beta is not None:
            self.five_year_beta = five_year_beta
        if seven_year_beta is not None:
            self.seven_year_beta = seven_year_beta
        if ten_year_beta is not None:
            self.ten_year_beta = ten_year_beta
        if security is not None:
            self.security = security

    @property
    def period_type(self):
        """Gets the period_type of this Beta.  # noqa: E501

        Type of period for this beta value.  # noqa: E501

        :return: The period_type of this Beta.  # noqa: E501
        :rtype: str
        """
        return self._period_type
        
    @property
    def period_type_dict(self):
        """Gets the period_type of this Beta.  # noqa: E501

        Type of period for this beta value. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The period_type of this Beta.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.period_type
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
            result = { 'period_type': value }

        
        return result
        

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this Beta.

        Type of period for this beta value.  # noqa: E501

        :param period_type: The period_type of this Beta.  # noqa: E501
        :type: str
        """
        allowed_values = ["weekly", "monthly"]  # noqa: E501
        if period_type not in allowed_values:
            raise ValueError(
                "Invalid value for `period_type` ({0}), must be one of {1}"  # noqa: E501
                .format(period_type, allowed_values)
            )

        self._period_type = period_type

    @property
    def one_year_beta(self):
        """Gets the one_year_beta of this Beta.  # noqa: E501

        The one year beta value for this security.  # noqa: E501

        :return: The one_year_beta of this Beta.  # noqa: E501
        :rtype: float
        """
        return self._one_year_beta
        
    @property
    def one_year_beta_dict(self):
        """Gets the one_year_beta of this Beta.  # noqa: E501

        The one year beta value for this security. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The one_year_beta of this Beta.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.one_year_beta
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
            result = { 'one_year_beta': value }

        
        return result
        

    @one_year_beta.setter
    def one_year_beta(self, one_year_beta):
        """Sets the one_year_beta of this Beta.

        The one year beta value for this security.  # noqa: E501

        :param one_year_beta: The one_year_beta of this Beta.  # noqa: E501
        :type: float
        """

        self._one_year_beta = one_year_beta

    @property
    def three_year_beta(self):
        """Gets the three_year_beta of this Beta.  # noqa: E501

        The three year beta value for this security.  # noqa: E501

        :return: The three_year_beta of this Beta.  # noqa: E501
        :rtype: float
        """
        return self._three_year_beta
        
    @property
    def three_year_beta_dict(self):
        """Gets the three_year_beta of this Beta.  # noqa: E501

        The three year beta value for this security. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The three_year_beta of this Beta.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.three_year_beta
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
            result = { 'three_year_beta': value }

        
        return result
        

    @three_year_beta.setter
    def three_year_beta(self, three_year_beta):
        """Sets the three_year_beta of this Beta.

        The three year beta value for this security.  # noqa: E501

        :param three_year_beta: The three_year_beta of this Beta.  # noqa: E501
        :type: float
        """

        self._three_year_beta = three_year_beta

    @property
    def five_year_beta(self):
        """Gets the five_year_beta of this Beta.  # noqa: E501

        The five year beta value for this security.  # noqa: E501

        :return: The five_year_beta of this Beta.  # noqa: E501
        :rtype: float
        """
        return self._five_year_beta
        
    @property
    def five_year_beta_dict(self):
        """Gets the five_year_beta of this Beta.  # noqa: E501

        The five year beta value for this security. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The five_year_beta of this Beta.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.five_year_beta
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
            result = { 'five_year_beta': value }

        
        return result
        

    @five_year_beta.setter
    def five_year_beta(self, five_year_beta):
        """Sets the five_year_beta of this Beta.

        The five year beta value for this security.  # noqa: E501

        :param five_year_beta: The five_year_beta of this Beta.  # noqa: E501
        :type: float
        """

        self._five_year_beta = five_year_beta

    @property
    def seven_year_beta(self):
        """Gets the seven_year_beta of this Beta.  # noqa: E501

        The seven year beta value for this security.  # noqa: E501

        :return: The seven_year_beta of this Beta.  # noqa: E501
        :rtype: float
        """
        return self._seven_year_beta
        
    @property
    def seven_year_beta_dict(self):
        """Gets the seven_year_beta of this Beta.  # noqa: E501

        The seven year beta value for this security. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The seven_year_beta of this Beta.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.seven_year_beta
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
            result = { 'seven_year_beta': value }

        
        return result
        

    @seven_year_beta.setter
    def seven_year_beta(self, seven_year_beta):
        """Sets the seven_year_beta of this Beta.

        The seven year beta value for this security.  # noqa: E501

        :param seven_year_beta: The seven_year_beta of this Beta.  # noqa: E501
        :type: float
        """

        self._seven_year_beta = seven_year_beta

    @property
    def ten_year_beta(self):
        """Gets the ten_year_beta of this Beta.  # noqa: E501

        The ten year beta value for this security.  # noqa: E501

        :return: The ten_year_beta of this Beta.  # noqa: E501
        :rtype: float
        """
        return self._ten_year_beta
        
    @property
    def ten_year_beta_dict(self):
        """Gets the ten_year_beta of this Beta.  # noqa: E501

        The ten year beta value for this security. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ten_year_beta of this Beta.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ten_year_beta
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
            result = { 'ten_year_beta': value }

        
        return result
        

    @ten_year_beta.setter
    def ten_year_beta(self, ten_year_beta):
        """Sets the ten_year_beta of this Beta.

        The ten year beta value for this security.  # noqa: E501

        :param ten_year_beta: The ten_year_beta of this Beta.  # noqa: E501
        :type: float
        """

        self._ten_year_beta = ten_year_beta

    @property
    def security(self):
        """Gets the security of this Beta.  # noqa: E501

        The Security.  # noqa: E501

        :return: The security of this Beta.  # noqa: E501
        :rtype: SecuritySummary
        """
        return self._security
        
    @property
    def security_dict(self):
        """Gets the security of this Beta.  # noqa: E501

        The Security. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The security of this Beta.  # noqa: E501
        :rtype: SecuritySummary
        """

        result = None

        value = self.security
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
            result = { 'security': value }

        
        return result
        

    @security.setter
    def security(self, security):
        """Sets the security of this Beta.

        The Security.  # noqa: E501

        :param security: The security of this Beta.  # noqa: E501
        :type: SecuritySummary
        """

        self._security = security

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
        if not isinstance(other, Beta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
