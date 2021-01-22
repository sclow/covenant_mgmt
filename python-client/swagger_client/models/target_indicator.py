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


class TargetIndicator(object):
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
        'computer_name': 'str',
        'user_name': 'str',
        'id': 'int',
        'type': 'IndicatorType'
    }

    attribute_map = {
        'computer_name': 'computerName',
        'user_name': 'userName',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, computer_name=None, user_name=None, id=None, type=None):  # noqa: E501
        """TargetIndicator - a model defined in Swagger"""  # noqa: E501

        self._computer_name = None
        self._user_name = None
        self._id = None
        self._type = None
        self.discriminator = None

        if computer_name is not None:
            self.computer_name = computer_name
        if user_name is not None:
            self.user_name = user_name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def computer_name(self):
        """Gets the computer_name of this TargetIndicator.  # noqa: E501


        :return: The computer_name of this TargetIndicator.  # noqa: E501
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this TargetIndicator.


        :param computer_name: The computer_name of this TargetIndicator.  # noqa: E501
        :type: str
        """

        self._computer_name = computer_name

    @property
    def user_name(self):
        """Gets the user_name of this TargetIndicator.  # noqa: E501


        :return: The user_name of this TargetIndicator.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this TargetIndicator.


        :param user_name: The user_name of this TargetIndicator.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def id(self):
        """Gets the id of this TargetIndicator.  # noqa: E501


        :return: The id of this TargetIndicator.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TargetIndicator.


        :param id: The id of this TargetIndicator.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this TargetIndicator.  # noqa: E501


        :return: The type of this TargetIndicator.  # noqa: E501
        :rtype: IndicatorType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TargetIndicator.


        :param type: The type of this TargetIndicator.  # noqa: E501
        :type: IndicatorType
        """

        self._type = type

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
        if issubclass(TargetIndicator, dict):
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
        if not isinstance(other, TargetIndicator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
