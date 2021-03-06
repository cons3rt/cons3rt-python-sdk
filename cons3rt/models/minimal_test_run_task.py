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


class MinimalTestRunTask(object):
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
        'report_uri': 'str',
        'test_bundle': 'MinimalTestBundle',
        'test_manager_status': 'str',
        'test_result': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'id': 'id',
        'project': 'project',
        'result': 'result',
        'start_time': 'startTime',
        'report_uri': 'reportUri',
        'test_bundle': 'testBundle',
        'test_manager_status': 'testManagerStatus',
        'test_result': 'testResult'
    }

    def __init__(self, creator=None, id=None, project=None, result=None, start_time=None, report_uri=None, test_bundle=None, test_manager_status=None, test_result=None, local_vars_configuration=None):  # noqa: E501
        """MinimalTestRunTask - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._creator = None
        self._id = None
        self._project = None
        self._result = None
        self._start_time = None
        self._report_uri = None
        self._test_bundle = None
        self._test_manager_status = None
        self._test_result = None
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
        if report_uri is not None:
            self.report_uri = report_uri
        if test_bundle is not None:
            self.test_bundle = test_bundle
        if test_manager_status is not None:
            self.test_manager_status = test_manager_status
        if test_result is not None:
            self.test_result = test_result

    @property
    def creator(self):
        """Gets the creator of this MinimalTestRunTask.  # noqa: E501


        :return: The creator of this MinimalTestRunTask.  # noqa: E501
        :rtype: MinimalUser
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this MinimalTestRunTask.


        :param creator: The creator of this MinimalTestRunTask.  # noqa: E501
        :type: MinimalUser
        """

        self._creator = creator

    @property
    def id(self):
        """Gets the id of this MinimalTestRunTask.  # noqa: E501


        :return: The id of this MinimalTestRunTask.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalTestRunTask.


        :param id: The id of this MinimalTestRunTask.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this MinimalTestRunTask.  # noqa: E501


        :return: The project of this MinimalTestRunTask.  # noqa: E501
        :rtype: MinimalProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this MinimalTestRunTask.


        :param project: The project of this MinimalTestRunTask.  # noqa: E501
        :type: MinimalProject
        """

        self._project = project

    @property
    def result(self):
        """Gets the result of this MinimalTestRunTask.  # noqa: E501


        :return: The result of this MinimalTestRunTask.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this MinimalTestRunTask.


        :param result: The result of this MinimalTestRunTask.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def start_time(self):
        """Gets the start_time of this MinimalTestRunTask.  # noqa: E501


        :return: The start_time of this MinimalTestRunTask.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this MinimalTestRunTask.


        :param start_time: The start_time of this MinimalTestRunTask.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def report_uri(self):
        """Gets the report_uri of this MinimalTestRunTask.  # noqa: E501


        :return: The report_uri of this MinimalTestRunTask.  # noqa: E501
        :rtype: str
        """
        return self._report_uri

    @report_uri.setter
    def report_uri(self, report_uri):
        """Sets the report_uri of this MinimalTestRunTask.


        :param report_uri: The report_uri of this MinimalTestRunTask.  # noqa: E501
        :type: str
        """

        self._report_uri = report_uri

    @property
    def test_bundle(self):
        """Gets the test_bundle of this MinimalTestRunTask.  # noqa: E501


        :return: The test_bundle of this MinimalTestRunTask.  # noqa: E501
        :rtype: MinimalTestBundle
        """
        return self._test_bundle

    @test_bundle.setter
    def test_bundle(self, test_bundle):
        """Sets the test_bundle of this MinimalTestRunTask.


        :param test_bundle: The test_bundle of this MinimalTestRunTask.  # noqa: E501
        :type: MinimalTestBundle
        """

        self._test_bundle = test_bundle

    @property
    def test_manager_status(self):
        """Gets the test_manager_status of this MinimalTestRunTask.  # noqa: E501


        :return: The test_manager_status of this MinimalTestRunTask.  # noqa: E501
        :rtype: str
        """
        return self._test_manager_status

    @test_manager_status.setter
    def test_manager_status(self, test_manager_status):
        """Sets the test_manager_status of this MinimalTestRunTask.


        :param test_manager_status: The test_manager_status of this MinimalTestRunTask.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "SCHEDULED", "SUBMITTED", "TESTING", "COMPLETED_WITH_ERROR", "COMPLETED_WITH_SUCCESS", "CANCELED", "ERROR", "TIMED_OUT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and test_manager_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `test_manager_status` ({0}), must be one of {1}"  # noqa: E501
                .format(test_manager_status, allowed_values)
            )

        self._test_manager_status = test_manager_status

    @property
    def test_result(self):
        """Gets the test_result of this MinimalTestRunTask.  # noqa: E501


        :return: The test_result of this MinimalTestRunTask.  # noqa: E501
        :rtype: str
        """
        return self._test_result

    @test_result.setter
    def test_result(self, test_result):
        """Sets the test_result of this MinimalTestRunTask.


        :param test_result: The test_result of this MinimalTestRunTask.  # noqa: E501
        :type: str
        """
        allowed_values = ["TEST_PASS", "TEST_FAIL", "TEST_CANCELED", "VERIFY_AGENT_PROXY_ERROR", "TEST_SETUP_ERROR", "TEST_RESULTS_CLEANUP_ERROR", "TEST_REPORT_UPLOAD_ERROR", "TEST_TEARDOWN_ERROR", "TEST_ENVIRONMENT_ERROR", "RETINA_ERROR", "SOAPUI_ERROR", "LISA_ERROR", "NESSUS_ERROR", "CERTIFY_ERROR", "SELENIUM_ERROR", "SCRIPT_ERROR", "WEBEXPLOITSUITE_ERROR", "SONAR_ERROR", "FORTIFY_ERROR", "TEST_TIMEOUT_ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and test_result not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `test_result` ({0}), must be one of {1}"  # noqa: E501
                .format(test_result, allowed_values)
            )

        self._test_result = test_result

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
        if not isinstance(other, MinimalTestRunTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalTestRunTask):
            return True

        return self.to_dict() != other.to_dict()
