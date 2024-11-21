# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.75.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.bulk_download_links import BulkDownloadLinks  # noqa: F401,E501


class BulkDownloadSummary(object):
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
        'format': 'str',
        'data_length_bytes': 'str',
        'update_frequency': 'str',
        'last_updated': 'date',
        'links': 'list[BulkDownloadLinks]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'format': 'format',
        'data_length_bytes': 'data_length_bytes',
        'update_frequency': 'update_frequency',
        'last_updated': 'last_updated',
        'links': 'links'
    }

    def __init__(self, id=None, name=None, format=None, data_length_bytes=None, update_frequency=None, last_updated=None, links=None):  # noqa: E501
        """BulkDownloadSummary - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._format = None
        self._data_length_bytes = None
        self._update_frequency = None
        self._last_updated = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if format is not None:
            self.format = format
        if data_length_bytes is not None:
            self.data_length_bytes = data_length_bytes
        if update_frequency is not None:
            self.update_frequency = update_frequency
        if last_updated is not None:
            self.last_updated = last_updated
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this BulkDownloadSummary.  # noqa: E501

        The Intrinio ID of the bulk download  # noqa: E501

        :return: The id of this BulkDownloadSummary.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this BulkDownloadSummary.  # noqa: E501

        The Intrinio ID of the bulk download as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this BulkDownloadSummary.  # noqa: E501
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
        """Sets the id of this BulkDownloadSummary.

        The Intrinio ID of the bulk download  # noqa: E501

        :param id: The id of this BulkDownloadSummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BulkDownloadSummary.  # noqa: E501

        The name of the bulk download  # noqa: E501

        :return: The name of this BulkDownloadSummary.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this BulkDownloadSummary.  # noqa: E501

        The name of the bulk download as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this BulkDownloadSummary.  # noqa: E501
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
        """Sets the name of this BulkDownloadSummary.

        The name of the bulk download  # noqa: E501

        :param name: The name of this BulkDownloadSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def format(self):
        """Gets the format of this BulkDownloadSummary.  # noqa: E501

        The file format of the bulk download  # noqa: E501

        :return: The format of this BulkDownloadSummary.  # noqa: E501
        :rtype: str
        """
        return self._format
        
    @property
    def format_dict(self):
        """Gets the format of this BulkDownloadSummary.  # noqa: E501

        The file format of the bulk download as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The format of this BulkDownloadSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.format
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
            result = { 'format': value }

        
        return result
        

    @format.setter
    def format(self, format):
        """Sets the format of this BulkDownloadSummary.

        The file format of the bulk download  # noqa: E501

        :param format: The format of this BulkDownloadSummary.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def data_length_bytes(self):
        """Gets the data_length_bytes of this BulkDownloadSummary.  # noqa: E501

        The total length of the bulk download data in bytes  # noqa: E501

        :return: The data_length_bytes of this BulkDownloadSummary.  # noqa: E501
        :rtype: str
        """
        return self._data_length_bytes
        
    @property
    def data_length_bytes_dict(self):
        """Gets the data_length_bytes of this BulkDownloadSummary.  # noqa: E501

        The total length of the bulk download data in bytes as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The data_length_bytes of this BulkDownloadSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.data_length_bytes
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
            result = { 'data_length_bytes': value }

        
        return result
        

    @data_length_bytes.setter
    def data_length_bytes(self, data_length_bytes):
        """Sets the data_length_bytes of this BulkDownloadSummary.

        The total length of the bulk download data in bytes  # noqa: E501

        :param data_length_bytes: The data_length_bytes of this BulkDownloadSummary.  # noqa: E501
        :type: str
        """

        self._data_length_bytes = data_length_bytes

    @property
    def update_frequency(self):
        """Gets the update_frequency of this BulkDownloadSummary.  # noqa: E501

        The update frequency for the bulk download  # noqa: E501

        :return: The update_frequency of this BulkDownloadSummary.  # noqa: E501
        :rtype: str
        """
        return self._update_frequency
        
    @property
    def update_frequency_dict(self):
        """Gets the update_frequency of this BulkDownloadSummary.  # noqa: E501

        The update frequency for the bulk download as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The update_frequency of this BulkDownloadSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.update_frequency
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
            result = { 'update_frequency': value }

        
        return result
        

    @update_frequency.setter
    def update_frequency(self, update_frequency):
        """Sets the update_frequency of this BulkDownloadSummary.

        The update frequency for the bulk download  # noqa: E501

        :param update_frequency: The update_frequency of this BulkDownloadSummary.  # noqa: E501
        :type: str
        """

        self._update_frequency = update_frequency

    @property
    def last_updated(self):
        """Gets the last_updated of this BulkDownloadSummary.  # noqa: E501

        The date on which the bulk download was last updated  # noqa: E501

        :return: The last_updated of this BulkDownloadSummary.  # noqa: E501
        :rtype: date
        """
        return self._last_updated
        
    @property
    def last_updated_dict(self):
        """Gets the last_updated of this BulkDownloadSummary.  # noqa: E501

        The date on which the bulk download was last updated as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_updated of this BulkDownloadSummary.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.last_updated
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
            result = { 'last_updated': value }

        
        return result
        

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this BulkDownloadSummary.

        The date on which the bulk download was last updated  # noqa: E501

        :param last_updated: The last_updated of this BulkDownloadSummary.  # noqa: E501
        :type: date
        """

        self._last_updated = last_updated

    @property
    def links(self):
        """Gets the links of this BulkDownloadSummary.  # noqa: E501

        Links to all of the files comprising the bulk download. Links expire in 24 hours.  # noqa: E501

        :return: The links of this BulkDownloadSummary.  # noqa: E501
        :rtype: list[BulkDownloadLinks]
        """
        return self._links
        
    @property
    def links_dict(self):
        """Gets the links of this BulkDownloadSummary.  # noqa: E501

        Links to all of the files comprising the bulk download. Links expire in 24 hours. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The links of this BulkDownloadSummary.  # noqa: E501
        :rtype: list[BulkDownloadLinks]
        """

        result = None

        value = self.links
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
            result = { 'links': value }

        
        return result
        

    @links.setter
    def links(self, links):
        """Sets the links of this BulkDownloadSummary.

        Links to all of the files comprising the bulk download. Links expire in 24 hours.  # noqa: E501

        :param links: The links of this BulkDownloadSummary.  # noqa: E501
        :type: list[BulkDownloadLinks]
        """

        self._links = links

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
        if not isinstance(other, BulkDownloadSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
