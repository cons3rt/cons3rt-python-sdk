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


class ContainerInstallation(object):
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
        'asset_type': 'str',
        'run_arguments': 'str'
    }

    attribute_map = {
        'asset_type': 'assetType',
        'run_arguments': 'runArguments'
    }

    def __init__(self, asset_type=None, run_arguments=None, local_vars_configuration=None):  # noqa: E501
        """ContainerInstallation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_type = None
        self._run_arguments = None
        self.discriminator = None

        if asset_type is not None:
            self.asset_type = asset_type
        if run_arguments is not None:
            self.run_arguments = run_arguments

    @property
    def asset_type(self):
        """Gets the asset_type of this ContainerInstallation.  # noqa: E501


        :return: The asset_type of this ContainerInstallation.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this ContainerInstallation.


        :param asset_type: The asset_type of this ContainerInstallation.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOCKER", "OCI"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and asset_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `asset_type` ({0}), must be one of {1}"  # noqa: E501
                .format(asset_type, allowed_values)
            )

        self._asset_type = asset_type

    @property
    def run_arguments(self):
        """Gets the run_arguments of this ContainerInstallation.  # noqa: E501


        :return: The run_arguments of this ContainerInstallation.  # noqa: E501
        :rtype: str
        """
        return self._run_arguments

    @run_arguments.setter
    def run_arguments(self, run_arguments):
        """Sets the run_arguments of this ContainerInstallation.


        :param run_arguments: The run_arguments of this ContainerInstallation.  # noqa: E501
        :type: str
        """

        self._run_arguments = run_arguments

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
        if not isinstance(other, ContainerInstallation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerInstallation):
            return True

        return self.to_dict() != other.to_dict()
