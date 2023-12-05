# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.47.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.filing import Filing  # noqa: F401,E501
from intrinio_sdk.models.thea_entity_answer import TheaEntityAnswer  # noqa: F401,E501


class ApiResponseFilingAnswers(object):
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
        'source': 'str',
        'query': 'str',
        'answers': 'list[TheaEntityAnswer]',
        'companies': 'list[Filing]'
    }

    attribute_map = {
        'source': 'source',
        'query': 'query',
        'answers': 'answers',
        'companies': 'companies'
    }

    def __init__(self, source=None, query=None, answers=None, companies=None):  # noqa: E501
        """ApiResponseFilingAnswers - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self._query = None
        self._answers = None
        self._companies = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if query is not None:
            self.query = query
        if answers is not None:
            self.answers = answers
        if companies is not None:
            self.companies = companies

    @property
    def source(self):
        """Gets the source of this ApiResponseFilingAnswers.  # noqa: E501

        The organziation the answer data was sourced from  # noqa: E501

        :return: The source of this ApiResponseFilingAnswers.  # noqa: E501
        :rtype: str
        """
        return self._source
        
    @property
    def source_dict(self):
        """Gets the source of this ApiResponseFilingAnswers.  # noqa: E501

        The organziation the answer data was sourced from as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The source of this ApiResponseFilingAnswers.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.source
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
            result = { 'source': value }

        
        return result
        

    @source.setter
    def source(self, source):
        """Sets the source of this ApiResponseFilingAnswers.

        The organziation the answer data was sourced from  # noqa: E501

        :param source: The source of this ApiResponseFilingAnswers.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def query(self):
        """Gets the query of this ApiResponseFilingAnswers.  # noqa: E501

        The query posed to the Thea API  # noqa: E501

        :return: The query of this ApiResponseFilingAnswers.  # noqa: E501
        :rtype: str
        """
        return self._query
        
    @property
    def query_dict(self):
        """Gets the query of this ApiResponseFilingAnswers.  # noqa: E501

        The query posed to the Thea API as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The query of this ApiResponseFilingAnswers.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.query
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
            result = { 'query': value }

        
        return result
        

    @query.setter
    def query(self, query):
        """Sets the query of this ApiResponseFilingAnswers.

        The query posed to the Thea API  # noqa: E501

        :param query: The query of this ApiResponseFilingAnswers.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def answers(self):
        """Gets the answers of this ApiResponseFilingAnswers.  # noqa: E501


        :return: The answers of this ApiResponseFilingAnswers.  # noqa: E501
        :rtype: list[TheaEntityAnswer]
        """
        return self._answers
        
    @property
    def answers_dict(self):
        """Gets the answers of this ApiResponseFilingAnswers.  # noqa: E501


        :return: The answers of this ApiResponseFilingAnswers.  # noqa: E501
        :rtype: list[TheaEntityAnswer]
        """

        result = None

        value = self.answers
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
            result = { 'answers': value }

        
        return result
        

    @answers.setter
    def answers(self, answers):
        """Sets the answers of this ApiResponseFilingAnswers.


        :param answers: The answers of this ApiResponseFilingAnswers.  # noqa: E501
        :type: list[TheaEntityAnswer]
        """

        self._answers = answers

    @property
    def companies(self):
        """Gets the companies of this ApiResponseFilingAnswers.  # noqa: E501


        :return: The companies of this ApiResponseFilingAnswers.  # noqa: E501
        :rtype: list[Filing]
        """
        return self._companies
        
    @property
    def companies_dict(self):
        """Gets the companies of this ApiResponseFilingAnswers.  # noqa: E501


        :return: The companies of this ApiResponseFilingAnswers.  # noqa: E501
        :rtype: list[Filing]
        """

        result = None

        value = self.companies
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
            result = { 'companies': value }

        
        return result
        

    @companies.setter
    def companies(self, companies):
        """Sets the companies of this ApiResponseFilingAnswers.


        :param companies: The companies of this ApiResponseFilingAnswers.  # noqa: E501
        :type: list[Filing]
        """

        self._companies = companies

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
        if not isinstance(other, ApiResponseFilingAnswers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
