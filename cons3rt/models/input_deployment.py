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


class InputDeployment(object):
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
        'name': 'str',
        'metadata': 'InputMetadata',
        'scenarios': 'list[InputScenarioFull]',
        'test_bundles': 'list[InputTestBundle]'
    }

    attribute_map = {
        'name': 'name',
        'metadata': 'metadata',
        'scenarios': 'scenarios',
        'test_bundles': 'testBundles'
    }

    def __init__(self, name=None, metadata=None, scenarios=None, test_bundles=None, local_vars_configuration=None):  # noqa: E501
        """InputDeployment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._metadata = None
        self._scenarios = None
        self._test_bundles = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if metadata is not None:
            self.metadata = metadata
        if scenarios is not None:
            self.scenarios = scenarios
        if test_bundles is not None:
            self.test_bundles = test_bundles

    @property
    def name(self):
        """Gets the name of this InputDeployment.  # noqa: E501


        :return: The name of this InputDeployment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputDeployment.


        :param name: The name of this InputDeployment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this InputDeployment.  # noqa: E501


        :return: The metadata of this InputDeployment.  # noqa: E501
        :rtype: InputMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InputDeployment.


        :param metadata: The metadata of this InputDeployment.  # noqa: E501
        :type: InputMetadata
        """

        self._metadata = metadata

    @property
    def scenarios(self):
        """Gets the scenarios of this InputDeployment.  # noqa: E501


        :return: The scenarios of this InputDeployment.  # noqa: E501
        :rtype: list[InputScenarioFull]
        """
        return self._scenarios

    @scenarios.setter
    def scenarios(self, scenarios):
        """Sets the scenarios of this InputDeployment.


        :param scenarios: The scenarios of this InputDeployment.  # noqa: E501
        :type: list[InputScenarioFull]
        """

        self._scenarios = scenarios

    @property
    def test_bundles(self):
        """Gets the test_bundles of this InputDeployment.  # noqa: E501


        :return: The test_bundles of this InputDeployment.  # noqa: E501
        :rtype: list[InputTestBundle]
        """
        return self._test_bundles

    @test_bundles.setter
    def test_bundles(self, test_bundles):
        """Sets the test_bundles of this InputDeployment.


        :param test_bundles: The test_bundles of this InputDeployment.  # noqa: E501
        :type: list[InputTestBundle]
        """

        self._test_bundles = test_bundles

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
        if not isinstance(other, InputDeployment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputDeployment):
            return True

        return self.to_dict() != other.to_dict()
