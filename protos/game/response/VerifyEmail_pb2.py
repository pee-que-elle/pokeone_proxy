# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VerifyEmail.proto

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
  name='VerifyEmail.proto',
  package='PSXAPI.Response759181634',
  syntax='proto2',
  serialized_pb=_b('\n\x11VerifyEmail.proto\x12\x18PSXAPI.Response759181634\"~\n\x0bVerifyEmail\x12]\n\x06Result\x18\x01 \x01(\x0e\x32\x45.PSXAPI.Response759181634.PREFIX_AGDFASBV1099110023.VerifyEmailResult:\x06\x46\x61iled\x12\x10\n\x08Username\x18\x02 \x01(\t\"V\n\x19PREFIX_AGDFASBV1099110023\"9\n\x11VerifyEmailResult\x12\n\n\x06\x46\x61iled\x10\x00\x12\x0c\n\x08Verified\x10\x01\x12\n\n\x06Resent\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV1099110023_VERIFYEMAILRESULT = _descriptor.EnumDescriptor(
  name='VerifyEmailResult',
  full_name='PSXAPI.Response759181634.PREFIX_AGDFASBV1099110023.VerifyEmailResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Failed', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Verified', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Resent', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=204,
  serialized_end=261,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1099110023_VERIFYEMAILRESULT)


_VERIFYEMAIL = _descriptor.Descriptor(
  name='VerifyEmail',
  full_name='PSXAPI.Response759181634.VerifyEmail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='PSXAPI.Response759181634.VerifyEmail.Result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Username', full_name='PSXAPI.Response759181634.VerifyEmail.Username', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=47,
  serialized_end=173,
)


_PREFIX_AGDFASBV1099110023 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1099110023',
  full_name='PSXAPI.Response759181634.PREFIX_AGDFASBV1099110023',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1099110023_VERIFYEMAILRESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=261,
)

_VERIFYEMAIL.fields_by_name['Result'].enum_type = _PREFIX_AGDFASBV1099110023_VERIFYEMAILRESULT
_PREFIX_AGDFASBV1099110023_VERIFYEMAILRESULT.containing_type = _PREFIX_AGDFASBV1099110023
DESCRIPTOR.message_types_by_name['VerifyEmail'] = _VERIFYEMAIL
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1099110023'] = _PREFIX_AGDFASBV1099110023

VerifyEmail = _reflection.GeneratedProtocolMessageType('VerifyEmail', (_message.Message,), dict(
  DESCRIPTOR = _VERIFYEMAIL,
  __module__ = 'VerifyEmail_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response759181634.VerifyEmail)
  ))
_sym_db.RegisterMessage(VerifyEmail)

PREFIX_AGDFASBV1099110023 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1099110023', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1099110023,
  __module__ = 'VerifyEmail_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response759181634.PREFIX_AGDFASBV1099110023)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1099110023)


# @@protoc_insertion_point(module_scope)
