# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MoveLINK.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bcl_pb2 as bcl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='MoveLINK.proto',
  package='MAPAPI.Response22',
  syntax='proto2',
  serialized_pb=_b('\n\x0eMoveLINK.proto\x12\x11MAPAPI.Response22\x1a\tbcl.proto\">\n\x08MoveLINK\x12\x32\n\x06Object\x18\x01 \x01(\x0b\x32\".MAPAPI.Response22.NPCObjectStruct\"R\n\x0fNPCObjectStruct\x12\x0c\n\x01x\x18\x01 \x01(\x05:\x01\x30\x12\x0c\n\x01y\x18\x02 \x01(\x05:\x01\x30\x12\x0c\n\x01z\x18\x03 \x01(\x05:\x01\x30\x12\x15\n\x02ID\x18\x04 \x01(\x0b\x32\t.bcl.Guid')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MOVELINK = _descriptor.Descriptor(
  name='MoveLINK',
  full_name='MAPAPI.Response22.MoveLINK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Object', full_name='MAPAPI.Response22.MoveLINK.Object', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=48,
  serialized_end=110,
)


_NPCOBJECTSTRUCT = _descriptor.Descriptor(
  name='NPCObjectStruct',
  full_name='MAPAPI.Response22.NPCObjectStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='MAPAPI.Response22.NPCObjectStruct.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='MAPAPI.Response22.NPCObjectStruct.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='MAPAPI.Response22.NPCObjectStruct.z', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ID', full_name='MAPAPI.Response22.NPCObjectStruct.ID', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=112,
  serialized_end=194,
)

_MOVELINK.fields_by_name['Object'].message_type = _NPCOBJECTSTRUCT
_NPCOBJECTSTRUCT.fields_by_name['ID'].message_type = bcl__pb2._GUID
DESCRIPTOR.message_types_by_name['MoveLINK'] = _MOVELINK
DESCRIPTOR.message_types_by_name['NPCObjectStruct'] = _NPCOBJECTSTRUCT

MoveLINK = _reflection.GeneratedProtocolMessageType('MoveLINK', (_message.Message,), dict(
  DESCRIPTOR = _MOVELINK,
  __module__ = 'MoveLINK_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response22.MoveLINK)
  ))
_sym_db.RegisterMessage(MoveLINK)

NPCObjectStruct = _reflection.GeneratedProtocolMessageType('NPCObjectStruct', (_message.Message,), dict(
  DESCRIPTOR = _NPCOBJECTSTRUCT,
  __module__ = 'MoveLINK_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response22.NPCObjectStruct)
  ))
_sym_db.RegisterMessage(NPCObjectStruct)


# @@protoc_insertion_point(module_scope)