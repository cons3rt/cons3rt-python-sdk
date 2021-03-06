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


class Composition(object):
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
        'deployment_run_options': 'CompositionRunOptions',
        'description': 'str',
        'id': 'int',
        'name': 'str',
        'project': 'Project',
        'scenario': 'Scenario'
    }

    attribute_map = {
        'deployment_run_options': 'deploymentRunOptions',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'project': 'project',
        'scenario': 'scenario'
    }

    def __init__(self, deployment_run_options=None, description=None, id=None, name=None, project=None, scenario=None, local_vars_configuration=None):  # noqa: E501
        """Composition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deployment_run_options = None
        self._description = None
        self._id = None
        self._name = None
        self._project = None
        self._scenario = None
        self.discriminator = None

        if deployment_run_options is not None:
            self.deployment_run_options = deployment_run_options
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        self.name = name
        if project is not None:
            self.project = project
        if scenario is not None:
            self.scenario = scenario

    @property
    def deployment_run_options(self):
        """Gets the deployment_run_options of this Composition.  # noqa: E501


        :return: The deployment_run_options of this Composition.  # noqa: E501
        :rtype: CompositionRunOptions
        """
        return self._deployment_run_options

    @deployment_run_options.setter
    def deployment_run_options(self, deployment_run_options):
        """Sets the deployment_run_options of this Composition.


        :param deployment_run_options: The deployment_run_options of this Composition.  # noqa: E501
        :type: CompositionRunOptions
        """

        self._deployment_run_options = deployment_run_options

    @property
    def description(self):
        """Gets the description of this Composition.  # noqa: E501


        :return: The description of this Composition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Composition.


        :param description: The description of this Composition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Composition.  # noqa: E501


        :return: The id of this Composition.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Composition.


        :param id: The id of this Composition.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Composition.  # noqa: E501


        :return: The name of this Composition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Composition.


        :param name: The name of this Composition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def project(self):
        """Gets the project of this Composition.  # noqa: E501


        :return: The project of this Composition.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Composition.


        :param project: The project of this Composition.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def scenario(self):
        """Gets the scenario of this Composition.  # noqa: E501


        :return: The scenario of this Composition.  # noqa: E501
        :rtype: Scenario
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this Composition.


        :param scenario: The scenario of this Composition.  # noqa: E501
        :type: Scenario
        """

        self._scenario = scenario

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
        if not isinstance(other, Composition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Composition):
            return True

        return self.to_dict() != other.to_dict()
