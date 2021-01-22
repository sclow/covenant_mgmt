# coding: utf-8

"""
    Covenant API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ReferenceAssembly(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'location': 'str',
        'dot_net_version': 'DotNetVersion'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'location': 'location',
        'dot_net_version': 'dotNetVersion'
    }

    def __init__(self, id=None, name=None, location=None, dot_net_version=None):  # noqa: E501
        """ReferenceAssembly - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._location = None
        self._dot_net_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if location is not None:
            self.location = location
        if dot_net_version is not None:
            self.dot_net_version = dot_net_version

    @property
    def id(self):
        """Gets the id of this ReferenceAssembly.  # noqa: E501


        :return: The id of this ReferenceAssembly.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReferenceAssembly.


        :param id: The id of this ReferenceAssembly.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ReferenceAssembly.  # noqa: E501


        :return: The name of this ReferenceAssembly.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReferenceAssembly.


        :param name: The name of this ReferenceAssembly.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def location(self):
        """Gets the location of this ReferenceAssembly.  # noqa: E501


        :return: The location of this ReferenceAssembly.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ReferenceAssembly.


        :param location: The location of this ReferenceAssembly.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def dot_net_version(self):
        """Gets the dot_net_version of this ReferenceAssembly.  # noqa: E501


        :return: The dot_net_version of this ReferenceAssembly.  # noqa: E501
        :rtype: DotNetVersion
        """
        return self._dot_net_version

    @dot_net_version.setter
    def dot_net_version(self, dot_net_version):
        """Sets the dot_net_version of this ReferenceAssembly.


        :param dot_net_version: The dot_net_version of this ReferenceAssembly.  # noqa: E501
        :type: DotNetVersion
        """

        self._dot_net_version = dot_net_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ReferenceAssembly, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReferenceAssembly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other