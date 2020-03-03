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


class DeploymentAssetMetric(object):
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
        'deployment_id': 'str',
        'total_deployment_run_duration': 'int',
        'average_deployment_run_duration': 'int',
        'median_deployment_run_duration': 'int',
        'longest_deployment_run_duration': 'int',
        'shortest_deployment_run_duration': 'int',
        'total_deployment_runs': 'int',
        'total_deployment_run_success': 'int',
        'total_deployment_run_error': 'int',
        'total_deployment_run_cancel': 'int',
        'total_deployment_run_unknown': 'int',
        'total_virtual_machines': 'int'
    }

    attribute_map = {
        'deployment_id': 'deploymentId',
        'total_deployment_run_duration': 'totalDeploymentRunDuration',
        'average_deployment_run_duration': 'averageDeploymentRunDuration',
        'median_deployment_run_duration': 'medianDeploymentRunDuration',
        'longest_deployment_run_duration': 'longestDeploymentRunDuration',
        'shortest_deployment_run_duration': 'shortestDeploymentRunDuration',
        'total_deployment_runs': 'totalDeploymentRuns',
        'total_deployment_run_success': 'totalDeploymentRunSuccess',
        'total_deployment_run_error': 'totalDeploymentRunError',
        'total_deployment_run_cancel': 'totalDeploymentRunCancel',
        'total_deployment_run_unknown': 'totalDeploymentRunUnknown',
        'total_virtual_machines': 'totalVirtualMachines'
    }

    def __init__(self, deployment_id=None, total_deployment_run_duration=None, average_deployment_run_duration=None, median_deployment_run_duration=None, longest_deployment_run_duration=None, shortest_deployment_run_duration=None, total_deployment_runs=None, total_deployment_run_success=None, total_deployment_run_error=None, total_deployment_run_cancel=None, total_deployment_run_unknown=None, total_virtual_machines=None, local_vars_configuration=None):  # noqa: E501
        """DeploymentAssetMetric - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deployment_id = None
        self._total_deployment_run_duration = None
        self._average_deployment_run_duration = None
        self._median_deployment_run_duration = None
        self._longest_deployment_run_duration = None
        self._shortest_deployment_run_duration = None
        self._total_deployment_runs = None
        self._total_deployment_run_success = None
        self._total_deployment_run_error = None
        self._total_deployment_run_cancel = None
        self._total_deployment_run_unknown = None
        self._total_virtual_machines = None
        self.discriminator = None

        if deployment_id is not None:
            self.deployment_id = deployment_id
        if total_deployment_run_duration is not None:
            self.total_deployment_run_duration = total_deployment_run_duration
        if average_deployment_run_duration is not None:
            self.average_deployment_run_duration = average_deployment_run_duration
        if median_deployment_run_duration is not None:
            self.median_deployment_run_duration = median_deployment_run_duration
        if longest_deployment_run_duration is not None:
            self.longest_deployment_run_duration = longest_deployment_run_duration
        if shortest_deployment_run_duration is not None:
            self.shortest_deployment_run_duration = shortest_deployment_run_duration
        if total_deployment_runs is not None:
            self.total_deployment_runs = total_deployment_runs
        if total_deployment_run_success is not None:
            self.total_deployment_run_success = total_deployment_run_success
        if total_deployment_run_error is not None:
            self.total_deployment_run_error = total_deployment_run_error
        if total_deployment_run_cancel is not None:
            self.total_deployment_run_cancel = total_deployment_run_cancel
        if total_deployment_run_unknown is not None:
            self.total_deployment_run_unknown = total_deployment_run_unknown
        if total_virtual_machines is not None:
            self.total_virtual_machines = total_virtual_machines

    @property
    def deployment_id(self):
        """Gets the deployment_id of this DeploymentAssetMetric.  # noqa: E501


        :return: The deployment_id of this DeploymentAssetMetric.  # noqa: E501
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this DeploymentAssetMetric.


        :param deployment_id: The deployment_id of this DeploymentAssetMetric.  # noqa: E501
        :type: str
        """

        self._deployment_id = deployment_id

    @property
    def total_deployment_run_duration(self):
        """Gets the total_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501


        :return: The total_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._total_deployment_run_duration

    @total_deployment_run_duration.setter
    def total_deployment_run_duration(self, total_deployment_run_duration):
        """Sets the total_deployment_run_duration of this DeploymentAssetMetric.


        :param total_deployment_run_duration: The total_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._total_deployment_run_duration = total_deployment_run_duration

    @property
    def average_deployment_run_duration(self):
        """Gets the average_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501


        :return: The average_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._average_deployment_run_duration

    @average_deployment_run_duration.setter
    def average_deployment_run_duration(self, average_deployment_run_duration):
        """Sets the average_deployment_run_duration of this DeploymentAssetMetric.


        :param average_deployment_run_duration: The average_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._average_deployment_run_duration = average_deployment_run_duration

    @property
    def median_deployment_run_duration(self):
        """Gets the median_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501


        :return: The median_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._median_deployment_run_duration

    @median_deployment_run_duration.setter
    def median_deployment_run_duration(self, median_deployment_run_duration):
        """Sets the median_deployment_run_duration of this DeploymentAssetMetric.


        :param median_deployment_run_duration: The median_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._median_deployment_run_duration = median_deployment_run_duration

    @property
    def longest_deployment_run_duration(self):
        """Gets the longest_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501


        :return: The longest_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._longest_deployment_run_duration

    @longest_deployment_run_duration.setter
    def longest_deployment_run_duration(self, longest_deployment_run_duration):
        """Sets the longest_deployment_run_duration of this DeploymentAssetMetric.


        :param longest_deployment_run_duration: The longest_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._longest_deployment_run_duration = longest_deployment_run_duration

    @property
    def shortest_deployment_run_duration(self):
        """Gets the shortest_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501


        :return: The shortest_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._shortest_deployment_run_duration

    @shortest_deployment_run_duration.setter
    def shortest_deployment_run_duration(self, shortest_deployment_run_duration):
        """Sets the shortest_deployment_run_duration of this DeploymentAssetMetric.


        :param shortest_deployment_run_duration: The shortest_deployment_run_duration of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._shortest_deployment_run_duration = shortest_deployment_run_duration

    @property
    def total_deployment_runs(self):
        """Gets the total_deployment_runs of this DeploymentAssetMetric.  # noqa: E501


        :return: The total_deployment_runs of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._total_deployment_runs

    @total_deployment_runs.setter
    def total_deployment_runs(self, total_deployment_runs):
        """Sets the total_deployment_runs of this DeploymentAssetMetric.


        :param total_deployment_runs: The total_deployment_runs of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._total_deployment_runs = total_deployment_runs

    @property
    def total_deployment_run_success(self):
        """Gets the total_deployment_run_success of this DeploymentAssetMetric.  # noqa: E501


        :return: The total_deployment_run_success of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._total_deployment_run_success

    @total_deployment_run_success.setter
    def total_deployment_run_success(self, total_deployment_run_success):
        """Sets the total_deployment_run_success of this DeploymentAssetMetric.


        :param total_deployment_run_success: The total_deployment_run_success of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._total_deployment_run_success = total_deployment_run_success

    @property
    def total_deployment_run_error(self):
        """Gets the total_deployment_run_error of this DeploymentAssetMetric.  # noqa: E501


        :return: The total_deployment_run_error of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._total_deployment_run_error

    @total_deployment_run_error.setter
    def total_deployment_run_error(self, total_deployment_run_error):
        """Sets the total_deployment_run_error of this DeploymentAssetMetric.


        :param total_deployment_run_error: The total_deployment_run_error of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._total_deployment_run_error = total_deployment_run_error

    @property
    def total_deployment_run_cancel(self):
        """Gets the total_deployment_run_cancel of this DeploymentAssetMetric.  # noqa: E501


        :return: The total_deployment_run_cancel of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._total_deployment_run_cancel

    @total_deployment_run_cancel.setter
    def total_deployment_run_cancel(self, total_deployment_run_cancel):
        """Sets the total_deployment_run_cancel of this DeploymentAssetMetric.


        :param total_deployment_run_cancel: The total_deployment_run_cancel of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._total_deployment_run_cancel = total_deployment_run_cancel

    @property
    def total_deployment_run_unknown(self):
        """Gets the total_deployment_run_unknown of this DeploymentAssetMetric.  # noqa: E501


        :return: The total_deployment_run_unknown of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._total_deployment_run_unknown

    @total_deployment_run_unknown.setter
    def total_deployment_run_unknown(self, total_deployment_run_unknown):
        """Sets the total_deployment_run_unknown of this DeploymentAssetMetric.


        :param total_deployment_run_unknown: The total_deployment_run_unknown of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._total_deployment_run_unknown = total_deployment_run_unknown

    @property
    def total_virtual_machines(self):
        """Gets the total_virtual_machines of this DeploymentAssetMetric.  # noqa: E501


        :return: The total_virtual_machines of this DeploymentAssetMetric.  # noqa: E501
        :rtype: int
        """
        return self._total_virtual_machines

    @total_virtual_machines.setter
    def total_virtual_machines(self, total_virtual_machines):
        """Sets the total_virtual_machines of this DeploymentAssetMetric.


        :param total_virtual_machines: The total_virtual_machines of this DeploymentAssetMetric.  # noqa: E501
        :type: int
        """

        self._total_virtual_machines = total_virtual_machines

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
        if not isinstance(other, DeploymentAssetMetric):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentAssetMetric):
            return True

        return self.to_dict() != other.to_dict()
