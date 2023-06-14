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

from intrinio_sdk.models.option_snapshot_group import OptionSnapshotGroup  # noqa: F401,E501


class OptionSnapshotsResult(object):
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
        'snapshots': 'list[OptionSnapshotGroup]'
    }

    attribute_map = {
        'snapshots': 'snapshots'
    }

    def __init__(self, snapshots=None):  # noqa: E501
        """OptionSnapshotsResult - a model defined in Swagger"""  # noqa: E501

        self._snapshots = None
        self.discriminator = None

        if snapshots is not None:
            self.snapshots = snapshots

    @property
    def snapshots(self):
        """Gets the snapshots of this OptionSnapshotsResult.  # noqa: E501

        List of all the snapshot groups comprising the queried result.  # noqa: E501

        :return: The snapshots of this OptionSnapshotsResult.  # noqa: E501
        :rtype: list[OptionSnapshotGroup]
        """
        return self._snapshots
        
    @property
    def snapshots_dict(self):
        """Gets the snapshots of this OptionSnapshotsResult.  # noqa: E501

        List of all the snapshot groups comprising the queried result. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The snapshots of this OptionSnapshotsResult.  # noqa: E501
        :rtype: list[OptionSnapshotGroup]
        """

        result = None

        value = self.snapshots
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
            result = { 'snapshots': value }

        
        return result
        

    @snapshots.setter
    def snapshots(self, snapshots):
        """Sets the snapshots of this OptionSnapshotsResult.

        List of all the snapshot groups comprising the queried result.  # noqa: E501

        :param snapshots: The snapshots of this OptionSnapshotsResult.  # noqa: E501
        :type: list[OptionSnapshotGroup]
        """

        self._snapshots = snapshots

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
        if not isinstance(other, OptionSnapshotsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
