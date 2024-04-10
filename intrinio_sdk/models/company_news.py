# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.56.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501
from intrinio_sdk.models.news_topic import NewsTopic  # noqa: F401,E501


class CompanyNews(object):
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
        'title': 'str',
        'publication_date': 'datetime',
        'url': 'str',
        'summary': 'str',
        'source': 'str',
        'company': 'CompanySummary',
        'topics': 'list[NewsTopic]',
        'copyright': 'str',
        'language': 'str',
        'word_count': 'int',
        'spam': 'bool',
        'business_relevance': 'float',
        'article_sentiment': 'str',
        'article_sentiment_confidence': 'float'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'publication_date': 'publication_date',
        'url': 'url',
        'summary': 'summary',
        'source': 'source',
        'company': 'company',
        'topics': 'topics',
        'copyright': 'copyright',
        'language': 'language',
        'word_count': 'word_count',
        'spam': 'spam',
        'business_relevance': 'business_relevance',
        'article_sentiment': 'article_sentiment',
        'article_sentiment_confidence': 'article_sentiment_confidence'
    }

    def __init__(self, id=None, title=None, publication_date=None, url=None, summary=None, source=None, company=None, topics=None, copyright=None, language=None, word_count=None, spam=None, business_relevance=None, article_sentiment=None, article_sentiment_confidence=None):  # noqa: E501
        """CompanyNews - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._publication_date = None
        self._url = None
        self._summary = None
        self._source = None
        self._company = None
        self._topics = None
        self._copyright = None
        self._language = None
        self._word_count = None
        self._spam = None
        self._business_relevance = None
        self._article_sentiment = None
        self._article_sentiment_confidence = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if publication_date is not None:
            self.publication_date = publication_date
        if url is not None:
            self.url = url
        if summary is not None:
            self.summary = summary
        if source is not None:
            self.source = source
        if company is not None:
            self.company = company
        if topics is not None:
            self.topics = topics
        if copyright is not None:
            self.copyright = copyright
        if language is not None:
            self.language = language
        if word_count is not None:
            self.word_count = word_count
        if spam is not None:
            self.spam = spam
        if business_relevance is not None:
            self.business_relevance = business_relevance
        if article_sentiment is not None:
            self.article_sentiment = article_sentiment
        if article_sentiment_confidence is not None:
            self.article_sentiment_confidence = article_sentiment_confidence

    @property
    def id(self):
        """Gets the id of this CompanyNews.  # noqa: E501

        The Intrinio ID for the news article  # noqa: E501

        :return: The id of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this CompanyNews.  # noqa: E501

        The Intrinio ID for the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this CompanyNews.  # noqa: E501
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
        """Sets the id of this CompanyNews.

        The Intrinio ID for the news article  # noqa: E501

        :param id: The id of this CompanyNews.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this CompanyNews.  # noqa: E501

        The title of the news article  # noqa: E501

        :return: The title of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._title
        
    @property
    def title_dict(self):
        """Gets the title of this CompanyNews.  # noqa: E501

        The title of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The title of this CompanyNews.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.title
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
            result = { 'title': value }

        
        return result
        

    @title.setter
    def title(self, title):
        """Sets the title of this CompanyNews.

        The title of the news article  # noqa: E501

        :param title: The title of this CompanyNews.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def publication_date(self):
        """Gets the publication_date of this CompanyNews.  # noqa: E501

        The publication date of the news article  # noqa: E501

        :return: The publication_date of this CompanyNews.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date
        
    @property
    def publication_date_dict(self):
        """Gets the publication_date of this CompanyNews.  # noqa: E501

        The publication date of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The publication_date of this CompanyNews.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.publication_date
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
            result = { 'publication_date': value }

        
        return result
        

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this CompanyNews.

        The publication date of the news article  # noqa: E501

        :param publication_date: The publication_date of this CompanyNews.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def url(self):
        """Gets the url of this CompanyNews.  # noqa: E501

        The url of the news article  # noqa: E501

        :return: The url of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._url
        
    @property
    def url_dict(self):
        """Gets the url of this CompanyNews.  # noqa: E501

        The url of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The url of this CompanyNews.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.url
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
            result = { 'url': value }

        
        return result
        

    @url.setter
    def url(self, url):
        """Sets the url of this CompanyNews.

        The url of the news article  # noqa: E501

        :param url: The url of this CompanyNews.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def summary(self):
        """Gets the summary of this CompanyNews.  # noqa: E501

        A summary of the news article  # noqa: E501

        :return: The summary of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._summary
        
    @property
    def summary_dict(self):
        """Gets the summary of this CompanyNews.  # noqa: E501

        A summary of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The summary of this CompanyNews.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.summary
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
            result = { 'summary': value }

        
        return result
        

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this CompanyNews.

        A summary of the news article  # noqa: E501

        :param summary: The summary of this CompanyNews.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def source(self):
        """Gets the source of this CompanyNews.  # noqa: E501

        The news source.  # noqa: E501

        :return: The source of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._source
        
    @property
    def source_dict(self):
        """Gets the source of this CompanyNews.  # noqa: E501

        The news source. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The source of this CompanyNews.  # noqa: E501
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
        """Sets the source of this CompanyNews.

        The news source.  # noqa: E501

        :param source: The source of this CompanyNews.  # noqa: E501
        :type: str
        """
        allowed_values = ["yahoo", "moody", "moody_us_news", "moody_us_press_releases"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def company(self):
        """Gets the company of this CompanyNews.  # noqa: E501

        The Company to which the new article pertains  # noqa: E501

        :return: The company of this CompanyNews.  # noqa: E501
        :rtype: CompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this CompanyNews.  # noqa: E501

        The Company to which the new article pertains as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The company of this CompanyNews.  # noqa: E501
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
        """Sets the company of this CompanyNews.

        The Company to which the new article pertains  # noqa: E501

        :param company: The company of this CompanyNews.  # noqa: E501
        :type: CompanySummary
        """

        self._company = company

    @property
    def topics(self):
        """Gets the topics of this CompanyNews.  # noqa: E501


        :return: The topics of this CompanyNews.  # noqa: E501
        :rtype: list[NewsTopic]
        """
        return self._topics
        
    @property
    def topics_dict(self):
        """Gets the topics of this CompanyNews.  # noqa: E501


        :return: The topics of this CompanyNews.  # noqa: E501
        :rtype: list[NewsTopic]
        """

        result = None

        value = self.topics
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
            result = { 'topics': value }

        
        return result
        

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this CompanyNews.


        :param topics: The topics of this CompanyNews.  # noqa: E501
        :type: list[NewsTopic]
        """

        self._topics = topics

    @property
    def copyright(self):
        """Gets the copyright of this CompanyNews.  # noqa: E501

        The copyright of the news article  # noqa: E501

        :return: The copyright of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._copyright
        
    @property
    def copyright_dict(self):
        """Gets the copyright of this CompanyNews.  # noqa: E501

        The copyright of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The copyright of this CompanyNews.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.copyright
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
            result = { 'copyright': value }

        
        return result
        

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this CompanyNews.

        The copyright of the news article  # noqa: E501

        :param copyright: The copyright of this CompanyNews.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def language(self):
        """Gets the language of this CompanyNews.  # noqa: E501

        The language code of the news article  # noqa: E501

        :return: The language of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._language
        
    @property
    def language_dict(self):
        """Gets the language of this CompanyNews.  # noqa: E501

        The language code of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The language of this CompanyNews.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.language
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
            result = { 'language': value }

        
        return result
        

    @language.setter
    def language(self, language):
        """Sets the language of this CompanyNews.

        The language code of the news article  # noqa: E501

        :param language: The language of this CompanyNews.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def word_count(self):
        """Gets the word_count of this CompanyNews.  # noqa: E501

        The word count of the news article  # noqa: E501

        :return: The word_count of this CompanyNews.  # noqa: E501
        :rtype: int
        """
        return self._word_count
        
    @property
    def word_count_dict(self):
        """Gets the word_count of this CompanyNews.  # noqa: E501

        The word count of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The word_count of this CompanyNews.  # noqa: E501
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
        """Sets the word_count of this CompanyNews.

        The word count of the news article  # noqa: E501

        :param word_count: The word_count of this CompanyNews.  # noqa: E501
        :type: int
        """

        self._word_count = word_count

    @property
    def spam(self):
        """Gets the spam of this CompanyNews.  # noqa: E501

        Whether the news article is marked as spam or not  # noqa: E501

        :return: The spam of this CompanyNews.  # noqa: E501
        :rtype: bool
        """
        return self._spam
        
    @property
    def spam_dict(self):
        """Gets the spam of this CompanyNews.  # noqa: E501

        Whether the news article is marked as spam or not as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The spam of this CompanyNews.  # noqa: E501
        :rtype: bool
        """

        result = None

        value = self.spam
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
            result = { 'spam': value }

        
        return result
        

    @spam.setter
    def spam(self, spam):
        """Sets the spam of this CompanyNews.

        Whether the news article is marked as spam or not  # noqa: E501

        :param spam: The spam of this CompanyNews.  # noqa: E501
        :type: bool
        """

        self._spam = spam

    @property
    def business_relevance(self):
        """Gets the business_relevance of this CompanyNews.  # noqa: E501

        How strongly correlated the news article is to the business  # noqa: E501

        :return: The business_relevance of this CompanyNews.  # noqa: E501
        :rtype: float
        """
        return self._business_relevance
        
    @property
    def business_relevance_dict(self):
        """Gets the business_relevance of this CompanyNews.  # noqa: E501

        How strongly correlated the news article is to the business as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The business_relevance of this CompanyNews.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.business_relevance
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
            result = { 'business_relevance': value }

        
        return result
        

    @business_relevance.setter
    def business_relevance(self, business_relevance):
        """Sets the business_relevance of this CompanyNews.

        How strongly correlated the news article is to the business  # noqa: E501

        :param business_relevance: The business_relevance of this CompanyNews.  # noqa: E501
        :type: float
        """

        self._business_relevance = business_relevance

    @property
    def article_sentiment(self):
        """Gets the article_sentiment of this CompanyNews.  # noqa: E501

        The news sentiment.  # noqa: E501

        :return: The article_sentiment of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._article_sentiment
        
    @property
    def article_sentiment_dict(self):
        """Gets the article_sentiment of this CompanyNews.  # noqa: E501

        The news sentiment. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The article_sentiment of this CompanyNews.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.article_sentiment
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
            result = { 'article_sentiment': value }

        
        return result
        

    @article_sentiment.setter
    def article_sentiment(self, article_sentiment):
        """Sets the article_sentiment of this CompanyNews.

        The news sentiment.  # noqa: E501

        :param article_sentiment: The article_sentiment of this CompanyNews.  # noqa: E501
        :type: str
        """
        allowed_values = ["positive", "neutral", "negative"]  # noqa: E501
        if article_sentiment not in allowed_values:
            raise ValueError(
                "Invalid value for `article_sentiment` ({0}), must be one of {1}"  # noqa: E501
                .format(article_sentiment, allowed_values)
            )

        self._article_sentiment = article_sentiment

    @property
    def article_sentiment_confidence(self):
        """Gets the article_sentiment_confidence of this CompanyNews.  # noqa: E501

        The confidence score of the sentiment rating  # noqa: E501

        :return: The article_sentiment_confidence of this CompanyNews.  # noqa: E501
        :rtype: float
        """
        return self._article_sentiment_confidence
        
    @property
    def article_sentiment_confidence_dict(self):
        """Gets the article_sentiment_confidence of this CompanyNews.  # noqa: E501

        The confidence score of the sentiment rating as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The article_sentiment_confidence of this CompanyNews.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.article_sentiment_confidence
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
            result = { 'article_sentiment_confidence': value }

        
        return result
        

    @article_sentiment_confidence.setter
    def article_sentiment_confidence(self, article_sentiment_confidence):
        """Sets the article_sentiment_confidence of this CompanyNews.

        The confidence score of the sentiment rating  # noqa: E501

        :param article_sentiment_confidence: The article_sentiment_confidence of this CompanyNews.  # noqa: E501
        :type: float
        """

        self._article_sentiment_confidence = article_sentiment_confidence

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
        if not isinstance(other, CompanyNews):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
