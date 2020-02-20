# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class DeploymentHost(object):
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
        'deployment': 'Deployment',
        'scenario': 'Scenario',
        'id': 'int',
        'build_order': 'int',
        'system_module': 'SystemModule',
        'system_role': 'str'
    }

    attribute_map = {
        'deployment': 'deployment',
        'scenario': 'scenario',
        'id': 'id',
        'build_order': 'buildOrder',
        'system_module': 'systemModule',
        'system_role': 'systemRole'
    }

    def __init__(self, deployment=None, scenario=None, id=None, build_order=None, system_module=None, system_role=None, local_vars_configuration=None):  # noqa: E501
        """DeploymentHost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deployment = None
        self._scenario = None
        self._id = None
        self._build_order = None
        self._system_module = None
        self._system_role = None
        self.discriminator = None

        if deployment is not None:
            self.deployment = deployment
        if scenario is not None:
            self.scenario = scenario
        if id is not None:
            self.id = id
        if build_order is not None:
            self.build_order = build_order
        if system_module is not None:
            self.system_module = system_module
        self.system_role = system_role

    @property
    def deployment(self):
        """Gets the deployment of this DeploymentHost.  # noqa: E501


        :return: The deployment of this DeploymentHost.  # noqa: E501
        :rtype: Deployment
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this DeploymentHost.


        :param deployment: The deployment of this DeploymentHost.  # noqa: E501
        :type: Deployment
        """

        self._deployment = deployment

    @property
    def scenario(self):
        """Gets the scenario of this DeploymentHost.  # noqa: E501


        :return: The scenario of this DeploymentHost.  # noqa: E501
        :rtype: Scenario
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this DeploymentHost.


        :param scenario: The scenario of this DeploymentHost.  # noqa: E501
        :type: Scenario
        """

        self._scenario = scenario

    @property
    def id(self):
        """Gets the id of this DeploymentHost.  # noqa: E501


        :return: The id of this DeploymentHost.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentHost.


        :param id: The id of this DeploymentHost.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def build_order(self):
        """Gets the build_order of this DeploymentHost.  # noqa: E501


        :return: The build_order of this DeploymentHost.  # noqa: E501
        :rtype: int
        """
        return self._build_order

    @build_order.setter
    def build_order(self, build_order):
        """Sets the build_order of this DeploymentHost.


        :param build_order: The build_order of this DeploymentHost.  # noqa: E501
        :type: int
        """

        self._build_order = build_order

    @property
    def system_module(self):
        """Gets the system_module of this DeploymentHost.  # noqa: E501


        :return: The system_module of this DeploymentHost.  # noqa: E501
        :rtype: SystemModule
        """
        return self._system_module

    @system_module.setter
    def system_module(self, system_module):
        """Sets the system_module of this DeploymentHost.


        :param system_module: The system_module of this DeploymentHost.  # noqa: E501
        :type: SystemModule
        """

        self._system_module = system_module

    @property
    def system_role(self):
        """Gets the system_role of this DeploymentHost.  # noqa: E501


        :return: The system_role of this DeploymentHost.  # noqa: E501
        :rtype: str
        """
        return self._system_role

    @system_role.setter
    def system_role(self, system_role):
        """Sets the system_role of this DeploymentHost.


        :param system_role: The system_role of this DeploymentHost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_role is None:  # noqa: E501
            raise ValueError("Invalid value for `system_role`, must not be `None`")  # noqa: E501

        self._system_role = system_role

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
        if not isinstance(other, DeploymentHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentHost):
            return True

        return self.to_dict() != other.to_dict()
