# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DailyLootbox.proto

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
  name='DailyLootbox.proto',
  package='PSXAPI.Response1312766341',
  syntax='proto2',
  serialized_pb=_b('\n\x12\x44\x61ilyLootbox.proto\x12\x19PSXAPI.Response1312766341\x1a\x16protobuf-net/bcl.proto\"\x87\x01\n\x0c\x44\x61ilyLootbox\x12Y\n\x04Type\x18\x01 \x01(\x0e\x32@.PSXAPI.Response1312766341.PREFIX_AGDFASBV1037873316.LootboxType:\tNoneValue\x12\x1c\n\x05Timer\x18\x02 \x01(\x0b\x32\r.bcl.TimeSpan\"P\n\x19PREFIX_AGDFASBV1037873316\"3\n\x0bLootboxType\x12\r\n\tNoneValue\x10\x00\x12\t\n\x05Small\x10\x01\x12\n\n\x06Normal\x10\x02')
  ,
  dependencies=[protobuf__net_dot_bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV1037873316_LOOTBOXTYPE = _descriptor.EnumDescriptor(
  name='LootboxType',
  full_name='PSXAPI.Response1312766341.PREFIX_AGDFASBV1037873316.LootboxType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Small', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Normal', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=240,
  serialized_end=291,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1037873316_LOOTBOXTYPE)


_DAILYLOOTBOX = _descriptor.Descriptor(
  name='DailyLootbox',
  full_name='PSXAPI.Response1312766341.DailyLootbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='PSXAPI.Response1312766341.DailyLootbox.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Timer', full_name='PSXAPI.Response1312766341.DailyLootbox.Timer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=74,
  serialized_end=209,
)


_PREFIX_AGDFASBV1037873316 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1037873316',
  full_name='PSXAPI.Response1312766341.PREFIX_AGDFASBV1037873316',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1037873316_LOOTBOXTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=291,
)

_DAILYLOOTBOX.fields_by_name['Type'].enum_type = _PREFIX_AGDFASBV1037873316_LOOTBOXTYPE
_DAILYLOOTBOX.fields_by_name['Timer'].message_type = protobuf__net_dot_bcl__pb2._TIMESPAN
_PREFIX_AGDFASBV1037873316_LOOTBOXTYPE.containing_type = _PREFIX_AGDFASBV1037873316
DESCRIPTOR.message_types_by_name['DailyLootbox'] = _DAILYLOOTBOX
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1037873316'] = _PREFIX_AGDFASBV1037873316

DailyLootbox = _reflection.GeneratedProtocolMessageType('DailyLootbox', (_message.Message,), dict(
  DESCRIPTOR = _DAILYLOOTBOX,
  __module__ = 'DailyLootbox_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1312766341.DailyLootbox)
  ))
_sym_db.RegisterMessage(DailyLootbox)

PREFIX_AGDFASBV1037873316 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1037873316', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1037873316,
  __module__ = 'DailyLootbox_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1312766341.PREFIX_AGDFASBV1037873316)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1037873316)


# @@protoc_insertion_point(module_scope)
