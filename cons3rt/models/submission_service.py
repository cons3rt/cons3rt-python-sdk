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


class SubmissionService(object):
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
        'host_logging_string': 'str',
        'credentials': 'Credentials',
        'enabled': 'bool',
        'id': 'int',
        'name': 'str',
        'submission_endpoint': 'SubmissionEndpoint'
    }

    attribute_map = {
        'host_logging_string': 'hostLoggingString',
        'credentials': 'credentials',
        'enabled': 'enabled',
        'id': 'id',
        'name': 'name',
        'submission_endpoint': 'submissionEndpoint'
    }

    def __init__(self, host_logging_string=None, credentials=None, enabled=None, id=None, name=None, submission_endpoint=None, local_vars_configuration=None):  # noqa: E501
        """SubmissionService - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host_logging_string = None
        self._credentials = None
        self._enabled = None
        self._id = None
        self._name = None
        self._submission_endpoint = None
        self.discriminator = None

        if host_logging_string is not None:
            self.host_logging_string = host_logging_string
        if credentials is not None:
            self.credentials = credentials
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        self.name = name
        self.submission_endpoint = submission_endpoint

    @property
    def host_logging_string(self):
        """Gets the host_logging_string of this SubmissionService.  # noqa: E501


        :return: The host_logging_string of this SubmissionService.  # noqa: E501
        :rtype: str
        """
        return self._host_logging_string

    @host_logging_string.setter
    def host_logging_string(self, host_logging_string):
        """Sets the host_logging_string of this SubmissionService.


        :param host_logging_string: The host_logging_string of this SubmissionService.  # noqa: E501
        :type: str
        """

        self._host_logging_string = host_logging_string

    @property
    def credentials(self):
        """Gets the credentials of this SubmissionService.  # noqa: E501


        :return: The credentials of this SubmissionService.  # noqa: E501
        :rtype: Credentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this SubmissionService.


        :param credentials: The credentials of this SubmissionService.  # noqa: E501
        :type: Credentials
        """

        self._credentials = credentials

    @property
    def enabled(self):
        """Gets the enabled of this SubmissionService.  # noqa: E501


        :return: The enabled of this SubmissionService.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SubmissionService.


        :param enabled: The enabled of this SubmissionService.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this SubmissionService.  # noqa: E501


        :return: The id of this SubmissionService.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubmissionService.


        :param id: The id of this SubmissionService.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SubmissionService.  # noqa: E501


        :return: The name of this SubmissionService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubmissionService.


        :param name: The name of this SubmissionService.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def submission_endpoint(self):
        """Gets the submission_endpoint of this SubmissionService.  # noqa: E501


        :return: The submission_endpoint of this SubmissionService.  # noqa: E501
        :rtype: SubmissionEndpoint
        """
        return self._submission_endpoint

    @submission_endpoint.setter
    def submission_endpoint(self, submission_endpoint):
        """Sets the submission_endpoint of this SubmissionService.


        :param submission_endpoint: The submission_endpoint of this SubmissionService.  # noqa: E501
        :type: SubmissionEndpoint
        """
        if self.local_vars_configuration.client_side_validation and submission_endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `submission_endpoint`, must not be `None`")  # noqa: E501

        self._submission_endpoint = submission_endpoint

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
        if not isinstance(other, SubmissionService):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubmissionService):
            return True

        return self.to_dict() != other.to_dict()
