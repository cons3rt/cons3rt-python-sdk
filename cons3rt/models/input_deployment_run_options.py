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


class InputDeploymentRunOptions(object):
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
        'deployment_run_name': 'str',
        'end_state': 'str',
        'description': 'str',
        'virtualization_realm_id': 'int',
        'locked': 'bool',
        'retain_on_error': 'bool',
        'username': 'str',
        'password': 'str',
        'earliest_start_time': 'datetime',
        'end_existing': 'bool',
        'duration': 'int',
        'properties': 'list[InputProperty]',
        'host_options': 'list[InputHostOption]',
        'power_schedule': 'PowerSchedule',
        'virt_realm_binding': 'InputVirtualizationRealmBinding',
        'id': 'int',
        'debug': 'bool',
        'end_date': 'datetime',
        'windows_domain_name': 'str'
    }

    attribute_map = {
        'deployment_run_name': 'deploymentRunName',
        'end_state': 'endState',
        'description': 'description',
        'virtualization_realm_id': 'virtualizationRealmId',
        'locked': 'locked',
        'retain_on_error': 'retainOnError',
        'username': 'username',
        'password': 'password',
        'earliest_start_time': 'earliestStartTime',
        'end_existing': 'endExisting',
        'duration': 'duration',
        'properties': 'properties',
        'host_options': 'hostOptions',
        'power_schedule': 'powerSchedule',
        'virt_realm_binding': 'virtRealmBinding',
        'id': 'id',
        'debug': 'debug',
        'end_date': 'endDate',
        'windows_domain_name': 'windowsDomainName'
    }

    def __init__(self, deployment_run_name=None, end_state=None, description=None, virtualization_realm_id=None, locked=None, retain_on_error=None, username=None, password=None, earliest_start_time=None, end_existing=None, duration=None, properties=None, host_options=None, power_schedule=None, virt_realm_binding=None, id=None, debug=None, end_date=None, windows_domain_name=None, local_vars_configuration=None):  # noqa: E501
        """InputDeploymentRunOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deployment_run_name = None
        self._end_state = None
        self._description = None
        self._virtualization_realm_id = None
        self._locked = None
        self._retain_on_error = None
        self._username = None
        self._password = None
        self._earliest_start_time = None
        self._end_existing = None
        self._duration = None
        self._properties = None
        self._host_options = None
        self._power_schedule = None
        self._virt_realm_binding = None
        self._id = None
        self._debug = None
        self._end_date = None
        self._windows_domain_name = None
        self.discriminator = None

        if deployment_run_name is not None:
            self.deployment_run_name = deployment_run_name
        self.end_state = end_state
        if description is not None:
            self.description = description
        if virtualization_realm_id is not None:
            self.virtualization_realm_id = virtualization_realm_id
        if locked is not None:
            self.locked = locked
        if retain_on_error is not None:
            self.retain_on_error = retain_on_error
        self.username = username
        self.password = password
        if earliest_start_time is not None:
            self.earliest_start_time = earliest_start_time
        if end_existing is not None:
            self.end_existing = end_existing
        if duration is not None:
            self.duration = duration
        if properties is not None:
            self.properties = properties
        if host_options is not None:
            self.host_options = host_options
        if power_schedule is not None:
            self.power_schedule = power_schedule
        if virt_realm_binding is not None:
            self.virt_realm_binding = virt_realm_binding
        if id is not None:
            self.id = id
        if debug is not None:
            self.debug = debug
        if end_date is not None:
            self.end_date = end_date
        if windows_domain_name is not None:
            self.windows_domain_name = windows_domain_name

    @property
    def deployment_run_name(self):
        """Gets the deployment_run_name of this InputDeploymentRunOptions.  # noqa: E501


        :return: The deployment_run_name of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._deployment_run_name

    @deployment_run_name.setter
    def deployment_run_name(self, deployment_run_name):
        """Sets the deployment_run_name of this InputDeploymentRunOptions.


        :param deployment_run_name: The deployment_run_name of this InputDeploymentRunOptions.  # noqa: E501
        :type: str
        """

        self._deployment_run_name = deployment_run_name

    @property
    def end_state(self):
        """Gets the end_state of this InputDeploymentRunOptions.  # noqa: E501


        :return: The end_state of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._end_state

    @end_state.setter
    def end_state(self, end_state):
        """Sets the end_state of this InputDeploymentRunOptions.


        :param end_state: The end_state of this InputDeploymentRunOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and end_state is None:  # noqa: E501
            raise ValueError("Invalid value for `end_state`, must not be `None`")  # noqa: E501
        allowed_values = ["UNKNOWN_STATE", "SYSTEMS_BUILT", "SCENARIO_BUILT", "TESTS_EXECUTED_RESOURCES_RELEASED", "TESTS_EXECUTED_RESOURCES_RESERVED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and end_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `end_state` ({0}), must be one of {1}"  # noqa: E501
                .format(end_state, allowed_values)
            )

        self._end_state = end_state

    @property
    def description(self):
        """Gets the description of this InputDeploymentRunOptions.  # noqa: E501


        :return: The description of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InputDeploymentRunOptions.


        :param description: The description of this InputDeploymentRunOptions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def virtualization_realm_id(self):
        """Gets the virtualization_realm_id of this InputDeploymentRunOptions.  # noqa: E501


        :return: The virtualization_realm_id of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._virtualization_realm_id

    @virtualization_realm_id.setter
    def virtualization_realm_id(self, virtualization_realm_id):
        """Sets the virtualization_realm_id of this InputDeploymentRunOptions.


        :param virtualization_realm_id: The virtualization_realm_id of this InputDeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._virtualization_realm_id = virtualization_realm_id

    @property
    def locked(self):
        """Gets the locked of this InputDeploymentRunOptions.  # noqa: E501


        :return: The locked of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this InputDeploymentRunOptions.


        :param locked: The locked of this InputDeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def retain_on_error(self):
        """Gets the retain_on_error of this InputDeploymentRunOptions.  # noqa: E501


        :return: The retain_on_error of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._retain_on_error

    @retain_on_error.setter
    def retain_on_error(self, retain_on_error):
        """Sets the retain_on_error of this InputDeploymentRunOptions.


        :param retain_on_error: The retain_on_error of this InputDeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._retain_on_error = retain_on_error

    @property
    def username(self):
        """Gets the username of this InputDeploymentRunOptions.  # noqa: E501


        :return: The username of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InputDeploymentRunOptions.


        :param username: The username of this InputDeploymentRunOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this InputDeploymentRunOptions.  # noqa: E501


        :return: The password of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InputDeploymentRunOptions.


        :param password: The password of this InputDeploymentRunOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def earliest_start_time(self):
        """Gets the earliest_start_time of this InputDeploymentRunOptions.  # noqa: E501


        :return: The earliest_start_time of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: datetime
        """
        return self._earliest_start_time

    @earliest_start_time.setter
    def earliest_start_time(self, earliest_start_time):
        """Sets the earliest_start_time of this InputDeploymentRunOptions.


        :param earliest_start_time: The earliest_start_time of this InputDeploymentRunOptions.  # noqa: E501
        :type: datetime
        """

        self._earliest_start_time = earliest_start_time

    @property
    def end_existing(self):
        """Gets the end_existing of this InputDeploymentRunOptions.  # noqa: E501


        :return: The end_existing of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._end_existing

    @end_existing.setter
    def end_existing(self, end_existing):
        """Sets the end_existing of this InputDeploymentRunOptions.


        :param end_existing: The end_existing of this InputDeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._end_existing = end_existing

    @property
    def duration(self):
        """Gets the duration of this InputDeploymentRunOptions.  # noqa: E501


        :return: The duration of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InputDeploymentRunOptions.


        :param duration: The duration of this InputDeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def properties(self):
        """Gets the properties of this InputDeploymentRunOptions.  # noqa: E501


        :return: The properties of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: list[InputProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this InputDeploymentRunOptions.


        :param properties: The properties of this InputDeploymentRunOptions.  # noqa: E501
        :type: list[InputProperty]
        """

        self._properties = properties

    @property
    def host_options(self):
        """Gets the host_options of this InputDeploymentRunOptions.  # noqa: E501


        :return: The host_options of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: list[InputHostOption]
        """
        return self._host_options

    @host_options.setter
    def host_options(self, host_options):
        """Sets the host_options of this InputDeploymentRunOptions.


        :param host_options: The host_options of this InputDeploymentRunOptions.  # noqa: E501
        :type: list[InputHostOption]
        """

        self._host_options = host_options

    @property
    def power_schedule(self):
        """Gets the power_schedule of this InputDeploymentRunOptions.  # noqa: E501


        :return: The power_schedule of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: PowerSchedule
        """
        return self._power_schedule

    @power_schedule.setter
    def power_schedule(self, power_schedule):
        """Sets the power_schedule of this InputDeploymentRunOptions.


        :param power_schedule: The power_schedule of this InputDeploymentRunOptions.  # noqa: E501
        :type: PowerSchedule
        """

        self._power_schedule = power_schedule

    @property
    def virt_realm_binding(self):
        """Gets the virt_realm_binding of this InputDeploymentRunOptions.  # noqa: E501


        :return: The virt_realm_binding of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: InputVirtualizationRealmBinding
        """
        return self._virt_realm_binding

    @virt_realm_binding.setter
    def virt_realm_binding(self, virt_realm_binding):
        """Sets the virt_realm_binding of this InputDeploymentRunOptions.


        :param virt_realm_binding: The virt_realm_binding of this InputDeploymentRunOptions.  # noqa: E501
        :type: InputVirtualizationRealmBinding
        """

        self._virt_realm_binding = virt_realm_binding

    @property
    def id(self):
        """Gets the id of this InputDeploymentRunOptions.  # noqa: E501


        :return: The id of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InputDeploymentRunOptions.


        :param id: The id of this InputDeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def debug(self):
        """Gets the debug of this InputDeploymentRunOptions.  # noqa: E501


        :return: The debug of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this InputDeploymentRunOptions.


        :param debug: The debug of this InputDeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._debug = debug

    @property
    def end_date(self):
        """Gets the end_date of this InputDeploymentRunOptions.  # noqa: E501


        :return: The end_date of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this InputDeploymentRunOptions.


        :param end_date: The end_date of this InputDeploymentRunOptions.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def windows_domain_name(self):
        """Gets the windows_domain_name of this InputDeploymentRunOptions.  # noqa: E501


        :return: The windows_domain_name of this InputDeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._windows_domain_name

    @windows_domain_name.setter
    def windows_domain_name(self, windows_domain_name):
        """Sets the windows_domain_name of this InputDeploymentRunOptions.


        :param windows_domain_name: The windows_domain_name of this InputDeploymentRunOptions.  # noqa: E501
        :type: str
        """

        self._windows_domain_name = windows_domain_name

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
        if not isinstance(other, InputDeploymentRunOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputDeploymentRunOptions):
            return True

        return self.to_dict() != other.to_dict()
