# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LinkPair.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobuf_net import bcl_pb2 as protobuf__net_dot_bcl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='LinkPair.proto',
  package='MAPAPI.Response1432085585',
  syntax='proto2',
  serialized_pb=_b('\n\x0eLinkPair.proto\x12\x19MAPAPI.Response1432085585\x1a\x16protobuf-net/bcl.proto\"S\n\x08LinkPair\x12\x18\n\x05Link1\x18\x01 \x01(\x0b\x32\t.bcl.Guid\x12\x18\n\x05Link2\x18\x02 \x01(\x0b\x32\t.bcl.Guid\x12\x13\n\x08\x44istance\x18\x03 \x01(\x05:\x01\x30')
  ,
  dependencies=[protobuf__net_dot_bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LINKPAIR = _descriptor.Descriptor(
  name='LinkPair',
  full_name='MAPAPI.Response1432085585.LinkPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Link1', full_name='MAPAPI.Response1432085585.LinkPair.Link1', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Link2', full_name='MAPAPI.Response1432085585.LinkPair.Link2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Distance', full_name='MAPAPI.Response1432085585.LinkPair.Distance', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=69,
  serialized_end=152,
)

_LINKPAIR.fields_by_name['Link1'].message_type = protobuf__net_dot_bcl__pb2._GUID
_LINKPAIR.fields_by_name['Link2'].message_type = protobuf__net_dot_bcl__pb2._GUID
DESCRIPTOR.message_types_by_name['LinkPair'] = _LINKPAIR

LinkPair = _reflection.GeneratedProtocolMessageType('LinkPair', (_message.Message,), dict(
  DESCRIPTOR = _LINKPAIR,
  __module__ = 'LinkPair_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response1432085585.LinkPair)
  ))
_sym_db.RegisterMessage(LinkPair)


# @@protoc_insertion_point(module_scope)
