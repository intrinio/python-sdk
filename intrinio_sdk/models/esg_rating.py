# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.63.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ESGRating(object):
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
        'date': 'date',
        'community_rating': 'float',
        'employee_rating': 'float',
        'environment_rating': 'float',
        'governance_rating': 'float'
    }

    attribute_map = {
        'date': 'date',
        'community_rating': 'community_rating',
        'employee_rating': 'employee_rating',
        'environment_rating': 'environment_rating',
        'governance_rating': 'governance_rating'
    }

    def __init__(self, date=None, community_rating=None, employee_rating=None, environment_rating=None, governance_rating=None):  # noqa: E501
        """ESGRating - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._community_rating = None
        self._employee_rating = None
        self._environment_rating = None
        self._governance_rating = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if community_rating is not None:
            self.community_rating = community_rating
        if employee_rating is not None:
            self.employee_rating = employee_rating
        if environment_rating is not None:
            self.environment_rating = environment_rating
        if governance_rating is not None:
            self.governance_rating = governance_rating

    @property
    def date(self):
        """Gets the date of this ESGRating.  # noqa: E501

        Indicates the date on which the ESG Rating was calculated.  # noqa: E501

        :return: The date of this ESGRating.  # noqa: E501
        :rtype: date
        """
        return self._date
        
    @property
    def date_dict(self):
        """Gets the date of this ESGRating.  # noqa: E501

        Indicates the date on which the ESG Rating was calculated. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date of this ESGRating.  # noqa: E501
        :rtype: date
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
        """Sets the date of this ESGRating.

        Indicates the date on which the ESG Rating was calculated.  # noqa: E501

        :param date: The date of this ESGRating.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def community_rating(self):
        """Gets the community_rating of this ESGRating.  # noqa: E501

        The Community Category reflects a company's citizenship, charitable giving, and volunteerism. This category covers the company's human rights record and treatment of its supply chain. It also covers the environmental and social impacts of the company's products and services, and the development of sustainable products, processes and technologies.  # noqa: E501

        :return: The community_rating of this ESGRating.  # noqa: E501
        :rtype: float
        """
        return self._community_rating
        
    @property
    def community_rating_dict(self):
        """Gets the community_rating of this ESGRating.  # noqa: E501

        The Community Category reflects a company's citizenship, charitable giving, and volunteerism. This category covers the company's human rights record and treatment of its supply chain. It also covers the environmental and social impacts of the company's products and services, and the development of sustainable products, processes and technologies. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The community_rating of this ESGRating.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.community_rating
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
            result = { 'community_rating': value }

        
        return result
        

    @community_rating.setter
    def community_rating(self, community_rating):
        """Sets the community_rating of this ESGRating.

        The Community Category reflects a company's citizenship, charitable giving, and volunteerism. This category covers the company's human rights record and treatment of its supply chain. It also covers the environmental and social impacts of the company's products and services, and the development of sustainable products, processes and technologies.  # noqa: E501

        :param community_rating: The community_rating of this ESGRating.  # noqa: E501
        :type: float
        """

        self._community_rating = community_rating

    @property
    def employee_rating(self):
        """Gets the employee_rating of this ESGRating.  # noqa: E501

        The Employees category includes disclosure of policies, programs, and performance in diversity, labor relations and labor rights. The evaluation focuses on the quality of policies and programs, compliance with national laws and regulations, and proactive management initiatives. The category includes evaluation of inclusive diversity policies, fair treatment of all employees, robust diversity (EEO-1) programs and training.  # noqa: E501

        :return: The employee_rating of this ESGRating.  # noqa: E501
        :rtype: float
        """
        return self._employee_rating
        
    @property
    def employee_rating_dict(self):
        """Gets the employee_rating of this ESGRating.  # noqa: E501

        The Employees category includes disclosure of policies, programs, and performance in diversity, labor relations and labor rights. The evaluation focuses on the quality of policies and programs, compliance with national laws and regulations, and proactive management initiatives. The category includes evaluation of inclusive diversity policies, fair treatment of all employees, robust diversity (EEO-1) programs and training. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The employee_rating of this ESGRating.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.employee_rating
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
            result = { 'employee_rating': value }

        
        return result
        

    @employee_rating.setter
    def employee_rating(self, employee_rating):
        """Sets the employee_rating of this ESGRating.

        The Employees category includes disclosure of policies, programs, and performance in diversity, labor relations and labor rights. The evaluation focuses on the quality of policies and programs, compliance with national laws and regulations, and proactive management initiatives. The category includes evaluation of inclusive diversity policies, fair treatment of all employees, robust diversity (EEO-1) programs and training.  # noqa: E501

        :param employee_rating: The employee_rating of this ESGRating.  # noqa: E501
        :type: float
        """

        self._employee_rating = employee_rating

    @property
    def environment_rating(self):
        """Gets the environment_rating of this ESGRating.  # noqa: E501

        The Environment category data covers a company's interactions with the environment at large, including use of natural resources. The category evaluates corporate environmental performance, compliance with environmental regulations, and mitigation of environmental footprint. It also includes leadership in addressing climate change through appropriate policies and strategies.  # noqa: E501

        :return: The environment_rating of this ESGRating.  # noqa: E501
        :rtype: float
        """
        return self._environment_rating
        
    @property
    def environment_rating_dict(self):
        """Gets the environment_rating of this ESGRating.  # noqa: E501

        The Environment category data covers a company's interactions with the environment at large, including use of natural resources. The category evaluates corporate environmental performance, compliance with environmental regulations, and mitigation of environmental footprint. It also includes leadership in addressing climate change through appropriate policies and strategies. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The environment_rating of this ESGRating.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.environment_rating
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
            result = { 'environment_rating': value }

        
        return result
        

    @environment_rating.setter
    def environment_rating(self, environment_rating):
        """Sets the environment_rating of this ESGRating.

        The Environment category data covers a company's interactions with the environment at large, including use of natural resources. The category evaluates corporate environmental performance, compliance with environmental regulations, and mitigation of environmental footprint. It also includes leadership in addressing climate change through appropriate policies and strategies.  # noqa: E501

        :param environment_rating: The environment_rating of this ESGRating.  # noqa: E501
        :type: float
        """

        self._environment_rating = environment_rating

    @property
    def governance_rating(self):
        """Gets the governance_rating of this ESGRating.  # noqa: E501

        Corporate governance refers to leadership structure and the values that determine corporate direction, ethics and performance. The Governance category covers disclosure of policies and procedures, board independence and diversity, executive compensation, attention to stakeholder concerns, and evaluation of a companys culture of ethical leadership and compliance.  # noqa: E501

        :return: The governance_rating of this ESGRating.  # noqa: E501
        :rtype: float
        """
        return self._governance_rating
        
    @property
    def governance_rating_dict(self):
        """Gets the governance_rating of this ESGRating.  # noqa: E501

        Corporate governance refers to leadership structure and the values that determine corporate direction, ethics and performance. The Governance category covers disclosure of policies and procedures, board independence and diversity, executive compensation, attention to stakeholder concerns, and evaluation of a companys culture of ethical leadership and compliance. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The governance_rating of this ESGRating.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.governance_rating
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
            result = { 'governance_rating': value }

        
        return result
        

    @governance_rating.setter
    def governance_rating(self, governance_rating):
        """Sets the governance_rating of this ESGRating.

        Corporate governance refers to leadership structure and the values that determine corporate direction, ethics and performance. The Governance category covers disclosure of policies and procedures, board independence and diversity, executive compensation, attention to stakeholder concerns, and evaluation of a companys culture of ethical leadership and compliance.  # noqa: E501

        :param governance_rating: The governance_rating of this ESGRating.  # noqa: E501
        :type: float
        """

        self._governance_rating = governance_rating

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
        if not isinstance(other, ESGRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
