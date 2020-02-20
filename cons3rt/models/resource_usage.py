# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class ResourceUsage(object):
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
        'num_cpus': 'int',
        'num_gpus': 'int',
        'ram_in_megabytes': 'int',
        'storage_in_megabytes': 'int',
        'virtual_machines': 'int'
    }

    attribute_map = {
        'num_cpus': 'numCpus',
        'num_gpus': 'numGpus',
        'ram_in_megabytes': 'ramInMegabytes',
        'storage_in_megabytes': 'storageInMegabytes',
        'virtual_machines': 'virtualMachines'
    }

    def __init__(self, num_cpus=None, num_gpus=None, ram_in_megabytes=None, storage_in_megabytes=None, virtual_machines=None, local_vars_configuration=None):  # noqa: E501
        """ResourceUsage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._num_cpus = None
        self._num_gpus = None
        self._ram_in_megabytes = None
        self._storage_in_megabytes = None
        self._virtual_machines = None
        self.discriminator = None

        if num_cpus is not None:
            self.num_cpus = num_cpus
        if num_gpus is not None:
            self.num_gpus = num_gpus
        if ram_in_megabytes is not None:
            self.ram_in_megabytes = ram_in_megabytes
        if storage_in_megabytes is not None:
            self.storage_in_megabytes = storage_in_megabytes
        if virtual_machines is not None:
            self.virtual_machines = virtual_machines

    @property
    def num_cpus(self):
        """Gets the num_cpus of this ResourceUsage.  # noqa: E501


        :return: The num_cpus of this ResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._num_cpus

    @num_cpus.setter
    def num_cpus(self, num_cpus):
        """Sets the num_cpus of this ResourceUsage.


        :param num_cpus: The num_cpus of this ResourceUsage.  # noqa: E501
        :type: int
        """

        self._num_cpus = num_cpus

    @property
    def num_gpus(self):
        """Gets the num_gpus of this ResourceUsage.  # noqa: E501


        :return: The num_gpus of this ResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._num_gpus

    @num_gpus.setter
    def num_gpus(self, num_gpus):
        """Sets the num_gpus of this ResourceUsage.


        :param num_gpus: The num_gpus of this ResourceUsage.  # noqa: E501
        :type: int
        """

        self._num_gpus = num_gpus

    @property
    def ram_in_megabytes(self):
        """Gets the ram_in_megabytes of this ResourceUsage.  # noqa: E501


        :return: The ram_in_megabytes of this ResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._ram_in_megabytes

    @ram_in_megabytes.setter
    def ram_in_megabytes(self, ram_in_megabytes):
        """Sets the ram_in_megabytes of this ResourceUsage.


        :param ram_in_megabytes: The ram_in_megabytes of this ResourceUsage.  # noqa: E501
        :type: int
        """

        self._ram_in_megabytes = ram_in_megabytes

    @property
    def storage_in_megabytes(self):
        """Gets the storage_in_megabytes of this ResourceUsage.  # noqa: E501


        :return: The storage_in_megabytes of this ResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._storage_in_megabytes

    @storage_in_megabytes.setter
    def storage_in_megabytes(self, storage_in_megabytes):
        """Sets the storage_in_megabytes of this ResourceUsage.


        :param storage_in_megabytes: The storage_in_megabytes of this ResourceUsage.  # noqa: E501
        :type: int
        """

        self._storage_in_megabytes = storage_in_megabytes

    @property
    def virtual_machines(self):
        """Gets the virtual_machines of this ResourceUsage.  # noqa: E501


        :return: The virtual_machines of this ResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._virtual_machines

    @virtual_machines.setter
    def virtual_machines(self, virtual_machines):
        """Sets the virtual_machines of this ResourceUsage.


        :param virtual_machines: The virtual_machines of this ResourceUsage.  # noqa: E501
        :type: int
        """

        self._virtual_machines = virtual_machines

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
        if not isinstance(other, ResourceUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceUsage):
            return True

        return self.to_dict() != other.to_dict()
