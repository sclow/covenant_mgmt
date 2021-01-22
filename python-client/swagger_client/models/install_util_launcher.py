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


class InstallUtilLauncher(object):
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
        'disk_code': 'str',
        'id': 'int',
        'listener_id': 'int',
        'implant_template_id': 'int',
        'name': 'str',
        'description': 'str',
        'type': 'LauncherType',
        'dot_net_version': 'DotNetVersion',
        'runtime_identifier': 'RuntimeIdentifier',
        'validate_cert': 'bool',
        'use_cert_pinning': 'bool',
        'smb_pipe_name': 'str',
        'delay': 'int',
        'jitter_percent': 'int',
        'connect_attempts': 'int',
        'kill_date': 'datetime',
        'launcher_string': 'str',
        'stager_code': 'str',
        'output_kind': 'OutputKind',
        'compress_stager': 'bool'
    }

    attribute_map = {
        'disk_code': 'diskCode',
        'id': 'id',
        'listener_id': 'listenerId',
        'implant_template_id': 'implantTemplateId',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'dot_net_version': 'dotNetVersion',
        'runtime_identifier': 'runtimeIdentifier',
        'validate_cert': 'validateCert',
        'use_cert_pinning': 'useCertPinning',
        'smb_pipe_name': 'smbPipeName',
        'delay': 'delay',
        'jitter_percent': 'jitterPercent',
        'connect_attempts': 'connectAttempts',
        'kill_date': 'killDate',
        'launcher_string': 'launcherString',
        'stager_code': 'stagerCode',
        'output_kind': 'outputKind',
        'compress_stager': 'compressStager'
    }

    def __init__(self, disk_code=None, id=None, listener_id=None, implant_template_id=None, name=None, description=None, type=None, dot_net_version=None, runtime_identifier=None, validate_cert=None, use_cert_pinning=None, smb_pipe_name=None, delay=None, jitter_percent=None, connect_attempts=None, kill_date=None, launcher_string=None, stager_code=None, output_kind=None, compress_stager=None):  # noqa: E501
        """InstallUtilLauncher - a model defined in Swagger"""  # noqa: E501

        self._disk_code = None
        self._id = None
        self._listener_id = None
        self._implant_template_id = None
        self._name = None
        self._description = None
        self._type = None
        self._dot_net_version = None
        self._runtime_identifier = None
        self._validate_cert = None
        self._use_cert_pinning = None
        self._smb_pipe_name = None
        self._delay = None
        self._jitter_percent = None
        self._connect_attempts = None
        self._kill_date = None
        self._launcher_string = None
        self._stager_code = None
        self._output_kind = None
        self._compress_stager = None
        self.discriminator = None

        if disk_code is not None:
            self.disk_code = disk_code
        if id is not None:
            self.id = id
        if listener_id is not None:
            self.listener_id = listener_id
        if implant_template_id is not None:
            self.implant_template_id = implant_template_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if dot_net_version is not None:
            self.dot_net_version = dot_net_version
        if runtime_identifier is not None:
            self.runtime_identifier = runtime_identifier
        if validate_cert is not None:
            self.validate_cert = validate_cert
        if use_cert_pinning is not None:
            self.use_cert_pinning = use_cert_pinning
        if smb_pipe_name is not None:
            self.smb_pipe_name = smb_pipe_name
        if delay is not None:
            self.delay = delay
        if jitter_percent is not None:
            self.jitter_percent = jitter_percent
        if connect_attempts is not None:
            self.connect_attempts = connect_attempts
        if kill_date is not None:
            self.kill_date = kill_date
        if launcher_string is not None:
            self.launcher_string = launcher_string
        if stager_code is not None:
            self.stager_code = stager_code
        if output_kind is not None:
            self.output_kind = output_kind
        if compress_stager is not None:
            self.compress_stager = compress_stager

    @property
    def disk_code(self):
        """Gets the disk_code of this InstallUtilLauncher.  # noqa: E501


        :return: The disk_code of this InstallUtilLauncher.  # noqa: E501
        :rtype: str
        """
        return self._disk_code

    @disk_code.setter
    def disk_code(self, disk_code):
        """Sets the disk_code of this InstallUtilLauncher.


        :param disk_code: The disk_code of this InstallUtilLauncher.  # noqa: E501
        :type: str
        """

        self._disk_code = disk_code

    @property
    def id(self):
        """Gets the id of this InstallUtilLauncher.  # noqa: E501


        :return: The id of this InstallUtilLauncher.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstallUtilLauncher.


        :param id: The id of this InstallUtilLauncher.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def listener_id(self):
        """Gets the listener_id of this InstallUtilLauncher.  # noqa: E501


        :return: The listener_id of this InstallUtilLauncher.  # noqa: E501
        :rtype: int
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this InstallUtilLauncher.


        :param listener_id: The listener_id of this InstallUtilLauncher.  # noqa: E501
        :type: int
        """

        self._listener_id = listener_id

    @property
    def implant_template_id(self):
        """Gets the implant_template_id of this InstallUtilLauncher.  # noqa: E501


        :return: The implant_template_id of this InstallUtilLauncher.  # noqa: E501
        :rtype: int
        """
        return self._implant_template_id

    @implant_template_id.setter
    def implant_template_id(self, implant_template_id):
        """Sets the implant_template_id of this InstallUtilLauncher.


        :param implant_template_id: The implant_template_id of this InstallUtilLauncher.  # noqa: E501
        :type: int
        """

        self._implant_template_id = implant_template_id

    @property
    def name(self):
        """Gets the name of this InstallUtilLauncher.  # noqa: E501


        :return: The name of this InstallUtilLauncher.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstallUtilLauncher.


        :param name: The name of this InstallUtilLauncher.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this InstallUtilLauncher.  # noqa: E501


        :return: The description of this InstallUtilLauncher.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstallUtilLauncher.


        :param description: The description of this InstallUtilLauncher.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this InstallUtilLauncher.  # noqa: E501


        :return: The type of this InstallUtilLauncher.  # noqa: E501
        :rtype: LauncherType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InstallUtilLauncher.


        :param type: The type of this InstallUtilLauncher.  # noqa: E501
        :type: LauncherType
        """

        self._type = type

    @property
    def dot_net_version(self):
        """Gets the dot_net_version of this InstallUtilLauncher.  # noqa: E501


        :return: The dot_net_version of this InstallUtilLauncher.  # noqa: E501
        :rtype: DotNetVersion
        """
        return self._dot_net_version

    @dot_net_version.setter
    def dot_net_version(self, dot_net_version):
        """Sets the dot_net_version of this InstallUtilLauncher.


        :param dot_net_version: The dot_net_version of this InstallUtilLauncher.  # noqa: E501
        :type: DotNetVersion
        """

        self._dot_net_version = dot_net_version

    @property
    def runtime_identifier(self):
        """Gets the runtime_identifier of this InstallUtilLauncher.  # noqa: E501


        :return: The runtime_identifier of this InstallUtilLauncher.  # noqa: E501
        :rtype: RuntimeIdentifier
        """
        return self._runtime_identifier

    @runtime_identifier.setter
    def runtime_identifier(self, runtime_identifier):
        """Sets the runtime_identifier of this InstallUtilLauncher.


        :param runtime_identifier: The runtime_identifier of this InstallUtilLauncher.  # noqa: E501
        :type: RuntimeIdentifier
        """

        self._runtime_identifier = runtime_identifier

    @property
    def validate_cert(self):
        """Gets the validate_cert of this InstallUtilLauncher.  # noqa: E501


        :return: The validate_cert of this InstallUtilLauncher.  # noqa: E501
        :rtype: bool
        """
        return self._validate_cert

    @validate_cert.setter
    def validate_cert(self, validate_cert):
        """Sets the validate_cert of this InstallUtilLauncher.


        :param validate_cert: The validate_cert of this InstallUtilLauncher.  # noqa: E501
        :type: bool
        """

        self._validate_cert = validate_cert

    @property
    def use_cert_pinning(self):
        """Gets the use_cert_pinning of this InstallUtilLauncher.  # noqa: E501


        :return: The use_cert_pinning of this InstallUtilLauncher.  # noqa: E501
        :rtype: bool
        """
        return self._use_cert_pinning

    @use_cert_pinning.setter
    def use_cert_pinning(self, use_cert_pinning):
        """Sets the use_cert_pinning of this InstallUtilLauncher.


        :param use_cert_pinning: The use_cert_pinning of this InstallUtilLauncher.  # noqa: E501
        :type: bool
        """

        self._use_cert_pinning = use_cert_pinning

    @property
    def smb_pipe_name(self):
        """Gets the smb_pipe_name of this InstallUtilLauncher.  # noqa: E501


        :return: The smb_pipe_name of this InstallUtilLauncher.  # noqa: E501
        :rtype: str
        """
        return self._smb_pipe_name

    @smb_pipe_name.setter
    def smb_pipe_name(self, smb_pipe_name):
        """Sets the smb_pipe_name of this InstallUtilLauncher.


        :param smb_pipe_name: The smb_pipe_name of this InstallUtilLauncher.  # noqa: E501
        :type: str
        """

        self._smb_pipe_name = smb_pipe_name

    @property
    def delay(self):
        """Gets the delay of this InstallUtilLauncher.  # noqa: E501


        :return: The delay of this InstallUtilLauncher.  # noqa: E501
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this InstallUtilLauncher.


        :param delay: The delay of this InstallUtilLauncher.  # noqa: E501
        :type: int
        """

        self._delay = delay

    @property
    def jitter_percent(self):
        """Gets the jitter_percent of this InstallUtilLauncher.  # noqa: E501


        :return: The jitter_percent of this InstallUtilLauncher.  # noqa: E501
        :rtype: int
        """
        return self._jitter_percent

    @jitter_percent.setter
    def jitter_percent(self, jitter_percent):
        """Sets the jitter_percent of this InstallUtilLauncher.


        :param jitter_percent: The jitter_percent of this InstallUtilLauncher.  # noqa: E501
        :type: int
        """

        self._jitter_percent = jitter_percent

    @property
    def connect_attempts(self):
        """Gets the connect_attempts of this InstallUtilLauncher.  # noqa: E501


        :return: The connect_attempts of this InstallUtilLauncher.  # noqa: E501
        :rtype: int
        """
        return self._connect_attempts

    @connect_attempts.setter
    def connect_attempts(self, connect_attempts):
        """Sets the connect_attempts of this InstallUtilLauncher.


        :param connect_attempts: The connect_attempts of this InstallUtilLauncher.  # noqa: E501
        :type: int
        """

        self._connect_attempts = connect_attempts

    @property
    def kill_date(self):
        """Gets the kill_date of this InstallUtilLauncher.  # noqa: E501


        :return: The kill_date of this InstallUtilLauncher.  # noqa: E501
        :rtype: datetime
        """
        return self._kill_date

    @kill_date.setter
    def kill_date(self, kill_date):
        """Sets the kill_date of this InstallUtilLauncher.


        :param kill_date: The kill_date of this InstallUtilLauncher.  # noqa: E501
        :type: datetime
        """

        self._kill_date = kill_date

    @property
    def launcher_string(self):
        """Gets the launcher_string of this InstallUtilLauncher.  # noqa: E501


        :return: The launcher_string of this InstallUtilLauncher.  # noqa: E501
        :rtype: str
        """
        return self._launcher_string

    @launcher_string.setter
    def launcher_string(self, launcher_string):
        """Sets the launcher_string of this InstallUtilLauncher.


        :param launcher_string: The launcher_string of this InstallUtilLauncher.  # noqa: E501
        :type: str
        """

        self._launcher_string = launcher_string

    @property
    def stager_code(self):
        """Gets the stager_code of this InstallUtilLauncher.  # noqa: E501


        :return: The stager_code of this InstallUtilLauncher.  # noqa: E501
        :rtype: str
        """
        return self._stager_code

    @stager_code.setter
    def stager_code(self, stager_code):
        """Sets the stager_code of this InstallUtilLauncher.


        :param stager_code: The stager_code of this InstallUtilLauncher.  # noqa: E501
        :type: str
        """

        self._stager_code = stager_code

    @property
    def output_kind(self):
        """Gets the output_kind of this InstallUtilLauncher.  # noqa: E501


        :return: The output_kind of this InstallUtilLauncher.  # noqa: E501
        :rtype: OutputKind
        """
        return self._output_kind

    @output_kind.setter
    def output_kind(self, output_kind):
        """Sets the output_kind of this InstallUtilLauncher.


        :param output_kind: The output_kind of this InstallUtilLauncher.  # noqa: E501
        :type: OutputKind
        """

        self._output_kind = output_kind

    @property
    def compress_stager(self):
        """Gets the compress_stager of this InstallUtilLauncher.  # noqa: E501


        :return: The compress_stager of this InstallUtilLauncher.  # noqa: E501
        :rtype: bool
        """
        return self._compress_stager

    @compress_stager.setter
    def compress_stager(self, compress_stager):
        """Sets the compress_stager of this InstallUtilLauncher.


        :param compress_stager: The compress_stager of this InstallUtilLauncher.  # noqa: E501
        :type: bool
        """

        self._compress_stager = compress_stager

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
        if issubclass(InstallUtilLauncher, dict):
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
        if not isinstance(other, InstallUtilLauncher):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other