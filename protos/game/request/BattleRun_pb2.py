# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BattleRun.proto

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
  name='BattleRun.proto',
  package='PSXAPI.Request368314452',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x42\x61ttleRun.proto\x12\x17PSXAPI.Request368314452\"\x1e\n\tBattleRun\x12\x11\n\tRequestID\x18\x01 \x02(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATTLERUN = _descriptor.Descriptor(
  name='BattleRun',
  full_name='PSXAPI.Request368314452.BattleRun',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RequestID', full_name='PSXAPI.Request368314452.BattleRun.RequestID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['BattleRun'] = _BATTLERUN

BattleRun = _reflection.GeneratedProtocolMessageType('BattleRun', (_message.Message,), dict(
  DESCRIPTOR = _BATTLERUN,
  __module__ = 'BattleRun_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request368314452.BattleRun)
  ))
_sym_db.RegisterMessage(BattleRun)


# @@protoc_insertion_point(module_scope)
