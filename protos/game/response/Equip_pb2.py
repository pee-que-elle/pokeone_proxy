# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Equip.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Equip.proto',
  package='PSXAPI.Response1094186717',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x45quip.proto\x12\x19PSXAPI.Response1094186717\"*\n\x05\x45quip\x12\x11\n\x06\x43lothe\x18\x01 \x01(\x05:\x01\x30\x12\x0e\n\x03Hat\x18\x02 \x01(\x05:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EQUIP = _descriptor.Descriptor(
  name='Equip',
  full_name='PSXAPI.Response1094186717.Equip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Clothe', full_name='PSXAPI.Response1094186717.Equip.Clothe', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hat', full_name='PSXAPI.Response1094186717.Equip.Hat', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=42,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['Equip'] = _EQUIP

Equip = _reflection.GeneratedProtocolMessageType('Equip', (_message.Message,), dict(
  DESCRIPTOR = _EQUIP,
  __module__ = 'Equip_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1094186717.Equip)
  ))
_sym_db.RegisterMessage(Equip)


# @@protoc_insertion_point(module_scope)
