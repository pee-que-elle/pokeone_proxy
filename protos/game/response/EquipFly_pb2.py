# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EquipFly.proto

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
  name='EquipFly.proto',
  package='PSXAPI.Response864927402',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x45quipFly.proto\x12\x18PSXAPI.Response864927402\"\x1b\n\x08\x45quipFly\x12\x0f\n\x04Skin\x18\x01 \x01(\x05:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EQUIPFLY = _descriptor.Descriptor(
  name='EquipFly',
  full_name='PSXAPI.Response864927402.EquipFly',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Skin', full_name='PSXAPI.Response864927402.EquipFly.Skin', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=44,
  serialized_end=71,
)

DESCRIPTOR.message_types_by_name['EquipFly'] = _EQUIPFLY

EquipFly = _reflection.GeneratedProtocolMessageType('EquipFly', (_message.Message,), dict(
  DESCRIPTOR = _EQUIPFLY,
  __module__ = 'EquipFly_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response864927402.EquipFly)
  ))
_sym_db.RegisterMessage(EquipFly)


# @@protoc_insertion_point(module_scope)
