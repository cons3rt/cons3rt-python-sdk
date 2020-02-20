# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class SubmitDeploymentRunRequestReturnType(object):
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
        'deployment_run_id': 'int',
        'message': 'str'
    }

    attribute_map = {
        'deployment_run_id': 'deploymentRunId',
        'message': 'message'
    }

    def __init__(self, deployment_run_id=None, message=None, local_vars_configuration=None):  # noqa: E501
        """SubmitDeploymentRunRequestReturnType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deployment_run_id = None
        self._message = None
        self.discriminator = None

        if deployment_run_id is not None:
            self.deployment_run_id = deployment_run_id
        if message is not None:
            self.message = message

    @property
    def deployment_run_id(self):
        """Gets the deployment_run_id of this SubmitDeploymentRunRequestReturnType.  # noqa: E501


        :return: The deployment_run_id of this SubmitDeploymentRunRequestReturnType.  # noqa: E501
        :rtype: int
        """
        return self._deployment_run_id

    @deployment_run_id.setter
    def deployment_run_id(self, deployment_run_id):
        """Sets the deployment_run_id of this SubmitDeploymentRunRequestReturnType.


        :param deployment_run_id: The deployment_run_id of this SubmitDeploymentRunRequestReturnType.  # noqa: E501
        :type: int
        """

        self._deployment_run_id = deployment_run_id

    @property
    def message(self):
        """Gets the message of this SubmitDeploymentRunRequestReturnType.  # noqa: E501


        :return: The message of this SubmitDeploymentRunRequestReturnType.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SubmitDeploymentRunRequestReturnType.


        :param message: The message of this SubmitDeploymentRunRequestReturnType.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, SubmitDeploymentRunRequestReturnType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubmitDeploymentRunRequestReturnType):
            return True

        return self.to_dict() != other.to_dict()
