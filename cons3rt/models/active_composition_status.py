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


class ActiveCompositionStatus(object):
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
        'name': 'str',
        'project_id': 'int',
        'stoppable': 'bool',
        'connectable': 'bool',
        'startable': 'bool',
        'type': 'str',
        'deployment_run_id': 'int',
        'deployment_run_status': 'str',
        'deployment_run_host': 'list[MinimalDeploymentRunHost]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'projectId',
        'stoppable': 'stoppable',
        'connectable': 'connectable',
        'startable': 'startable',
        'type': 'type',
        'deployment_run_id': 'deploymentRunId',
        'deployment_run_status': 'deploymentRunStatus',
        'deployment_run_host': 'deploymentRunHost'
    }

    def __init__(self, id=None, name=None, project_id=None, stoppable=None, connectable=None, startable=None, type=None, deployment_run_id=None, deployment_run_status=None, deployment_run_host=None, local_vars_configuration=None):  # noqa: E501
        """ActiveCompositionStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._project_id = None
        self._stoppable = None
        self._connectable = None
        self._startable = None
        self._type = None
        self._deployment_run_id = None
        self._deployment_run_status = None
        self._deployment_run_host = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if stoppable is not None:
            self.stoppable = stoppable
        if connectable is not None:
            self.connectable = connectable
        if startable is not None:
            self.startable = startable
        self.type = type
        if deployment_run_id is not None:
            self.deployment_run_id = deployment_run_id
        if deployment_run_status is not None:
            self.deployment_run_status = deployment_run_status
        if deployment_run_host is not None:
            self.deployment_run_host = deployment_run_host

    @property
    def id(self):
        """Gets the id of this ActiveCompositionStatus.  # noqa: E501


        :return: The id of this ActiveCompositionStatus.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActiveCompositionStatus.


        :param id: The id of this ActiveCompositionStatus.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ActiveCompositionStatus.  # noqa: E501


        :return: The name of this ActiveCompositionStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActiveCompositionStatus.


        :param name: The name of this ActiveCompositionStatus.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this ActiveCompositionStatus.  # noqa: E501


        :return: The project_id of this ActiveCompositionStatus.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ActiveCompositionStatus.


        :param project_id: The project_id of this ActiveCompositionStatus.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def stoppable(self):
        """Gets the stoppable of this ActiveCompositionStatus.  # noqa: E501


        :return: The stoppable of this ActiveCompositionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._stoppable

    @stoppable.setter
    def stoppable(self, stoppable):
        """Sets the stoppable of this ActiveCompositionStatus.


        :param stoppable: The stoppable of this ActiveCompositionStatus.  # noqa: E501
        :type: bool
        """

        self._stoppable = stoppable

    @property
    def connectable(self):
        """Gets the connectable of this ActiveCompositionStatus.  # noqa: E501


        :return: The connectable of this ActiveCompositionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._connectable

    @connectable.setter
    def connectable(self, connectable):
        """Sets the connectable of this ActiveCompositionStatus.


        :param connectable: The connectable of this ActiveCompositionStatus.  # noqa: E501
        :type: bool
        """

        self._connectable = connectable

    @property
    def startable(self):
        """Gets the startable of this ActiveCompositionStatus.  # noqa: E501


        :return: The startable of this ActiveCompositionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._startable

    @startable.setter
    def startable(self, startable):
        """Sets the startable of this ActiveCompositionStatus.


        :param startable: The startable of this ActiveCompositionStatus.  # noqa: E501
        :type: bool
        """

        self._startable = startable

    @property
    def type(self):
        """Gets the type of this ActiveCompositionStatus.  # noqa: E501


        :return: The type of this ActiveCompositionStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ActiveCompositionStatus.


        :param type: The type of this ActiveCompositionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def deployment_run_id(self):
        """Gets the deployment_run_id of this ActiveCompositionStatus.  # noqa: E501


        :return: The deployment_run_id of this ActiveCompositionStatus.  # noqa: E501
        :rtype: int
        """
        return self._deployment_run_id

    @deployment_run_id.setter
    def deployment_run_id(self, deployment_run_id):
        """Sets the deployment_run_id of this ActiveCompositionStatus.


        :param deployment_run_id: The deployment_run_id of this ActiveCompositionStatus.  # noqa: E501
        :type: int
        """

        self._deployment_run_id = deployment_run_id

    @property
    def deployment_run_status(self):
        """Gets the deployment_run_status of this ActiveCompositionStatus.  # noqa: E501


        :return: The deployment_run_status of this ActiveCompositionStatus.  # noqa: E501
        :rtype: str
        """
        return self._deployment_run_status

    @deployment_run_status.setter
    def deployment_run_status(self, deployment_run_status):
        """Sets the deployment_run_status of this ActiveCompositionStatus.


        :param deployment_run_status: The deployment_run_status of this ActiveCompositionStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "SCHEDULED", "SUBMITTED", "PROVISIONING_HOSTS", "HOSTS_PROVISIONED", "RESERVED", "RELEASE_REQUESTED", "RELEASING", "TESTING", "TESTED", "COMPLETED", "CANCELED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deployment_run_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deployment_run_status` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_run_status, allowed_values)
            )

        self._deployment_run_status = deployment_run_status

    @property
    def deployment_run_host(self):
        """Gets the deployment_run_host of this ActiveCompositionStatus.  # noqa: E501


        :return: The deployment_run_host of this ActiveCompositionStatus.  # noqa: E501
        :rtype: list[MinimalDeploymentRunHost]
        """
        return self._deployment_run_host

    @deployment_run_host.setter
    def deployment_run_host(self, deployment_run_host):
        """Sets the deployment_run_host of this ActiveCompositionStatus.


        :param deployment_run_host: The deployment_run_host of this ActiveCompositionStatus.  # noqa: E501
        :type: list[MinimalDeploymentRunHost]
        """

        self._deployment_run_host = deployment_run_host

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
        if not isinstance(other, ActiveCompositionStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActiveCompositionStatus):
            return True

        return self.to_dict() != other.to_dict()
