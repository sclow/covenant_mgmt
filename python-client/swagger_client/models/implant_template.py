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


class ImplantTemplate(object):
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
        'description': 'str',
        'language': 'ImplantLanguage',
        'comm_type': 'CommunicationType',
        'implant_direction': 'ImplantDirection',
        'compatible_listener_types': 'list[ListenerType]',
        'compatible_dot_net_versions': 'list[DotNetVersion]',
        'stager_code': 'str',
        'executor_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'language': 'language',
        'comm_type': 'commType',
        'implant_direction': 'implantDirection',
        'compatible_listener_types': 'compatibleListenerTypes',
        'compatible_dot_net_versions': 'compatibleDotNetVersions',
        'stager_code': 'stagerCode',
        'executor_code': 'executorCode'
    }

    def __init__(self, id=None, name=None, description=None, language=None, comm_type=None, implant_direction=None, compatible_listener_types=None, compatible_dot_net_versions=None, stager_code=None, executor_code=None):  # noqa: E501
        """ImplantTemplate - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._language = None
        self._comm_type = None
        self._implant_direction = None
        self._compatible_listener_types = None
        self._compatible_dot_net_versions = None
        self._stager_code = None
        self._executor_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if language is not None:
            self.language = language
        if comm_type is not None:
            self.comm_type = comm_type
        if implant_direction is not None:
            self.implant_direction = implant_direction
        if compatible_listener_types is not None:
            self.compatible_listener_types = compatible_listener_types
        if compatible_dot_net_versions is not None:
            self.compatible_dot_net_versions = compatible_dot_net_versions
        if stager_code is not None:
            self.stager_code = stager_code
        if executor_code is not None:
            self.executor_code = executor_code

    @property
    def id(self):
        """Gets the id of this ImplantTemplate.  # noqa: E501


        :return: The id of this ImplantTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImplantTemplate.


        :param id: The id of this ImplantTemplate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ImplantTemplate.  # noqa: E501


        :return: The name of this ImplantTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImplantTemplate.


        :param name: The name of this ImplantTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ImplantTemplate.  # noqa: E501


        :return: The description of this ImplantTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImplantTemplate.


        :param description: The description of this ImplantTemplate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def language(self):
        """Gets the language of this ImplantTemplate.  # noqa: E501


        :return: The language of this ImplantTemplate.  # noqa: E501
        :rtype: ImplantLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ImplantTemplate.


        :param language: The language of this ImplantTemplate.  # noqa: E501
        :type: ImplantLanguage
        """

        self._language = language

    @property
    def comm_type(self):
        """Gets the comm_type of this ImplantTemplate.  # noqa: E501


        :return: The comm_type of this ImplantTemplate.  # noqa: E501
        :rtype: CommunicationType
        """
        return self._comm_type

    @comm_type.setter
    def comm_type(self, comm_type):
        """Sets the comm_type of this ImplantTemplate.


        :param comm_type: The comm_type of this ImplantTemplate.  # noqa: E501
        :type: CommunicationType
        """

        self._comm_type = comm_type

    @property
    def implant_direction(self):
        """Gets the implant_direction of this ImplantTemplate.  # noqa: E501


        :return: The implant_direction of this ImplantTemplate.  # noqa: E501
        :rtype: ImplantDirection
        """
        return self._implant_direction

    @implant_direction.setter
    def implant_direction(self, implant_direction):
        """Sets the implant_direction of this ImplantTemplate.


        :param implant_direction: The implant_direction of this ImplantTemplate.  # noqa: E501
        :type: ImplantDirection
        """

        self._implant_direction = implant_direction

    @property
    def compatible_listener_types(self):
        """Gets the compatible_listener_types of this ImplantTemplate.  # noqa: E501


        :return: The compatible_listener_types of this ImplantTemplate.  # noqa: E501
        :rtype: list[ListenerType]
        """
        return self._compatible_listener_types

    @compatible_listener_types.setter
    def compatible_listener_types(self, compatible_listener_types):
        """Sets the compatible_listener_types of this ImplantTemplate.


        :param compatible_listener_types: The compatible_listener_types of this ImplantTemplate.  # noqa: E501
        :type: list[ListenerType]
        """

        self._compatible_listener_types = compatible_listener_types

    @property
    def compatible_dot_net_versions(self):
        """Gets the compatible_dot_net_versions of this ImplantTemplate.  # noqa: E501


        :return: The compatible_dot_net_versions of this ImplantTemplate.  # noqa: E501
        :rtype: list[DotNetVersion]
        """
        return self._compatible_dot_net_versions

    @compatible_dot_net_versions.setter
    def compatible_dot_net_versions(self, compatible_dot_net_versions):
        """Sets the compatible_dot_net_versions of this ImplantTemplate.


        :param compatible_dot_net_versions: The compatible_dot_net_versions of this ImplantTemplate.  # noqa: E501
        :type: list[DotNetVersion]
        """

        self._compatible_dot_net_versions = compatible_dot_net_versions

    @property
    def stager_code(self):
        """Gets the stager_code of this ImplantTemplate.  # noqa: E501


        :return: The stager_code of this ImplantTemplate.  # noqa: E501
        :rtype: str
        """
        return self._stager_code

    @stager_code.setter
    def stager_code(self, stager_code):
        """Sets the stager_code of this ImplantTemplate.


        :param stager_code: The stager_code of this ImplantTemplate.  # noqa: E501
        :type: str
        """

        self._stager_code = stager_code

    @property
    def executor_code(self):
        """Gets the executor_code of this ImplantTemplate.  # noqa: E501


        :return: The executor_code of this ImplantTemplate.  # noqa: E501
        :rtype: str
        """
        return self._executor_code

    @executor_code.setter
    def executor_code(self, executor_code):
        """Sets the executor_code of this ImplantTemplate.


        :param executor_code: The executor_code of this ImplantTemplate.  # noqa: E501
        :type: str
        """

        self._executor_code = executor_code

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
        if issubclass(ImplantTemplate, dict):
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
        if not isinstance(other, ImplantTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other