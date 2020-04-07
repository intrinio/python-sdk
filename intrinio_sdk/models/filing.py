# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501


class Filing(object):
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
        'filing_date': 'date',
        'accepted_date': 'datetime',
        'period_end_date': 'date',
        'report_type': 'str',
        'sec_unique_id': 'str',
        'filing_url': 'str',
        'report_url': 'str',
        'instance_url': 'str',
        'industry_category': 'str',
        'industry_group': 'str',
        'word_count': 'int',
        'company': 'CompanySummary'
    }

    attribute_map = {
        'id': 'id',
        'filing_date': 'filing_date',
        'accepted_date': 'accepted_date',
        'period_end_date': 'period_end_date',
        'report_type': 'report_type',
        'sec_unique_id': 'sec_unique_id',
        'filing_url': 'filing_url',
        'report_url': 'report_url',
        'instance_url': 'instance_url',
        'industry_category': 'industry_category',
        'industry_group': 'industry_group',
        'word_count': 'word_count',
        'company': 'company'
    }

    def __init__(self, id=None, filing_date=None, accepted_date=None, period_end_date=None, report_type=None, sec_unique_id=None, filing_url=None, report_url=None, instance_url=None, industry_category=None, industry_group=None, word_count=None, company=None):  # noqa: E501
        """Filing - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._filing_date = None
        self._accepted_date = None
        self._period_end_date = None
        self._report_type = None
        self._sec_unique_id = None
        self._filing_url = None
        self._report_url = None
        self._instance_url = None
        self._industry_category = None
        self._industry_group = None
        self._word_count = None
        self._company = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if filing_date is not None:
            self.filing_date = filing_date
        if accepted_date is not None:
            self.accepted_date = accepted_date
        if period_end_date is not None:
            self.period_end_date = period_end_date
        if report_type is not None:
            self.report_type = report_type
        if sec_unique_id is not None:
            self.sec_unique_id = sec_unique_id
        if filing_url is not None:
            self.filing_url = filing_url
        if report_url is not None:
            self.report_url = report_url
        if instance_url is not None:
            self.instance_url = instance_url
        if industry_category is not None:
            self.industry_category = industry_category
        if industry_group is not None:
            self.industry_group = industry_group
        if word_count is not None:
            self.word_count = word_count
        if company is not None:
            self.company = company

    @property
    def id(self):
        """Gets the id of this Filing.  # noqa: E501

        The Intrinio ID of the Filing  # noqa: E501

        :return: The id of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this Filing.  # noqa: E501

        The Intrinio ID of the Filing as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this Filing.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.id
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
            result = { 'id': value }

        
        return result
        

    @id.setter
    def id(self, id):
        """Sets the id of this Filing.

        The Intrinio ID of the Filing  # noqa: E501

        :param id: The id of this Filing.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def filing_date(self):
        """Gets the filing_date of this Filing.  # noqa: E501

        The date when the filing was submitted to the SEC by the company  # noqa: E501

        :return: The filing_date of this Filing.  # noqa: E501
        :rtype: date
        """
        return self._filing_date
        
    @property
    def filing_date_dict(self):
        """Gets the filing_date of this Filing.  # noqa: E501

        The date when the filing was submitted to the SEC by the company as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The filing_date of this Filing.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.filing_date
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
            result = { 'filing_date': value }

        
        return result
        

    @filing_date.setter
    def filing_date(self, filing_date):
        """Sets the filing_date of this Filing.

        The date when the filing was submitted to the SEC by the company  # noqa: E501

        :param filing_date: The filing_date of this Filing.  # noqa: E501
        :type: date
        """

        self._filing_date = filing_date

    @property
    def accepted_date(self):
        """Gets the accepted_date of this Filing.  # noqa: E501

        The date and time when the filing was accepted by SEC  # noqa: E501

        :return: The accepted_date of this Filing.  # noqa: E501
        :rtype: datetime
        """
        return self._accepted_date
        
    @property
    def accepted_date_dict(self):
        """Gets the accepted_date of this Filing.  # noqa: E501

        The date and time when the filing was accepted by SEC as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The accepted_date of this Filing.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.accepted_date
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
            result = { 'accepted_date': value }

        
        return result
        

    @accepted_date.setter
    def accepted_date(self, accepted_date):
        """Sets the accepted_date of this Filing.

        The date and time when the filing was accepted by SEC  # noqa: E501

        :param accepted_date: The accepted_date of this Filing.  # noqa: E501
        :type: datetime
        """

        self._accepted_date = accepted_date

    @property
    def period_end_date(self):
        """Gets the period_end_date of this Filing.  # noqa: E501

        The ending date of the fiscal period for the filing  # noqa: E501

        :return: The period_end_date of this Filing.  # noqa: E501
        :rtype: date
        """
        return self._period_end_date
        
    @property
    def period_end_date_dict(self):
        """Gets the period_end_date of this Filing.  # noqa: E501

        The ending date of the fiscal period for the filing as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The period_end_date of this Filing.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.period_end_date
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
            result = { 'period_end_date': value }

        
        return result
        

    @period_end_date.setter
    def period_end_date(self, period_end_date):
        """Sets the period_end_date of this Filing.

        The ending date of the fiscal period for the filing  # noqa: E501

        :param period_end_date: The period_end_date of this Filing.  # noqa: E501
        :type: date
        """

        self._period_end_date = period_end_date

    @property
    def report_type(self):
        """Gets the report_type of this Filing.  # noqa: E501

        The filing <a href=\"https://docs.intrinio.com/documentation/sec_filing_report_types\" target=\"_blank\">report type</a>  # noqa: E501

        :return: The report_type of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._report_type
        
    @property
    def report_type_dict(self):
        """Gets the report_type of this Filing.  # noqa: E501

        The filing <a href=\"https://docs.intrinio.com/documentation/sec_filing_report_types\" target=\"_blank\">report type</a> as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The report_type of this Filing.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.report_type
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
            result = { 'report_type': value }

        
        return result
        

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this Filing.

        The filing <a href=\"https://docs.intrinio.com/documentation/sec_filing_report_types\" target=\"_blank\">report type</a>  # noqa: E501

        :param report_type: The report_type of this Filing.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def sec_unique_id(self):
        """Gets the sec_unique_id of this Filing.  # noqa: E501

        A unique identifier for the filing provided by the SEC  # noqa: E501

        :return: The sec_unique_id of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._sec_unique_id
        
    @property
    def sec_unique_id_dict(self):
        """Gets the sec_unique_id of this Filing.  # noqa: E501

        A unique identifier for the filing provided by the SEC as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sec_unique_id of this Filing.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.sec_unique_id
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
            result = { 'sec_unique_id': value }

        
        return result
        

    @sec_unique_id.setter
    def sec_unique_id(self, sec_unique_id):
        """Sets the sec_unique_id of this Filing.

        A unique identifier for the filing provided by the SEC  # noqa: E501

        :param sec_unique_id: The sec_unique_id of this Filing.  # noqa: E501
        :type: str
        """

        self._sec_unique_id = sec_unique_id

    @property
    def filing_url(self):
        """Gets the filing_url of this Filing.  # noqa: E501

        The URL to the filing page on the SEC site  # noqa: E501

        :return: The filing_url of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._filing_url
        
    @property
    def filing_url_dict(self):
        """Gets the filing_url of this Filing.  # noqa: E501

        The URL to the filing page on the SEC site as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The filing_url of this Filing.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.filing_url
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
            result = { 'filing_url': value }

        
        return result
        

    @filing_url.setter
    def filing_url(self, filing_url):
        """Sets the filing_url of this Filing.

        The URL to the filing page on the SEC site  # noqa: E501

        :param filing_url: The filing_url of this Filing.  # noqa: E501
        :type: str
        """

        self._filing_url = filing_url

    @property
    def report_url(self):
        """Gets the report_url of this Filing.  # noqa: E501

        The URL to the actual report on the SEC site  # noqa: E501

        :return: The report_url of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._report_url
        
    @property
    def report_url_dict(self):
        """Gets the report_url of this Filing.  # noqa: E501

        The URL to the actual report on the SEC site as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The report_url of this Filing.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.report_url
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
            result = { 'report_url': value }

        
        return result
        

    @report_url.setter
    def report_url(self, report_url):
        """Sets the report_url of this Filing.

        The URL to the actual report on the SEC site  # noqa: E501

        :param report_url: The report_url of this Filing.  # noqa: E501
        :type: str
        """

        self._report_url = report_url

    @property
    def instance_url(self):
        """Gets the instance_url of this Filing.  # noqa: E501

        The URL for the XBRL filing for the report  # noqa: E501

        :return: The instance_url of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._instance_url
        
    @property
    def instance_url_dict(self):
        """Gets the instance_url of this Filing.  # noqa: E501

        The URL for the XBRL filing for the report as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The instance_url of this Filing.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.instance_url
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
            result = { 'instance_url': value }

        
        return result
        

    @instance_url.setter
    def instance_url(self, instance_url):
        """Sets the instance_url of this Filing.

        The URL for the XBRL filing for the report  # noqa: E501

        :param instance_url: The instance_url of this Filing.  # noqa: E501
        :type: str
        """

        self._instance_url = instance_url

    @property
    def industry_category(self):
        """Gets the industry_category of this Filing.  # noqa: E501

        The company's operating industry category  # noqa: E501

        :return: The industry_category of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._industry_category
        
    @property
    def industry_category_dict(self):
        """Gets the industry_category of this Filing.  # noqa: E501

        The company's operating industry category as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The industry_category of this Filing.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.industry_category
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
            result = { 'industry_category': value }

        
        return result
        

    @industry_category.setter
    def industry_category(self, industry_category):
        """Sets the industry_category of this Filing.

        The company's operating industry category  # noqa: E501

        :param industry_category: The industry_category of this Filing.  # noqa: E501
        :type: str
        """

        self._industry_category = industry_category

    @property
    def industry_group(self):
        """Gets the industry_group of this Filing.  # noqa: E501

        The company's operating industry group  # noqa: E501

        :return: The industry_group of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._industry_group
        
    @property
    def industry_group_dict(self):
        """Gets the industry_group of this Filing.  # noqa: E501

        The company's operating industry group as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The industry_group of this Filing.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.industry_group
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
            result = { 'industry_group': value }

        
        return result
        

    @industry_group.setter
    def industry_group(self, industry_group):
        """Sets the industry_group of this Filing.

        The company's operating industry group  # noqa: E501

        :param industry_group: The industry_group of this Filing.  # noqa: E501
        :type: str
        """

        self._industry_group = industry_group

    @property
    def word_count(self):
        """Gets the word_count of this Filing.  # noqa: E501

        The number of words in the filing  # noqa: E501

        :return: The word_count of this Filing.  # noqa: E501
        :rtype: int
        """
        return self._word_count
        
    @property
    def word_count_dict(self):
        """Gets the word_count of this Filing.  # noqa: E501

        The number of words in the filing as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The word_count of this Filing.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.word_count
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
            result = { 'word_count': value }

        
        return result
        

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this Filing.

        The number of words in the filing  # noqa: E501

        :param word_count: The word_count of this Filing.  # noqa: E501
        :type: int
        """

        self._word_count = word_count

    @property
    def company(self):
        """Gets the company of this Filing.  # noqa: E501


        :return: The company of this Filing.  # noqa: E501
        :rtype: CompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this Filing.  # noqa: E501


        :return: The company of this Filing.  # noqa: E501
        :rtype: CompanySummary
        """

        result = None

        value = self.company
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
            result = { 'company': value }

        
        return result
        

    @company.setter
    def company(self, company):
        """Sets the company of this Filing.


        :param company: The company of this Filing.  # noqa: E501
        :type: CompanySummary
        """

        self._company = company

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
        if not isinstance(other, Filing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
