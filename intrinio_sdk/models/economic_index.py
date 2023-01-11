# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.34.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EconomicIndex(object):
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
        'symbol': 'str',
        'name': 'str',
        'continent': 'str',
        'country': 'str',
        'update_frequency': 'str',
        'last_updated': 'datetime',
        'description': 'str',
        'observation_start': 'date',
        'observation_end': 'date',
        'seasonal_adjustment': 'str',
        'units': 'str'
    }

    attribute_map = {
        'id': 'id',
        'symbol': 'symbol',
        'name': 'name',
        'continent': 'continent',
        'country': 'country',
        'update_frequency': 'update_frequency',
        'last_updated': 'last_updated',
        'description': 'description',
        'observation_start': 'observation_start',
        'observation_end': 'observation_end',
        'seasonal_adjustment': 'seasonal_adjustment',
        'units': 'units'
    }

    def __init__(self, id=None, symbol=None, name=None, continent=None, country=None, update_frequency=None, last_updated=None, description=None, observation_start=None, observation_end=None, seasonal_adjustment=None, units=None):  # noqa: E501
        """EconomicIndex - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._symbol = None
        self._name = None
        self._continent = None
        self._country = None
        self._update_frequency = None
        self._last_updated = None
        self._description = None
        self._observation_start = None
        self._observation_end = None
        self._seasonal_adjustment = None
        self._units = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if symbol is not None:
            self.symbol = symbol
        if name is not None:
            self.name = name
        if continent is not None:
            self.continent = continent
        if country is not None:
            self.country = country
        if update_frequency is not None:
            self.update_frequency = update_frequency
        if last_updated is not None:
            self.last_updated = last_updated
        if description is not None:
            self.description = description
        if observation_start is not None:
            self.observation_start = observation_start
        if observation_end is not None:
            self.observation_end = observation_end
        if seasonal_adjustment is not None:
            self.seasonal_adjustment = seasonal_adjustment
        if units is not None:
            self.units = units

    @property
    def id(self):
        """Gets the id of this EconomicIndex.  # noqa: E501

        The Intrinio ID for the Index  # noqa: E501

        :return: The id of this EconomicIndex.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this EconomicIndex.  # noqa: E501

        The Intrinio ID for the Index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this EconomicIndex.  # noqa: E501
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
        """Sets the id of this EconomicIndex.

        The Intrinio ID for the Index  # noqa: E501

        :param id: The id of this EconomicIndex.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def symbol(self):
        """Gets the symbol of this EconomicIndex.  # noqa: E501

        The symbol used to identify the Index  # noqa: E501

        :return: The symbol of this EconomicIndex.  # noqa: E501
        :rtype: str
        """
        return self._symbol
        
    @property
    def symbol_dict(self):
        """Gets the symbol of this EconomicIndex.  # noqa: E501

        The symbol used to identify the Index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The symbol of this EconomicIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.symbol
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
            result = { 'symbol': value }

        
        return result
        

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this EconomicIndex.

        The symbol used to identify the Index  # noqa: E501

        :param symbol: The symbol of this EconomicIndex.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def name(self):
        """Gets the name of this EconomicIndex.  # noqa: E501

        The name of the Index  # noqa: E501

        :return: The name of this EconomicIndex.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this EconomicIndex.  # noqa: E501

        The name of the Index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this EconomicIndex.  # noqa: E501
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
        """Sets the name of this EconomicIndex.

        The name of the Index  # noqa: E501

        :param name: The name of this EconomicIndex.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def continent(self):
        """Gets the continent of this EconomicIndex.  # noqa: E501

        The continent of the country of focus for the Index  # noqa: E501

        :return: The continent of this EconomicIndex.  # noqa: E501
        :rtype: str
        """
        return self._continent
        
    @property
    def continent_dict(self):
        """Gets the continent of this EconomicIndex.  # noqa: E501

        The continent of the country of focus for the Index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The continent of this EconomicIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.continent
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
            result = { 'continent': value }

        
        return result
        

    @continent.setter
    def continent(self, continent):
        """Sets the continent of this EconomicIndex.

        The continent of the country of focus for the Index  # noqa: E501

        :param continent: The continent of this EconomicIndex.  # noqa: E501
        :type: str
        """

        self._continent = continent

    @property
    def country(self):
        """Gets the country of this EconomicIndex.  # noqa: E501

        The country of focus for the Index  # noqa: E501

        :return: The country of this EconomicIndex.  # noqa: E501
        :rtype: str
        """
        return self._country
        
    @property
    def country_dict(self):
        """Gets the country of this EconomicIndex.  # noqa: E501

        The country of focus for the Index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The country of this EconomicIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.country
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
            result = { 'country': value }

        
        return result
        

    @country.setter
    def country(self, country):
        """Sets the country of this EconomicIndex.

        The country of focus for the Index  # noqa: E501

        :param country: The country of this EconomicIndex.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def update_frequency(self):
        """Gets the update_frequency of this EconomicIndex.  # noqa: E501

        How often the Index is updated  # noqa: E501

        :return: The update_frequency of this EconomicIndex.  # noqa: E501
        :rtype: str
        """
        return self._update_frequency
        
    @property
    def update_frequency_dict(self):
        """Gets the update_frequency of this EconomicIndex.  # noqa: E501

        How often the Index is updated as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The update_frequency of this EconomicIndex.  # noqa: E501
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
        """Sets the update_frequency of this EconomicIndex.

        How often the Index is updated  # noqa: E501

        :param update_frequency: The update_frequency of this EconomicIndex.  # noqa: E501
        :type: str
        """

        self._update_frequency = update_frequency

    @property
    def last_updated(self):
        """Gets the last_updated of this EconomicIndex.  # noqa: E501

        When the Index was updated last  # noqa: E501

        :return: The last_updated of this EconomicIndex.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated
        
    @property
    def last_updated_dict(self):
        """Gets the last_updated of this EconomicIndex.  # noqa: E501

        When the Index was updated last as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_updated of this EconomicIndex.  # noqa: E501
        :rtype: datetime
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
        """Sets the last_updated of this EconomicIndex.

        When the Index was updated last  # noqa: E501

        :param last_updated: The last_updated of this EconomicIndex.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def description(self):
        """Gets the description of this EconomicIndex.  # noqa: E501

        A paragraph describing the index and its scope  # noqa: E501

        :return: The description of this EconomicIndex.  # noqa: E501
        :rtype: str
        """
        return self._description
        
    @property
    def description_dict(self):
        """Gets the description of this EconomicIndex.  # noqa: E501

        A paragraph describing the index and its scope as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The description of this EconomicIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.description
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
            result = { 'description': value }

        
        return result
        

    @description.setter
    def description(self, description):
        """Sets the description of this EconomicIndex.

        A paragraph describing the index and its scope  # noqa: E501

        :param description: The description of this EconomicIndex.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def observation_start(self):
        """Gets the observation_start of this EconomicIndex.  # noqa: E501

        The earliest date for which data is available  # noqa: E501

        :return: The observation_start of this EconomicIndex.  # noqa: E501
        :rtype: date
        """
        return self._observation_start
        
    @property
    def observation_start_dict(self):
        """Gets the observation_start of this EconomicIndex.  # noqa: E501

        The earliest date for which data is available as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The observation_start of this EconomicIndex.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.observation_start
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
            result = { 'observation_start': value }

        
        return result
        

    @observation_start.setter
    def observation_start(self, observation_start):
        """Sets the observation_start of this EconomicIndex.

        The earliest date for which data is available  # noqa: E501

        :param observation_start: The observation_start of this EconomicIndex.  # noqa: E501
        :type: date
        """

        self._observation_start = observation_start

    @property
    def observation_end(self):
        """Gets the observation_end of this EconomicIndex.  # noqa: E501

        The latest date for which data is available  # noqa: E501

        :return: The observation_end of this EconomicIndex.  # noqa: E501
        :rtype: date
        """
        return self._observation_end
        
    @property
    def observation_end_dict(self):
        """Gets the observation_end of this EconomicIndex.  # noqa: E501

        The latest date for which data is available as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The observation_end of this EconomicIndex.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.observation_end
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
            result = { 'observation_end': value }

        
        return result
        

    @observation_end.setter
    def observation_end(self, observation_end):
        """Sets the observation_end of this EconomicIndex.

        The latest date for which data is available  # noqa: E501

        :param observation_end: The observation_end of this EconomicIndex.  # noqa: E501
        :type: date
        """

        self._observation_end = observation_end

    @property
    def seasonal_adjustment(self):
        """Gets the seasonal_adjustment of this EconomicIndex.  # noqa: E501

        Whether the data is adjusted to account for seasonality  # noqa: E501

        :return: The seasonal_adjustment of this EconomicIndex.  # noqa: E501
        :rtype: str
        """
        return self._seasonal_adjustment
        
    @property
    def seasonal_adjustment_dict(self):
        """Gets the seasonal_adjustment of this EconomicIndex.  # noqa: E501

        Whether the data is adjusted to account for seasonality as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The seasonal_adjustment of this EconomicIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.seasonal_adjustment
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
            result = { 'seasonal_adjustment': value }

        
        return result
        

    @seasonal_adjustment.setter
    def seasonal_adjustment(self, seasonal_adjustment):
        """Sets the seasonal_adjustment of this EconomicIndex.

        Whether the data is adjusted to account for seasonality  # noqa: E501

        :param seasonal_adjustment: The seasonal_adjustment of this EconomicIndex.  # noqa: E501
        :type: str
        """

        self._seasonal_adjustment = seasonal_adjustment

    @property
    def units(self):
        """Gets the units of this EconomicIndex.  # noqa: E501

        The units of the data  # noqa: E501

        :return: The units of this EconomicIndex.  # noqa: E501
        :rtype: str
        """
        return self._units
        
    @property
    def units_dict(self):
        """Gets the units of this EconomicIndex.  # noqa: E501

        The units of the data as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The units of this EconomicIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.units
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
            result = { 'units': value }

        
        return result
        

    @units.setter
    def units(self, units):
        """Sets the units of this EconomicIndex.

        The units of the data  # noqa: E501

        :param units: The units of this EconomicIndex.  # noqa: E501
        :type: str
        """

        self._units = units

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
        if not isinstance(other, EconomicIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
