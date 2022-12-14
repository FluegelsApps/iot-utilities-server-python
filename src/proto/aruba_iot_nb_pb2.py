# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-nb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import src.proto.aruba_iot_types_pb2 as aruba__iot__types__pb2
import src.proto.aruba_iot_nb_telemetry_pb2 as aruba__iot__nb__telemetry__pb2
import src.proto.aruba_iot_nb_action_results_pb2 as aruba__iot__nb__action__results__pb2
import src.proto.aruba_iot_nb_characteristic_pb2 as aruba__iot__nb__characteristic__pb2
import src.proto.aruba_iot_nb_ble_data_pb2 as aruba__iot__nb__ble__data__pb2
import src.proto.aruba_iot_nb_wifi_data_pb2 as aruba__iot__nb__wifi__data__pb2
import src.proto.aruba_iot_nb_device_count_pb2 as aruba__iot__nb__device__count__pb2
import src.proto.aruba_iot_nb_status_pb2 as aruba__iot__nb__status__pb2
import src.proto.aruba_iot_nb_zb_pb2 as aruba__iot__nb__zb__pb2
import src.proto.aruba_iot_nb_serial_data_pb2 as aruba__iot__nb__serial__data__pb2
import src.proto.aruba_iot_nb_ap_health_update_pb2 as aruba__iot__nb__ap__health__update__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-nb.proto',
  package='aruba_telemetry',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x61ruba-iot-nb.proto\x12\x0f\x61ruba_telemetry\x1a\x15\x61ruba-iot-types.proto\x1a\x1c\x61ruba-iot-nb-telemetry.proto\x1a!aruba-iot-nb-action-results.proto\x1a!aruba-iot-nb-characteristic.proto\x1a\x1b\x61ruba-iot-nb-ble-data.proto\x1a\x1c\x61ruba-iot-nb-wifi-data.proto\x1a\x1f\x61ruba-iot-nb-device-count.proto\x1a\x19\x61ruba-iot-nb-status.proto\x1a\x15\x61ruba-iot-nb-zb.proto\x1a\x1e\x61ruba-iot-nb-serial-data.proto\x1a#aruba-iot-nb-ap-health-update.proto\"\x83\x01\n\x08Reporter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03mac\x18\x02 \x01(\x0c\x12\x0c\n\x04ipv4\x18\x03 \x01(\t\x12\x0c\n\x04ipv6\x18\x04 \x01(\t\x12\x0e\n\x06hwType\x18\x05 \x01(\t\x12\x11\n\tswVersion\x18\x06 \x01(\t\x12\x0f\n\x07swBuild\x18\x07 \x01(\t\x12\x0c\n\x04time\x18\x08 \x01(\x04\"\xb2\x04\n\tTelemetry\x12#\n\x04meta\x18\x01 \x02(\x0b\x32\x15.aruba_telemetry.Meta\x12+\n\x08reporter\x18\x02 \x02(\x0b\x32\x19.aruba_telemetry.Reporter\x12+\n\x08reported\x18\x03 \x03(\x0b\x32\x19.aruba_telemetry.Reported\x12.\n\x07results\x18\x04 \x03(\x0b\x32\x1d.aruba_telemetry.ActionResult\x12\x38\n\x0f\x63haracteristics\x18\x05 \x03(\x0b\x32\x1f.aruba_telemetry.Characteristic\x12)\n\x07\x62leData\x18\x06 \x03(\x0b\x32\x18.aruba_telemetry.BleData\x12+\n\x08wifiData\x18\x07 \x03(\x0b\x32\x19.aruba_telemetry.WiFiData\x12.\n\x08\x64\x65vCount\x18\x08 \x01(\x0b\x32\x1c.aruba_telemetry.DeviceCount\x12\'\n\x06status\x18\t \x01(\x0b\x32\x17.aruba_telemetry.Status\x12(\n\x06zigbee\x18\n \x01(\x0b\x32\x18.aruba_telemetry.NbZbMsg\x12.\n\x07nbSData\x18\x0b \x03(\x0b\x32\x1d.aruba_telemetry.NbSerialData\x12\x31\n\x08\x61pHealth\x18\x0c \x01(\x0b\x32\x1f.aruba_telemetry.ApHealthUpdate')
  ,
  dependencies=[aruba__iot__types__pb2.DESCRIPTOR,aruba__iot__nb__telemetry__pb2.DESCRIPTOR,aruba__iot__nb__action__results__pb2.DESCRIPTOR,aruba__iot__nb__characteristic__pb2.DESCRIPTOR,aruba__iot__nb__ble__data__pb2.DESCRIPTOR,aruba__iot__nb__wifi__data__pb2.DESCRIPTOR,aruba__iot__nb__device__count__pb2.DESCRIPTOR,aruba__iot__nb__status__pb2.DESCRIPTOR,aruba__iot__nb__zb__pb2.DESCRIPTOR,aruba__iot__nb__serial__data__pb2.DESCRIPTOR,aruba__iot__nb__ap__health__update__pb2.DESCRIPTOR,])




_REPORTER = _descriptor.Descriptor(
  name='Reporter',
  full_name='aruba_telemetry.Reporter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='aruba_telemetry.Reporter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mac', full_name='aruba_telemetry.Reporter.mac', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv4', full_name='aruba_telemetry.Reporter.ipv4', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6', full_name='aruba_telemetry.Reporter.ipv6', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hwType', full_name='aruba_telemetry.Reporter.hwType', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='swVersion', full_name='aruba_telemetry.Reporter.swVersion', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='swBuild', full_name='aruba_telemetry.Reporter.swBuild', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='aruba_telemetry.Reporter.time', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=374,
  serialized_end=505,
)


_TELEMETRY = _descriptor.Descriptor(
  name='Telemetry',
  full_name='aruba_telemetry.Telemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='aruba_telemetry.Telemetry.meta', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reporter', full_name='aruba_telemetry.Telemetry.reporter', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reported', full_name='aruba_telemetry.Telemetry.reported', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='aruba_telemetry.Telemetry.results', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='characteristics', full_name='aruba_telemetry.Telemetry.characteristics', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bleData', full_name='aruba_telemetry.Telemetry.bleData', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wifiData', full_name='aruba_telemetry.Telemetry.wifiData', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devCount', full_name='aruba_telemetry.Telemetry.devCount', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='aruba_telemetry.Telemetry.status', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zigbee', full_name='aruba_telemetry.Telemetry.zigbee', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nbSData', full_name='aruba_telemetry.Telemetry.nbSData', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apHealth', full_name='aruba_telemetry.Telemetry.apHealth', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=508,
  serialized_end=1070,
)

_TELEMETRY.fields_by_name['meta'].message_type = aruba__iot__types__pb2._META
_TELEMETRY.fields_by_name['reporter'].message_type = _REPORTER
_TELEMETRY.fields_by_name['reported'].message_type = aruba__iot__nb__telemetry__pb2._REPORTED
_TELEMETRY.fields_by_name['results'].message_type = aruba__iot__nb__action__results__pb2._ACTIONRESULT
_TELEMETRY.fields_by_name['characteristics'].message_type = aruba__iot__nb__characteristic__pb2._CHARACTERISTIC
_TELEMETRY.fields_by_name['bleData'].message_type = aruba__iot__nb__ble__data__pb2._BLEDATA
_TELEMETRY.fields_by_name['wifiData'].message_type = aruba__iot__nb__wifi__data__pb2._WIFIDATA
_TELEMETRY.fields_by_name['devCount'].message_type = aruba__iot__nb__device__count__pb2._DEVICECOUNT
_TELEMETRY.fields_by_name['status'].message_type = aruba__iot__nb__status__pb2._STATUS
_TELEMETRY.fields_by_name['zigbee'].message_type = aruba__iot__nb__zb__pb2._NBZBMSG
_TELEMETRY.fields_by_name['nbSData'].message_type = aruba__iot__nb__serial__data__pb2._NBSERIALDATA
_TELEMETRY.fields_by_name['apHealth'].message_type = aruba__iot__nb__ap__health__update__pb2._APHEALTHUPDATE
DESCRIPTOR.message_types_by_name['Reporter'] = _REPORTER
DESCRIPTOR.message_types_by_name['Telemetry'] = _TELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Reporter = _reflection.GeneratedProtocolMessageType('Reporter', (_message.Message,), dict(
  DESCRIPTOR = _REPORTER,
  __module__ = 'aruba_iot_nb_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.Reporter)
  ))
_sym_db.RegisterMessage(Reporter)

Telemetry = _reflection.GeneratedProtocolMessageType('Telemetry', (_message.Message,), dict(
  DESCRIPTOR = _TELEMETRY,
  __module__ = 'aruba_iot_nb_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.Telemetry)
  ))
_sym_db.RegisterMessage(Telemetry)


# @@protoc_insertion_point(module_scope)
