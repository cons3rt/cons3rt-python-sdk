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


class MinimalDeploymentRun(object):
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
        'creator': 'MinimalUser',
        'id': 'int',
        'project': 'MinimalProject',
        'result': 'str',
        'start_time': 'int',
        'canceled': 'bool',
        'deployment_run_status': 'str',
        'description': 'str',
        'fap_status': 'str',
        'locked': 'bool',
        'name': 'str',
        'deployment_run_result_type': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'id': 'id',
        'project': 'project',
        'result': 'result',
        'start_time': 'startTime',
        'canceled': 'canceled',
        'deployment_run_status': 'deploymentRunStatus',
        'description': 'description',
        'fap_status': 'fapStatus',
        'locked': 'locked',
        'name': 'name',
        'deployment_run_result_type': 'deploymentRunResultType'
    }

    def __init__(self, creator=None, id=None, project=None, result=None, start_time=None, canceled=None, deployment_run_status=None, description=None, fap_status=None, locked=None, name=None, deployment_run_result_type=None, local_vars_configuration=None):  # noqa: E501
        """MinimalDeploymentRun - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._creator = None
        self._id = None
        self._project = None
        self._result = None
        self._start_time = None
        self._canceled = None
        self._deployment_run_status = None
        self._description = None
        self._fap_status = None
        self._locked = None
        self._name = None
        self._deployment_run_result_type = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        if id is not None:
            self.id = id
        if project is not None:
            self.project = project
        if result is not None:
            self.result = result
        if start_time is not None:
            self.start_time = start_time
        if canceled is not None:
            self.canceled = canceled
        if deployment_run_status is not None:
            self.deployment_run_status = deployment_run_status
        if description is not None:
            self.description = description
        if fap_status is not None:
            self.fap_status = fap_status
        if locked is not None:
            self.locked = locked
        if name is not None:
            self.name = name
        if deployment_run_result_type is not None:
            self.deployment_run_result_type = deployment_run_result_type

    @property
    def creator(self):
        """Gets the creator of this MinimalDeploymentRun.  # noqa: E501


        :return: The creator of this MinimalDeploymentRun.  # noqa: E501
        :rtype: MinimalUser
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this MinimalDeploymentRun.


        :param creator: The creator of this MinimalDeploymentRun.  # noqa: E501
        :type: MinimalUser
        """

        self._creator = creator

    @property
    def id(self):
        """Gets the id of this MinimalDeploymentRun.  # noqa: E501


        :return: The id of this MinimalDeploymentRun.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalDeploymentRun.


        :param id: The id of this MinimalDeploymentRun.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this MinimalDeploymentRun.  # noqa: E501


        :return: The project of this MinimalDeploymentRun.  # noqa: E501
        :rtype: MinimalProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this MinimalDeploymentRun.


        :param project: The project of this MinimalDeploymentRun.  # noqa: E501
        :type: MinimalProject
        """

        self._project = project

    @property
    def result(self):
        """Gets the result of this MinimalDeploymentRun.  # noqa: E501


        :return: The result of this MinimalDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this MinimalDeploymentRun.


        :param result: The result of this MinimalDeploymentRun.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def start_time(self):
        """Gets the start_time of this MinimalDeploymentRun.  # noqa: E501


        :return: The start_time of this MinimalDeploymentRun.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this MinimalDeploymentRun.


        :param start_time: The start_time of this MinimalDeploymentRun.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def canceled(self):
        """Gets the canceled of this MinimalDeploymentRun.  # noqa: E501


        :return: The canceled of this MinimalDeploymentRun.  # noqa: E501
        :rtype: bool
        """
        return self._canceled

    @canceled.setter
    def canceled(self, canceled):
        """Sets the canceled of this MinimalDeploymentRun.


        :param canceled: The canceled of this MinimalDeploymentRun.  # noqa: E501
        :type: bool
        """

        self._canceled = canceled

    @property
    def deployment_run_status(self):
        """Gets the deployment_run_status of this MinimalDeploymentRun.  # noqa: E501


        :return: The deployment_run_status of this MinimalDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._deployment_run_status

    @deployment_run_status.setter
    def deployment_run_status(self, deployment_run_status):
        """Sets the deployment_run_status of this MinimalDeploymentRun.


        :param deployment_run_status: The deployment_run_status of this MinimalDeploymentRun.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "SCHEDULED", "SUBMITTED", "PROVISIONING_HOSTS", "HOSTS_PROVISIONED", "RESERVED", "RELEASE_REQUESTED", "RELEASING", "TESTING", "TESTED", "REDEPLOYING_HOSTS", "COMPLETED", "CANCELED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deployment_run_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deployment_run_status` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_run_status, allowed_values)
            )

        self._deployment_run_status = deployment_run_status

    @property
    def description(self):
        """Gets the description of this MinimalDeploymentRun.  # noqa: E501


        :return: The description of this MinimalDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MinimalDeploymentRun.


        :param description: The description of this MinimalDeploymentRun.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fap_status(self):
        """Gets the fap_status of this MinimalDeploymentRun.  # noqa: E501


        :return: The fap_status of this MinimalDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._fap_status

    @fap_status.setter
    def fap_status(self, fap_status):
        """Sets the fap_status of this MinimalDeploymentRun.


        :param fap_status: The fap_status of this MinimalDeploymentRun.  # noqa: E501
        :type: str
        """
        allowed_values = ["REQUESTED", "BUILDING_HOSTSET", "BUILDING_HOSTSET_ERROR", "HOSTSET_BUILT_POWERED_OFF", "POWERING_ON", "POWERING_ON_ERROR", "POWERED_ON", "AWAITING_AGENT_CHECK_IN", "AGENT_CHECK_IN_ERROR", "AGENT_CHECK_IN_SUCCESS", "BUILDING_SOURCE", "SOURCE_BUILT", "BUILDING_SOURCE_ERROR", "BUILDING_SYSTEMS", "BUILDING_SYSTEMS_ERROR", "SYSTEMS_BUILT", "BUILDING_SCENARIO", "BUILDING_SCENARIO_ERROR", "SCENARIO_BUILT", "REBOOTING", "REBOOTING_ERROR", "RESERVED", "RELEASE_REQUESTED", "RELEASING", "RELEASING_SCENARIO_ERROR", "COMPLETE", "UNKNOWN", "CANCELED", "INVALID_STATE_ERROR", "FAP_SERVICE_COMMUNICATIONS_ERROR", "INVALID_REQUEST_ERROR", "REDEPLOYING_HOSTS", "REDEPLOYING_HOSTS_ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and fap_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `fap_status` ({0}), must be one of {1}"  # noqa: E501
                .format(fap_status, allowed_values)
            )

        self._fap_status = fap_status

    @property
    def locked(self):
        """Gets the locked of this MinimalDeploymentRun.  # noqa: E501


        :return: The locked of this MinimalDeploymentRun.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this MinimalDeploymentRun.


        :param locked: The locked of this MinimalDeploymentRun.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def name(self):
        """Gets the name of this MinimalDeploymentRun.  # noqa: E501


        :return: The name of this MinimalDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MinimalDeploymentRun.


        :param name: The name of this MinimalDeploymentRun.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def deployment_run_result_type(self):
        """Gets the deployment_run_result_type of this MinimalDeploymentRun.  # noqa: E501


        :return: The deployment_run_result_type of this MinimalDeploymentRun.  # noqa: E501
        :rtype: str
        """
        return self._deployment_run_result_type

    @deployment_run_result_type.setter
    def deployment_run_result_type(self, deployment_run_result_type):
        """Sets the deployment_run_result_type of this MinimalDeploymentRun.


        :param deployment_run_result_type: The deployment_run_result_type of this MinimalDeploymentRun.  # noqa: E501
        :type: str
        """
        allowed_values = ["ERROR", "SUCCESS", "CANCELED", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deployment_run_result_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deployment_run_result_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_run_result_type, allowed_values)
            )

        self._deployment_run_result_type = deployment_run_result_type

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
        if not isinstance(other, MinimalDeploymentRun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalDeploymentRun):
            return True

        return self.to_dict() != other.to_dict()
