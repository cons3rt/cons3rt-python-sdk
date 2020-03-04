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


class FullSoftwareAsset(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'offline': 'bool',
        'state': 'str',
        'visibility': 'str',
        'creator': 'MinimalUser',
        'owning_project': 'MinimalProject',
        'trusted_projects': 'list[MinimalProject]',
        'dependent_asset_count': 'int',
        'metadata': 'FullMetadata',
        'impact_level': 'str',
        'categories': 'list[MinimalCategory]',
        'subtype': 'str',
        'architecture': 'str',
        'bits': 'str',
        'dependencies': 'str',
        'os_family': 'str',
        'product_family': 'str',
        'required_cpu': 'int',
        'required_cpu_speed': 'int',
        'application_type': 'str',
        'vendor_message': 'str',
        'build_engine': 'str',
        'build_script': 'str',
        'build_script_name': 'str',
        'checkout_script': 'str',
        'checkout_script_name': 'str',
        'deploy_script': 'str',
        'deploy_script_name': 'str',
        'install_script': 'str',
        'install_script_name': 'str',
        'required_disk': 'int',
        'required_ram': 'int',
        'software_type': 'str',
        'version': 'str',
        'source_code_type': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'offline': 'offline',
        'state': 'state',
        'visibility': 'visibility',
        'creator': 'creator',
        'owning_project': 'owningProject',
        'trusted_projects': 'trustedProjects',
        'dependent_asset_count': 'dependentAssetCount',
        'metadata': 'metadata',
        'impact_level': 'impactLevel',
        'categories': 'categories',
        'subtype': 'subtype',
        'architecture': 'architecture',
        'bits': 'bits',
        'dependencies': 'dependencies',
        'os_family': 'osFamily',
        'product_family': 'productFamily',
        'required_cpu': 'requiredCpu',
        'required_cpu_speed': 'requiredCpuSpeed',
        'application_type': 'applicationType',
        'vendor_message': 'vendorMessage',
        'build_engine': 'buildEngine',
        'build_script': 'buildScript',
        'build_script_name': 'buildScriptName',
        'checkout_script': 'checkoutScript',
        'checkout_script_name': 'checkoutScriptName',
        'deploy_script': 'deployScript',
        'deploy_script_name': 'deployScriptName',
        'install_script': 'installScript',
        'install_script_name': 'installScriptName',
        'required_disk': 'requiredDisk',
        'required_ram': 'requiredRam',
        'software_type': 'softwareType',
        'version': 'version',
        'source_code_type': 'sourceCodeType',
        'vendor': 'vendor'
    }

    def __init__(self, id=None, name=None, description=None, offline=None, state=None, visibility=None, creator=None, owning_project=None, trusted_projects=None, dependent_asset_count=None, metadata=None, impact_level=None, categories=None, subtype=None, architecture=None, bits=None, dependencies=None, os_family=None, product_family=None, required_cpu=None, required_cpu_speed=None, application_type=None, vendor_message=None, build_engine=None, build_script=None, build_script_name=None, checkout_script=None, checkout_script_name=None, deploy_script=None, deploy_script_name=None, install_script=None, install_script_name=None, required_disk=None, required_ram=None, software_type=None, version=None, source_code_type=None, vendor=None, local_vars_configuration=None):  # noqa: E501
        """FullSoftwareAsset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._offline = None
        self._state = None
        self._visibility = None
        self._creator = None
        self._owning_project = None
        self._trusted_projects = None
        self._dependent_asset_count = None
        self._metadata = None
        self._impact_level = None
        self._categories = None
        self._subtype = None
        self._architecture = None
        self._bits = None
        self._dependencies = None
        self._os_family = None
        self._product_family = None
        self._required_cpu = None
        self._required_cpu_speed = None
        self._application_type = None
        self._vendor_message = None
        self._build_engine = None
        self._build_script = None
        self._build_script_name = None
        self._checkout_script = None
        self._checkout_script_name = None
        self._deploy_script = None
        self._deploy_script_name = None
        self._install_script = None
        self._install_script_name = None
        self._required_disk = None
        self._required_ram = None
        self._software_type = None
        self._version = None
        self._source_code_type = None
        self._vendor = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if offline is not None:
            self.offline = offline
        if state is not None:
            self.state = state
        if visibility is not None:
            self.visibility = visibility
        if creator is not None:
            self.creator = creator
        if owning_project is not None:
            self.owning_project = owning_project
        if trusted_projects is not None:
            self.trusted_projects = trusted_projects
        if dependent_asset_count is not None:
            self.dependent_asset_count = dependent_asset_count
        if metadata is not None:
            self.metadata = metadata
        if impact_level is not None:
            self.impact_level = impact_level
        if categories is not None:
            self.categories = categories
        self.subtype = subtype
        if architecture is not None:
            self.architecture = architecture
        if bits is not None:
            self.bits = bits
        if dependencies is not None:
            self.dependencies = dependencies
        if os_family is not None:
            self.os_family = os_family
        if product_family is not None:
            self.product_family = product_family
        if required_cpu is not None:
            self.required_cpu = required_cpu
        if required_cpu_speed is not None:
            self.required_cpu_speed = required_cpu_speed
        if application_type is not None:
            self.application_type = application_type
        if vendor_message is not None:
            self.vendor_message = vendor_message
        if build_engine is not None:
            self.build_engine = build_engine
        if build_script is not None:
            self.build_script = build_script
        if build_script_name is not None:
            self.build_script_name = build_script_name
        if checkout_script is not None:
            self.checkout_script = checkout_script
        if checkout_script_name is not None:
            self.checkout_script_name = checkout_script_name
        if deploy_script is not None:
            self.deploy_script = deploy_script
        if deploy_script_name is not None:
            self.deploy_script_name = deploy_script_name
        if install_script is not None:
            self.install_script = install_script
        if install_script_name is not None:
            self.install_script_name = install_script_name
        if required_disk is not None:
            self.required_disk = required_disk
        if required_ram is not None:
            self.required_ram = required_ram
        if software_type is not None:
            self.software_type = software_type
        if version is not None:
            self.version = version
        if source_code_type is not None:
            self.source_code_type = source_code_type
        if vendor is not None:
            self.vendor = vendor

    @property
    def id(self):
        """Gets the id of this FullSoftwareAsset.  # noqa: E501


        :return: The id of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FullSoftwareAsset.


        :param id: The id of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FullSoftwareAsset.  # noqa: E501


        :return: The name of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FullSoftwareAsset.


        :param name: The name of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this FullSoftwareAsset.  # noqa: E501


        :return: The description of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FullSoftwareAsset.


        :param description: The description of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def offline(self):
        """Gets the offline of this FullSoftwareAsset.  # noqa: E501


        :return: The offline of this FullSoftwareAsset.  # noqa: E501
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this FullSoftwareAsset.


        :param offline: The offline of this FullSoftwareAsset.  # noqa: E501
        :type: bool
        """

        self._offline = offline

    @property
    def state(self):
        """Gets the state of this FullSoftwareAsset.  # noqa: E501


        :return: The state of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FullSoftwareAsset.


        :param state: The state of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_DEVELOPMENT", "CERTIFIED", "DEPRECATED", "RETIRED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def visibility(self):
        """Gets the visibility of this FullSoftwareAsset.  # noqa: E501


        :return: The visibility of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this FullSoftwareAsset.


        :param visibility: The visibility of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["OWNER", "OWNING_PROJECT", "TRUSTED_PROJECTS", "COMMUNITY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and visibility not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def creator(self):
        """Gets the creator of this FullSoftwareAsset.  # noqa: E501


        :return: The creator of this FullSoftwareAsset.  # noqa: E501
        :rtype: MinimalUser
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this FullSoftwareAsset.


        :param creator: The creator of this FullSoftwareAsset.  # noqa: E501
        :type: MinimalUser
        """

        self._creator = creator

    @property
    def owning_project(self):
        """Gets the owning_project of this FullSoftwareAsset.  # noqa: E501


        :return: The owning_project of this FullSoftwareAsset.  # noqa: E501
        :rtype: MinimalProject
        """
        return self._owning_project

    @owning_project.setter
    def owning_project(self, owning_project):
        """Sets the owning_project of this FullSoftwareAsset.


        :param owning_project: The owning_project of this FullSoftwareAsset.  # noqa: E501
        :type: MinimalProject
        """

        self._owning_project = owning_project

    @property
    def trusted_projects(self):
        """Gets the trusted_projects of this FullSoftwareAsset.  # noqa: E501


        :return: The trusted_projects of this FullSoftwareAsset.  # noqa: E501
        :rtype: list[MinimalProject]
        """
        return self._trusted_projects

    @trusted_projects.setter
    def trusted_projects(self, trusted_projects):
        """Sets the trusted_projects of this FullSoftwareAsset.


        :param trusted_projects: The trusted_projects of this FullSoftwareAsset.  # noqa: E501
        :type: list[MinimalProject]
        """

        self._trusted_projects = trusted_projects

    @property
    def dependent_asset_count(self):
        """Gets the dependent_asset_count of this FullSoftwareAsset.  # noqa: E501


        :return: The dependent_asset_count of this FullSoftwareAsset.  # noqa: E501
        :rtype: int
        """
        return self._dependent_asset_count

    @dependent_asset_count.setter
    def dependent_asset_count(self, dependent_asset_count):
        """Sets the dependent_asset_count of this FullSoftwareAsset.


        :param dependent_asset_count: The dependent_asset_count of this FullSoftwareAsset.  # noqa: E501
        :type: int
        """

        self._dependent_asset_count = dependent_asset_count

    @property
    def metadata(self):
        """Gets the metadata of this FullSoftwareAsset.  # noqa: E501


        :return: The metadata of this FullSoftwareAsset.  # noqa: E501
        :rtype: FullMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FullSoftwareAsset.


        :param metadata: The metadata of this FullSoftwareAsset.  # noqa: E501
        :type: FullMetadata
        """

        self._metadata = metadata

    @property
    def impact_level(self):
        """Gets the impact_level of this FullSoftwareAsset.  # noqa: E501


        :return: The impact_level of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._impact_level

    @impact_level.setter
    def impact_level(self, impact_level):
        """Sets the impact_level of this FullSoftwareAsset.


        :param impact_level: The impact_level of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "FEDRAMP_LOW", "FEDRAMP_MODERATE_DOD_LEVEL_2", "FEDRAMP_HIGH_DOD_LEVEL_4", "DOD_LEVEL_5", "DOD_LEVEL_6"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and impact_level not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `impact_level` ({0}), must be one of {1}"  # noqa: E501
                .format(impact_level, allowed_values)
            )

        self._impact_level = impact_level

    @property
    def categories(self):
        """Gets the categories of this FullSoftwareAsset.  # noqa: E501


        :return: The categories of this FullSoftwareAsset.  # noqa: E501
        :rtype: list[MinimalCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this FullSoftwareAsset.


        :param categories: The categories of this FullSoftwareAsset.  # noqa: E501
        :type: list[MinimalCategory]
        """

        self._categories = categories

    @property
    def subtype(self):
        """Gets the subtype of this FullSoftwareAsset.  # noqa: E501


        :return: The subtype of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this FullSoftwareAsset.


        :param subtype: The subtype of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    @property
    def architecture(self):
        """Gets the architecture of this FullSoftwareAsset.  # noqa: E501


        :return: The architecture of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this FullSoftwareAsset.


        :param architecture: The architecture of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["X86", "X64", "ARM", "SPARC", "PPCLE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and architecture not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `architecture` ({0}), must be one of {1}"  # noqa: E501
                .format(architecture, allowed_values)
            )

        self._architecture = architecture

    @property
    def bits(self):
        """Gets the bits of this FullSoftwareAsset.  # noqa: E501


        :return: The bits of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._bits

    @bits.setter
    def bits(self, bits):
        """Sets the bits of this FullSoftwareAsset.


        :param bits: The bits of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["BITS32", "BITS64"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and bits not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `bits` ({0}), must be one of {1}"  # noqa: E501
                .format(bits, allowed_values)
            )

        self._bits = bits

    @property
    def dependencies(self):
        """Gets the dependencies of this FullSoftwareAsset.  # noqa: E501


        :return: The dependencies of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this FullSoftwareAsset.


        :param dependencies: The dependencies of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._dependencies = dependencies

    @property
    def os_family(self):
        """Gets the os_family of this FullSoftwareAsset.  # noqa: E501


        :return: The os_family of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """Sets the os_family of this FullSoftwareAsset.


        :param os_family: The os_family of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["LINUX", "OS_X", "SOLARIS", "WINDOWS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and os_family not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `os_family` ({0}), must be one of {1}"  # noqa: E501
                .format(os_family, allowed_values)
            )

        self._os_family = os_family

    @property
    def product_family(self):
        """Gets the product_family of this FullSoftwareAsset.  # noqa: E501


        :return: The product_family of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._product_family

    @product_family.setter
    def product_family(self, product_family):
        """Sets the product_family of this FullSoftwareAsset.


        :param product_family: The product_family of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._product_family = product_family

    @property
    def required_cpu(self):
        """Gets the required_cpu of this FullSoftwareAsset.  # noqa: E501


        :return: The required_cpu of this FullSoftwareAsset.  # noqa: E501
        :rtype: int
        """
        return self._required_cpu

    @required_cpu.setter
    def required_cpu(self, required_cpu):
        """Sets the required_cpu of this FullSoftwareAsset.


        :param required_cpu: The required_cpu of this FullSoftwareAsset.  # noqa: E501
        :type: int
        """

        self._required_cpu = required_cpu

    @property
    def required_cpu_speed(self):
        """Gets the required_cpu_speed of this FullSoftwareAsset.  # noqa: E501


        :return: The required_cpu_speed of this FullSoftwareAsset.  # noqa: E501
        :rtype: int
        """
        return self._required_cpu_speed

    @required_cpu_speed.setter
    def required_cpu_speed(self, required_cpu_speed):
        """Sets the required_cpu_speed of this FullSoftwareAsset.


        :param required_cpu_speed: The required_cpu_speed of this FullSoftwareAsset.  # noqa: E501
        :type: int
        """

        self._required_cpu_speed = required_cpu_speed

    @property
    def application_type(self):
        """Gets the application_type of this FullSoftwareAsset.  # noqa: E501


        :return: The application_type of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """Sets the application_type of this FullSoftwareAsset.


        :param application_type: The application_type of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._application_type = application_type

    @property
    def vendor_message(self):
        """Gets the vendor_message of this FullSoftwareAsset.  # noqa: E501


        :return: The vendor_message of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._vendor_message

    @vendor_message.setter
    def vendor_message(self, vendor_message):
        """Sets the vendor_message of this FullSoftwareAsset.


        :param vendor_message: The vendor_message of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._vendor_message = vendor_message

    @property
    def build_engine(self):
        """Gets the build_engine of this FullSoftwareAsset.  # noqa: E501


        :return: The build_engine of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._build_engine

    @build_engine.setter
    def build_engine(self, build_engine):
        """Sets the build_engine of this FullSoftwareAsset.


        :param build_engine: The build_engine of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._build_engine = build_engine

    @property
    def build_script(self):
        """Gets the build_script of this FullSoftwareAsset.  # noqa: E501


        :return: The build_script of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._build_script

    @build_script.setter
    def build_script(self, build_script):
        """Sets the build_script of this FullSoftwareAsset.


        :param build_script: The build_script of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._build_script = build_script

    @property
    def build_script_name(self):
        """Gets the build_script_name of this FullSoftwareAsset.  # noqa: E501


        :return: The build_script_name of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._build_script_name

    @build_script_name.setter
    def build_script_name(self, build_script_name):
        """Sets the build_script_name of this FullSoftwareAsset.


        :param build_script_name: The build_script_name of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._build_script_name = build_script_name

    @property
    def checkout_script(self):
        """Gets the checkout_script of this FullSoftwareAsset.  # noqa: E501


        :return: The checkout_script of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._checkout_script

    @checkout_script.setter
    def checkout_script(self, checkout_script):
        """Sets the checkout_script of this FullSoftwareAsset.


        :param checkout_script: The checkout_script of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._checkout_script = checkout_script

    @property
    def checkout_script_name(self):
        """Gets the checkout_script_name of this FullSoftwareAsset.  # noqa: E501


        :return: The checkout_script_name of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._checkout_script_name

    @checkout_script_name.setter
    def checkout_script_name(self, checkout_script_name):
        """Sets the checkout_script_name of this FullSoftwareAsset.


        :param checkout_script_name: The checkout_script_name of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._checkout_script_name = checkout_script_name

    @property
    def deploy_script(self):
        """Gets the deploy_script of this FullSoftwareAsset.  # noqa: E501


        :return: The deploy_script of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._deploy_script

    @deploy_script.setter
    def deploy_script(self, deploy_script):
        """Sets the deploy_script of this FullSoftwareAsset.


        :param deploy_script: The deploy_script of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._deploy_script = deploy_script

    @property
    def deploy_script_name(self):
        """Gets the deploy_script_name of this FullSoftwareAsset.  # noqa: E501


        :return: The deploy_script_name of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._deploy_script_name

    @deploy_script_name.setter
    def deploy_script_name(self, deploy_script_name):
        """Sets the deploy_script_name of this FullSoftwareAsset.


        :param deploy_script_name: The deploy_script_name of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._deploy_script_name = deploy_script_name

    @property
    def install_script(self):
        """Gets the install_script of this FullSoftwareAsset.  # noqa: E501


        :return: The install_script of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._install_script

    @install_script.setter
    def install_script(self, install_script):
        """Sets the install_script of this FullSoftwareAsset.


        :param install_script: The install_script of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._install_script = install_script

    @property
    def install_script_name(self):
        """Gets the install_script_name of this FullSoftwareAsset.  # noqa: E501


        :return: The install_script_name of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._install_script_name

    @install_script_name.setter
    def install_script_name(self, install_script_name):
        """Sets the install_script_name of this FullSoftwareAsset.


        :param install_script_name: The install_script_name of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._install_script_name = install_script_name

    @property
    def required_disk(self):
        """Gets the required_disk of this FullSoftwareAsset.  # noqa: E501


        :return: The required_disk of this FullSoftwareAsset.  # noqa: E501
        :rtype: int
        """
        return self._required_disk

    @required_disk.setter
    def required_disk(self, required_disk):
        """Sets the required_disk of this FullSoftwareAsset.


        :param required_disk: The required_disk of this FullSoftwareAsset.  # noqa: E501
        :type: int
        """

        self._required_disk = required_disk

    @property
    def required_ram(self):
        """Gets the required_ram of this FullSoftwareAsset.  # noqa: E501


        :return: The required_ram of this FullSoftwareAsset.  # noqa: E501
        :rtype: int
        """
        return self._required_ram

    @required_ram.setter
    def required_ram(self, required_ram):
        """Sets the required_ram of this FullSoftwareAsset.


        :param required_ram: The required_ram of this FullSoftwareAsset.  # noqa: E501
        :type: int
        """

        self._required_ram = required_ram

    @property
    def software_type(self):
        """Gets the software_type of this FullSoftwareAsset.  # noqa: E501


        :return: The software_type of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._software_type

    @software_type.setter
    def software_type(self, software_type):
        """Sets the software_type of this FullSoftwareAsset.


        :param software_type: The software_type of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["APPLICATION", "SOURCE_CODE", "TEST_TOOL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and software_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `software_type` ({0}), must be one of {1}"  # noqa: E501
                .format(software_type, allowed_values)
            )

        self._software_type = software_type

    @property
    def version(self):
        """Gets the version of this FullSoftwareAsset.  # noqa: E501


        :return: The version of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FullSoftwareAsset.


        :param version: The version of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def source_code_type(self):
        """Gets the source_code_type of this FullSoftwareAsset.  # noqa: E501


        :return: The source_code_type of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._source_code_type

    @source_code_type.setter
    def source_code_type(self, source_code_type):
        """Sets the source_code_type of this FullSoftwareAsset.


        :param source_code_type: The source_code_type of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._source_code_type = source_code_type

    @property
    def vendor(self):
        """Gets the vendor of this FullSoftwareAsset.  # noqa: E501


        :return: The vendor of this FullSoftwareAsset.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this FullSoftwareAsset.


        :param vendor: The vendor of this FullSoftwareAsset.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

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
        if not isinstance(other, FullSoftwareAsset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullSoftwareAsset):
            return True

        return self.to_dict() != other.to_dict()
