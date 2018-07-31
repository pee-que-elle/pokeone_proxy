# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Lootbox.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Lootbox.proto',
  package='PSXAPI.Request42',
  syntax='proto2',
  serialized_pb=_b('\n\rLootbox.proto\x12\x10PSXAPI.Request42\"g\n\x07Lootbox\x12/\n\x06\x41\x63tion\x18\x01 \x02(\x0e\x32\x1f.PSXAPI.Request42.LootboxAction\x12+\n\x04Type\x18\x02 \x02(\x0e\x32\x1d.PSXAPI.Request42.LootboxType*%\n\rLootboxAction\x12\n\n\x06__None\x10\x00\x12\x08\n\x04Open\x10\x01*1\n\x0bLootboxType\x12\x0b\n\x07__None0\x10\x00\x12\t\n\x05Small\x10\x01\x12\n\n\x06Normal\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_LOOTBOXACTION = _descriptor.EnumDescriptor(
  name='LootboxAction',
  full_name='PSXAPI.Request42.LootboxAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Open', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=140,
  serialized_end=177,
)
_sym_db.RegisterEnumDescriptor(_LOOTBOXACTION)

LootboxAction = enum_type_wrapper.EnumTypeWrapper(_LOOTBOXACTION)
_LOOTBOXTYPE = _descriptor.EnumDescriptor(
  name='LootboxType',
  full_name='PSXAPI.Request42.LootboxType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None0', index=0, number=0,
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
  serialized_start=179,
  serialized_end=228,
)
_sym_db.RegisterEnumDescriptor(_LOOTBOXTYPE)

LootboxType = enum_type_wrapper.EnumTypeWrapper(_LOOTBOXTYPE)
__None = 0
Open = 1
__None0 = 0
Small = 1
Normal = 2



_LOOTBOX = _descriptor.Descriptor(
  name='Lootbox',
  full_name='PSXAPI.Request42.Lootbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Request42.Lootbox.Action', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Type', full_name='PSXAPI.Request42.Lootbox.Type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=35,
  serialized_end=138,
)

_LOOTBOX.fields_by_name['Action'].enum_type = _LOOTBOXACTION
_LOOTBOX.fields_by_name['Type'].enum_type = _LOOTBOXTYPE
DESCRIPTOR.message_types_by_name['Lootbox'] = _LOOTBOX
DESCRIPTOR.enum_types_by_name['LootboxAction'] = _LOOTBOXACTION
DESCRIPTOR.enum_types_by_name['LootboxType'] = _LOOTBOXTYPE

Lootbox = _reflection.GeneratedProtocolMessageType('Lootbox', (_message.Message,), dict(
  DESCRIPTOR = _LOOTBOX,
  __module__ = 'Lootbox_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request42.Lootbox)
  ))
_sym_db.RegisterMessage(Lootbox)


# @@protoc_insertion_point(module_scope)