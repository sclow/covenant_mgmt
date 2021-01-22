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


class GruntCommand(object):
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
        'command': 'str',
        'command_time': 'datetime',
        'command_output_id': 'int',
        'command_output': 'CommandOutput',
        'user_id': 'str',
        'user': 'CovenantUser',
        'grunt_tasking_id': 'int',
        'grunt_tasking': 'GruntTasking',
        'grunt_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'command': 'command',
        'command_time': 'commandTime',
        'command_output_id': 'commandOutputId',
        'command_output': 'commandOutput',
        'user_id': 'userId',
        'user': 'user',
        'grunt_tasking_id': 'gruntTaskingId',
        'grunt_tasking': 'gruntTasking',
        'grunt_id': 'gruntId'
    }

    def __init__(self, id=None, command=None, command_time=None, command_output_id=None, command_output=None, user_id=None, user=None, grunt_tasking_id=None, grunt_tasking=None, grunt_id=None):  # noqa: E501
        """GruntCommand - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._command = None
        self._command_time = None
        self._command_output_id = None
        self._command_output = None
        self._user_id = None
        self._user = None
        self._grunt_tasking_id = None
        self._grunt_tasking = None
        self._grunt_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.command = command
        self.command_time = command_time
        self.command_output_id = command_output_id
        if command_output is not None:
            self.command_output = command_output
        self.user_id = user_id
        if user is not None:
            self.user = user
        if grunt_tasking_id is not None:
            self.grunt_tasking_id = grunt_tasking_id
        if grunt_tasking is not None:
            self.grunt_tasking = grunt_tasking
        if grunt_id is not None:
            self.grunt_id = grunt_id

    @property
    def id(self):
        """Gets the id of this GruntCommand.  # noqa: E501


        :return: The id of this GruntCommand.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GruntCommand.


        :param id: The id of this GruntCommand.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def command(self):
        """Gets the command of this GruntCommand.  # noqa: E501


        :return: The command of this GruntCommand.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this GruntCommand.


        :param command: The command of this GruntCommand.  # noqa: E501
        :type: str
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def command_time(self):
        """Gets the command_time of this GruntCommand.  # noqa: E501


        :return: The command_time of this GruntCommand.  # noqa: E501
        :rtype: datetime
        """
        return self._command_time

    @command_time.setter
    def command_time(self, command_time):
        """Sets the command_time of this GruntCommand.


        :param command_time: The command_time of this GruntCommand.  # noqa: E501
        :type: datetime
        """
        if command_time is None:
            raise ValueError("Invalid value for `command_time`, must not be `None`")  # noqa: E501

        self._command_time = command_time

    @property
    def command_output_id(self):
        """Gets the command_output_id of this GruntCommand.  # noqa: E501


        :return: The command_output_id of this GruntCommand.  # noqa: E501
        :rtype: int
        """
        return self._command_output_id

    @command_output_id.setter
    def command_output_id(self, command_output_id):
        """Sets the command_output_id of this GruntCommand.


        :param command_output_id: The command_output_id of this GruntCommand.  # noqa: E501
        :type: int
        """
        if command_output_id is None:
            raise ValueError("Invalid value for `command_output_id`, must not be `None`")  # noqa: E501

        self._command_output_id = command_output_id

    @property
    def command_output(self):
        """Gets the command_output of this GruntCommand.  # noqa: E501


        :return: The command_output of this GruntCommand.  # noqa: E501
        :rtype: CommandOutput
        """
        return self._command_output

    @command_output.setter
    def command_output(self, command_output):
        """Sets the command_output of this GruntCommand.


        :param command_output: The command_output of this GruntCommand.  # noqa: E501
        :type: CommandOutput
        """

        self._command_output = command_output

    @property
    def user_id(self):
        """Gets the user_id of this GruntCommand.  # noqa: E501


        :return: The user_id of this GruntCommand.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GruntCommand.


        :param user_id: The user_id of this GruntCommand.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def user(self):
        """Gets the user of this GruntCommand.  # noqa: E501


        :return: The user of this GruntCommand.  # noqa: E501
        :rtype: CovenantUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this GruntCommand.


        :param user: The user of this GruntCommand.  # noqa: E501
        :type: CovenantUser
        """

        self._user = user

    @property
    def grunt_tasking_id(self):
        """Gets the grunt_tasking_id of this GruntCommand.  # noqa: E501


        :return: The grunt_tasking_id of this GruntCommand.  # noqa: E501
        :rtype: int
        """
        return self._grunt_tasking_id

    @grunt_tasking_id.setter
    def grunt_tasking_id(self, grunt_tasking_id):
        """Sets the grunt_tasking_id of this GruntCommand.


        :param grunt_tasking_id: The grunt_tasking_id of this GruntCommand.  # noqa: E501
        :type: int
        """

        self._grunt_tasking_id = grunt_tasking_id

    @property
    def grunt_tasking(self):
        """Gets the grunt_tasking of this GruntCommand.  # noqa: E501


        :return: The grunt_tasking of this GruntCommand.  # noqa: E501
        :rtype: GruntTasking
        """
        return self._grunt_tasking

    @grunt_tasking.setter
    def grunt_tasking(self, grunt_tasking):
        """Sets the grunt_tasking of this GruntCommand.


        :param grunt_tasking: The grunt_tasking of this GruntCommand.  # noqa: E501
        :type: GruntTasking
        """

        self._grunt_tasking = grunt_tasking

    @property
    def grunt_id(self):
        """Gets the grunt_id of this GruntCommand.  # noqa: E501


        :return: The grunt_id of this GruntCommand.  # noqa: E501
        :rtype: int
        """
        return self._grunt_id

    @grunt_id.setter
    def grunt_id(self, grunt_id):
        """Sets the grunt_id of this GruntCommand.


        :param grunt_id: The grunt_id of this GruntCommand.  # noqa: E501
        :type: int
        """

        self._grunt_id = grunt_id

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
        if issubclass(GruntCommand, dict):
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
        if not isinstance(other, GruntCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other