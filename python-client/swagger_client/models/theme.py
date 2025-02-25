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


class Theme(object):
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
        'background_color': 'str',
        'background_text_color': 'str',
        'primary_color': 'str',
        'primary_text_color': 'str',
        'primary_highlight_color': 'str',
        'secondary_color': 'str',
        'secondary_text_color': 'str',
        'secondary_highlight_color': 'str',
        'terminal_color': 'str',
        'terminal_text_color': 'str',
        'terminal_highlight_color': 'str',
        'terminal_border_color': 'str',
        'navbar_color': 'str',
        'sidebar_color': 'str',
        'input_color': 'str',
        'input_disabled_color': 'str',
        'input_text_color': 'str',
        'input_highlight_color': 'str',
        'text_links_color': 'str',
        'code_mirror_theme': 'CodeMirrorTheme'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'background_color': 'backgroundColor',
        'background_text_color': 'backgroundTextColor',
        'primary_color': 'primaryColor',
        'primary_text_color': 'primaryTextColor',
        'primary_highlight_color': 'primaryHighlightColor',
        'secondary_color': 'secondaryColor',
        'secondary_text_color': 'secondaryTextColor',
        'secondary_highlight_color': 'secondaryHighlightColor',
        'terminal_color': 'terminalColor',
        'terminal_text_color': 'terminalTextColor',
        'terminal_highlight_color': 'terminalHighlightColor',
        'terminal_border_color': 'terminalBorderColor',
        'navbar_color': 'navbarColor',
        'sidebar_color': 'sidebarColor',
        'input_color': 'inputColor',
        'input_disabled_color': 'inputDisabledColor',
        'input_text_color': 'inputTextColor',
        'input_highlight_color': 'inputHighlightColor',
        'text_links_color': 'textLinksColor',
        'code_mirror_theme': 'codeMirrorTheme'
    }

    def __init__(self, id=None, name=None, description=None, background_color=None, background_text_color=None, primary_color=None, primary_text_color=None, primary_highlight_color=None, secondary_color=None, secondary_text_color=None, secondary_highlight_color=None, terminal_color=None, terminal_text_color=None, terminal_highlight_color=None, terminal_border_color=None, navbar_color=None, sidebar_color=None, input_color=None, input_disabled_color=None, input_text_color=None, input_highlight_color=None, text_links_color=None, code_mirror_theme=None):  # noqa: E501
        """Theme - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._background_color = None
        self._background_text_color = None
        self._primary_color = None
        self._primary_text_color = None
        self._primary_highlight_color = None
        self._secondary_color = None
        self._secondary_text_color = None
        self._secondary_highlight_color = None
        self._terminal_color = None
        self._terminal_text_color = None
        self._terminal_highlight_color = None
        self._terminal_border_color = None
        self._navbar_color = None
        self._sidebar_color = None
        self._input_color = None
        self._input_disabled_color = None
        self._input_text_color = None
        self._input_highlight_color = None
        self._text_links_color = None
        self._code_mirror_theme = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if background_color is not None:
            self.background_color = background_color
        if background_text_color is not None:
            self.background_text_color = background_text_color
        if primary_color is not None:
            self.primary_color = primary_color
        if primary_text_color is not None:
            self.primary_text_color = primary_text_color
        if primary_highlight_color is not None:
            self.primary_highlight_color = primary_highlight_color
        if secondary_color is not None:
            self.secondary_color = secondary_color
        if secondary_text_color is not None:
            self.secondary_text_color = secondary_text_color
        if secondary_highlight_color is not None:
            self.secondary_highlight_color = secondary_highlight_color
        if terminal_color is not None:
            self.terminal_color = terminal_color
        if terminal_text_color is not None:
            self.terminal_text_color = terminal_text_color
        if terminal_highlight_color is not None:
            self.terminal_highlight_color = terminal_highlight_color
        if terminal_border_color is not None:
            self.terminal_border_color = terminal_border_color
        if navbar_color is not None:
            self.navbar_color = navbar_color
        if sidebar_color is not None:
            self.sidebar_color = sidebar_color
        if input_color is not None:
            self.input_color = input_color
        if input_disabled_color is not None:
            self.input_disabled_color = input_disabled_color
        if input_text_color is not None:
            self.input_text_color = input_text_color
        if input_highlight_color is not None:
            self.input_highlight_color = input_highlight_color
        if text_links_color is not None:
            self.text_links_color = text_links_color
        if code_mirror_theme is not None:
            self.code_mirror_theme = code_mirror_theme

    @property
    def id(self):
        """Gets the id of this Theme.  # noqa: E501


        :return: The id of this Theme.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Theme.


        :param id: The id of this Theme.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Theme.  # noqa: E501


        :return: The name of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Theme.


        :param name: The name of this Theme.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Theme.  # noqa: E501


        :return: The description of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Theme.


        :param description: The description of this Theme.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def background_color(self):
        """Gets the background_color of this Theme.  # noqa: E501


        :return: The background_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this Theme.


        :param background_color: The background_color of this Theme.  # noqa: E501
        :type: str
        """
        if background_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', background_color):  # noqa: E501
            raise ValueError(r"Invalid value for `background_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._background_color = background_color

    @property
    def background_text_color(self):
        """Gets the background_text_color of this Theme.  # noqa: E501


        :return: The background_text_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._background_text_color

    @background_text_color.setter
    def background_text_color(self, background_text_color):
        """Sets the background_text_color of this Theme.


        :param background_text_color: The background_text_color of this Theme.  # noqa: E501
        :type: str
        """
        if background_text_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', background_text_color):  # noqa: E501
            raise ValueError(r"Invalid value for `background_text_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._background_text_color = background_text_color

    @property
    def primary_color(self):
        """Gets the primary_color of this Theme.  # noqa: E501


        :return: The primary_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._primary_color

    @primary_color.setter
    def primary_color(self, primary_color):
        """Sets the primary_color of this Theme.


        :param primary_color: The primary_color of this Theme.  # noqa: E501
        :type: str
        """
        if primary_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', primary_color):  # noqa: E501
            raise ValueError(r"Invalid value for `primary_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._primary_color = primary_color

    @property
    def primary_text_color(self):
        """Gets the primary_text_color of this Theme.  # noqa: E501


        :return: The primary_text_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._primary_text_color

    @primary_text_color.setter
    def primary_text_color(self, primary_text_color):
        """Sets the primary_text_color of this Theme.


        :param primary_text_color: The primary_text_color of this Theme.  # noqa: E501
        :type: str
        """
        if primary_text_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', primary_text_color):  # noqa: E501
            raise ValueError(r"Invalid value for `primary_text_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._primary_text_color = primary_text_color

    @property
    def primary_highlight_color(self):
        """Gets the primary_highlight_color of this Theme.  # noqa: E501


        :return: The primary_highlight_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._primary_highlight_color

    @primary_highlight_color.setter
    def primary_highlight_color(self, primary_highlight_color):
        """Sets the primary_highlight_color of this Theme.


        :param primary_highlight_color: The primary_highlight_color of this Theme.  # noqa: E501
        :type: str
        """
        if primary_highlight_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', primary_highlight_color):  # noqa: E501
            raise ValueError(r"Invalid value for `primary_highlight_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._primary_highlight_color = primary_highlight_color

    @property
    def secondary_color(self):
        """Gets the secondary_color of this Theme.  # noqa: E501


        :return: The secondary_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._secondary_color

    @secondary_color.setter
    def secondary_color(self, secondary_color):
        """Sets the secondary_color of this Theme.


        :param secondary_color: The secondary_color of this Theme.  # noqa: E501
        :type: str
        """
        if secondary_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', secondary_color):  # noqa: E501
            raise ValueError(r"Invalid value for `secondary_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._secondary_color = secondary_color

    @property
    def secondary_text_color(self):
        """Gets the secondary_text_color of this Theme.  # noqa: E501


        :return: The secondary_text_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._secondary_text_color

    @secondary_text_color.setter
    def secondary_text_color(self, secondary_text_color):
        """Sets the secondary_text_color of this Theme.


        :param secondary_text_color: The secondary_text_color of this Theme.  # noqa: E501
        :type: str
        """
        if secondary_text_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', secondary_text_color):  # noqa: E501
            raise ValueError(r"Invalid value for `secondary_text_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._secondary_text_color = secondary_text_color

    @property
    def secondary_highlight_color(self):
        """Gets the secondary_highlight_color of this Theme.  # noqa: E501


        :return: The secondary_highlight_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._secondary_highlight_color

    @secondary_highlight_color.setter
    def secondary_highlight_color(self, secondary_highlight_color):
        """Sets the secondary_highlight_color of this Theme.


        :param secondary_highlight_color: The secondary_highlight_color of this Theme.  # noqa: E501
        :type: str
        """
        if secondary_highlight_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', secondary_highlight_color):  # noqa: E501
            raise ValueError(r"Invalid value for `secondary_highlight_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._secondary_highlight_color = secondary_highlight_color

    @property
    def terminal_color(self):
        """Gets the terminal_color of this Theme.  # noqa: E501


        :return: The terminal_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._terminal_color

    @terminal_color.setter
    def terminal_color(self, terminal_color):
        """Sets the terminal_color of this Theme.


        :param terminal_color: The terminal_color of this Theme.  # noqa: E501
        :type: str
        """
        if terminal_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', terminal_color):  # noqa: E501
            raise ValueError(r"Invalid value for `terminal_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._terminal_color = terminal_color

    @property
    def terminal_text_color(self):
        """Gets the terminal_text_color of this Theme.  # noqa: E501


        :return: The terminal_text_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._terminal_text_color

    @terminal_text_color.setter
    def terminal_text_color(self, terminal_text_color):
        """Sets the terminal_text_color of this Theme.


        :param terminal_text_color: The terminal_text_color of this Theme.  # noqa: E501
        :type: str
        """
        if terminal_text_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', terminal_text_color):  # noqa: E501
            raise ValueError(r"Invalid value for `terminal_text_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._terminal_text_color = terminal_text_color

    @property
    def terminal_highlight_color(self):
        """Gets the terminal_highlight_color of this Theme.  # noqa: E501


        :return: The terminal_highlight_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._terminal_highlight_color

    @terminal_highlight_color.setter
    def terminal_highlight_color(self, terminal_highlight_color):
        """Sets the terminal_highlight_color of this Theme.


        :param terminal_highlight_color: The terminal_highlight_color of this Theme.  # noqa: E501
        :type: str
        """
        if terminal_highlight_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', terminal_highlight_color):  # noqa: E501
            raise ValueError(r"Invalid value for `terminal_highlight_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._terminal_highlight_color = terminal_highlight_color

    @property
    def terminal_border_color(self):
        """Gets the terminal_border_color of this Theme.  # noqa: E501


        :return: The terminal_border_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._terminal_border_color

    @terminal_border_color.setter
    def terminal_border_color(self, terminal_border_color):
        """Sets the terminal_border_color of this Theme.


        :param terminal_border_color: The terminal_border_color of this Theme.  # noqa: E501
        :type: str
        """
        if terminal_border_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', terminal_border_color):  # noqa: E501
            raise ValueError(r"Invalid value for `terminal_border_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._terminal_border_color = terminal_border_color

    @property
    def navbar_color(self):
        """Gets the navbar_color of this Theme.  # noqa: E501


        :return: The navbar_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._navbar_color

    @navbar_color.setter
    def navbar_color(self, navbar_color):
        """Sets the navbar_color of this Theme.


        :param navbar_color: The navbar_color of this Theme.  # noqa: E501
        :type: str
        """
        if navbar_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', navbar_color):  # noqa: E501
            raise ValueError(r"Invalid value for `navbar_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._navbar_color = navbar_color

    @property
    def sidebar_color(self):
        """Gets the sidebar_color of this Theme.  # noqa: E501


        :return: The sidebar_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._sidebar_color

    @sidebar_color.setter
    def sidebar_color(self, sidebar_color):
        """Sets the sidebar_color of this Theme.


        :param sidebar_color: The sidebar_color of this Theme.  # noqa: E501
        :type: str
        """
        if sidebar_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', sidebar_color):  # noqa: E501
            raise ValueError(r"Invalid value for `sidebar_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._sidebar_color = sidebar_color

    @property
    def input_color(self):
        """Gets the input_color of this Theme.  # noqa: E501


        :return: The input_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._input_color

    @input_color.setter
    def input_color(self, input_color):
        """Sets the input_color of this Theme.


        :param input_color: The input_color of this Theme.  # noqa: E501
        :type: str
        """
        if input_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', input_color):  # noqa: E501
            raise ValueError(r"Invalid value for `input_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._input_color = input_color

    @property
    def input_disabled_color(self):
        """Gets the input_disabled_color of this Theme.  # noqa: E501


        :return: The input_disabled_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._input_disabled_color

    @input_disabled_color.setter
    def input_disabled_color(self, input_disabled_color):
        """Sets the input_disabled_color of this Theme.


        :param input_disabled_color: The input_disabled_color of this Theme.  # noqa: E501
        :type: str
        """
        if input_disabled_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', input_disabled_color):  # noqa: E501
            raise ValueError(r"Invalid value for `input_disabled_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._input_disabled_color = input_disabled_color

    @property
    def input_text_color(self):
        """Gets the input_text_color of this Theme.  # noqa: E501


        :return: The input_text_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._input_text_color

    @input_text_color.setter
    def input_text_color(self, input_text_color):
        """Sets the input_text_color of this Theme.


        :param input_text_color: The input_text_color of this Theme.  # noqa: E501
        :type: str
        """
        if input_text_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', input_text_color):  # noqa: E501
            raise ValueError(r"Invalid value for `input_text_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._input_text_color = input_text_color

    @property
    def input_highlight_color(self):
        """Gets the input_highlight_color of this Theme.  # noqa: E501


        :return: The input_highlight_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._input_highlight_color

    @input_highlight_color.setter
    def input_highlight_color(self, input_highlight_color):
        """Sets the input_highlight_color of this Theme.


        :param input_highlight_color: The input_highlight_color of this Theme.  # noqa: E501
        :type: str
        """
        if input_highlight_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', input_highlight_color):  # noqa: E501
            raise ValueError(r"Invalid value for `input_highlight_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._input_highlight_color = input_highlight_color

    @property
    def text_links_color(self):
        """Gets the text_links_color of this Theme.  # noqa: E501


        :return: The text_links_color of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._text_links_color

    @text_links_color.setter
    def text_links_color(self, text_links_color):
        """Sets the text_links_color of this Theme.


        :param text_links_color: The text_links_color of this Theme.  # noqa: E501
        :type: str
        """
        if text_links_color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', text_links_color):  # noqa: E501
            raise ValueError(r"Invalid value for `text_links_color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._text_links_color = text_links_color

    @property
    def code_mirror_theme(self):
        """Gets the code_mirror_theme of this Theme.  # noqa: E501


        :return: The code_mirror_theme of this Theme.  # noqa: E501
        :rtype: CodeMirrorTheme
        """
        return self._code_mirror_theme

    @code_mirror_theme.setter
    def code_mirror_theme(self, code_mirror_theme):
        """Sets the code_mirror_theme of this Theme.


        :param code_mirror_theme: The code_mirror_theme of this Theme.  # noqa: E501
        :type: CodeMirrorTheme
        """

        self._code_mirror_theme = code_mirror_theme

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
        if issubclass(Theme, dict):
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
        if not isinstance(other, Theme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
