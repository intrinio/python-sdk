# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.63.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OptionSnapshotGroup(object):
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
        'time': 'datetime',
        'files': 'list[object]'
    }

    attribute_map = {
        'time': 'time',
        'files': 'files'
    }

    def __init__(self, time=None, files=None):  # noqa: E501
        """OptionSnapshotGroup - a model defined in Swagger"""  # noqa: E501

        self._time = None
        self._files = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if files is not None:
            self.files = files

    @property
    def time(self):
        """Gets the time of this OptionSnapshotGroup.  # noqa: E501

        The UTC timestamp of this snapshot group.  # noqa: E501

        :return: The time of this OptionSnapshotGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._time
        
    @property
    def time_dict(self):
        """Gets the time of this OptionSnapshotGroup.  # noqa: E501

        The UTC timestamp of this snapshot group. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The time of this OptionSnapshotGroup.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.time
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
            result = { 'time': value }

        
        return result
        

    @time.setter
    def time(self, time):
        """Sets the time of this OptionSnapshotGroup.

        The UTC timestamp of this snapshot group.  # noqa: E501

        :param time: The time of this OptionSnapshotGroup.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def files(self):
        """Gets the files of this OptionSnapshotGroup.  # noqa: E501

        List of all the snapshot parts of this group.  # noqa: E501

        :return: The files of this OptionSnapshotGroup.  # noqa: E501
        :rtype: list[object]
        """
        return self._files
        
    @property
    def files_dict(self):
        """Gets the files of this OptionSnapshotGroup.  # noqa: E501

        List of all the snapshot parts of this group. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The files of this OptionSnapshotGroup.  # noqa: E501
        :rtype: list[object]
        """

        result = None

        value = self.files
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
            result = { 'files': value }

        
        return result
        

    @files.setter
    def files(self, files):
        """Sets the files of this OptionSnapshotGroup.

        List of all the snapshot parts of this group.  # noqa: E501

        :param files: The files of this OptionSnapshotGroup.  # noqa: E501
        :type: list[object]
        """

        self._files = files

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
        if not isinstance(other, OptionSnapshotGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
