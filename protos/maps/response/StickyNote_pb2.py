# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: StickyNote.proto

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
  name='StickyNote.proto',
  package='MAPAPI.Response1623491950',
  syntax='proto2',
  serialized_pb=_b('\n\x10StickyNote.proto\x12\x19MAPAPI.Response1623491950\"\x1a\n\nStickyNote\x12\x0c\n\x04Note\x18\x01 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STICKYNOTE = _descriptor.Descriptor(
  name='StickyNote',
  full_name='MAPAPI.Response1623491950.StickyNote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Note', full_name='MAPAPI.Response1623491950.StickyNote.Note', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['StickyNote'] = _STICKYNOTE

StickyNote = _reflection.GeneratedProtocolMessageType('StickyNote', (_message.Message,), dict(
  DESCRIPTOR = _STICKYNOTE,
  __module__ = 'StickyNote_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response1623491950.StickyNote)
  ))
_sym_db.RegisterMessage(StickyNote)


# @@protoc_insertion_point(module_scope)
