# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class MinimalTemplateRegistration(object):
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
        'id': 'int',
        'template_uuid': 'str',
        'template_data': 'MinimalCons3rtTemplateData',
        'offline': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'template_uuid': 'templateUuid',
        'template_data': 'templateData',
        'offline': 'offline'
    }

    def __init__(self, id=None, template_uuid=None, template_data=None, offline=None, local_vars_configuration=None):  # noqa: E501
        """MinimalTemplateRegistration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._template_uuid = None
        self._template_data = None
        self._offline = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if template_uuid is not None:
            self.template_uuid = template_uuid
        if template_data is not None:
            self.template_data = template_data
        if offline is not None:
            self.offline = offline

    @property
    def id(self):
        """Gets the id of this MinimalTemplateRegistration.  # noqa: E501


        :return: The id of this MinimalTemplateRegistration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalTemplateRegistration.


        :param id: The id of this MinimalTemplateRegistration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def template_uuid(self):
        """Gets the template_uuid of this MinimalTemplateRegistration.  # noqa: E501


        :return: The template_uuid of this MinimalTemplateRegistration.  # noqa: E501
        :rtype: str
        """
        return self._template_uuid

    @template_uuid.setter
    def template_uuid(self, template_uuid):
        """Sets the template_uuid of this MinimalTemplateRegistration.


        :param template_uuid: The template_uuid of this MinimalTemplateRegistration.  # noqa: E501
        :type: str
        """

        self._template_uuid = template_uuid

    @property
    def template_data(self):
        """Gets the template_data of this MinimalTemplateRegistration.  # noqa: E501


        :return: The template_data of this MinimalTemplateRegistration.  # noqa: E501
        :rtype: MinimalCons3rtTemplateData
        """
        return self._template_data

    @template_data.setter
    def template_data(self, template_data):
        """Sets the template_data of this MinimalTemplateRegistration.


        :param template_data: The template_data of this MinimalTemplateRegistration.  # noqa: E501
        :type: MinimalCons3rtTemplateData
        """

        self._template_data = template_data

    @property
    def offline(self):
        """Gets the offline of this MinimalTemplateRegistration.  # noqa: E501


        :return: The offline of this MinimalTemplateRegistration.  # noqa: E501
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this MinimalTemplateRegistration.


        :param offline: The offline of this MinimalTemplateRegistration.  # noqa: E501
        :type: bool
        """

        self._offline = offline

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
        if not isinstance(other, MinimalTemplateRegistration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalTemplateRegistration):
            return True

        return self.to_dict() != other.to_dict()
