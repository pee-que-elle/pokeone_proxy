# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Login.proto

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
  name='Login.proto',
  package='PSXAPI.Request73469391',
  syntax='proto2',
  serialized_pb=_b('\n\x0bLogin.proto\x12\x16PSXAPI.Request73469391\"C\n\x18PREFIX_AGDFASBV122362143\"\'\n\x0e\x43lientPlatform\x12\r\n\tNoneValue\x10\x00\x12\x06\n\x02PC\x10\x01\"\x96\x01\n\x05Login\x12\x0c\n\x04Name\x18\x01 \x02(\t\x12\x10\n\x08Password\x18\x02 \x01(\t\x12\x0f\n\x07Version\x18\x03 \x01(\t\x12\\\n\x08Platform\x18\x04 \x01(\x0e\x32?.PSXAPI.Request73469391.PREFIX_AGDFASBV122362143.ClientPlatform:\tNoneValue')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV122362143_CLIENTPLATFORM = _descriptor.EnumDescriptor(
  name='ClientPlatform',
  full_name='PSXAPI.Request73469391.PREFIX_AGDFASBV122362143.ClientPlatform',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PC', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=67,
  serialized_end=106,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV122362143_CLIENTPLATFORM)


_PREFIX_AGDFASBV122362143 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV122362143',
  full_name='PSXAPI.Request73469391.PREFIX_AGDFASBV122362143',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV122362143_CLIENTPLATFORM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=106,
)


_LOGIN = _descriptor.Descriptor(
  name='Login',
  full_name='PSXAPI.Request73469391.Login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='PSXAPI.Request73469391.Login.Name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Password', full_name='PSXAPI.Request73469391.Login.Password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Version', full_name='PSXAPI.Request73469391.Login.Version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Platform', full_name='PSXAPI.Request73469391.Login.Platform', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=109,
  serialized_end=259,
)

_PREFIX_AGDFASBV122362143_CLIENTPLATFORM.containing_type = _PREFIX_AGDFASBV122362143
_LOGIN.fields_by_name['Platform'].enum_type = _PREFIX_AGDFASBV122362143_CLIENTPLATFORM
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV122362143'] = _PREFIX_AGDFASBV122362143
DESCRIPTOR.message_types_by_name['Login'] = _LOGIN

PREFIX_AGDFASBV122362143 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV122362143', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV122362143,
  __module__ = 'Login_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request73469391.PREFIX_AGDFASBV122362143)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV122362143)

Login = _reflection.GeneratedProtocolMessageType('Login', (_message.Message,), dict(
  DESCRIPTOR = _LOGIN,
  __module__ = 'Login_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request73469391.Login)
  ))
_sym_db.RegisterMessage(Login)


# @@protoc_insertion_point(module_scope)
