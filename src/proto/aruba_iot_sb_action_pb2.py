# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-sb-action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import src.proto.aruba_iot_types_pb2 as aruba__iot__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-sb-action.proto',
  package='aruba_telemetry',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x61ruba-iot-sb-action.proto\x12\x0f\x61ruba_telemetry\x1a\x15\x61ruba-iot-types.proto\"\x89\x01\n\x0e\x41uthentication\x12\x35\n\x06method\x18\x01 \x01(\x0e\x32%.aruba_telemetry.AuthenticationMethod\x12\x0f\n\x07\x62onding\x18\x02 \x01(\x08\x12\x0f\n\x07passkey\x18\x03 \x01(\t\x12\x0e\n\x06keyOob\x18\x04 \x01(\x0c\x12\x0e\n\x06keyOwn\x18\x05 \x01(\x0c\"\xa6\x02\n\x06\x41\x63tion\x12\x10\n\x08\x61\x63tionId\x18\x01 \x01(\t\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.aruba_telemetry.ActionType\x12\x11\n\tdeviceMac\x18\x03 \x01(\x0c\x12\x13\n\x0bserviceUuid\x18\x04 \x01(\x0c\x12\x1a\n\x12\x63haracteristicUuid\x18\x05 \x01(\x0c\x12\x0f\n\x07timeOut\x18\x06 \x01(\r\x12\r\n\x05value\x18\x07 \x01(\x0c\x12\x37\n\x0e\x61uthentication\x18\x08 \x01(\x0b\x32\x1f.aruba_telemetry.Authentication\x12\x32\n\nbondingKey\x18\t \x01(\x0b\x32\x1e.aruba_telemetry.BleBondingKey\x12\x0e\n\x06\x61pbMac\x18\n \x01(\x0c*b\n\x14\x41uthenticationMethod\x12\x08\n\x04none\x10\x00\x12\x0b\n\x07passkey\x10\x01\x12\x07\n\x03oob\x10\x02\x12\x0c\n\x08lescNone\x10\x03\x12\x0f\n\x0blescPasskey\x10\x04\x12\x0b\n\x07lescOob\x10\x05')
  ,
  dependencies=[aruba__iot__types__pb2.DESCRIPTOR,])

_AUTHENTICATIONMETHOD = _descriptor.EnumDescriptor(
  name='AuthenticationMethod',
  full_name='aruba_telemetry.AuthenticationMethod',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='none', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='passkey', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='oob', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='lescNone', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='lescPasskey', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='lescOob', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=506,
  serialized_end=604,
)
_sym_db.RegisterEnumDescriptor(_AUTHENTICATIONMETHOD)

AuthenticationMethod = enum_type_wrapper.EnumTypeWrapper(_AUTHENTICATIONMETHOD)
none = 0
passkey = 1
oob = 2
lescNone = 3
lescPasskey = 4
lescOob = 5



_AUTHENTICATION = _descriptor.Descriptor(
  name='Authentication',
  full_name='aruba_telemetry.Authentication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='aruba_telemetry.Authentication.method', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bonding', full_name='aruba_telemetry.Authentication.bonding', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passkey', full_name='aruba_telemetry.Authentication.passkey', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyOob', full_name='aruba_telemetry.Authentication.keyOob', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyOwn', full_name='aruba_telemetry.Authentication.keyOwn', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=207,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='aruba_telemetry.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionId', full_name='aruba_telemetry.Action.actionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='aruba_telemetry.Action.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceMac', full_name='aruba_telemetry.Action.deviceMac', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serviceUuid', full_name='aruba_telemetry.Action.serviceUuid', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='characteristicUuid', full_name='aruba_telemetry.Action.characteristicUuid', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeOut', full_name='aruba_telemetry.Action.timeOut', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='aruba_telemetry.Action.value', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authentication', full_name='aruba_telemetry.Action.authentication', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bondingKey', full_name='aruba_telemetry.Action.bondingKey', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apbMac', full_name='aruba_telemetry.Action.apbMac', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=504,
)

_AUTHENTICATION.fields_by_name['method'].enum_type = _AUTHENTICATIONMETHOD
_ACTION.fields_by_name['type'].enum_type = aruba__iot__types__pb2._ACTIONTYPE
_ACTION.fields_by_name['authentication'].message_type = _AUTHENTICATION
_ACTION.fields_by_name['bondingKey'].message_type = aruba__iot__types__pb2._BLEBONDINGKEY
DESCRIPTOR.message_types_by_name['Authentication'] = _AUTHENTICATION
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.enum_types_by_name['AuthenticationMethod'] = _AUTHENTICATIONMETHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Authentication = _reflection.GeneratedProtocolMessageType('Authentication', (_message.Message,), dict(
  DESCRIPTOR = _AUTHENTICATION,
  __module__ = 'aruba_iot_sb_action_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.Authentication)
  ))
_sym_db.RegisterMessage(Authentication)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
  DESCRIPTOR = _ACTION,
  __module__ = 'aruba_iot_sb_action_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.Action)
  ))
_sym_db.RegisterMessage(Action)


# @@protoc_insertion_point(module_scope)
