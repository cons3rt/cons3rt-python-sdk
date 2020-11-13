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


class MinimalDeploymentRunOptions(object):
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
        'duration': 'int',
        'earliest_start_time': 'datetime',
        'end_existing': 'bool',
        'host_options': 'list[HostOption]',
        'id': 'int',
        'locked': 'bool',
        'virtualization_realm_id': 'int',
        'properties': 'list[ModelProperty]',
        'retain_on_error': 'bool',
        'root_password': 'str',
        'creator': 'MinimalUser'
    }

    attribute_map = {
        'debug': 'debug',
        'deployment_run_name': 'deploymentRunName',
        'deployment_to_submit': 'deploymentToSubmit',
        'description': 'description',
        'end_state': 'endState',
        'duration': 'duration',
        'earliest_start_time': 'earliestStartTime',
        'end_existing': 'endExisting',
        'host_options': 'hostOptions',
        'id': 'id',
        'locked': 'locked',
        'virtualization_realm_id': 'virtualizationRealmId',
        'properties': 'properties',
        'retain_on_error': 'retainOnError',
        'root_password': 'rootPassword',
        'creator': 'creator'
    }

    def __init__(self, debug=None, deployment_run_name=None, deployment_to_submit=None, description=None, end_state=None, duration=None, earliest_start_time=None, end_existing=None, host_options=None, id=None, locked=None, virtualization_realm_id=None, properties=None, retain_on_error=None, root_password=None, creator=None, local_vars_configuration=None):  # noqa: E501
        """MinimalDeploymentRunOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._debug = None
        self._deployment_run_name = None
        self._deployment_to_submit = None
        self._description = None
        self._end_state = None
        self._duration = None
        self._earliest_start_time = None
        self._end_existing = None
        self._host_options = None
        self._id = None
        self._locked = None
        self._virtualization_realm_id = None
        self._properties = None
        self._retain_on_error = None
        self._root_password = None
        self._creator = None
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
        if duration is not None:
            self.duration = duration
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
        if virtualization_realm_id is not None:
            self.virtualization_realm_id = virtualization_realm_id
        if properties is not None:
            self.properties = properties
        if retain_on_error is not None:
            self.retain_on_error = retain_on_error
        if root_password is not None:
            self.root_password = root_password
        if creator is not None:
            self.creator = creator

    @property
    def debug(self):
        """Gets the debug of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The debug of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this MinimalDeploymentRunOptions.


        :param debug: The debug of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._debug = debug

    @property
    def deployment_run_name(self):
        """Gets the deployment_run_name of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The deployment_run_name of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._deployment_run_name

    @deployment_run_name.setter
    def deployment_run_name(self, deployment_run_name):
        """Sets the deployment_run_name of this MinimalDeploymentRunOptions.


        :param deployment_run_name: The deployment_run_name of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: str
        """

        self._deployment_run_name = deployment_run_name

    @property
    def deployment_to_submit(self):
        """Gets the deployment_to_submit of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The deployment_to_submit of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._deployment_to_submit

    @deployment_to_submit.setter
    def deployment_to_submit(self, deployment_to_submit):
        """Sets the deployment_to_submit of this MinimalDeploymentRunOptions.


        :param deployment_to_submit: The deployment_to_submit of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._deployment_to_submit = deployment_to_submit

    @property
    def description(self):
        """Gets the description of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The description of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MinimalDeploymentRunOptions.


        :param description: The description of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_state(self):
        """Gets the end_state of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The end_state of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._end_state

    @end_state.setter
    def end_state(self, end_state):
        """Sets the end_state of this MinimalDeploymentRunOptions.


        :param end_state: The end_state of this MinimalDeploymentRunOptions.  # noqa: E501
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
    def duration(self):
        """Gets the duration of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The duration of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MinimalDeploymentRunOptions.


        :param duration: The duration of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def earliest_start_time(self):
        """Gets the earliest_start_time of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The earliest_start_time of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: datetime
        """
        return self._earliest_start_time

    @earliest_start_time.setter
    def earliest_start_time(self, earliest_start_time):
        """Sets the earliest_start_time of this MinimalDeploymentRunOptions.


        :param earliest_start_time: The earliest_start_time of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: datetime
        """

        self._earliest_start_time = earliest_start_time

    @property
    def end_existing(self):
        """Gets the end_existing of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The end_existing of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._end_existing

    @end_existing.setter
    def end_existing(self, end_existing):
        """Sets the end_existing of this MinimalDeploymentRunOptions.


        :param end_existing: The end_existing of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._end_existing = end_existing

    @property
    def host_options(self):
        """Gets the host_options of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The host_options of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: list[HostOption]
        """
        return self._host_options

    @host_options.setter
    def host_options(self, host_options):
        """Sets the host_options of this MinimalDeploymentRunOptions.


        :param host_options: The host_options of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: list[HostOption]
        """

        self._host_options = host_options

    @property
    def id(self):
        """Gets the id of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The id of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalDeploymentRunOptions.


        :param id: The id of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def locked(self):
        """Gets the locked of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The locked of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this MinimalDeploymentRunOptions.


        :param locked: The locked of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def virtualization_realm_id(self):
        """Gets the virtualization_realm_id of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The virtualization_realm_id of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._virtualization_realm_id

    @virtualization_realm_id.setter
    def virtualization_realm_id(self, virtualization_realm_id):
        """Sets the virtualization_realm_id of this MinimalDeploymentRunOptions.


        :param virtualization_realm_id: The virtualization_realm_id of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: int
        """

        self._virtualization_realm_id = virtualization_realm_id

    @property
    def properties(self):
        """Gets the properties of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The properties of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this MinimalDeploymentRunOptions.


        :param properties: The properties of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: list[ModelProperty]
        """

        self._properties = properties

    @property
    def retain_on_error(self):
        """Gets the retain_on_error of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The retain_on_error of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: bool
        """
        return self._retain_on_error

    @retain_on_error.setter
    def retain_on_error(self, retain_on_error):
        """Sets the retain_on_error of this MinimalDeploymentRunOptions.


        :param retain_on_error: The retain_on_error of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: bool
        """

        self._retain_on_error = retain_on_error

    @property
    def root_password(self):
        """Gets the root_password of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The root_password of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._root_password

    @root_password.setter
    def root_password(self, root_password):
        """Sets the root_password of this MinimalDeploymentRunOptions.


        :param root_password: The root_password of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: str
        """

        self._root_password = root_password

    @property
    def creator(self):
        """Gets the creator of this MinimalDeploymentRunOptions.  # noqa: E501


        :return: The creator of this MinimalDeploymentRunOptions.  # noqa: E501
        :rtype: MinimalUser
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this MinimalDeploymentRunOptions.


        :param creator: The creator of this MinimalDeploymentRunOptions.  # noqa: E501
        :type: MinimalUser
        """

        self._creator = creator

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
        if not isinstance(other, MinimalDeploymentRunOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalDeploymentRunOptions):
            return True

        return self.to_dict() != other.to_dict()
