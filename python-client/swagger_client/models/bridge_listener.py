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


class BridgeListener(object):
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
        'is_bridge_connected': 'bool',
        'implant_read_code': 'str',
        'implant_write_code': 'str',
        'id': 'int',
        'name': 'str',
        'guid': 'str',
        'description': 'str',
        'bind_address': 'str',
        'bind_port': 'int',
        'connect_addresses': 'list[str]',
        'connect_port': 'int',
        'profile_id': 'int',
        'profile': 'Profile',
        'listener_type_id': 'int',
        'listener_type': 'ListenerType',
        'status': 'ListenerStatus',
        'covenant_url': 'str',
        'covenant_token': 'str',
        'start_time': 'datetime'
    }

    attribute_map = {
        'is_bridge_connected': 'isBridgeConnected',
        'implant_read_code': 'implantReadCode',
        'implant_write_code': 'implantWriteCode',
        'id': 'id',
        'name': 'name',
        'guid': 'guid',
        'description': 'description',
        'bind_address': 'bindAddress',
        'bind_port': 'bindPort',
        'connect_addresses': 'connectAddresses',
        'connect_port': 'connectPort',
        'profile_id': 'profileId',
        'profile': 'profile',
        'listener_type_id': 'listenerTypeId',
        'listener_type': 'listenerType',
        'status': 'status',
        'covenant_url': 'covenantUrl',
        'covenant_token': 'covenantToken',
        'start_time': 'startTime'
    }

    def __init__(self, is_bridge_connected=None, implant_read_code=None, implant_write_code=None, id=None, name=None, guid=None, description=None, bind_address=None, bind_port=None, connect_addresses=None, connect_port=None, profile_id=None, profile=None, listener_type_id=None, listener_type=None, status=None, covenant_url=None, covenant_token=None, start_time=None):  # noqa: E501
        """BridgeListener - a model defined in Swagger"""  # noqa: E501

        self._is_bridge_connected = None
        self._implant_read_code = None
        self._implant_write_code = None
        self._id = None
        self._name = None
        self._guid = None
        self._description = None
        self._bind_address = None
        self._bind_port = None
        self._connect_addresses = None
        self._connect_port = None
        self._profile_id = None
        self._profile = None
        self._listener_type_id = None
        self._listener_type = None
        self._status = None
        self._covenant_url = None
        self._covenant_token = None
        self._start_time = None
        self.discriminator = None

        if is_bridge_connected is not None:
            self.is_bridge_connected = is_bridge_connected
        if implant_read_code is not None:
            self.implant_read_code = implant_read_code
        if implant_write_code is not None:
            self.implant_write_code = implant_write_code
        if id is not None:
            self.id = id
        self.name = name
        self.guid = guid
        self.description = description
        self.bind_address = bind_address
        self.bind_port = bind_port
        self.connect_addresses = connect_addresses
        self.connect_port = connect_port
        self.profile_id = profile_id
        if profile is not None:
            self.profile = profile
        self.listener_type_id = listener_type_id
        if listener_type is not None:
            self.listener_type = listener_type
        self.status = status
        if covenant_url is not None:
            self.covenant_url = covenant_url
        if covenant_token is not None:
            self.covenant_token = covenant_token
        if start_time is not None:
            self.start_time = start_time

    @property
    def is_bridge_connected(self):
        """Gets the is_bridge_connected of this BridgeListener.  # noqa: E501


        :return: The is_bridge_connected of this BridgeListener.  # noqa: E501
        :rtype: bool
        """
        return self._is_bridge_connected

    @is_bridge_connected.setter
    def is_bridge_connected(self, is_bridge_connected):
        """Sets the is_bridge_connected of this BridgeListener.


        :param is_bridge_connected: The is_bridge_connected of this BridgeListener.  # noqa: E501
        :type: bool
        """

        self._is_bridge_connected = is_bridge_connected

    @property
    def implant_read_code(self):
        """Gets the implant_read_code of this BridgeListener.  # noqa: E501


        :return: The implant_read_code of this BridgeListener.  # noqa: E501
        :rtype: str
        """
        return self._implant_read_code

    @implant_read_code.setter
    def implant_read_code(self, implant_read_code):
        """Sets the implant_read_code of this BridgeListener.


        :param implant_read_code: The implant_read_code of this BridgeListener.  # noqa: E501
        :type: str
        """

        self._implant_read_code = implant_read_code

    @property
    def implant_write_code(self):
        """Gets the implant_write_code of this BridgeListener.  # noqa: E501


        :return: The implant_write_code of this BridgeListener.  # noqa: E501
        :rtype: str
        """
        return self._implant_write_code

    @implant_write_code.setter
    def implant_write_code(self, implant_write_code):
        """Sets the implant_write_code of this BridgeListener.


        :param implant_write_code: The implant_write_code of this BridgeListener.  # noqa: E501
        :type: str
        """

        self._implant_write_code = implant_write_code

    @property
    def id(self):
        """Gets the id of this BridgeListener.  # noqa: E501


        :return: The id of this BridgeListener.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BridgeListener.


        :param id: The id of this BridgeListener.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BridgeListener.  # noqa: E501


        :return: The name of this BridgeListener.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BridgeListener.


        :param name: The name of this BridgeListener.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def guid(self):
        """Gets the guid of this BridgeListener.  # noqa: E501


        :return: The guid of this BridgeListener.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this BridgeListener.


        :param guid: The guid of this BridgeListener.  # noqa: E501
        :type: str
        """
        if guid is None:
            raise ValueError("Invalid value for `guid`, must not be `None`")  # noqa: E501
        if guid is not None and len(guid) > 100:
            raise ValueError("Invalid value for `guid`, length must be less than or equal to `100`")  # noqa: E501
        if guid is not None and len(guid) < 0:
            raise ValueError("Invalid value for `guid`, length must be greater than or equal to `0`")  # noqa: E501
        if guid is not None and not re.search(r'^[a-zA-Z0-9]*$', guid):  # noqa: E501
            raise ValueError(r"Invalid value for `guid`, must be a follow pattern or equal to `/^[a-zA-Z0-9]*$/`")  # noqa: E501

        self._guid = guid

    @property
    def description(self):
        """Gets the description of this BridgeListener.  # noqa: E501


        :return: The description of this BridgeListener.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BridgeListener.


        :param description: The description of this BridgeListener.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def bind_address(self):
        """Gets the bind_address of this BridgeListener.  # noqa: E501


        :return: The bind_address of this BridgeListener.  # noqa: E501
        :rtype: str
        """
        return self._bind_address

    @bind_address.setter
    def bind_address(self, bind_address):
        """Sets the bind_address of this BridgeListener.


        :param bind_address: The bind_address of this BridgeListener.  # noqa: E501
        :type: str
        """
        if bind_address is None:
            raise ValueError("Invalid value for `bind_address`, must not be `None`")  # noqa: E501
        if bind_address is not None and not re.search(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', bind_address):  # noqa: E501
            raise ValueError(r"Invalid value for `bind_address`, must be a follow pattern or equal to `/^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/`")  # noqa: E501

        self._bind_address = bind_address

    @property
    def bind_port(self):
        """Gets the bind_port of this BridgeListener.  # noqa: E501


        :return: The bind_port of this BridgeListener.  # noqa: E501
        :rtype: int
        """
        return self._bind_port

    @bind_port.setter
    def bind_port(self, bind_port):
        """Sets the bind_port of this BridgeListener.


        :param bind_port: The bind_port of this BridgeListener.  # noqa: E501
        :type: int
        """
        if bind_port is None:
            raise ValueError("Invalid value for `bind_port`, must not be `None`")  # noqa: E501
        if bind_port is not None and bind_port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `bind_port`, must be a value less than or equal to `65535`")  # noqa: E501
        if bind_port is not None and bind_port < 1:  # noqa: E501
            raise ValueError("Invalid value for `bind_port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._bind_port = bind_port

    @property
    def connect_addresses(self):
        """Gets the connect_addresses of this BridgeListener.  # noqa: E501


        :return: The connect_addresses of this BridgeListener.  # noqa: E501
        :rtype: list[str]
        """
        return self._connect_addresses

    @connect_addresses.setter
    def connect_addresses(self, connect_addresses):
        """Sets the connect_addresses of this BridgeListener.


        :param connect_addresses: The connect_addresses of this BridgeListener.  # noqa: E501
        :type: list[str]
        """
        if connect_addresses is None:
            raise ValueError("Invalid value for `connect_addresses`, must not be `None`")  # noqa: E501

        self._connect_addresses = connect_addresses

    @property
    def connect_port(self):
        """Gets the connect_port of this BridgeListener.  # noqa: E501


        :return: The connect_port of this BridgeListener.  # noqa: E501
        :rtype: int
        """
        return self._connect_port

    @connect_port.setter
    def connect_port(self, connect_port):
        """Sets the connect_port of this BridgeListener.


        :param connect_port: The connect_port of this BridgeListener.  # noqa: E501
        :type: int
        """
        if connect_port is None:
            raise ValueError("Invalid value for `connect_port`, must not be `None`")  # noqa: E501
        if connect_port is not None and connect_port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `connect_port`, must be a value less than or equal to `65535`")  # noqa: E501
        if connect_port is not None and connect_port < 1:  # noqa: E501
            raise ValueError("Invalid value for `connect_port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._connect_port = connect_port

    @property
    def profile_id(self):
        """Gets the profile_id of this BridgeListener.  # noqa: E501


        :return: The profile_id of this BridgeListener.  # noqa: E501
        :rtype: int
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this BridgeListener.


        :param profile_id: The profile_id of this BridgeListener.  # noqa: E501
        :type: int
        """
        if profile_id is None:
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id

    @property
    def profile(self):
        """Gets the profile of this BridgeListener.  # noqa: E501


        :return: The profile of this BridgeListener.  # noqa: E501
        :rtype: Profile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this BridgeListener.


        :param profile: The profile of this BridgeListener.  # noqa: E501
        :type: Profile
        """

        self._profile = profile

    @property
    def listener_type_id(self):
        """Gets the listener_type_id of this BridgeListener.  # noqa: E501


        :return: The listener_type_id of this BridgeListener.  # noqa: E501
        :rtype: int
        """
        return self._listener_type_id

    @listener_type_id.setter
    def listener_type_id(self, listener_type_id):
        """Sets the listener_type_id of this BridgeListener.


        :param listener_type_id: The listener_type_id of this BridgeListener.  # noqa: E501
        :type: int
        """
        if listener_type_id is None:
            raise ValueError("Invalid value for `listener_type_id`, must not be `None`")  # noqa: E501

        self._listener_type_id = listener_type_id

    @property
    def listener_type(self):
        """Gets the listener_type of this BridgeListener.  # noqa: E501


        :return: The listener_type of this BridgeListener.  # noqa: E501
        :rtype: ListenerType
        """
        return self._listener_type

    @listener_type.setter
    def listener_type(self, listener_type):
        """Sets the listener_type of this BridgeListener.


        :param listener_type: The listener_type of this BridgeListener.  # noqa: E501
        :type: ListenerType
        """

        self._listener_type = listener_type

    @property
    def status(self):
        """Gets the status of this BridgeListener.  # noqa: E501


        :return: The status of this BridgeListener.  # noqa: E501
        :rtype: ListenerStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BridgeListener.


        :param status: The status of this BridgeListener.  # noqa: E501
        :type: ListenerStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def covenant_url(self):
        """Gets the covenant_url of this BridgeListener.  # noqa: E501


        :return: The covenant_url of this BridgeListener.  # noqa: E501
        :rtype: str
        """
        return self._covenant_url

    @covenant_url.setter
    def covenant_url(self, covenant_url):
        """Sets the covenant_url of this BridgeListener.


        :param covenant_url: The covenant_url of this BridgeListener.  # noqa: E501
        :type: str
        """

        self._covenant_url = covenant_url

    @property
    def covenant_token(self):
        """Gets the covenant_token of this BridgeListener.  # noqa: E501


        :return: The covenant_token of this BridgeListener.  # noqa: E501
        :rtype: str
        """
        return self._covenant_token

    @covenant_token.setter
    def covenant_token(self, covenant_token):
        """Sets the covenant_token of this BridgeListener.


        :param covenant_token: The covenant_token of this BridgeListener.  # noqa: E501
        :type: str
        """

        self._covenant_token = covenant_token

    @property
    def start_time(self):
        """Gets the start_time of this BridgeListener.  # noqa: E501


        :return: The start_time of this BridgeListener.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BridgeListener.


        :param start_time: The start_time of this BridgeListener.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

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
        if issubclass(BridgeListener, dict):
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
        if not isinstance(other, BridgeListener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other