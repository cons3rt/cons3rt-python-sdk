# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class TestTool(object):
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
        'test_tool_type': 'str',
        'test_tool_vendor': 'str',
        'auto_registered': 'bool',
        'description': 'str',
        'hostname': 'str',
        'id': 'int',
        'instance_limit': 'int',
        'name': 'str',
        'properties': 'list[ModelProperty]',
        'test_run_tasks': 'list[int]',
        'test_tool_agent_installed': 'bool',
        'version': 'str',
        'tma_enabled': 'bool',
        'tma_online': 'bool',
        'tma_service_name': 'str',
        'tma_version': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'test_tool_type': 'testToolType',
        'test_tool_vendor': 'testToolVendor',
        'auto_registered': 'autoRegistered',
        'description': 'description',
        'hostname': 'hostname',
        'id': 'id',
        'instance_limit': 'instanceLimit',
        'name': 'name',
        'properties': 'properties',
        'test_run_tasks': 'testRunTasks',
        'test_tool_agent_installed': 'testToolAgentInstalled',
        'version': 'version',
        'tma_enabled': 'tmaEnabled',
        'tma_online': 'tmaOnline',
        'tma_service_name': 'tmaServiceName',
        'tma_version': 'tmaVersion',
        'visibility': 'visibility'
    }

    def __init__(self, test_tool_type=None, test_tool_vendor=None, auto_registered=None, description=None, hostname=None, id=None, instance_limit=None, name=None, properties=None, test_run_tasks=None, test_tool_agent_installed=None, version=None, tma_enabled=None, tma_online=None, tma_service_name=None, tma_version=None, visibility=None, local_vars_configuration=None):  # noqa: E501
        """TestTool - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._test_tool_type = None
        self._test_tool_vendor = None
        self._auto_registered = None
        self._description = None
        self._hostname = None
        self._id = None
        self._instance_limit = None
        self._name = None
        self._properties = None
        self._test_run_tasks = None
        self._test_tool_agent_installed = None
        self._version = None
        self._tma_enabled = None
        self._tma_online = None
        self._tma_service_name = None
        self._tma_version = None
        self._visibility = None
        self.discriminator = None

        if test_tool_type is not None:
            self.test_tool_type = test_tool_type
        if test_tool_vendor is not None:
            self.test_tool_vendor = test_tool_vendor
        if auto_registered is not None:
            self.auto_registered = auto_registered
        if description is not None:
            self.description = description
        if hostname is not None:
            self.hostname = hostname
        if id is not None:
            self.id = id
        if instance_limit is not None:
            self.instance_limit = instance_limit
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties
        if test_run_tasks is not None:
            self.test_run_tasks = test_run_tasks
        if test_tool_agent_installed is not None:
            self.test_tool_agent_installed = test_tool_agent_installed
        if version is not None:
            self.version = version
        if tma_enabled is not None:
            self.tma_enabled = tma_enabled
        if tma_online is not None:
            self.tma_online = tma_online
        if tma_service_name is not None:
            self.tma_service_name = tma_service_name
        if tma_version is not None:
            self.tma_version = tma_version
        if visibility is not None:
            self.visibility = visibility

    @property
    def test_tool_type(self):
        """Gets the test_tool_type of this TestTool.  # noqa: E501


        :return: The test_tool_type of this TestTool.  # noqa: E501
        :rtype: str
        """
        return self._test_tool_type

    @test_tool_type.setter
    def test_tool_type(self, test_tool_type):
        """Sets the test_tool_type of this TestTool.


        :param test_tool_type: The test_tool_type of this TestTool.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "LISA", "SOAPUI", "SELENIUM", "RETINA", "NESSUS", "CERTIFY", "SCRIPT", "WEBEXPLOITSUITE", "FORTIFY", "SONAR", "POWERSHELL", "MOCK"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and test_tool_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `test_tool_type` ({0}), must be one of {1}"  # noqa: E501
                .format(test_tool_type, allowed_values)
            )

        self._test_tool_type = test_tool_type

    @property
    def test_tool_vendor(self):
        """Gets the test_tool_vendor of this TestTool.  # noqa: E501


        :return: The test_tool_vendor of this TestTool.  # noqa: E501
        :rtype: str
        """
        return self._test_tool_vendor

    @test_tool_vendor.setter
    def test_tool_vendor(self, test_tool_vendor):
        """Sets the test_tool_vendor of this TestTool.


        :param test_tool_vendor: The test_tool_vendor of this TestTool.  # noqa: E501
        :type: str
        """

        self._test_tool_vendor = test_tool_vendor

    @property
    def auto_registered(self):
        """Gets the auto_registered of this TestTool.  # noqa: E501


        :return: The auto_registered of this TestTool.  # noqa: E501
        :rtype: bool
        """
        return self._auto_registered

    @auto_registered.setter
    def auto_registered(self, auto_registered):
        """Sets the auto_registered of this TestTool.


        :param auto_registered: The auto_registered of this TestTool.  # noqa: E501
        :type: bool
        """

        self._auto_registered = auto_registered

    @property
    def description(self):
        """Gets the description of this TestTool.  # noqa: E501


        :return: The description of this TestTool.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TestTool.


        :param description: The description of this TestTool.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hostname(self):
        """Gets the hostname of this TestTool.  # noqa: E501


        :return: The hostname of this TestTool.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this TestTool.


        :param hostname: The hostname of this TestTool.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this TestTool.  # noqa: E501


        :return: The id of this TestTool.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestTool.


        :param id: The id of this TestTool.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def instance_limit(self):
        """Gets the instance_limit of this TestTool.  # noqa: E501


        :return: The instance_limit of this TestTool.  # noqa: E501
        :rtype: int
        """
        return self._instance_limit

    @instance_limit.setter
    def instance_limit(self, instance_limit):
        """Sets the instance_limit of this TestTool.


        :param instance_limit: The instance_limit of this TestTool.  # noqa: E501
        :type: int
        """

        self._instance_limit = instance_limit

    @property
    def name(self):
        """Gets the name of this TestTool.  # noqa: E501


        :return: The name of this TestTool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestTool.


        :param name: The name of this TestTool.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this TestTool.  # noqa: E501


        :return: The properties of this TestTool.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TestTool.


        :param properties: The properties of this TestTool.  # noqa: E501
        :type: list[ModelProperty]
        """

        self._properties = properties

    @property
    def test_run_tasks(self):
        """Gets the test_run_tasks of this TestTool.  # noqa: E501


        :return: The test_run_tasks of this TestTool.  # noqa: E501
        :rtype: list[int]
        """
        return self._test_run_tasks

    @test_run_tasks.setter
    def test_run_tasks(self, test_run_tasks):
        """Sets the test_run_tasks of this TestTool.


        :param test_run_tasks: The test_run_tasks of this TestTool.  # noqa: E501
        :type: list[int]
        """

        self._test_run_tasks = test_run_tasks

    @property
    def test_tool_agent_installed(self):
        """Gets the test_tool_agent_installed of this TestTool.  # noqa: E501


        :return: The test_tool_agent_installed of this TestTool.  # noqa: E501
        :rtype: bool
        """
        return self._test_tool_agent_installed

    @test_tool_agent_installed.setter
    def test_tool_agent_installed(self, test_tool_agent_installed):
        """Sets the test_tool_agent_installed of this TestTool.


        :param test_tool_agent_installed: The test_tool_agent_installed of this TestTool.  # noqa: E501
        :type: bool
        """

        self._test_tool_agent_installed = test_tool_agent_installed

    @property
    def version(self):
        """Gets the version of this TestTool.  # noqa: E501


        :return: The version of this TestTool.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TestTool.


        :param version: The version of this TestTool.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def tma_enabled(self):
        """Gets the tma_enabled of this TestTool.  # noqa: E501


        :return: The tma_enabled of this TestTool.  # noqa: E501
        :rtype: bool
        """
        return self._tma_enabled

    @tma_enabled.setter
    def tma_enabled(self, tma_enabled):
        """Sets the tma_enabled of this TestTool.


        :param tma_enabled: The tma_enabled of this TestTool.  # noqa: E501
        :type: bool
        """

        self._tma_enabled = tma_enabled

    @property
    def tma_online(self):
        """Gets the tma_online of this TestTool.  # noqa: E501


        :return: The tma_online of this TestTool.  # noqa: E501
        :rtype: bool
        """
        return self._tma_online

    @tma_online.setter
    def tma_online(self, tma_online):
        """Sets the tma_online of this TestTool.


        :param tma_online: The tma_online of this TestTool.  # noqa: E501
        :type: bool
        """

        self._tma_online = tma_online

    @property
    def tma_service_name(self):
        """Gets the tma_service_name of this TestTool.  # noqa: E501


        :return: The tma_service_name of this TestTool.  # noqa: E501
        :rtype: str
        """
        return self._tma_service_name

    @tma_service_name.setter
    def tma_service_name(self, tma_service_name):
        """Sets the tma_service_name of this TestTool.


        :param tma_service_name: The tma_service_name of this TestTool.  # noqa: E501
        :type: str
        """

        self._tma_service_name = tma_service_name

    @property
    def tma_version(self):
        """Gets the tma_version of this TestTool.  # noqa: E501


        :return: The tma_version of this TestTool.  # noqa: E501
        :rtype: str
        """
        return self._tma_version

    @tma_version.setter
    def tma_version(self, tma_version):
        """Sets the tma_version of this TestTool.


        :param tma_version: The tma_version of this TestTool.  # noqa: E501
        :type: str
        """

        self._tma_version = tma_version

    @property
    def visibility(self):
        """Gets the visibility of this TestTool.  # noqa: E501


        :return: The visibility of this TestTool.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this TestTool.


        :param visibility: The visibility of this TestTool.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "OWNER", "OWNING_PROJECT", "COMMUNITY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and visibility not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

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
        if not isinstance(other, TestTool):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestTool):
            return True

        return self.to_dict() != other.to_dict()
