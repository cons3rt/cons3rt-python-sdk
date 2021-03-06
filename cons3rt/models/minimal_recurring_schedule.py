"""
   Copyright 2020 Jackpine Technologies Corporation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration

__author__ = 'Jackpine Technologies Corporation'
__copyright__ = 'Copyright 2020, Jackpine Technologies Corporation'
__license__ = 'Apache 2.0',
__version__ = '1.0.0'
__maintainer__ = 'API Support'
__email__ = 'support@cons3rt.com'


class MinimalRecurringSchedule(object):
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
        'id': 'int',
        'complete': 'bool',
        'end_date': 'int',
        'max_iterations': 'int',
        'deployment_run_options': 'MinimalDeploymentRunOptions',
        'remaining_iterations': 'int',
        'schedule': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'complete': 'complete',
        'end_date': 'endDate',
        'max_iterations': 'maxIterations',
        'deployment_run_options': 'deploymentRunOptions',
        'remaining_iterations': 'remainingIterations',
        'schedule': 'schedule',
        'timezone': 'timezone'
    }

    def __init__(self, id=None, complete=None, end_date=None, max_iterations=None, deployment_run_options=None, remaining_iterations=None, schedule=None, timezone=None, local_vars_configuration=None):  # noqa: E501
        """MinimalRecurringSchedule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._complete = None
        self._end_date = None
        self._max_iterations = None
        self._deployment_run_options = None
        self._remaining_iterations = None
        self._schedule = None
        self._timezone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if complete is not None:
            self.complete = complete
        if end_date is not None:
            self.end_date = end_date
        if max_iterations is not None:
            self.max_iterations = max_iterations
        self.deployment_run_options = deployment_run_options
        if remaining_iterations is not None:
            self.remaining_iterations = remaining_iterations
        self.schedule = schedule
        self.timezone = timezone

    @property
    def id(self):
        """Gets the id of this MinimalRecurringSchedule.  # noqa: E501


        :return: The id of this MinimalRecurringSchedule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalRecurringSchedule.


        :param id: The id of this MinimalRecurringSchedule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def complete(self):
        """Gets the complete of this MinimalRecurringSchedule.  # noqa: E501


        :return: The complete of this MinimalRecurringSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this MinimalRecurringSchedule.


        :param complete: The complete of this MinimalRecurringSchedule.  # noqa: E501
        :type: bool
        """

        self._complete = complete

    @property
    def end_date(self):
        """Gets the end_date of this MinimalRecurringSchedule.  # noqa: E501


        :return: The end_date of this MinimalRecurringSchedule.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this MinimalRecurringSchedule.


        :param end_date: The end_date of this MinimalRecurringSchedule.  # noqa: E501
        :type: int
        """

        self._end_date = end_date

    @property
    def max_iterations(self):
        """Gets the max_iterations of this MinimalRecurringSchedule.  # noqa: E501


        :return: The max_iterations of this MinimalRecurringSchedule.  # noqa: E501
        :rtype: int
        """
        return self._max_iterations

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        """Sets the max_iterations of this MinimalRecurringSchedule.


        :param max_iterations: The max_iterations of this MinimalRecurringSchedule.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_iterations is not None and max_iterations < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_iterations`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_iterations = max_iterations

    @property
    def deployment_run_options(self):
        """Gets the deployment_run_options of this MinimalRecurringSchedule.  # noqa: E501


        :return: The deployment_run_options of this MinimalRecurringSchedule.  # noqa: E501
        :rtype: MinimalDeploymentRunOptions
        """
        return self._deployment_run_options

    @deployment_run_options.setter
    def deployment_run_options(self, deployment_run_options):
        """Sets the deployment_run_options of this MinimalRecurringSchedule.


        :param deployment_run_options: The deployment_run_options of this MinimalRecurringSchedule.  # noqa: E501
        :type: MinimalDeploymentRunOptions
        """
        if self.local_vars_configuration.client_side_validation and deployment_run_options is None:  # noqa: E501
            raise ValueError("Invalid value for `deployment_run_options`, must not be `None`")  # noqa: E501

        self._deployment_run_options = deployment_run_options

    @property
    def remaining_iterations(self):
        """Gets the remaining_iterations of this MinimalRecurringSchedule.  # noqa: E501


        :return: The remaining_iterations of this MinimalRecurringSchedule.  # noqa: E501
        :rtype: int
        """
        return self._remaining_iterations

    @remaining_iterations.setter
    def remaining_iterations(self, remaining_iterations):
        """Sets the remaining_iterations of this MinimalRecurringSchedule.


        :param remaining_iterations: The remaining_iterations of this MinimalRecurringSchedule.  # noqa: E501
        :type: int
        """

        self._remaining_iterations = remaining_iterations

    @property
    def schedule(self):
        """Gets the schedule of this MinimalRecurringSchedule.  # noqa: E501


        :return: The schedule of this MinimalRecurringSchedule.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this MinimalRecurringSchedule.


        :param schedule: The schedule of this MinimalRecurringSchedule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and schedule is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

    @property
    def timezone(self):
        """Gets the timezone of this MinimalRecurringSchedule.  # noqa: E501


        :return: The timezone of this MinimalRecurringSchedule.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this MinimalRecurringSchedule.


        :param timezone: The timezone of this MinimalRecurringSchedule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and timezone is None:  # noqa: E501
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

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
        if not isinstance(other, MinimalRecurringSchedule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalRecurringSchedule):
            return True

        return self.to_dict() != other.to_dict()
