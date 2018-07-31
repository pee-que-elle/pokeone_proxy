# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Loot.proto

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


import bcl_pb2 as bcl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Loot.proto',
  package='PSXAPI.Response49',
  syntax='proto2',
  serialized_pb=_b('\n\nLoot.proto\x12\x11PSXAPI.Response49\x1a\tbcl.proto\"~\n\x04Loot\x12)\n\x04Vote\x18\x01 \x01(\x0b\x32\x1b.PSXAPI.Response49.LootVote\x12;\n\x06Result\x18\x02 \x01(\x0e\x32!.PSXAPI.Response49.LootVoteResult:\x08TimedOut\x12\x0e\n\x06Winner\x18\x03 \x01(\t\"n\n\x08LootVote\x12\x19\n\x06VoteID\x18\x01 \x01(\x0b\x32\t.bcl.Guid\x12\x11\n\x06ItemID\x18\x02 \x01(\x05:\x01\x30\x12\x13\n\x08Quantity\x18\x03 \x01(\r:\x01\x30\x12\x1f\n\x08\x44uration\x18\x04 \x01(\x0b\x32\r.bcl.TimeSpan*=\n\x0eLootVoteResult\x12\x0c\n\x08TimedOut\x10\x00\x12\x07\n\x03Won\x10\x01\x12\x08\n\x04Lost\x10\x02\x12\n\n\x06Passed\x10\x03')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_LOOTVOTERESULT = _descriptor.EnumDescriptor(
  name='LootVoteResult',
  full_name='PSXAPI.Response49.LootVoteResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TimedOut', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Won', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Lost', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Passed', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=284,
  serialized_end=345,
)
_sym_db.RegisterEnumDescriptor(_LOOTVOTERESULT)

LootVoteResult = enum_type_wrapper.EnumTypeWrapper(_LOOTVOTERESULT)
TimedOut = 0
Won = 1
Lost = 2
Passed = 3



_LOOT = _descriptor.Descriptor(
  name='Loot',
  full_name='PSXAPI.Response49.Loot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Vote', full_name='PSXAPI.Response49.Loot.Vote', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Result', full_name='PSXAPI.Response49.Loot.Result', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Winner', full_name='PSXAPI.Response49.Loot.Winner', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=44,
  serialized_end=170,
)


_LOOTVOTE = _descriptor.Descriptor(
  name='LootVote',
  full_name='PSXAPI.Response49.LootVote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='VoteID', full_name='PSXAPI.Response49.LootVote.VoteID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ItemID', full_name='PSXAPI.Response49.LootVote.ItemID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Quantity', full_name='PSXAPI.Response49.LootVote.Quantity', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Duration', full_name='PSXAPI.Response49.LootVote.Duration', index=3,
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
  serialized_start=172,
  serialized_end=282,
)

_LOOT.fields_by_name['Vote'].message_type = _LOOTVOTE
_LOOT.fields_by_name['Result'].enum_type = _LOOTVOTERESULT
_LOOTVOTE.fields_by_name['VoteID'].message_type = bcl__pb2._GUID
_LOOTVOTE.fields_by_name['Duration'].message_type = bcl__pb2._TIMESPAN
DESCRIPTOR.message_types_by_name['Loot'] = _LOOT
DESCRIPTOR.message_types_by_name['LootVote'] = _LOOTVOTE
DESCRIPTOR.enum_types_by_name['LootVoteResult'] = _LOOTVOTERESULT

Loot = _reflection.GeneratedProtocolMessageType('Loot', (_message.Message,), dict(
  DESCRIPTOR = _LOOT,
  __module__ = 'Loot_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response49.Loot)
  ))
_sym_db.RegisterMessage(Loot)

LootVote = _reflection.GeneratedProtocolMessageType('LootVote', (_message.Message,), dict(
  DESCRIPTOR = _LOOTVOTE,
  __module__ = 'Loot_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response49.LootVote)
  ))
_sym_db.RegisterMessage(LootVote)


# @@protoc_insertion_point(module_scope)