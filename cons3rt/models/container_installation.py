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


class ContainerInstallation(object):
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
        'asset_id': 'int',
        'asset_name': 'str',
        'average_installation_time': 'int',
        'end_date': 'datetime',
        'error': 'str',
        'id': 'int',
        'load_order': 'int',
        'start_date': 'datetime',
        'status': 'str',
        'subtype': 'str',
        'asset_type': 'str',
        'run_arguments': 'str'
    }

    attribute_map = {
        'asset_id': 'assetId',
        'asset_name': 'assetName',
        'average_installation_time': 'averageInstallationTime',
        'end_date': 'endDate',
        'error': 'error',
        'id': 'id',
        'load_order': 'loadOrder',
        'start_date': 'startDate',
        'status': 'status',
        'subtype': 'subtype',
        'asset_type': 'assetType',
        'run_arguments': 'runArguments'
    }

    def __init__(self, asset_id=None, asset_name=None, average_installation_time=None, end_date=None, error=None, id=None, load_order=None, start_date=None, status=None, subtype=None, asset_type=None, run_arguments=None, local_vars_configuration=None):  # noqa: E501
        """ContainerInstallation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_id = None
        self._asset_name = None
        self._average_installation_time = None
        self._end_date = None
        self._error = None
        self._id = None
        self._load_order = None
        self._start_date = None
        self._status = None
        self._subtype = None
        self._asset_type = None
        self._run_arguments = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if asset_name is not None:
            self.asset_name = asset_name
        if average_installation_time is not None:
            self.average_installation_time = average_installation_time
        if end_date is not None:
            self.end_date = end_date
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if load_order is not None:
            self.load_order = load_order
        if start_date is not None:
            self.start_date = start_date
        if status is not None:
            self.status = status
        self.subtype = subtype
        if asset_type is not None:
            self.asset_type = asset_type
        if run_arguments is not None:
            self.run_arguments = run_arguments

    @property
    def asset_id(self):
        """Gets the asset_id of this ContainerInstallation.  # noqa: E501


        :return: The asset_id of this ContainerInstallation.  # noqa: E501
        :rtype: int
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ContainerInstallation.


        :param asset_id: The asset_id of this ContainerInstallation.  # noqa: E501
        :type: int
        """

        self._asset_id = asset_id

    @property
    def asset_name(self):
        """Gets the asset_name of this ContainerInstallation.  # noqa: E501


        :return: The asset_name of this ContainerInstallation.  # noqa: E501
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this ContainerInstallation.


        :param asset_name: The asset_name of this ContainerInstallation.  # noqa: E501
        :type: str
        """

        self._asset_name = asset_name

    @property
    def average_installation_time(self):
        """Gets the average_installation_time of this ContainerInstallation.  # noqa: E501


        :return: The average_installation_time of this ContainerInstallation.  # noqa: E501
        :rtype: int
        """
        return self._average_installation_time

    @average_installation_time.setter
    def average_installation_time(self, average_installation_time):
        """Sets the average_installation_time of this ContainerInstallation.


        :param average_installation_time: The average_installation_time of this ContainerInstallation.  # noqa: E501
        :type: int
        """

        self._average_installation_time = average_installation_time

    @property
    def end_date(self):
        """Gets the end_date of this ContainerInstallation.  # noqa: E501


        :return: The end_date of this ContainerInstallation.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ContainerInstallation.


        :param end_date: The end_date of this ContainerInstallation.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def error(self):
        """Gets the error of this ContainerInstallation.  # noqa: E501


        :return: The error of this ContainerInstallation.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ContainerInstallation.


        :param error: The error of this ContainerInstallation.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def id(self):
        """Gets the id of this ContainerInstallation.  # noqa: E501


        :return: The id of this ContainerInstallation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContainerInstallation.


        :param id: The id of this ContainerInstallation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def load_order(self):
        """Gets the load_order of this ContainerInstallation.  # noqa: E501


        :return: The load_order of this ContainerInstallation.  # noqa: E501
        :rtype: int
        """
        return self._load_order

    @load_order.setter
    def load_order(self, load_order):
        """Sets the load_order of this ContainerInstallation.


        :param load_order: The load_order of this ContainerInstallation.  # noqa: E501
        :type: int
        """

        self._load_order = load_order

    @property
    def start_date(self):
        """Gets the start_date of this ContainerInstallation.  # noqa: E501


        :return: The start_date of this ContainerInstallation.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ContainerInstallation.


        :param start_date: The start_date of this ContainerInstallation.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this ContainerInstallation.  # noqa: E501


        :return: The status of this ContainerInstallation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ContainerInstallation.


        :param status: The status of this ContainerInstallation.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "PENDING", "PREPARING", "DOWNLOADING", "EXPANDING", "INSTALLING", "INSTALLED", "REBOOTING", "ERROR", "COMPLETE", "STARTING", "STARTED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def subtype(self):
        """Gets the subtype of this ContainerInstallation.  # noqa: E501


        :return: The subtype of this ContainerInstallation.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this ContainerInstallation.


        :param subtype: The subtype of this ContainerInstallation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    @property
    def asset_type(self):
        """Gets the asset_type of this ContainerInstallation.  # noqa: E501


        :return: The asset_type of this ContainerInstallation.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this ContainerInstallation.


        :param asset_type: The asset_type of this ContainerInstallation.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOCKER", "OCI"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and asset_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `asset_type` ({0}), must be one of {1}"  # noqa: E501
                .format(asset_type, allowed_values)
            )

        self._asset_type = asset_type

    @property
    def run_arguments(self):
        """Gets the run_arguments of this ContainerInstallation.  # noqa: E501


        :return: The run_arguments of this ContainerInstallation.  # noqa: E501
        :rtype: str
        """
        return self._run_arguments

    @run_arguments.setter
    def run_arguments(self, run_arguments):
        """Sets the run_arguments of this ContainerInstallation.


        :param run_arguments: The run_arguments of this ContainerInstallation.  # noqa: E501
        :type: str
        """

        self._run_arguments = run_arguments

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
        if not isinstance(other, ContainerInstallation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerInstallation):
            return True

        return self.to_dict() != other.to_dict()
