# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UploadResponse.proto

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
  name='UploadResponse.proto',
  package='MAPAPI.Response1727245255',
  syntax='proto2',
  serialized_pb=_b('\n\x14UploadResponse.proto\x12\x19MAPAPI.Response1727245255\";\n\x0eUploadResponse\x12\x0f\n\x07MapName\x18\x01 \x01(\t\x12\x18\n\tSucceeded\x18\x02 \x01(\x08:\x05\x66\x61lse')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UPLOADRESPONSE = _descriptor.Descriptor(
  name='UploadResponse',
  full_name='MAPAPI.Response1727245255.UploadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MapName', full_name='MAPAPI.Response1727245255.UploadResponse.MapName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Succeeded', full_name='MAPAPI.Response1727245255.UploadResponse.Succeeded', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=51,
  serialized_end=110,
)

DESCRIPTOR.message_types_by_name['UploadResponse'] = _UPLOADRESPONSE

UploadResponse = _reflection.GeneratedProtocolMessageType('UploadResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADRESPONSE,
  __module__ = 'UploadResponse_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response1727245255.UploadResponse)
  ))
_sym_db.RegisterMessage(UploadResponse)


# @@protoc_insertion_point(module_scope)
