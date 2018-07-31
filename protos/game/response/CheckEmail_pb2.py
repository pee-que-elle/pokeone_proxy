# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CheckEmail.proto

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
  name='CheckEmail.proto',
  package='PSXAPI.Response13',
  syntax='proto2',
  serialized_pb=_b('\n\x10\x43heckEmail.proto\x12\x11PSXAPI.Response13\"X\n\nCheckEmail\x12\r\n\x05\x45mail\x18\x01 \x02(\t\x12;\n\x06Result\x18\x02 \x01(\x0e\x32#.PSXAPI.Response13.CheckEmailResult:\x06\x46\x61iled*-\n\x10\x43heckEmailResult\x12\n\n\x06\x46\x61iled\x10\x00\x12\r\n\tAvailable\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CHECKEMAILRESULT = _descriptor.EnumDescriptor(
  name='CheckEmailResult',
  full_name='PSXAPI.Response13.CheckEmailResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Failed', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Available', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=129,
  serialized_end=174,
)
_sym_db.RegisterEnumDescriptor(_CHECKEMAILRESULT)

CheckEmailResult = enum_type_wrapper.EnumTypeWrapper(_CHECKEMAILRESULT)
Failed = 0
Available = 1



_CHECKEMAIL = _descriptor.Descriptor(
  name='CheckEmail',
  full_name='PSXAPI.Response13.CheckEmail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Email', full_name='PSXAPI.Response13.CheckEmail.Email', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Result', full_name='PSXAPI.Response13.CheckEmail.Result', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=39,
  serialized_end=127,
)

_CHECKEMAIL.fields_by_name['Result'].enum_type = _CHECKEMAILRESULT
DESCRIPTOR.message_types_by_name['CheckEmail'] = _CHECKEMAIL
DESCRIPTOR.enum_types_by_name['CheckEmailResult'] = _CHECKEMAILRESULT

CheckEmail = _reflection.GeneratedProtocolMessageType('CheckEmail', (_message.Message,), dict(
  DESCRIPTOR = _CHECKEMAIL,
  __module__ = 'CheckEmail_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response13.CheckEmail)
  ))
_sym_db.RegisterMessage(CheckEmail)


# @@protoc_insertion_point(module_scope)