# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class PowerSchedule(object):
    """NOTE: This class is auto-generated. Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'mode': 'str',
        'weekday_end_time_hour': 'int',
        'weekday_end_time_minutes': 'int',
        'weekday_start_time_hour': 'int',
        'weekday_start_time_minutes': 'int',
        'weekend_end_time_hour': 'int',
        'weekend_end_time_minutes': 'int',
        'weekend_start_time_hour': 'int',
        'weekend_start_time_minutes': 'int'
    }

    attribute_map = {
        'mode': 'mode',
        'weekday_end_time_hour': 'weekdayEndTimeHour',
        'weekday_end_time_minutes': 'weekdayEndTimeMinutes',
        'weekday_start_time_hour': 'weekdayStartTimeHour',
        'weekday_start_time_minutes': 'weekdayStartTimeMinutes',
        'weekend_end_time_hour': 'weekendEndTimeHour',
        'weekend_end_time_minutes': 'weekendEndTimeMinutes',
        'weekend_start_time_hour': 'weekendStartTimeHour',
        'weekend_start_time_minutes': 'weekendStartTimeMinutes'
    }

    def __init__(self, mode=None, weekday_end_time_hour=None, weekday_end_time_minutes=None, weekday_start_time_hour=None, weekday_start_time_minutes=None, weekend_end_time_hour=None, weekend_end_time_minutes=None, weekend_start_time_hour=None, weekend_start_time_minutes=None, local_vars_configuration=None):  # noqa: E501
        """PowerSchedule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mode = None
        self._weekday_end_time_hour = None
        self._weekday_end_time_minutes = None
        self._weekday_start_time_hour = None
        self._weekday_start_time_minutes = None
        self._weekend_end_time_hour = None
        self._weekend_end_time_minutes = None
        self._weekend_start_time_hour = None
        self._weekend_start_time_minutes = None
        self.discriminator = None

        self.mode = mode
        if weekday_end_time_hour is not None:
            self.weekday_end_time_hour = weekday_end_time_hour
        if weekday_end_time_minutes is not None:
            self.weekday_end_time_minutes = weekday_end_time_minutes
        if weekday_start_time_hour is not None:
            self.weekday_start_time_hour = weekday_start_time_hour
        if weekday_start_time_minutes is not None:
            self.weekday_start_time_minutes = weekday_start_time_minutes
        if weekend_end_time_hour is not None:
            self.weekend_end_time_hour = weekend_end_time_hour
        if weekend_end_time_minutes is not None:
            self.weekend_end_time_minutes = weekend_end_time_minutes
        if weekend_start_time_hour is not None:
            self.weekend_start_time_hour = weekend_start_time_hour
        if weekend_start_time_minutes is not None:
            self.weekend_start_time_minutes = weekend_start_time_minutes

    @property
    def mode(self):
        """Gets the mode of this PowerSchedule.  # noqa: E501


        :return: The mode of this PowerSchedule.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this PowerSchedule.


        :param mode: The mode of this PowerSchedule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mode is None:  # noqa: E501
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["NONE", "ECO_MODE", "LOW_COST", "WEEKEND_SHUTDOWN", "CUSTOM"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def weekday_end_time_hour(self):
        """Gets the weekday_end_time_hour of this PowerSchedule.  # noqa: E501


        :return: The weekday_end_time_hour of this PowerSchedule.  # noqa: E501
        :rtype: int
        """
        return self._weekday_end_time_hour

    @weekday_end_time_hour.setter
    def weekday_end_time_hour(self, weekday_end_time_hour):
        """Sets the weekday_end_time_hour of this PowerSchedule.


        :param weekday_end_time_hour: The weekday_end_time_hour of this PowerSchedule.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                weekday_end_time_hour is not None and weekday_end_time_hour > 23):  # noqa: E501
            raise ValueError("Invalid value for `weekday_end_time_hour`, must be a value less than or equal to `23`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                weekday_end_time_hour is not None and weekday_end_time_hour < 0):  # noqa: E501
            raise ValueError("Invalid value for `weekday_end_time_hour`, must be a value greater than or equal to `0`")  # noqa: E501

        self._weekday_end_time_hour = weekday_end_time_hour

    @property
    def weekday_end_time_minutes(self):
        """Gets the weekday_end_time_minutes of this PowerSchedule.  # noqa: E501


        :return: The weekday_end_time_minutes of this PowerSchedule.  # noqa: E501
        :rtype: int
        """
        return self._weekday_end_time_minutes

    @weekday_end_time_minutes.setter
    def weekday_end_time_minutes(self, weekday_end_time_minutes):
        """Sets the weekday_end_time_minutes of this PowerSchedule.


        :param weekday_end_time_minutes: The weekday_end_time_minutes of this PowerSchedule.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                weekday_end_time_minutes is not None and weekday_end_time_minutes > 59):  # noqa: E501
            raise ValueError("Invalid value for `weekday_end_time_minutes`, must be a value less than or equal to `59`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                weekday_end_time_minutes is not None and weekday_end_time_minutes < 0):  # noqa: E501
            raise ValueError("Invalid value for `weekday_end_time_minutes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._weekday_end_time_minutes = weekday_end_time_minutes

    @property
    def weekday_start_time_hour(self):
        """Gets the weekday_start_time_hour of this PowerSchedule.  # noqa: E501


        :return: The weekday_start_time_hour of this PowerSchedule.  # noqa: E501
        :rtype: int
        """
        return self._weekday_start_time_hour

    @weekday_start_time_hour.setter
    def weekday_start_time_hour(self, weekday_start_time_hour):
        """Sets the weekday_start_time_hour of this PowerSchedule.


        :param weekday_start_time_hour: The weekday_start_time_hour of this PowerSchedule.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                weekday_start_time_hour is not None and weekday_start_time_hour > 23):  # noqa: E501
            raise ValueError("Invalid value for `weekday_start_time_hour`, must be a value less than or equal to `23`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                weekday_start_time_hour is not None and weekday_start_time_hour < 0):  # noqa: E501
            raise ValueError("Invalid value for `weekday_start_time_hour`, must be a value greater than or equal to `0`")  # noqa: E501

        self._weekday_start_time_hour = weekday_start_time_hour

    @property
    def weekday_start_time_minutes(self):
        """Gets the weekday_start_time_minutes of this PowerSchedule.  # noqa: E501


        :return: The weekday_start_time_minutes of this PowerSchedule.  # noqa: E501
        :rtype: int
        """
        return self._weekday_start_time_minutes

    @weekday_start_time_minutes.setter
    def weekday_start_time_minutes(self, weekday_start_time_minutes):
        """Sets the weekday_start_time_minutes of this PowerSchedule.


        :param weekday_start_time_minutes: The weekday_start_time_minutes of this PowerSchedule.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                weekday_start_time_minutes is not None and weekday_start_time_minutes > 59):  # noqa: E501
            raise ValueError("Invalid value for `weekday_start_time_minutes`, must be a value less than or equal to `59`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                weekday_start_time_minutes is not None and weekday_start_time_minutes < 0):  # noqa: E501
            raise ValueError("Invalid value for `weekday_start_time_minutes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._weekday_start_time_minutes = weekday_start_time_minutes

    @property
    def weekend_end_time_hour(self):
        """Gets the weekend_end_time_hour of this PowerSchedule.  # noqa: E501


        :return: The weekend_end_time_hour of this PowerSchedule.  # noqa: E501
        :rtype: int
        """
        return self._weekend_end_time_hour

    @weekend_end_time_hour.setter
    def weekend_end_time_hour(self, weekend_end_time_hour):
        """Sets the weekend_end_time_hour of this PowerSchedule.


        :param weekend_end_time_hour: The weekend_end_time_hour of this PowerSchedule.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                weekend_end_time_hour is not None and weekend_end_time_hour > 23):  # noqa: E501
            raise ValueError("Invalid value for `weekend_end_time_hour`, must be a value less than or equal to `23`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                weekend_end_time_hour is not None and weekend_end_time_hour < 0):  # noqa: E501
            raise ValueError("Invalid value for `weekend_end_time_hour`, must be a value greater than or equal to `0`")  # noqa: E501

        self._weekend_end_time_hour = weekend_end_time_hour

    @property
    def weekend_end_time_minutes(self):
        """Gets the weekend_end_time_minutes of this PowerSchedule.  # noqa: E501


        :return: The weekend_end_time_minutes of this PowerSchedule.  # noqa: E501
        :rtype: int
        """
        return self._weekend_end_time_minutes

    @weekend_end_time_minutes.setter
    def weekend_end_time_minutes(self, weekend_end_time_minutes):
        """Sets the weekend_end_time_minutes of this PowerSchedule.


        :param weekend_end_time_minutes: The weekend_end_time_minutes of this PowerSchedule.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                weekend_end_time_minutes is not None and weekend_end_time_minutes > 59):  # noqa: E501
            raise ValueError("Invalid value for `weekend_end_time_minutes`, must be a value less than or equal to `59`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                weekend_end_time_minutes is not None and weekend_end_time_minutes < 0):  # noqa: E501
            raise ValueError("Invalid value for `weekend_end_time_minutes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._weekend_end_time_minutes = weekend_end_time_minutes

    @property
    def weekend_start_time_hour(self):
        """Gets the weekend_start_time_hour of this PowerSchedule.  # noqa: E501


        :return: The weekend_start_time_hour of this PowerSchedule.  # noqa: E501
        :rtype: int
        """
        return self._weekend_start_time_hour

    @weekend_start_time_hour.setter
    def weekend_start_time_hour(self, weekend_start_time_hour):
        """Sets the weekend_start_time_hour of this PowerSchedule.


        :param weekend_start_time_hour: The weekend_start_time_hour of this PowerSchedule.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                weekend_start_time_hour is not None and weekend_start_time_hour > 23):  # noqa: E501
            raise ValueError("Invalid value for `weekend_start_time_hour`, must be a value less than or equal to `23`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                weekend_start_time_hour is not None and weekend_start_time_hour < 0):  # noqa: E501
            raise ValueError("Invalid value for `weekend_start_time_hour`, must be a value greater than or equal to `0`")  # noqa: E501

        self._weekend_start_time_hour = weekend_start_time_hour

    @property
    def weekend_start_time_minutes(self):
        """Gets the weekend_start_time_minutes of this PowerSchedule.  # noqa: E501


        :return: The weekend_start_time_minutes of this PowerSchedule.  # noqa: E501
        :rtype: int
        """
        return self._weekend_start_time_minutes

    @weekend_start_time_minutes.setter
    def weekend_start_time_minutes(self, weekend_start_time_minutes):
        """Sets the weekend_start_time_minutes of this PowerSchedule.


        :param weekend_start_time_minutes: The weekend_start_time_minutes of this PowerSchedule.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                weekend_start_time_minutes is not None and weekend_start_time_minutes > 59):  # noqa: E501
            raise ValueError("Invalid value for `weekend_start_time_minutes`, must be a value less than or equal to `59`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                weekend_start_time_minutes is not None and weekend_start_time_minutes < 0):  # noqa: E501
            raise ValueError("Invalid value for `weekend_start_time_minutes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._weekend_start_time_minutes = weekend_start_time_minutes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, PowerSchedule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PowerSchedule):
            return True

        return self.to_dict() != other.to_dict()
