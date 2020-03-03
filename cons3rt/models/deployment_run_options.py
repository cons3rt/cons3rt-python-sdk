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


class DeploymentRunOptions(object):
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
        'debug': 'bool',
        'deployment_run_name': 'str',
        'deployment_to_submit': 'int',
        'description': 'str',
        'end_state': 'str',
        'earliest_start_time': 'int',
        'end_existing': 'bool',
        'host_options': 'list[HostOption]',
        'id': 'int',
        'locked': 'bool',
        'password': 'str',
        'power_schedule': 'PowerSchedule',
        'virtualization_realm_id': 'int',
        'properties': 'list[ModelProperty]',
        'quick_build_cleanup_overridden': 'bool',
        'duration': 'int',
        'end_date': 'int',
        'retain_on_error': 'bool',
        'task_group': 'str',
        'username': 'str',
        'virt_realm_binding': 'VirtualizationRealmBinding',
        'windows_domain_name': 'str'
    }

    attribute_map = {
        'debug': 'debug',
        'deployment_run_name': 'deploymentRunName',
        'deployment_to_submit': 'deploymentToSubmit',
        'description': 'description',
        'end_state': 'endState',
        'earliest_start_time': 'earliestStartTime',
        'end_existing': 'endExisting',
        'host_options': 'hostOptions',
        'id': 'id',
        'locked': 'locked',
        'password': 'password',
        'power_schedule': 'powerSchedule',
        'virtualization_realm_id': 'virtualizationRealmId',
        'properties': 'properties',
        'quick_build_cleanup_overridden': 'quickBuildCleanupOverridden',
        'duration': 'duration',
        'end_date': 'endDate',
        'retain_on_error': 'retainOnError',
        'task_group': 'taskGroup',
        'username': 'username',
        'virt_realm_binding': 'virtRealmBinding',
        'windows_domain_name': 'windowsDomainName'
    }

    def __init__(self, debug=None, deployment_run_name=None, deployment_to_submit=None, description=None, end_state=None, earliest_start_time=None, end_existing=None, host_options=None, id=None, locked=None, password=None, power_schedule=None, virtualization_realm_id=None, properties=None, quick_build_cleanup_overridden=None, duration=None, end_date=None, retain_on_error=None, task_group=None, username=None, virt_realm_binding=None, windows_domain_name=None, local_vars_configuration=None):  # noqa: E501
        """DeploymentRunOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._debug = None
        self._deployment_run_name = None
        self._deployment_to_submit = None
        self._description = None
        self._end_state = None
        self._earliest_start_time = None
        self._end_existing = None
        self._host_options = None
        self._id = None
        self._locked = None
        self._password = None
        self._power_schedule = None
        self._virtualization_realm_id = None
        self._properties = None
        self._quick_build_cleanup_overridden = None
        self._duration = None
        self._end_date = None
        self._retain_on_error = None
        self._task_group = None
        self._username = None
        self._virt_realm_binding = None
        self._windows_domain_name = None
        self.discriminator = None

        if debug is not None:
            self.debug = debug
        if deployment_run_name is not None:
            self.deployment_run_name = deployment_run_name
        if deployment_to_submit is not None:
            self.deployment_to_submit = deployment_to_submit
        if description is not None:
            self.description = description
        if end_state is not None:
            self.end_state = end_state
        if earliest_start_time is not None:
            self.earliest_start_time = earliest_start_time
        if end_existing is not None:
            self.end_existing = end_existing
        if host_options is not None:
            self.host_options = host_options
        if id is not None:
            self.id = id
        if locked is not None:
            self.locked = locked
        self.password = password
        if power_schedule is not None:
            self.power_schedule = power_schedule
        if virtualization_realm_id is not None:
            self.virtualization_realm_id = virtualization_realm_id
        if properties is not None:
            self.properties = properties
        if quick_build_cleanup_overridden is not None:
            self.quick_build_cleanup_overridden = quick_build_cleanup_overridden
        if duration is not None:
            self.duration = duration
        if end_date is not None:
            self.end_date = end_date
        if retain_on_error is not None:
            self.retain_on_error = retain_on_error
        if task_group is not None:
            self.task_group = task_group
        self.username = username
        if virt_realm_binding is not None:
            self.virt_realm_binding = virt_realm_binding
        if windows_domain_name is not None:
            self.windows_domain_name = windows_domain_name

    @property
    def debug(self):
        """Gets the debug of this DeploymentRunOptions.  # noqa: E501


        :return: The debug of this DeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this DeploymentRunOptions.


        :param debug: The debug of this DeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._debug = debug

    @property
    def deployment_run_name(self):
        """Gets the deployment_run_name of this DeploymentRunOptions.  # noqa: E501


        :return: The deployment_run_name of this DeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._deployment_run_name

    @deployment_run_name.setter
    def deployment_run_name(self, deployment_run_name):
        """Sets the deployment_run_name of this DeploymentRunOptions.


        :param deployment_run_name: The deployment_run_name of this DeploymentRunOptions.  # noqa: E501
        :type: str
        """

        self._deployment_run_name = deployment_run_name

    @property
    def deployment_to_submit(self):
        """Gets the deployment_to_submit of this DeploymentRunOptions.  # noqa: E501


        :return: The deployment_to_submit of this DeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._deployment_to_submit

    @deployment_to_submit.setter
    def deployment_to_submit(self, deployment_to_submit):
        """Sets the deployment_to_submit of this DeploymentRunOptions.


        :param deployment_to_submit: The deployment_to_submit of this DeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._deployment_to_submit = deployment_to_submit

    @property
    def description(self):
        """Gets the description of this DeploymentRunOptions.  # noqa: E501


        :return: The description of this DeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeploymentRunOptions.


        :param description: The description of this DeploymentRunOptions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_state(self):
        """Gets the end_state of this DeploymentRunOptions.  # noqa: E501


        :return: The end_state of this DeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._end_state

    @end_state.setter
    def end_state(self, end_state):
        """Sets the end_state of this DeploymentRunOptions.


        :param end_state: The end_state of this DeploymentRunOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN_STATE", "SYSTEMS_BUILT", "SCENARIO_BUILT", "TESTS_EXECUTED_RESOURCES_RELEASED", "TESTS_EXECUTED_RESOURCES_RESERVED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and end_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `end_state` ({0}), must be one of {1}"  # noqa: E501
                .format(end_state, allowed_values)
            )

        self._end_state = end_state

    @property
    def earliest_start_time(self):
        """Gets the earliest_start_time of this DeploymentRunOptions.  # noqa: E501


        :return: The earliest_start_time of this DeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._earliest_start_time

    @earliest_start_time.setter
    def earliest_start_time(self, earliest_start_time):
        """Sets the earliest_start_time of this DeploymentRunOptions.


        :param earliest_start_time: The earliest_start_time of this DeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._earliest_start_time = earliest_start_time

    @property
    def end_existing(self):
        """Gets the end_existing of this DeploymentRunOptions.  # noqa: E501


        :return: The end_existing of this DeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._end_existing

    @end_existing.setter
    def end_existing(self, end_existing):
        """Sets the end_existing of this DeploymentRunOptions.


        :param end_existing: The end_existing of this DeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._end_existing = end_existing

    @property
    def host_options(self):
        """Gets the host_options of this DeploymentRunOptions.  # noqa: E501


        :return: The host_options of this DeploymentRunOptions.  # noqa: E501
        :rtype: list[HostOption]
        """
        return self._host_options

    @host_options.setter
    def host_options(self, host_options):
        """Sets the host_options of this DeploymentRunOptions.


        :param host_options: The host_options of this DeploymentRunOptions.  # noqa: E501
        :type: list[HostOption]
        """

        self._host_options = host_options

    @property
    def id(self):
        """Gets the id of this DeploymentRunOptions.  # noqa: E501


        :return: The id of this DeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentRunOptions.


        :param id: The id of this DeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def locked(self):
        """Gets the locked of this DeploymentRunOptions.  # noqa: E501


        :return: The locked of this DeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this DeploymentRunOptions.


        :param locked: The locked of this DeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def password(self):
        """Gets the password of this DeploymentRunOptions.  # noqa: E501


        :return: The password of this DeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DeploymentRunOptions.


        :param password: The password of this DeploymentRunOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def power_schedule(self):
        """Gets the power_schedule of this DeploymentRunOptions.  # noqa: E501


        :return: The power_schedule of this DeploymentRunOptions.  # noqa: E501
        :rtype: PowerSchedule
        """
        return self._power_schedule

    @power_schedule.setter
    def power_schedule(self, power_schedule):
        """Sets the power_schedule of this DeploymentRunOptions.


        :param power_schedule: The power_schedule of this DeploymentRunOptions.  # noqa: E501
        :type: PowerSchedule
        """

        self._power_schedule = power_schedule

    @property
    def virtualization_realm_id(self):
        """Gets the virtualization_realm_id of this DeploymentRunOptions.  # noqa: E501


        :return: The virtualization_realm_id of this DeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._virtualization_realm_id

    @virtualization_realm_id.setter
    def virtualization_realm_id(self, virtualization_realm_id):
        """Sets the virtualization_realm_id of this DeploymentRunOptions.


        :param virtualization_realm_id: The virtualization_realm_id of this DeploymentRunOptions.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                virtualization_realm_id is not None and virtualization_realm_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `virtualization_realm_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._virtualization_realm_id = virtualization_realm_id

    @property
    def properties(self):
        """Gets the properties of this DeploymentRunOptions.  # noqa: E501


        :return: The properties of this DeploymentRunOptions.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DeploymentRunOptions.


        :param properties: The properties of this DeploymentRunOptions.  # noqa: E501
        :type: list[ModelProperty]
        """

        self._properties = properties

    @property
    def quick_build_cleanup_overridden(self):
        """Gets the quick_build_cleanup_overridden of this DeploymentRunOptions.  # noqa: E501


        :return: The quick_build_cleanup_overridden of this DeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._quick_build_cleanup_overridden

    @quick_build_cleanup_overridden.setter
    def quick_build_cleanup_overridden(self, quick_build_cleanup_overridden):
        """Sets the quick_build_cleanup_overridden of this DeploymentRunOptions.


        :param quick_build_cleanup_overridden: The quick_build_cleanup_overridden of this DeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._quick_build_cleanup_overridden = quick_build_cleanup_overridden

    @property
    def duration(self):
        """Gets the duration of this DeploymentRunOptions.  # noqa: E501


        :return: The duration of this DeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DeploymentRunOptions.


        :param duration: The duration of this DeploymentRunOptions.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration > 153722867280912):  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value less than or equal to `153722867280912`")  # noqa: E501

        self._duration = duration

    @property
    def end_date(self):
        """Gets the end_date of this DeploymentRunOptions.  # noqa: E501


        :return: The end_date of this DeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this DeploymentRunOptions.


        :param end_date: The end_date of this DeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._end_date = end_date

    @property
    def retain_on_error(self):
        """Gets the retain_on_error of this DeploymentRunOptions.  # noqa: E501


        :return: The retain_on_error of this DeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._retain_on_error

    @retain_on_error.setter
    def retain_on_error(self, retain_on_error):
        """Sets the retain_on_error of this DeploymentRunOptions.


        :param retain_on_error: The retain_on_error of this DeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._retain_on_error = retain_on_error

    @property
    def task_group(self):
        """Gets the task_group of this DeploymentRunOptions.  # noqa: E501


        :return: The task_group of this DeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._task_group

    @task_group.setter
    def task_group(self, task_group):
        """Sets the task_group of this DeploymentRunOptions.


        :param task_group: The task_group of this DeploymentRunOptions.  # noqa: E501
        :type: str
        """

        self._task_group = task_group

    @property
    def username(self):
        """Gets the username of this DeploymentRunOptions.  # noqa: E501


        :return: The username of this DeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DeploymentRunOptions.


        :param username: The username of this DeploymentRunOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def virt_realm_binding(self):
        """Gets the virt_realm_binding of this DeploymentRunOptions.  # noqa: E501


        :return: The virt_realm_binding of this DeploymentRunOptions.  # noqa: E501
        :rtype: VirtualizationRealmBinding
        """
        return self._virt_realm_binding

    @virt_realm_binding.setter
    def virt_realm_binding(self, virt_realm_binding):
        """Sets the virt_realm_binding of this DeploymentRunOptions.


        :param virt_realm_binding: The virt_realm_binding of this DeploymentRunOptions.  # noqa: E501
        :type: VirtualizationRealmBinding
        """

        self._virt_realm_binding = virt_realm_binding

    @property
    def windows_domain_name(self):
        """Gets the windows_domain_name of this DeploymentRunOptions.  # noqa: E501


        :return: The windows_domain_name of this DeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._windows_domain_name

    @windows_domain_name.setter
    def windows_domain_name(self, windows_domain_name):
        """Sets the windows_domain_name of this DeploymentRunOptions.


        :param windows_domain_name: The windows_domain_name of this DeploymentRunOptions.  # noqa: E501
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
        if not isinstance(other, DeploymentRunOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentRunOptions):
            return True

        return self.to_dict() != other.to_dict()
