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


class Cons3rtTemplateData(object):
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
        'display_name': 'str',
        'operating_system': 'str',
        'virt_realm_template_name': 'str',
        'cons3rt_agent_installed': 'bool',
        'container_capable': 'bool',
        'disks': 'list[Disk]',
        'fail_count': 'int',
        'has_gpu': 'bool',
        'id': 'int',
        'license': 'str',
        'max_num_cpus': 'int',
        'max_ram_in_megabytes': 'int',
        'note': 'str',
        'package_management_type': 'str',
        'power_on_delay_override': 'int',
        'power_shell_version': 'str',
        'template_registration': 'TemplateRegistration',
        'remote_access_templates': 'list[RemoteAccessTemplate]',
        'service_management_type': 'str',
        'user_count': 'int',
        'virt_realm_id': 'int'
    }

    attribute_map = {
        'display_name': 'displayName',
        'operating_system': 'operatingSystem',
        'virt_realm_template_name': 'virtRealmTemplateName',
        'cons3rt_agent_installed': 'cons3rtAgentInstalled',
        'container_capable': 'containerCapable',
        'disks': 'disks',
        'fail_count': 'failCount',
        'has_gpu': 'hasGpu',
        'id': 'id',
        'license': 'license',
        'max_num_cpus': 'maxNumCpus',
        'max_ram_in_megabytes': 'maxRamInMegabytes',
        'note': 'note',
        'package_management_type': 'packageManagementType',
        'power_on_delay_override': 'powerOnDelayOverride',
        'power_shell_version': 'powerShellVersion',
        'template_registration': 'templateRegistration',
        'remote_access_templates': 'remoteAccessTemplates',
        'service_management_type': 'serviceManagementType',
        'user_count': 'userCount',
        'virt_realm_id': 'virtRealmId'
    }

    def __init__(self, display_name=None, operating_system=None, virt_realm_template_name=None, cons3rt_agent_installed=None, container_capable=None, disks=None, fail_count=None, has_gpu=None, id=None, license=None, max_num_cpus=None, max_ram_in_megabytes=None, note=None, package_management_type=None, power_on_delay_override=None, power_shell_version=None, template_registration=None, remote_access_templates=None, service_management_type=None, user_count=None, virt_realm_id=None, local_vars_configuration=None):  # noqa: E501
        """Cons3rtTemplateData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._operating_system = None
        self._virt_realm_template_name = None
        self._cons3rt_agent_installed = None
        self._container_capable = None
        self._disks = None
        self._fail_count = None
        self._has_gpu = None
        self._id = None
        self._license = None
        self._max_num_cpus = None
        self._max_ram_in_megabytes = None
        self._note = None
        self._package_management_type = None
        self._power_on_delay_override = None
        self._power_shell_version = None
        self._template_registration = None
        self._remote_access_templates = None
        self._service_management_type = None
        self._user_count = None
        self._virt_realm_id = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        self.operating_system = operating_system
        self.virt_realm_template_name = virt_realm_template_name
        if cons3rt_agent_installed is not None:
            self.cons3rt_agent_installed = cons3rt_agent_installed
        if container_capable is not None:
            self.container_capable = container_capable
        if disks is not None:
            self.disks = disks
        if fail_count is not None:
            self.fail_count = fail_count
        if has_gpu is not None:
            self.has_gpu = has_gpu
        if id is not None:
            self.id = id
        if license is not None:
            self.license = license
        if max_num_cpus is not None:
            self.max_num_cpus = max_num_cpus
        if max_ram_in_megabytes is not None:
            self.max_ram_in_megabytes = max_ram_in_megabytes
        if note is not None:
            self.note = note
        if package_management_type is not None:
            self.package_management_type = package_management_type
        if power_on_delay_override is not None:
            self.power_on_delay_override = power_on_delay_override
        if power_shell_version is not None:
            self.power_shell_version = power_shell_version
        if template_registration is not None:
            self.template_registration = template_registration
        if remote_access_templates is not None:
            self.remote_access_templates = remote_access_templates
        if service_management_type is not None:
            self.service_management_type = service_management_type
        if user_count is not None:
            self.user_count = user_count
        if virt_realm_id is not None:
            self.virt_realm_id = virt_realm_id

    @property
    def display_name(self):
        """Gets the display_name of this Cons3rtTemplateData.  # noqa: E501


        :return: The display_name of this Cons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Cons3rtTemplateData.


        :param display_name: The display_name of this Cons3rtTemplateData.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def operating_system(self):
        """Gets the operating_system of this Cons3rtTemplateData.  # noqa: E501


        :return: The operating_system of this Cons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this Cons3rtTemplateData.


        :param operating_system: The operating_system of this Cons3rtTemplateData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and operating_system is None:  # noqa: E501
            raise ValueError("Invalid value for `operating_system`, must not be `None`")  # noqa: E501
        allowed_values = ["AMAZON_LINUX_2_LATEST_X64", "AMAZON_LINUX_LATEST_X64", "CENTOS_6_X64", "CENTOS_6_X86", "CENTOS_7_X64", "CENTOS_8_X64", "CORE_OS_1221_X64", "F5_BIGIP_X64", "FEDORA_23_X64", "FORTISIEM", "GENERIC_LINUX_X64", "GENERIC_WINDOWS_X64", "KALI_ROLLING_X64", "ORACLE_LINUX_6_X64", "ORACLE_LINUX_7_X64", "ORACLE_LINUX_8_X64", "OS_X_10", "OS_X_11", "PALO_ALTO_NETWORKS_PAN_OS_X64", "RASPBIAN", "RHEL_5_X64", "RHEL_5_X86", "RHEL_6_X64", "RHEL_6_X86", "RHEL_7_ATOMIC_HOST", "RHEL_7_PPCLE", "RHEL_7_X64", "RHEL_8_X64", "SOLARIS_11_X64", "UBUNTU_12_X64", "UBUNTU_14_X64", "UBUNTU_16_X64", "UBUNTU_18_X64", "UBUNTU_20_X64", "UBUNTU_CORE", "VYOS_1_1_X64", "VYOS_1_2_X64", "VYOS_1_3_X64", "WINDOWS_10_X64", "WINDOWS_7_X64", "WINDOWS_7_X86", "WINDOWS_8_X64", "WINDOWS_SERVER_2008_R2_X64", "WINDOWS_SERVER_2008_X64", "WINDOWS_SERVER_2012_R2_X64", "WINDOWS_SERVER_2012_X64", "WINDOWS_SERVER_2016_X64", "WINDOWS_SERVER_2019_X64", "WINDOWS_XP_X86"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operating_system not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `operating_system` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system, allowed_values)
            )

        self._operating_system = operating_system

    @property
    def virt_realm_template_name(self):
        """Gets the virt_realm_template_name of this Cons3rtTemplateData.  # noqa: E501


        :return: The virt_realm_template_name of this Cons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._virt_realm_template_name

    @virt_realm_template_name.setter
    def virt_realm_template_name(self, virt_realm_template_name):
        """Sets the virt_realm_template_name of this Cons3rtTemplateData.


        :param virt_realm_template_name: The virt_realm_template_name of this Cons3rtTemplateData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and virt_realm_template_name is None:  # noqa: E501
            raise ValueError("Invalid value for `virt_realm_template_name`, must not be `None`")  # noqa: E501

        self._virt_realm_template_name = virt_realm_template_name

    @property
    def cons3rt_agent_installed(self):
        """Gets the cons3rt_agent_installed of this Cons3rtTemplateData.  # noqa: E501


        :return: The cons3rt_agent_installed of this Cons3rtTemplateData.  # noqa: E501
        :rtype: bool
        """
        return self._cons3rt_agent_installed

    @cons3rt_agent_installed.setter
    def cons3rt_agent_installed(self, cons3rt_agent_installed):
        """Sets the cons3rt_agent_installed of this Cons3rtTemplateData.


        :param cons3rt_agent_installed: The cons3rt_agent_installed of this Cons3rtTemplateData.  # noqa: E501
        :type: bool
        """

        self._cons3rt_agent_installed = cons3rt_agent_installed

    @property
    def container_capable(self):
        """Gets the container_capable of this Cons3rtTemplateData.  # noqa: E501


        :return: The container_capable of this Cons3rtTemplateData.  # noqa: E501
        :rtype: bool
        """
        return self._container_capable

    @container_capable.setter
    def container_capable(self, container_capable):
        """Sets the container_capable of this Cons3rtTemplateData.


        :param container_capable: The container_capable of this Cons3rtTemplateData.  # noqa: E501
        :type: bool
        """

        self._container_capable = container_capable

    @property
    def disks(self):
        """Gets the disks of this Cons3rtTemplateData.  # noqa: E501


        :return: The disks of this Cons3rtTemplateData.  # noqa: E501
        :rtype: list[Disk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this Cons3rtTemplateData.


        :param disks: The disks of this Cons3rtTemplateData.  # noqa: E501
        :type: list[Disk]
        """

        self._disks = disks

    @property
    def fail_count(self):
        """Gets the fail_count of this Cons3rtTemplateData.  # noqa: E501


        :return: The fail_count of this Cons3rtTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._fail_count

    @fail_count.setter
    def fail_count(self, fail_count):
        """Sets the fail_count of this Cons3rtTemplateData.


        :param fail_count: The fail_count of this Cons3rtTemplateData.  # noqa: E501
        :type: int
        """

        self._fail_count = fail_count

    @property
    def has_gpu(self):
        """Gets the has_gpu of this Cons3rtTemplateData.  # noqa: E501


        :return: The has_gpu of this Cons3rtTemplateData.  # noqa: E501
        :rtype: bool
        """
        return self._has_gpu

    @has_gpu.setter
    def has_gpu(self, has_gpu):
        """Sets the has_gpu of this Cons3rtTemplateData.


        :param has_gpu: The has_gpu of this Cons3rtTemplateData.  # noqa: E501
        :type: bool
        """

        self._has_gpu = has_gpu

    @property
    def id(self):
        """Gets the id of this Cons3rtTemplateData.  # noqa: E501


        :return: The id of this Cons3rtTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Cons3rtTemplateData.


        :param id: The id of this Cons3rtTemplateData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def license(self):
        """Gets the license of this Cons3rtTemplateData.  # noqa: E501


        :return: The license of this Cons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Cons3rtTemplateData.


        :param license: The license of this Cons3rtTemplateData.  # noqa: E501
        :type: str
        """

        self._license = license

    @property
    def max_num_cpus(self):
        """Gets the max_num_cpus of this Cons3rtTemplateData.  # noqa: E501


        :return: The max_num_cpus of this Cons3rtTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._max_num_cpus

    @max_num_cpus.setter
    def max_num_cpus(self, max_num_cpus):
        """Sets the max_num_cpus of this Cons3rtTemplateData.


        :param max_num_cpus: The max_num_cpus of this Cons3rtTemplateData.  # noqa: E501
        :type: int
        """

        self._max_num_cpus = max_num_cpus

    @property
    def max_ram_in_megabytes(self):
        """Gets the max_ram_in_megabytes of this Cons3rtTemplateData.  # noqa: E501


        :return: The max_ram_in_megabytes of this Cons3rtTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._max_ram_in_megabytes

    @max_ram_in_megabytes.setter
    def max_ram_in_megabytes(self, max_ram_in_megabytes):
        """Sets the max_ram_in_megabytes of this Cons3rtTemplateData.


        :param max_ram_in_megabytes: The max_ram_in_megabytes of this Cons3rtTemplateData.  # noqa: E501
        :type: int
        """

        self._max_ram_in_megabytes = max_ram_in_megabytes

    @property
    def note(self):
        """Gets the note of this Cons3rtTemplateData.  # noqa: E501


        :return: The note of this Cons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Cons3rtTemplateData.


        :param note: The note of this Cons3rtTemplateData.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def package_management_type(self):
        """Gets the package_management_type of this Cons3rtTemplateData.  # noqa: E501


        :return: The package_management_type of this Cons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._package_management_type

    @package_management_type.setter
    def package_management_type(self, package_management_type):
        """Sets the package_management_type of this Cons3rtTemplateData.


        :param package_management_type: The package_management_type of this Cons3rtTemplateData.  # noqa: E501
        :type: str
        """
        allowed_values = ["APP_STORE", "APT_GET", "DNF", "DOCKER", "NONE", "PKGADD", "SNAP", "YUM"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and package_management_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `package_management_type` ({0}), must be one of {1}"  # noqa: E501
                .format(package_management_type, allowed_values)
            )

        self._package_management_type = package_management_type

    @property
    def power_on_delay_override(self):
        """Gets the power_on_delay_override of this Cons3rtTemplateData.  # noqa: E501


        :return: The power_on_delay_override of this Cons3rtTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._power_on_delay_override

    @power_on_delay_override.setter
    def power_on_delay_override(self, power_on_delay_override):
        """Sets the power_on_delay_override of this Cons3rtTemplateData.


        :param power_on_delay_override: The power_on_delay_override of this Cons3rtTemplateData.  # noqa: E501
        :type: int
        """

        self._power_on_delay_override = power_on_delay_override

    @property
    def power_shell_version(self):
        """Gets the power_shell_version of this Cons3rtTemplateData.  # noqa: E501


        :return: The power_shell_version of this Cons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._power_shell_version

    @power_shell_version.setter
    def power_shell_version(self, power_shell_version):
        """Sets the power_shell_version of this Cons3rtTemplateData.


        :param power_shell_version: The power_shell_version of this Cons3rtTemplateData.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "POWERSHELL_1_0", "POWERSHELL_2_0", "POWERSHELL_3_0", "POWERSHELL_4_0", "POWERSHELL_5_0", "POWERSHELL_6_0"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and power_shell_version not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `power_shell_version` ({0}), must be one of {1}"  # noqa: E501
                .format(power_shell_version, allowed_values)
            )

        self._power_shell_version = power_shell_version

    @property
    def template_registration(self):
        """Gets the template_registration of this Cons3rtTemplateData.  # noqa: E501


        :return: The template_registration of this Cons3rtTemplateData.  # noqa: E501
        :rtype: TemplateRegistration
        """
        return self._template_registration

    @template_registration.setter
    def template_registration(self, template_registration):
        """Sets the template_registration of this Cons3rtTemplateData.


        :param template_registration: The template_registration of this Cons3rtTemplateData.  # noqa: E501
        :type: TemplateRegistration
        """

        self._template_registration = template_registration

    @property
    def remote_access_templates(self):
        """Gets the remote_access_templates of this Cons3rtTemplateData.  # noqa: E501


        :return: The remote_access_templates of this Cons3rtTemplateData.  # noqa: E501
        :rtype: list[RemoteAccessTemplate]
        """
        return self._remote_access_templates

    @remote_access_templates.setter
    def remote_access_templates(self, remote_access_templates):
        """Sets the remote_access_templates of this Cons3rtTemplateData.


        :param remote_access_templates: The remote_access_templates of this Cons3rtTemplateData.  # noqa: E501
        :type: list[RemoteAccessTemplate]
        """

        self._remote_access_templates = remote_access_templates

    @property
    def service_management_type(self):
        """Gets the service_management_type of this Cons3rtTemplateData.  # noqa: E501


        :return: The service_management_type of this Cons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._service_management_type

    @service_management_type.setter
    def service_management_type(self, service_management_type):
        """Sets the service_management_type of this Cons3rtTemplateData.


        :param service_management_type: The service_management_type of this Cons3rtTemplateData.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYSTEMD", "INITD", "LAUNCHD", "UNKNOWN", "UPDATE_RC", "UPSTART", "WINDOWS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and service_management_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `service_management_type` ({0}), must be one of {1}"  # noqa: E501
                .format(service_management_type, allowed_values)
            )

        self._service_management_type = service_management_type

    @property
    def user_count(self):
        """Gets the user_count of this Cons3rtTemplateData.  # noqa: E501


        :return: The user_count of this Cons3rtTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this Cons3rtTemplateData.


        :param user_count: The user_count of this Cons3rtTemplateData.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def virt_realm_id(self):
        """Gets the virt_realm_id of this Cons3rtTemplateData.  # noqa: E501


        :return: The virt_realm_id of this Cons3rtTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._virt_realm_id

    @virt_realm_id.setter
    def virt_realm_id(self, virt_realm_id):
        """Sets the virt_realm_id of this Cons3rtTemplateData.


        :param virt_realm_id: The virt_realm_id of this Cons3rtTemplateData.  # noqa: E501
        :type: int
        """

        self._virt_realm_id = virt_realm_id

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
        if not isinstance(other, Cons3rtTemplateData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cons3rtTemplateData):
            return True

        return self.to_dict() != other.to_dict()
