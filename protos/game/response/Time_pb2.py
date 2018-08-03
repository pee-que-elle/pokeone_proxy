# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Time.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobuf_net import bcl_pb2 as protobuf__net_dot_bcl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Time.proto',
  package='PSXAPI.Response1323571940',
  syntax='proto2',
  serialized_pb=_b('\n\nTime.proto\x12\x19PSXAPI.Response1323571940\x1a\x16protobuf-net/bcl.proto\"b\n\x18PREFIX_AGDFASBV708095433\"F\n\x0bGameDayTime\x12\t\n\x05Unset\x10\x00\x12\x0b\n\x07Morning\x10\x01\x12\x07\n\x03\x44\x61y\x10\x02\x12\x0b\n\x07\x45vening\x10\x03\x12\t\n\x05Night\x10\x04\"d\n\x19PREFIX_AGDFASBV1371346520\"G\n\nGameSeason\x12\t\n\x05Unset\x10\x00\x12\n\n\x06Spring\x10\x01\x12\n\n\x06Summer\x10\x02\x12\n\n\x06\x41utumn\x10\x03\x12\n\n\x06Winter\x10\x04\"\xf9\x02\n\x04Time\x12$\n\rServerTimeUtc\x18\x01 \x01(\x0b\x32\r.bcl.DateTime\x12\x1f\n\x08GameTime\x18\x02 \x01(\x0b\x32\r.bcl.TimeSpan\x12[\n\x0bGameDayTime\x18\x03 \x01(\x0e\x32?.PSXAPI.Response1323571940.PREFIX_AGDFASBV708095433.GameDayTime:\x05Unset\x12Z\n\nGameSeason\x18\x04 \x01(\x0e\x32?.PSXAPI.Response1323571940.PREFIX_AGDFASBV1371346520.GameSeason:\x05Unset\x12\x15\n\nTimeFactor\x18\x05 \x01(\x01:\x01\x30\x12Z\n\x07Weather\x18\x06 \x01(\x0e\x32\x41.PSXAPI.Response1323571940.PREFIX_AGDFASBV1111956081.WeatherState:\x06Normal\"K\n\x19PREFIX_AGDFASBV1111956081\".\n\x0cWeatherState\x12\n\n\x06Normal\x10\x00\x12\x08\n\x04Rain\x10\x01\x12\x08\n\x04Snow\x10\x02')
  ,
  dependencies=[protobuf__net_dot_bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV708095433_GAMEDAYTIME = _descriptor.EnumDescriptor(
  name='GameDayTime',
  full_name='PSXAPI.Response1323571940.PREFIX_AGDFASBV708095433.GameDayTime',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unset', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Morning', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Day', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Evening', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Night', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=93,
  serialized_end=163,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV708095433_GAMEDAYTIME)

_PREFIX_AGDFASBV1371346520_GAMESEASON = _descriptor.EnumDescriptor(
  name='GameSeason',
  full_name='PSXAPI.Response1323571940.PREFIX_AGDFASBV1371346520.GameSeason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unset', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Spring', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Summer', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Autumn', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Winter', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=194,
  serialized_end=265,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1371346520_GAMESEASON)

_PREFIX_AGDFASBV1111956081_WEATHERSTATE = _descriptor.EnumDescriptor(
  name='WeatherState',
  full_name='PSXAPI.Response1323571940.PREFIX_AGDFASBV1111956081.WeatherState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Normal', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Rain', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Snow', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=676,
  serialized_end=722,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1111956081_WEATHERSTATE)


_PREFIX_AGDFASBV708095433 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV708095433',
  full_name='PSXAPI.Response1323571940.PREFIX_AGDFASBV708095433',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV708095433_GAMEDAYTIME,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=163,
)


_PREFIX_AGDFASBV1371346520 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1371346520',
  full_name='PSXAPI.Response1323571940.PREFIX_AGDFASBV1371346520',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1371346520_GAMESEASON,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=265,
)


_TIME = _descriptor.Descriptor(
  name='Time',
  full_name='PSXAPI.Response1323571940.Time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ServerTimeUtc', full_name='PSXAPI.Response1323571940.Time.ServerTimeUtc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GameTime', full_name='PSXAPI.Response1323571940.Time.GameTime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GameDayTime', full_name='PSXAPI.Response1323571940.Time.GameDayTime', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GameSeason', full_name='PSXAPI.Response1323571940.Time.GameSeason', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeFactor', full_name='PSXAPI.Response1323571940.Time.TimeFactor', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Weather', full_name='PSXAPI.Response1323571940.Time.Weather', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=645,
)


_PREFIX_AGDFASBV1111956081 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1111956081',
  full_name='PSXAPI.Response1323571940.PREFIX_AGDFASBV1111956081',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1111956081_WEATHERSTATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=647,
  serialized_end=722,
)

_PREFIX_AGDFASBV708095433_GAMEDAYTIME.containing_type = _PREFIX_AGDFASBV708095433
_PREFIX_AGDFASBV1371346520_GAMESEASON.containing_type = _PREFIX_AGDFASBV1371346520
_TIME.fields_by_name['ServerTimeUtc'].message_type = protobuf__net_dot_bcl__pb2._DATETIME
_TIME.fields_by_name['GameTime'].message_type = protobuf__net_dot_bcl__pb2._TIMESPAN
_TIME.fields_by_name['GameDayTime'].enum_type = _PREFIX_AGDFASBV708095433_GAMEDAYTIME
_TIME.fields_by_name['GameSeason'].enum_type = _PREFIX_AGDFASBV1371346520_GAMESEASON
_TIME.fields_by_name['Weather'].enum_type = _PREFIX_AGDFASBV1111956081_WEATHERSTATE
_PREFIX_AGDFASBV1111956081_WEATHERSTATE.containing_type = _PREFIX_AGDFASBV1111956081
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV708095433'] = _PREFIX_AGDFASBV708095433
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1371346520'] = _PREFIX_AGDFASBV1371346520
DESCRIPTOR.message_types_by_name['Time'] = _TIME
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1111956081'] = _PREFIX_AGDFASBV1111956081

PREFIX_AGDFASBV708095433 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV708095433', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV708095433,
  __module__ = 'Time_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1323571940.PREFIX_AGDFASBV708095433)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV708095433)

PREFIX_AGDFASBV1371346520 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1371346520', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1371346520,
  __module__ = 'Time_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1323571940.PREFIX_AGDFASBV1371346520)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1371346520)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), dict(
  DESCRIPTOR = _TIME,
  __module__ = 'Time_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1323571940.Time)
  ))
_sym_db.RegisterMessage(Time)

PREFIX_AGDFASBV1111956081 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1111956081', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1111956081,
  __module__ = 'Time_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1323571940.PREFIX_AGDFASBV1111956081)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1111956081)


# @@protoc_insertion_point(module_scope)
