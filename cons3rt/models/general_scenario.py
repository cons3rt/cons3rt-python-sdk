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


class GeneralScenario(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'offline': 'bool',
        'state': 'str',
        'visibility': 'str',
        'scenario_build_order': 'int',
        'scenario_hosts': 'list[MinimalScenarioHost]',
        'prepare_scenario_configuration': 'MinimalConfiguration',
        'teardown_scenario_configuration': 'MinimalConfiguration'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'offline': 'offline',
        'state': 'state',
        'visibility': 'visibility',
        'scenario_build_order': 'scenarioBuildOrder',
        'scenario_hosts': 'scenarioHosts',
        'prepare_scenario_configuration': 'prepareScenarioConfiguration',
        'teardown_scenario_configuration': 'teardownScenarioConfiguration'
    }

    def __init__(self, id=None, name=None, description=None, offline=None, state=None, visibility=None, scenario_build_order=None, scenario_hosts=None, prepare_scenario_configuration=None, teardown_scenario_configuration=None, local_vars_configuration=None):  # noqa: E501
        """GeneralScenario - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._offline = None
        self._state = None
        self._visibility = None
        self._scenario_build_order = None
        self._scenario_hosts = None
        self._prepare_scenario_configuration = None
        self._teardown_scenario_configuration = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if offline is not None:
            self.offline = offline
        if state is not None:
            self.state = state
        if visibility is not None:
            self.visibility = visibility
        if scenario_build_order is not None:
            self.scenario_build_order = scenario_build_order
        if scenario_hosts is not None:
            self.scenario_hosts = scenario_hosts
        if prepare_scenario_configuration is not None:
            self.prepare_scenario_configuration = prepare_scenario_configuration
        if teardown_scenario_configuration is not None:
            self.teardown_scenario_configuration = teardown_scenario_configuration

    @property
    def id(self):
        """Gets the id of this GeneralScenario.  # noqa: E501


        :return: The id of this GeneralScenario.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GeneralScenario.


        :param id: The id of this GeneralScenario.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GeneralScenario.  # noqa: E501


        :return: The name of this GeneralScenario.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GeneralScenario.


        :param name: The name of this GeneralScenario.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this GeneralScenario.  # noqa: E501


        :return: The description of this GeneralScenario.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GeneralScenario.


        :param description: The description of this GeneralScenario.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def offline(self):
        """Gets the offline of this GeneralScenario.  # noqa: E501


        :return: The offline of this GeneralScenario.  # noqa: E501
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this GeneralScenario.


        :param offline: The offline of this GeneralScenario.  # noqa: E501
        :type: bool
        """

        self._offline = offline

    @property
    def state(self):
        """Gets the state of this GeneralScenario.  # noqa: E501


        :return: The state of this GeneralScenario.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GeneralScenario.


        :param state: The state of this GeneralScenario.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_DEVELOPMENT", "CERTIFIED", "DEPRECATED", "RETIRED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def visibility(self):
        """Gets the visibility of this GeneralScenario.  # noqa: E501


        :return: The visibility of this GeneralScenario.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this GeneralScenario.


        :param visibility: The visibility of this GeneralScenario.  # noqa: E501
        :type: str
        """
        allowed_values = ["OWNER", "OWNING_PROJECT", "TRUSTED_PROJECTS", "COMMUNITY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and visibility not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def scenario_build_order(self):
        """Gets the scenario_build_order of this GeneralScenario.  # noqa: E501


        :return: The scenario_build_order of this GeneralScenario.  # noqa: E501
        :rtype: int
        """
        return self._scenario_build_order

    @scenario_build_order.setter
    def scenario_build_order(self, scenario_build_order):
        """Sets the scenario_build_order of this GeneralScenario.


        :param scenario_build_order: The scenario_build_order of this GeneralScenario.  # noqa: E501
        :type: int
        """

        self._scenario_build_order = scenario_build_order

    @property
    def scenario_hosts(self):
        """Gets the scenario_hosts of this GeneralScenario.  # noqa: E501


        :return: The scenario_hosts of this GeneralScenario.  # noqa: E501
        :rtype: list[MinimalScenarioHost]
        """
        return self._scenario_hosts

    @scenario_hosts.setter
    def scenario_hosts(self, scenario_hosts):
        """Sets the scenario_hosts of this GeneralScenario.


        :param scenario_hosts: The scenario_hosts of this GeneralScenario.  # noqa: E501
        :type: list[MinimalScenarioHost]
        """

        self._scenario_hosts = scenario_hosts

    @property
    def prepare_scenario_configuration(self):
        """Gets the prepare_scenario_configuration of this GeneralScenario.  # noqa: E501


        :return: The prepare_scenario_configuration of this GeneralScenario.  # noqa: E501
        :rtype: MinimalConfiguration
        """
        return self._prepare_scenario_configuration

    @prepare_scenario_configuration.setter
    def prepare_scenario_configuration(self, prepare_scenario_configuration):
        """Sets the prepare_scenario_configuration of this GeneralScenario.


        :param prepare_scenario_configuration: The prepare_scenario_configuration of this GeneralScenario.  # noqa: E501
        :type: MinimalConfiguration
        """

        self._prepare_scenario_configuration = prepare_scenario_configuration

    @property
    def teardown_scenario_configuration(self):
        """Gets the teardown_scenario_configuration of this GeneralScenario.  # noqa: E501


        :return: The teardown_scenario_configuration of this GeneralScenario.  # noqa: E501
        :rtype: MinimalConfiguration
        """
        return self._teardown_scenario_configuration

    @teardown_scenario_configuration.setter
    def teardown_scenario_configuration(self, teardown_scenario_configuration):
        """Sets the teardown_scenario_configuration of this GeneralScenario.


        :param teardown_scenario_configuration: The teardown_scenario_configuration of this GeneralScenario.  # noqa: E501
        :type: MinimalConfiguration
        """

        self._teardown_scenario_configuration = teardown_scenario_configuration

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
        if not isinstance(other, GeneralScenario):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralScenario):
            return True

        return self.to_dict() != other.to_dict()
