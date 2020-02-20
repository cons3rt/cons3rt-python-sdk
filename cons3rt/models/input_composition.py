# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputComposition(object):
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
        'description': 'str',
        'deployment_run_options': 'InputCompositionRunOptions'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'deployment_run_options': 'deploymentRunOptions'
    }

    def __init__(self, name=None, description=None, deployment_run_options=None, local_vars_configuration=None):  # noqa: E501
        """InputComposition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._deployment_run_options = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.deployment_run_options = deployment_run_options

    @property
    def name(self):
        """Gets the name of this InputComposition.  # noqa: E501


        :return: The name of this InputComposition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputComposition.


        :param name: The name of this InputComposition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this InputComposition.  # noqa: E501


        :return: The description of this InputComposition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InputComposition.


        :param description: The description of this InputComposition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def deployment_run_options(self):
        """Gets the deployment_run_options of this InputComposition.  # noqa: E501


        :return: The deployment_run_options of this InputComposition.  # noqa: E501
        :rtype: InputCompositionRunOptions
        """
        return self._deployment_run_options

    @deployment_run_options.setter
    def deployment_run_options(self, deployment_run_options):
        """Sets the deployment_run_options of this InputComposition.


        :param deployment_run_options: The deployment_run_options of this InputComposition.  # noqa: E501
        :type: InputCompositionRunOptions
        """
        if self.local_vars_configuration.client_side_validation and deployment_run_options is None:  # noqa: E501
            raise ValueError("Invalid value for `deployment_run_options`, must not be `None`")  # noqa: E501

        self._deployment_run_options = deployment_run_options

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
        if not isinstance(other, InputComposition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputComposition):
            return True

        return self.to_dict() != other.to_dict()
