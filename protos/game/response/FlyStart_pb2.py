# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FlyStart.proto

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
  name='FlyStart.proto',
  package='PSXAPI.Response27',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x46lyStart.proto\x12\x11PSXAPI.Response27\"3\n\x08\x46lyStart\x12\x11\n\tStartArea\x18\x01 \x01(\t\x12\x14\n\x0cLandingAreas\x18\x02 \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FLYSTART = _descriptor.Descriptor(
  name='FlyStart',
  full_name='PSXAPI.Response27.FlyStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StartArea', full_name='PSXAPI.Response27.FlyStart.StartArea', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LandingAreas', full_name='PSXAPI.Response27.FlyStart.LandingAreas', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=37,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['FlyStart'] = _FLYSTART

FlyStart = _reflection.GeneratedProtocolMessageType('FlyStart', (_message.Message,), dict(
  DESCRIPTOR = _FLYSTART,
  __module__ = 'FlyStart_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response27.FlyStart)
  ))
_sym_db.RegisterMessage(FlyStart)


# @@protoc_insertion_point(module_scope)