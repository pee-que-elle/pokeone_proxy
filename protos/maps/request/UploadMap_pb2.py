# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UploadMap.proto

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
  name='UploadMap.proto',
  package='MAPAPI.Request556004732',
  syntax='proto2',
  serialized_pb=_b('\n\x0fUploadMap.proto\x12\x17MAPAPI.Request556004732\"-\n\tUploadMap\x12\x0f\n\x07MapName\x18\x01 \x01(\t\x12\x0f\n\x07MapData\x18\x02 \x01(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UPLOADMAP = _descriptor.Descriptor(
  name='UploadMap',
  full_name='MAPAPI.Request556004732.UploadMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MapName', full_name='MAPAPI.Request556004732.UploadMap.MapName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MapData', full_name='MAPAPI.Request556004732.UploadMap.MapData', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['UploadMap'] = _UPLOADMAP

UploadMap = _reflection.GeneratedProtocolMessageType('UploadMap', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADMAP,
  __module__ = 'UploadMap_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Request556004732.UploadMap)
  ))
_sym_db.RegisterMessage(UploadMap)


# @@protoc_insertion_point(module_scope)
