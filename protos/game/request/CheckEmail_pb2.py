# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CheckEmail.proto

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
  name='CheckEmail.proto',
  package='PSXAPI.Request1912430579',
  syntax='proto2',
  serialized_pb=_b('\n\x10\x43heckEmail.proto\x12\x18PSXAPI.Request1912430579\"\x1b\n\nCheckEmail\x12\r\n\x05\x45mail\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHECKEMAIL = _descriptor.Descriptor(
  name='CheckEmail',
  full_name='PSXAPI.Request1912430579.CheckEmail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Email', full_name='PSXAPI.Request1912430579.CheckEmail.Email', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=46,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['CheckEmail'] = _CHECKEMAIL

CheckEmail = _reflection.GeneratedProtocolMessageType('CheckEmail', (_message.Message,), dict(
  DESCRIPTOR = _CHECKEMAIL,
  __module__ = 'CheckEmail_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request1912430579.CheckEmail)
  ))
_sym_db.RegisterMessage(CheckEmail)


# @@protoc_insertion_point(module_scope)
