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


class GruntTaskAuthor(object):
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
        'handle': 'str',
        'link': 'str',
        'grunt_tasks': 'list[GruntTask]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'handle': 'handle',
        'link': 'link',
        'grunt_tasks': 'gruntTasks'
    }

    def __init__(self, id=None, name=None, handle=None, link=None, grunt_tasks=None):  # noqa: E501
        """GruntTaskAuthor - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._handle = None
        self._link = None
        self._grunt_tasks = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if handle is not None:
            self.handle = handle
        if link is not None:
            self.link = link
        if grunt_tasks is not None:
            self.grunt_tasks = grunt_tasks

    @property
    def id(self):
        """Gets the id of this GruntTaskAuthor.  # noqa: E501


        :return: The id of this GruntTaskAuthor.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GruntTaskAuthor.


        :param id: The id of this GruntTaskAuthor.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GruntTaskAuthor.  # noqa: E501


        :return: The name of this GruntTaskAuthor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GruntTaskAuthor.


        :param name: The name of this GruntTaskAuthor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def handle(self):
        """Gets the handle of this GruntTaskAuthor.  # noqa: E501


        :return: The handle of this GruntTaskAuthor.  # noqa: E501
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this GruntTaskAuthor.


        :param handle: The handle of this GruntTaskAuthor.  # noqa: E501
        :type: str
        """

        self._handle = handle

    @property
    def link(self):
        """Gets the link of this GruntTaskAuthor.  # noqa: E501


        :return: The link of this GruntTaskAuthor.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this GruntTaskAuthor.


        :param link: The link of this GruntTaskAuthor.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def grunt_tasks(self):
        """Gets the grunt_tasks of this GruntTaskAuthor.  # noqa: E501


        :return: The grunt_tasks of this GruntTaskAuthor.  # noqa: E501
        :rtype: list[GruntTask]
        """
        return self._grunt_tasks

    @grunt_tasks.setter
    def grunt_tasks(self, grunt_tasks):
        """Sets the grunt_tasks of this GruntTaskAuthor.


        :param grunt_tasks: The grunt_tasks of this GruntTaskAuthor.  # noqa: E501
        :type: list[GruntTask]
        """

        self._grunt_tasks = grunt_tasks

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
        if issubclass(GruntTaskAuthor, dict):
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
        if not isinstance(other, GruntTaskAuthor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
