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


class HostedFile(object):
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
        'listener_id': 'int',
        'path': 'str',
        'content': 'str'
    }

    attribute_map = {
        'id': 'id',
        'listener_id': 'listenerId',
        'path': 'path',
        'content': 'content'
    }

    def __init__(self, id=None, listener_id=None, path=None, content=None):  # noqa: E501
        """HostedFile - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._listener_id = None
        self._path = None
        self._content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if listener_id is not None:
            self.listener_id = listener_id
        if path is not None:
            self.path = path
        if content is not None:
            self.content = content

    @property
    def id(self):
        """Gets the id of this HostedFile.  # noqa: E501


        :return: The id of this HostedFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostedFile.


        :param id: The id of this HostedFile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def listener_id(self):
        """Gets the listener_id of this HostedFile.  # noqa: E501


        :return: The listener_id of this HostedFile.  # noqa: E501
        :rtype: int
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this HostedFile.


        :param listener_id: The listener_id of this HostedFile.  # noqa: E501
        :type: int
        """

        self._listener_id = listener_id

    @property
    def path(self):
        """Gets the path of this HostedFile.  # noqa: E501


        :return: The path of this HostedFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HostedFile.


        :param path: The path of this HostedFile.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def content(self):
        """Gets the content of this HostedFile.  # noqa: E501


        :return: The content of this HostedFile.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this HostedFile.


        :param content: The content of this HostedFile.  # noqa: E501
        :type: str
        """

        self._content = content

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
        if issubclass(HostedFile, dict):
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
        if not isinstance(other, HostedFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
